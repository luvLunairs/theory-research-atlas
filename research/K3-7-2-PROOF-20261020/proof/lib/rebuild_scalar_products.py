"""Reconstruct cover-product scalar rows without coefficient files or solvers.

Witness metadata contains literal ternary words only. Rows are expansions of
  E[ prod_a (sum_{v in B2(a)} X_v - 1) prod_b X_b prod_c (1-X_c) ] >= 0.
All factors are nonnegative for every radius-two cover.  No symmetry of the
code is imposed; o identifies expectations under uniform isometry averaging.

Up to three ball factors are multiplied by literal 99-point enumeration.
Four factors use a freshly constructed ordered-tuple adjacency operator:
A1^2=14I+A1+2A2, hence B2=(A1^2+A1-12I)/2.  No cached coefficient matrix,
discovery convolution, pickle, numerical eigenvalue, or solver is read.
"""
from pathlib import Path
from collections import Counter
import itertools,json,time
import numpy as np
from scipy.sparse import coo_matrix

METADATA=Path(__file__).resolve().parent.parent/'data/scalar-product-witnesses.json'
QUARTIC='quartic-cuts29-r1.npz'

def require(ok,why):
    if not ok:raise ValueError(why)

def sparse(row):return {int(i):int(row[i]) for i in np.flatnonzero(row)}

class Rebuilder:
    def __init__(self,o):
        self.o=o;self.V=o.V;require(self.V==4085,'degree-four orbit count')
        self.ball_cache={};self.row_cache={};self.adjacency=None
    def points(self,strings):
        require(isinstance(strings,list),'point list type')
        require(all(type(s) is str and len(s)==7 and set(s)<=set('012') for s in strings),'literal ternary words')
        return [np.array([int(c) for c in s],dtype=np.int64) for s in strings]
    def ball(self,p):
        key=tuple(map(int,p))
        if key not in self.ball_cache:
            result=self.o.words[np.count_nonzero(self.o.words!=p,axis=1)<=2]
            require(len(result)==99,'literal radius-two ball size');self.ball_cache[key]=result
        return self.ball_cache[key]
    def monomial_sum(self,balls,fixed):
        require(len(balls)+len(fixed)<=4,'monomial degree exceeds four')
        row=np.zeros(self.V+1,dtype=np.int64)
        if not balls:row[self.o.moment(fixed)]=1
        elif len(balls)==1:
            ids=self.o.moments([balls[0]]+fixed)
            row+=np.bincount(ids.ravel(),minlength=self.V+1)
        elif len(balls)==2:
            first=[np.repeat(balls[0],99,axis=0),np.tile(balls[1],(99,1))]
            ids=self.o.moments(first+fixed);row+=np.bincount(ids.ravel(),minlength=self.V+1)
        elif len(balls)==3:
            first=[np.repeat(balls[0],99,axis=0),np.tile(balls[1],(99,1))]
            for p in balls[2]:
                ids=self.o.moments(first+[p]+fixed);row+=np.bincount(ids.ravel(),minlength=self.V+1)
        else:raise ValueError('literal multiplication limited to three balls')
        require(int(row.sum())==99**len(balls),'literal expansion mass')
        return row
    def direct(self,covers,ones,zeros):
        row=np.zeros(self.V+1,dtype=np.int64);balls=[self.ball(p) for p in covers]
        for active in range(1<<len(covers)):
            selected=[balls[i] for i in range(len(balls)) if active&(1<<i)]
            for absent in range(1<<len(zeros)):
                fixed=ones+[zeros[i] for i in range(len(zeros)) if absent&(1<<i)]
                sign=(-1)**(len(covers)-active.bit_count()+absent.bit_count())
                row+=sign*self.monomial_sum(selected,fixed)
        return row
    def build_adjacency(self):
        o=self.o;T=len(o.counts);require(T==77520,'ordered tuple composition count')
        points=np.array([o.points(c) for c in o.counts],dtype=np.int64)
        self.tuple_points=points;self.raw=o.counts@o.powers;order=np.argsort(self.raw);sorted_raw=self.raw[order]
        self.raw_order=order;self.sorted_raw=sorted_raw;self.adjacency=[]
        # Enumerate each actual coordinate and its two alternative symbols.
        for slot in range(4):
            sources=[];targets=[]
            for coordinate in range(7):
                column=points[:,:,coordinate]
                oldpattern=o.pattern_lookup[27*column[:,0]+9*column[:,1]+3*column[:,2]+column[:,3]]
                for delta in (1,2):
                    changed=column.copy();changed[:,slot]=(changed[:,slot]+delta)%3
                    pattern=o.pattern_lookup[27*changed[:,0]+9*changed[:,1]+3*changed[:,2]+changed[:,3]]
                    raw=self.raw-o.powers[oldpattern]+o.powers[pattern];pos=np.searchsorted(sorted_raw,raw)
                    require(np.array_equal(sorted_raw[pos],raw),'ordered tuple neighbor encoding')
                    sources.append(np.arange(T));targets.append(order[pos])
            mat=coo_matrix((np.ones(14*T,dtype=np.int64),(np.concatenate(sources),np.concatenate(targets))),shape=(T,T)).tocsr()
            require(np.all(np.asarray(mat.sum(axis=1)).ravel()==14),'one-coordinate degree')
            self.adjacency.append(mat.T.tocsr())
        self.projections=[]
        for mask in range(16):
            indices=o.moments([points[:,i] for i in range(4) if mask&(1<<i)]) if mask else np.full(T,self.V,dtype=np.int64)
            self.projections.append(indices)
        # Literal all2187 control for the one-coordinate two-step identity.
        wt=np.count_nonzero(o.words,axis=1);two_step=np.zeros(2187,dtype=np.int64)
        for p in o.words[wt==1]:two_step+=np.count_nonzero(o.words!=p,axis=1)==1
        require(np.array_equal(two_step,np.where(wt==0,14,np.where(wt==1,1,np.where(wt==2,2,0)))),'A1 squared identity')
    def apply_ball(self,weights,slot):
        A=self.adjacency[slot];first=A@weights;numerator=A@first+first-12*weights
        require(np.all(numerator%2==0),'ball recurrence integrality')
        result=numerator//2
        require(np.min(result)>=0 and int(result.sum())==99*int(weights.sum()),'ball recurrence positivity and mass')
        return result
    def recurrence(self,points,cover_mask,fixed_mask):
        if self.adjacency is None:self.build_adjacency()
        p=np.asarray(points,dtype=np.int64)
        require(p.shape==(4,7),'four ordered anchor words')
        pattern=self.o.pattern_lookup[27*p[0]+9*p[1]+3*p[2]+p[3]]
        raw=int(np.sum(self.o.powers[pattern]));pos=int(np.searchsorted(self.sorted_raw,raw))
        require(int(self.sorted_raw[pos])==raw,'witness tuple state')
        initial=np.zeros(len(self.raw),dtype=np.int64);initial[self.raw_order[pos]]=1
        weights={0:initial};row=np.zeros(self.V+1,dtype=np.int64)
        for active in range(16):
            if active&~cover_mask:continue
            if active:
                bit=active&-active;weights[active]=self.apply_ball(weights[active^bit],bit.bit_length()-1)
            sign=(-1)**(cover_mask.bit_count()-active.bit_count())
            np.add.at(row,self.projections[active|fixed_mask],sign*weights[active])
        return row
    def row(self,witness):
        require(set(witness)=={'covers','ones','zeros'},'product witness schema')
        key=json.dumps(witness,sort_keys=True,separators=(',',':'))
        if key in self.row_cache:return self.row_cache[key]
        covers=self.points(witness['covers']);ones=self.points(witness['ones']);zeros=self.points(witness['zeros'])
        require(len(covers)+len(ones)+len(zeros)<=4,'product witness degree')
        if len(covers)==4:
            require(not ones and not zeros,'four-cover atoms');row=self.recurrence(covers,15,0)
        else:row=self.direct(covers,ones,zeros)
        require(int(row.sum())==(0 if zeros else 98**len(covers)),'all-one polynomial evaluation')
        answer=sparse(row);self.row_cache[key]=answer;return answer

def rebuild(certificate,o):
    """Return nonzero certificate rows; indices0..4084 are moments,4085 constant."""
    metadata=json.loads(METADATA.read_text(encoding='utf-8'))['families']
    wanted={g['name']:{int(i) for i,v in zip(g['row_indices'],g['weight_numerators']) if int(v)} for g in certificate['linear_groups']}
    require(set(metadata)=={'two_cover','accumulated_full_r0',QUARTIC},'scalar-product family names')
    builder=Rebuilder(o);result={};started=time.monotonic();control_done=False
    for name,rows in metadata.items():
        expected={i for i in wanted.get(name,set()) if name!=QUARTIC or i<30}
        require(set(map(int,rows))==expected,'witness/certificate row selection '+name)
        result[name]={}
        for number,(index,witness) in enumerate(rows.items()):
            result[name][int(index)]=builder.row(witness)
            # One literal99^3 expansion also verifies the recurrence/projection.
            if not control_done and len(witness['covers'])==3 and len(witness['ones'])==1 and not witness['zeros']:
                points=builder.points(witness['covers']+witness['ones'])
                require(sparse(builder.recurrence(points,7,8))==result[name][int(index)],'literal triple/recurrence cross-control');control_done=True
            if (number+1)%100==0:print('scalar-products',name,number+1,'seconds',time.monotonic()-started,flush=True)
    require(control_done,'triple-product recurrence control exercised')
    return result
