"""Independent exact audit of the degree-four M28 certificate.

Imports no discovery builder or coefficient cache. NumPy is used only for
bounded integer orbit enumeration and counting; final certificate arithmetic
uses Python integers. The frozen independent phase2 checker reconstructs the
old60 blocks/cuts. New rows are expanded directly as Boolean polynomials.
"""
import argparse,hashlib,importlib.util,itertools,json,math,time
from collections import Counter
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
OLD=HERE/'check_lower27_certificate.py'
OLD_HASH='f938798d41bc94182a303d95f5cceed0399ffc235574cec7c53124dd2abe31d2'

def require(ok,message):
    if not ok:raise ValueError(message)

def compositions(n,k):
    # Stars and bars, in increasing lexicographic order of multiplicities.
    for bars in itertools.combinations(range(n+k-1),k-1):
        positions=(-1,)+bars+(n+k-1,)
        yield tuple(positions[i+1]-positions[i]-1 for i in range(k))

def relabel(v):
    names={};return tuple(names.setdefault(int(x),len(names)) for x in v)

class Orbits:
    def __init__(self):
        self.words=np.array(list(itertools.product(range(3),repeat=7)),dtype=np.int64)
        self.errors=self.words[np.count_nonzero(self.words,axis=1)<=2]
        require(len(self.errors)==99,'ball size')
        patterns=sorted({relabel(w) for w in itertools.product(range(3),repeat=4)})
        self.patterns=np.array(patterns,dtype=np.int64);self.pl={p:i for i,p in enumerate(patterns)}
        self.pattern_lookup=np.array([self.pl[relabel(w)] for w in itertools.product(range(3),repeat=4)],dtype=np.int64)
        self.powers=np.array([8**i for i in range(14)],dtype=np.int64)
        self.counts=np.array(list(compositions(7,14)),dtype=np.int64)
        require(self.counts.shape==(77520,14),'histogram count')
        self.raw=self.counts@self.powers
        permutations=list(itertools.permutations(range(4)))
        transforms=[[self.pl[relabel([p[i] for i in perm])] for p in patterns] for perm in permutations]
        canonical=np.min(np.stack([self.counts@self.powers[t] for t in transforms]),axis=0)+(1<<50)
        pairs=list(itertools.combinations(range(4),2))
        distances=np.stack([self.counts@(self.patterns[:,a]!=self.patterns[:,b]) for a,b in pairs],axis=1)
        # Repeated rows represent moments of fewer than four DISTINCT points.
        for row in np.flatnonzero(np.any(distances==0,axis=1)):
            c=self.counts[row];reps=[]
            for a in range(4):
                if not any(int(c@(self.patterns[:,a]!=self.patterns[:,b]))==0 for b in reps):reps.append(a)
            while len(reps)<3:reps.append(reps[0])
            a,b,d=reps
            ds=sorted(int(c@(self.patterns[:,i]!=self.patterns[:,j])) for i,j in [(a,b),(a,d),(b,d)])
            e=int(c@((self.patterns[:,a]!=self.patterns[:,b])&(self.patterns[:,a]!=self.patterns[:,d])&(self.patterns[:,b]!=self.patterns[:,d])))
            canonical[row]=((ds[0]*8+ds[1])*8+ds[2])*8+e
        self.codes=sorted(map(int,set(canonical)));self.V=len(self.codes);require(self.V==4085,'moment orbit count')
        self.index={c:i for i,c in enumerate(self.codes)}
        self.orbit_by_composition=np.array([self.index[int(c)] for c in canonical],dtype=np.int64)
        order=np.argsort(self.raw);self.sorted_raw=self.raw[order];self.sorted_index=self.orbit_by_composition[order]
        require(len(np.unique(self.raw))==77520,'raw histogram encoding injectivity')
        # Representatives used only to interpret the certificate row numbering.
        first={}
        for i,c in enumerate(canonical):first.setdefault(int(c),i)
        self.representatives=np.array([self.points(self.counts[first[c]]) for c in self.codes],dtype=np.int64)
        root_transforms=[[self.pl[relabel([p[i] for i in (0,)+perm])] for p in patterns] for perm in itertools.permutations((1,2,3))]
        rootcodes=np.min(np.stack([self.counts@self.powers[t] for t in root_transforms]),axis=0)
        firstroot={}
        for i,c in enumerate(rootcodes):firstroot.setdefault(int(c),i)
        self.root_representatives=np.array([self.points(self.counts[firstroot[c]]) for c in sorted(firstroot)],dtype=np.int64)
        self.T=len(self.root_representatives);require(self.T==14176,'rooted orbit count')
        self.lower_representatives={}
        for c0,c1,c2,c3,c4 in compositions(7,5):
            x=np.array([0]*(c0+c1)+[1]*(c2+c3+c4),dtype=np.int64)
            y=np.array([0]*c0+[1]*c1+[0]*c2+[1]*c3+[2]*c4,dtype=np.int64)
            key=self.moment([np.zeros(7,dtype=np.int64),x,y])
            self.lower_representatives.setdefault(key,(x,y))
        require(set(self.lower_representatives)==set(range(95)),'lower orbit representatives')
    def points(self,c):return np.repeat(self.patterns,c,axis=0).T
    def lookup_raw(self,raw):
        positions=np.searchsorted(self.sorted_raw,raw)
        require(np.all(positions<len(self.sorted_raw)),'raw orbit missing')
        require(np.array_equal(self.sorted_raw[positions],raw),'raw orbit mismatch')
        return self.sorted_index[positions]
    def moments(self,points):
        # points is a list of (N,7) arrays, or broadcastable (1,7) arrays.
        if not points:raise ValueError('batch empty moment unsupported')
        ps=list(points)
        while len(ps)<4:ps.append(ps[0])
        require(len(ps)==4,'moment degree exceeds4')
        ids=self.pattern_lookup[27*ps[0]+9*ps[1]+3*ps[2]+ps[3]]
        raw=np.sum(self.powers[ids],axis=-1,dtype=np.int64)
        return self.lookup_raw(raw)
    def moment(self,points):
        if not points:return self.V
        return int(self.moments([np.asarray(p,dtype=np.int64)[None,:] for p in points])[0])
    def covering(self,points):
        ps=[np.asarray(p,dtype=np.int64)[None,:] for p in points]
        rows=Counter(map(int,self.moments(ps+[self.errors])))
        rows[self.moment(points)]-=1
        return rows

def subsets(mask):
    s=mask
    while True:
        yield s
        if s==0:return
        s=(s-1)&mask

def add_row(total,row,weight,M,V):
    if weight==0:return
    for col,value in row.items():
        if value:total[col]+=weight*int(value)*(2187 if col==V else M)

def factor_gram(block,dim):
    f=block['factor_numerators']
    require(len(f)==dim and f and len(f[0])>0,'factor dimension')
    require(all(len(r)==len(f[0]) and all(type(v) is int for v in r) for r in f),'noninteger Gram factor')
    return [[sum(f[i][k]*f[j][k] for k in range(len(f[0]))) for j in range(dim)] for i in range(dim)]

def shell_counts(o):
    # For fixed root pair (0,u), enumerate ordered(v,w) by their coordinate
    # equality patterns. The multinomial multiplicity is an exact orbit size.
    V=o.V;result=np.zeros((8*64,V),dtype=np.int64)
    fac=[math.factorial(i) for i in range(8)];P=o.patterns
    agree=P[:,0]==P[:,1]
    d=o.counts@(P[:,0]!=P[:,1])
    iv=o.counts@(P[:,2]!=0);iw=o.counts@(P[:,3]!=0)
    gammas=[]
    for c,dd in zip(o.counts,d):
        twos=sum(int(c[t]) for t in range(14) if agree[t] and t!=o.pl[(0,0,0,0)])
        numerator=fac[7-int(dd)]*fac[int(dd)]*2**twos
        denominator=math.prod(fac[int(x)] for x in c)
        require(numerator%denominator==0,'noninteger conditional orbit size')
        gammas.append(numerator//denominator)
    gammas=np.array(gammas,dtype=np.int64)
    require(all(int(gammas[d==dd].sum())==2187**2 for dd in range(8)),'conditional ordered pair counts')
    started=time.monotonic()
    for start in range(0,77520,512):
        stop=min(start+512,77520)
        points=np.array([o.points(c) for c in o.counts[start:stop]],dtype=np.int64)
        u,v,w=points[:,1,:],points[:,2,:],points[:,3,:]
        indices=o.moments([u[:,None,:],v[:,None,:],w[:,None,:],o.errors[None,:,:]])
        rows=d[start:stop]*64+iv[start:stop]*8+iw[start:stop]
        np.add.at(result,(rows[:,None],indices),gammas[start:stop,None])
        low=o.moments([u,v,w])
        np.add.at(result,(rows,low),-gammas[start:stop])
        if start%10240==0:print('independent shell histograms',stop,'seconds',time.monotonic()-started,flush=True)
    require(np.max(np.abs(result))<2187**2*100,'integer coefficient safety bound')
    for dd in range(8):require(np.array_equal(result[dd*64:(dd+1)*64].reshape(8,8,V),result[dd*64:(dd+1)*64].reshape(8,8,V).transpose(1,0,2)),'shell symmetry')
    shell_sizes=[math.comb(7,i)*2**i for i in range(8)]
    tensor=result.reshape(8,8,8,V)
    for dd in range(8):
        for i in range(8):
            require(np.array_equal(shell_sizes[dd]*tensor[dd,i],shell_sizes[i]*tensor[i,dd]),'radial triple-shell coefficient identity')
    return result
