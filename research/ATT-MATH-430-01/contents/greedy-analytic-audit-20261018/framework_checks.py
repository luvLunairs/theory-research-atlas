"""Adversarial finite checks of general sum identities, not a proof. MIT.

Uses literal unequal integer pairs as the reference. No greedy census,
old generators, third-party libraries or approval state is involved.
"""
from pathlib import Path
import argparse
import hashlib
import itertools
import json
import platform
import time

HERE=Path(__file__).resolve().parent

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def ints(a,b):
    return set(range(a,b+1))

def add(A,B,strict=False):
    return {a+b for a in A for b in B if not strict or a!=b}

def diagonal_formula(I,J):
    a,b=I;c,d=J
    if a>b or c>d:return set()
    result=ints(a+c,b+d)
    if a==b:result.discard(2*a)
    elif c==d:result.discard(2*c)
    else:
        if a==c:result.discard(2*a)
        if b==d:result.discard(2*b)
    return result

def image(m,A,I):
    return {m*q+r for q in A for r in I}

def rectangle_formula(m,A,I):
    l,u=A;a,b=I
    if l>u or a>b:return set()
    return (image(m,ints(2*l,2*u),ints(2*a+1,2*b-1)) |
            image(m,ints(2*l+1,2*u-1),{2*a,2*b}))

def check():
    interval_inputs=[(a,b) for a in range(-2,4) for b in range(a,4)]+[(1,0)]
    mixed_count=0
    for I,J in itertools.product(interval_inputs,repeat=2):
        assert diagonal_formula(I,J)==add(ints(*I),ints(*J),True),(I,J)
        mixed_count+=1
    blocks=[set(),{0},{1},{0,1},{0,2},{0,1,2}]
    cylinder_count=rectangle_count=0
    for m in range(1,6):
        residues=[ints(a,b) for a in range(m) for b in range(a,m)]+[set()]
        cylinders=list(itertools.product(blocks,residues))
        for (A,I),(B,J) in itertools.product(cylinders,repeat=2):
            literal=add(image(m,A,I),image(m,B,J),True)
            formula=image(m,add(A,B,True),add(I,J))|image(m,add(A,B),add(I,J,True))
            assert literal==formula,(m,A,I,B,J)
            cylinder_count+=1
        for A in [(a,b) for a in range(3) for b in range(a,3)]+[(1,0)]:
            for I in [(a,b) for a in range(m) for b in range(a,m)]+[(1,0)]:
                C=image(m,ints(*A),ints(*I))
                assert rectangle_formula(m,A,I)==add(C,C,True),(m,A,I)
                rectangle_count+=1
    # Refute the unguarded rectangle specialization literally.
    m=3
    empty_C=image(m,ints(0,1),ints(1,0))
    unguarded=image(m,ints(0,2),ints(3,-1))|image(m,ints(1,1),{2,0})
    assert empty_C==set() and unguarded=={3,5}
    assert add({2},{1,2,3},True)=={3,5}
    # Refute extending the f4 k>=6 row to k=5; distinct late entries.
    k=5;m=32*k+1
    x=6*m+8*(2*k-5);y=7*m+8*(2*k-5);z=13*m+8*(2*k)
    assert (x,y,z)==(1006,1167,2173) and x!=y and x+y==z
    return dict(mixed_interval_cases=mixed_count,cylinder_cases=cylinder_count,
                rectangle_cases=rectangle_count,
                retained_refutations={
                    'unguarded_empty_residue_interval':dict(m=3,A=[0,1],I=[1,0],
                                                           actual=[],false_output=sorted(unguarded)),
                    'singleton_interior_diagonal':dict(I=[2,2],J=[1,3],strict_sum=[3,5]),
                    'invalid_f4_formula_at_k5':dict(m=m,x=x,y=y,z=z)})

def main():
    p=argparse.ArgumentParser();p.add_argument('--verify-only',action='store_true');args=p.parse_args()
    cpu=time.process_time();wall=time.perf_counter()
    result=dict(outcome='pass',scope='Finite adversarial checks of written general identities; not universal proof',
                results=check(),python=platform.python_version(),
                hashes={name:sha(HERE/name) for name in ('framework.md','framework_checks.py')},
                independent_verification=False,formal_verification=False)
    result.update(process_cpu_seconds=time.process_time()-cpu,wall_seconds=time.perf_counter()-wall)
    dest=HERE/'framework-checks.json'
    if args.verify_only:
        old=json.loads(dest.read_text(encoding='utf-8'))
        stable=lambda x:{k:v for k,v in x.items() if k not in ('process_cpu_seconds','wall_seconds')}
        assert stable(old)==stable(result),'Exact retained outcome or hash mismatch'
        print('PASS: general strict-sum identities, empty/singleton cases and retained failed extension; read-only.')
    else:
        dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result,indent=2))

if __name__=='__main__':main()
