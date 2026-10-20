"""Exact Fourier-quadratic controls; optionally rebuild every coefficient.

No discovery builder is imported. Fourier values use integer coordinates in
Z[omega]; all checks are exact, with no FFT or numerical eigenvalues.
"""
from collections import Counter
from itertools import combinations_with_replacement, permutations, product
from math import factorial, comb
from pathlib import Path
import argparse
import hashlib
import json
import pickle
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=HERE.parent/"fourpoint"

import numpy as np
from scipy.sparse import csr_matrix
from audit_fivepoint import Canonical
from audit_fourier_pair import collapsed_codes


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frequency_representative(v):
    v=tuple(int(x)%3 for x in v)
    return min(v,tuple((3-x)%3 for x in v))


def local_transform(canonical):
    frequencies=sorted({frequency_representative(f) for f in product(range(3),repeat=4)
                        if sum(f)%3==0})
    assert len(frequencies)==14
    lookup={f:i for i,f in enumerate(frequencies)}
    patterns=canonical.patterns[4]
    pairs=list(__import__('itertools').combinations(range(4),2))
    pattern_lookup={sum(1<<i for i,(a,b) in enumerate(pairs) if p[a]==p[b]):j
                    for j,p in enumerate(patterns)}
    local=np.zeros((14,14),dtype=np.int64)
    for fi,f in enumerate(frequencies):
        phase_count=np.zeros((14,3),dtype=np.int64)
        for tail in product(range(3),repeat=3):
            p=(0,)+tail
            signature=sum(1<<i for i,(a,b) in enumerate(pairs) if p[a]==p[b])
            phase=sum(a*b for a,b in zip(f,p))%3
            phase_count[pattern_lookup[signature],phase]+=1
        assert np.array_equal(phase_count[:,1],phase_count[:,2])
        local[fi]=phase_count[:,0]-phase_count[:,1]
        expected=[1 if len(set(p))==1 else 2 if sum(a*b for a,b in zip(f,p))%3==0 else -1
                  for p in patterns]
        assert list(local[fi])==expected
    permutations_map=np.array([[lookup[frequency_representative([f[i] for i in p])]
                                for f in frequencies] for p in permutations(range(4))])
    return frequencies,lookup,local,permutations_map


def rebuild_all(codes,canonical,frequencies,flocal,local,transforms):
    V=len(codes)
    lookup={int(code):i for i,code in enumerate(codes)}
    powers=np.array([8**i for i in range(14)],dtype=np.int64)
    levels=[]
    maps=[]
    previous=np.array([0],dtype=np.int64)
    previous_tuples=[()]
    for degree in range(1,8):
        tuples=list(combinations_with_replacement(range(14),degree))
        keys=np.array([sum(int(powers[i]) for i in t) for t in tuples],dtype=np.int64)
        order=np.argsort(keys)
        destinations=np.stack([order[np.searchsorted(keys[order],previous+powers[i])] for i in range(14)])
        assert np.array_equal(keys[destinations],previous[None,:]+powers[:,None])
        maps.append((len(tuples),destinations))
        levels.append(tuples)
        previous=keys
        previous_tuples=tuples
    point_patterns=np.array(canonical.patterns[4],dtype=np.int64)
    point_arrays=point_patterns[np.array(levels[-1])].transpose(0,2,1)
    point_codes=collapsed_codes(canonical,point_arrays)
    indices=np.array([lookup[int(code)] for code in point_codes],dtype=np.int64)
    del point_arrays
    counts=np.array([np.bincount(t,minlength=14) for t in levels[-1]],dtype=np.int64)
    canonical_frequency=np.min(np.stack([counts@powers[t] for t in transforms]),axis=0)
    keys,first=np.unique(canonical_frequency,return_index=True)
    key_lookup={int(key):i for i,key in enumerate(keys)}
    assert len(keys)==4190
    transformed=np.empty((4190,V),dtype=np.int64)
    maximum_l1=0
    for ri,ci in enumerate(first):
        coefficients=np.array([1],dtype=np.int64)
        for degree,f in enumerate(levels[-1][ci]):
            size,destination=maps[degree]
            nxt=np.zeros(size,dtype=np.int64)
            # Every fixed-pattern destination map is injective, so += adds
            # exactly once per prior monomial; no floating-point bincount.
            for p in range(14):
                nxt[destination[p]]+=int(local[f,p])*coefficients
            coefficients=nxt
        l1=sum(abs(int(value)) for value in coefficients)
        assert l1<=3**21
        maximum_l1=max(maximum_l1,l1)
        row=np.zeros(V,dtype=np.int64)
        np.add.at(row,indices,coefficients)
        transformed[ri]=row
        if ri%500==0:
            print('independent Fourier transform row',ri,flush=True)
    # Independently generate all (l,m) counts by seven nine-choice
    # coordinate polynomials. Outside coordinates fold simultaneous signs.
    outside=sorted({min((l,m),((-l)%3,(-m)%3)) for l,m in product(range(3),repeat=2)})
    inside=list(product(range(3),repeat=2))
    assert len(outside)==5 and len(inside)==9
    pair_frequencies=[]
    for l,m in outside:
        pair_frequencies.append(flocal[frequency_representative((l,-l,-m,m))])
    for l,m in inside:
        pair_frequencies.append(flocal[frequency_representative((l,1-l,-m,m-1))])
    report=[];matrices=[]
    for k in range(8):
        labels=[(b,a,c) for b in range(8-k) for a in range(k+1) for c in range(a,k-a+1)]
        label_index={tuple(label):i for i,label in enumerate(labels)}
        dim=len(labels)
        polynomial={0:1}
        for coordinate in range(7):
            options=Counter()
            for l,m in product(range(3),repeat=2):
                position=5+inside.index((l,m)) if coordinate<k else outside.index(min((l,m),((-l)%3,(-m)%3)))
                options[position]+=1
            nxt=Counter()
            for key,coefficient in polynomial.items():
                for position,amount in options.items():
                    nxt[key+int(powers[position])]+=coefficient*amount
            polynomial=nxt
        assert sum(polynomial.values())==2187**2
        histogram=np.array([[(key//int(p))%8 for p in powers] for key in polynomial],dtype=np.int64)
        fc=np.zeros_like(histogram)
        for i,frequency_type in enumerate(pair_frequencies):
            fc[:,frequency_type]+=histogram[:,i]
        orbit_keys=np.min(np.stack([fc@powers[t] for t in transforms]),axis=0)
        compression=np.zeros((dim*dim,4190),dtype=np.int64)
        for h,key,weight in zip(histogram,orbit_keys,polynomial.values()):
            lb=sum(int(h[i])*(l!=0) for i,(l,m) in enumerate(outside))
            mb=sum(int(h[i])*(m!=0) for i,(l,m) in enumerate(outside))
            l0=sum(int(h[5+i])*(l==0) for i,(l,m) in enumerate(inside))
            l1=sum(int(h[5+i])*(l==1) for i,(l,m) in enumerate(inside))
            m0=sum(int(h[5+i])*(m==0) for i,(l,m) in enumerate(inside))
            m1=sum(int(h[5+i])*(m==1) for i,(l,m) in enumerate(inside))
            row=label_index[(lb,min(l0,l1),max(l0,l1))]*dim+label_index[(mb,min(m0,m1),max(m0,m1))]
            compression[row,key_lookup[int(key)]]+=weight
        sizes=np.array([comb(7-k,b)*2**b*factorial(k)//(factorial(a)*factorial(c)*factorial(k-a-c))*(1 if a==c else 2) for b,a,c in labels],dtype=np.int64)
        assert np.array_equal(compression.sum(axis=1).reshape(dim,dim),np.outer(sizes,sizes))
        # This uniform absolute bound proves the integer sparse product safe.
        assert (2187**2)*maximum_l1<2**63
        rebuilt=csr_matrix(compression)@transformed
        matrices.append(csr_matrix(rebuilt))
        report.append({'weight':k,'dimension':dim,'conditional_histograms':len(polynomial),
                       'all_integer_coefficients_match':True})
        print('independent full quadratic block pass',k,dim,flush=True)
    return matrices



def rebuild(codes):
    canonical=Canonical()
    frequencies,lookup,local,transforms=local_transform(canonical)
    return rebuild_all(codes,canonical,frequencies,lookup,local,transforms)
