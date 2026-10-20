"""Independent coefficient audit: 209 conditional Gram squares and 4 quartics.

The 30 remaining quartic rows are separately reconstructed by the scalar
products auditor. No discovery coefficient generator is imported here.
All products used in enumeration are bounded below 2**63; aggregate digests
are over exact integers, and the final certificate uses Python integers.
"""
import argparse, hashlib, json, math, pickle, time
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix, hstack, load_npz, save_npz, vstack
from check_shell28_certificate import Orbits, require

HERE=Path(__file__).resolve().parent
PHASE=HERE.parent
SNAPSHOT=PHASE/'lower/full-cover-fourier-quadratic-fivepoint-dual-29.pkl'
SNAPSHOT_HASH='e57debc476976b5e293c4c03b88f943243c2704fccf5bcb9d414a67766322f37'
ORBIT_CHECKER_HASH='9b166642dccbebbfcde141783b7c91a07b47c29791e2ed23dd012a65998c2671'
PSDNAME='selected-psd-cuts-29-01234567-0-0-CLARABEL-boolean8-integer-products-quartic-psdoracle.npz'
QUARTICNAME='quartic-cuts29-r1.npz'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def canonical(matrix):
    matrix=csr_matrix(matrix).copy()
    matrix.sum_duplicates();matrix.sort_indices();matrix.eliminate_zeros()
    require(all(int(x)==x for x in matrix.data),'noninteger matrix')
    payload=[list(matrix.shape),matrix.indptr.tolist(),matrix.indices.tolist(),[int(x) for x in matrix.data]]
    return hashlib.sha256(json.dumps(payload,separators=(',',':')).encode()).hexdigest()

def embed(matrix,V=4294):
    require(matrix.shape[1]==4086,'old moment shape')
    return hstack([matrix[:,:4085],csr_matrix((matrix.shape[0],V-4085)),matrix[:,4085:]],format='csr')

def same(a,b):
    require(a.shape==b.shape,'matrix shape mismatch')
    delta=csr_matrix(a-b);delta.eliminate_zeros()
    require(delta.nnz==0,'coefficient discrepancy')

def gram_squares(o,metadata):
    """E[X_0 X_u (sum_i v_i T_i)**2], with T_i shell indicator sums.

    For d(0,u)=d, T_(b,r0,r1) sums X_v over points v with b nonzero
    positions where u=0, r0 zeros where u=1, and r1 ones where u=1.
    Count ordered(v,w) by equality patterns of(0,u,v,w).
    """
    P=o.patterns;c=o.counts
    dd=c@(P[:,0]!=P[:,1])
    same_anchor=P[:,0]==P[:,1]
    bv=c@(same_anchor&(P[:,2]!=P[:,0]))
    bw=c@(same_anchor&(P[:,3]!=P[:,0]))
    v0=c@(~same_anchor&(P[:,2]==P[:,0]));v1=c@(~same_anchor&(P[:,2]==P[:,1]))
    w0=c@(~same_anchor&(P[:,3]==P[:,0]));w1=c@(~same_anchor&(P[:,3]==P[:,1]))
    fs=[math.factorial(i) for i in range(8)]
    gamma=[]
    for row,d in zip(c,dd):
        twos=int(row@(same_anchor&np.any(P!=P[:,0,None],axis=1)))
        num=fs[7-int(d)]*fs[int(d)]*2**twos
        den=math.prod(fs[int(n)] for n in row)
        require(num%den==0,'nonintegral ordered-pair orbit cardinality')
        gamma.append(num//den)
    gamma=np.array(gamma,dtype=np.int64)
    indices={}
    for d in range(1,8):
        labels=[(b,r0,r1) for b in range(8-d) for r0 in range(d+1) for r1 in range(d-r0+1)]
        lookup={q:i for i,q in enumerate(labels)}
        selected=np.flatnonzero(dd==d)
        require(int(gamma[selected].sum())==2187**2,'conditional pair cardinality')
        vi=np.array([lookup[(int(bv[j]),int(v0[j]),int(v1[j]))] for j in selected])
        wi=np.array([lookup[(int(bw[j]),int(w0[j]),int(w1[j]))] for j in selected])
        indices[d]=(selected,vi,wi,len(labels))
    rows=[]
    for record in metadata:
        kind,block=record['block'];require(kind=='pair' and block%3==0,'unsupported non-both Gram square')
        d=block//3+1;selected,vi,wi,dimension=indices[d]
        require(all(type(x) is int for x in record['vector']),'noninteger vector')
        vector=np.array(record['vector'],dtype=np.int64)
        require(len(vector)==dimension,'vector dimension')
        # This bound controls every intermediate sum, including signed sums.
        require(max(map(abs,record['vector']))**2*2187**2<2**63,'int64 sum bound')
        coefficients=np.zeros(o.V+1,dtype=np.int64)
        np.add.at(coefficients,o.orbit_by_composition[selected],gamma[selected]*vector[vi]*vector[wi])
        divisor=math.gcd(*map(int,coefficients));require(divisor>0,'zero square')
        rows.append(coefficients//divisor)
    return csr_matrix(np.array(rows,dtype=np.int64))

def conditional_cubic(o,d):
    """Direct expansion of X_u*(A_0-1)*(A_0-3)*(A_0-4).

    Enumerate all ordered triples of the 99 actual error words. This does
    not use the discovery histogram convolution or its coefficient cache.
    """
    u=np.array([1]*d+[0]*(7-d),dtype=np.int64)
    errors=o.errors
    power=[]
    row=np.zeros(o.V+1,dtype=np.int64);row[o.moment([u])]=1;power.append(row)
    for k in (1,2,3):
        row=np.zeros(o.V+1,dtype=np.int64)
        if k==1:
            np.add.at(row,o.moments([u[None,:],errors]),1)
        elif k==2:
            ix=o.moments([u[None,None,:],errors[:,None,:],errors[None,:,:]])
            np.add.at(row,ix.ravel(),1)
        else:
            for e in errors:
                ix=o.moments([u[None,None,:],e[None,None,:],errors[:,None,:],errors[None,:,:]])
                np.add.at(row,ix.ravel(),1)
        require(int(row.sum())==99**k,'ordered ball tuple count')
        power.append(row)
    return -12*power[0]+19*power[1]-8*power[2]+power[3]
