"""Standalone exact replay of the accepted K_3(7,2)>=30 certificate.

Every nonzero scalar and Gram coefficient is regenerated from finite words,
coordinate partitions, or integer polynomial products. No solver, pickle,
saved coefficient matrix, previous pass report, or floating dual is loaded.
"""
if not __debug__:
    raise RuntimeError('Run without -O, -OO, or PYTHONOPTIMIZE: exact audit assertions are required.')
import argparse,hashlib,itertools,json,math,sys,time
from collections import Counter
from fractions import Fraction
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'lib'));sys.dont_write_bytecode=True
import numpy as np
from scipy.sparse import csr_matrix
from audit_fivepoint import Canonical
from check_shell28_certificate import Orbits,subsets,shell_counts,require
from audit_full29_root_scalars import gram_squares,conditional_cubic
import audit_fourier_pair,rebuild_radial,rebuild_fourier_quadratic

CERT_SHA='7aff789b16f702aac7dc3cac37642760878bc6fc0ff25f52214f0c8e1922a4c4'
BOX_SHA='355eb1930b175fe7192ad6172c3e23a41f51876905be5d0550a06fd660963f40'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def sparse_row(a,i=0):
    a=csr_matrix(a);a.sum_duplicates();a.sort_indices()
    require(np.array_equal(a.data,np.rint(a.data)),'integer polynomial coefficients')
    return {int(a.indices[p]):int(a.data[p]) for p in range(a.indptr[i],a.indptr[i+1]) if a.data[p]}


def fifth_coordinates(o,canonical):
    ball1=list(map(int,np.flatnonzero(np.count_nonzero(o.words,axis=1)<=1)))
    actual=list(itertools.combinations(ball1,4));keys=canonical.codes(o.words[np.array(actual)])
    reps4={}
    for key,subset in zip(keys,actual):reps4.setdefault(int(key),subset)
    require(len(reps4)==5,'five B1 four-point orbits')
    reps5={};extensions=[]
    for code,subset in reps4.items():
        row=Counter({code:4});extra=[w for w in range(2187) if w not in subset]
        points=np.concatenate([np.tile(o.words[list(subset)],(len(extra),1,1)),o.words[extra,None,:]],axis=1)
        for key,pp in zip(canonical.codes(points),points):
            reps5.setdefault(int(key),pp);row[int(key)]+=1
        require(sum(row.values())==2187,'all point extensions counted');extensions.append(row)
    codes=o.codes+sorted(reps5);require(len(codes)==4294 and len(set(codes))==4294,'4294 moment orbits')
    lookup={code:i for i,code in enumerate(codes)}
    fixed=[{lookup[k]:int(v) for k,v in row.items()} for row in extensions]
    return codes,lookup,reps4,reps5,fixed


def run(output):
    start=time.monotonic()
    require(sha(HERE/'certificate.json')==CERT_SHA,'original certificate digest')
    require(sha(HERE/'orbit-box.json')==BOX_SHA,'original box digest')
    cert=json.loads((HERE/'certificate.json').read_text());box=json.loads((HERE/'orbit-box.json').read_text())
    require(cert['size']==29 and cert['variables']==4294,'target')
    require(cert['weight_denominator_bits']==120 and cert['factor_denominator_bits']==60,'exact dyadic scales')
    M=29;V=4294;total=[0]*(V+1);groups={g['name']:g for g in cert['linear_groups']}
    require(len(groups)==len(cert['linear_groups'])==9,'scalar family count')
    def active(name):
        g=groups[name];ids=g['row_indices'];weights=g['weight_numerators']
        require(ids==sorted(set(ids)) and len(ids)==len(weights),'ordered scalar support')
        require(all(type(i)is int and i>=0 for i in ids) and all(type(w)is int and w>=0 for w in weights),'nonnegative integer weights')
        return {i:w for i,w in zip(ids,weights) if w}
    def add(row,w=1,width=V):
        require(type(w)is int,'integer multiplier')
        for c,v in row.items():
            c=V if int(c)==width else int(c);v=int(v)
            require(0<=c<=V,'moment column')
            total[c]+=w*v*(2187 if c==V else M)
    def contract(raw,f,width):
        d=len(f);require(d>0 and all(len(row)==len(f[0]) and all(type(v)is int for v in row) for row in f),'integer rectangular factor')
        raw=csr_matrix(raw);require(raw.shape==(d*d,width+1),'Gram coefficient shape')
        for i in range(d):
            for j in range(d):
                w=sum(f[i][a]*f[j][a] for a in range(len(f[0])))
                if w:add(sparse_row(raw,d*i+j),w,width)
    o=Orbits();canonical=Canonical();codes,lookup,reps4,reps5,fixed=fifth_coordinates(o,canonical)
    metadata=json.loads((HERE/'data/scalar-selection.json').read_text());covered={name:set() for name in groups}
    require(not active('old') and not active('pair_integer'),'zero unused scalar families')
    cover_cache={}
    for index,w in active('boolean_cover_all').items():
        mask,t=divmod(index,o.T);require(0<=mask<8 and 0<=t<o.T,'Boolean cover index')
        points=o.root_representatives[t][1:];row=Counter()
        for sub in subsets(7^mask):
            key=(t,mask|sub)
            if key not in cover_cache:cover_cache[key]=o.covering([points[i] for i in range(3) if key[1]&(1<<i)])
            for c,v in cover_cache[key].items():row[c]+=(-1 if sub.bit_count()%2 else 1)*v
        add(row,w,o.V);covered['boolean_cover_all'].add(index)
    for index,w in active('atoms4').items():
        source=metadata['atoms4'][str(index)];mask,t=divmod(source,o.V);require(0<=mask<16,'four-atom mask')
        points=o.representatives[t];row=Counter()
        for sub in subsets(15^mask):row[o.moment([points[j] for j in range(4) if (mask|sub)&(1<<j)])]+=(-1 if sub.bit_count()%2 else 1)
        add(row,w,o.V);covered['atoms4'].add(index)
    for index,w in active('atoms5').items():
        pi,ones=divmod(index,32);require(0<=pi<209,'fifth atom index');points=reps5[codes[4085+pi]];row=Counter()
        for sub in subsets(31^ones):
            mask=ones|sub;column=V if not mask else lookup[int(canonical.codes(points[[i for i in range(5) if mask&(1<<i)]])[0])]
            row[column]+=(-1 if sub.bit_count()%2 else 1)
        add(row,w);covered['atoms5'].add(index)
    name=metadata['selected_psd_name'];require(name in groups,'conditional square family')
    ids=sorted(active(name));records=[metadata['selected_psd'][str(i)] for i in ids]
    squares=gram_squares(o,records)
    for n,i in enumerate(ids):add(sparse_row(squares,n),active(name)[i],o.V);covered[name].add(i)
    require(all((a-1)*(a-3)*(a-4)>=0 for a in range(1,M+1)),'conditional integer cubic is nonnegative')
    for index,w in active('quartic-cuts29-r1.npz').items():
        if index<30:continue
        require(30<=index<34,'conditional cubic index');d=[7,3,3,7][index-30]
        add(dict(enumerate(conditional_cubic(o,d))),w,o.V);covered['quartic-cuts29-r1.npz'].add(index)
    from rebuild_scalar_products import rebuild
    products=rebuild(cert,o)
    for name,rows in products.items():
        require(name in ('two_cover','accumulated_full_r0','quartic-cuts29-r1.npz'),'cover-product family')
        for index,row in rows.items():
            require(index in active(name) and index not in covered[name],'cover-product support')
            add(row,active(name)[index],o.V);covered[name].add(index)
    require(all(covered[name]==set(active(name)) for name in groups),'every nonzero scalar row regenerated')
    print('all4753 nonzero scalar rows regenerated',time.monotonic()-start,flush=True)
    nonzero=[]
    for block in cert['psd_factors']:
        f=block['factor_numerators'];require(f and f[0] and all(len(row)==len(f[0]) and all(type(x)is int for x in row) for row in f),'integer Gram factor')
        if any(any(row) for row in f):nonzero.append(block)
    require(len(nonzero)==16,'nonzero Gram support')
    shells=shell_counts(o);radial=rebuild_radial.rebuild(o.codes);fp=audit_fourier_pair.rebuild(o.codes)
    fq=rebuild_fourier_quadratic.rebuild(o.codes)
    nonzero_columns=0
    for b in nonzero:
        name=b['name'];kind,index=name[:2];f=b['factor_numerators'];nonzero_columns+=sum(any(row[j] for row in f) for j in range(len(f[0])))
        if kind=='shell':
            require(index in (6,8,10,12,14) and len(f)==8,'present shell support')
            raw=csr_matrix(np.column_stack([shells[64*(index//2):64*(index//2+1)],np.zeros(64,dtype=np.int64)]))
        elif kind=='radial_selected_integer':
            weights=index;j=name[2];require(len(weights)==8 and all(type(x)is int for x in weights) and type(j)is int,'integer shell-count polynomial')
            amplitude=sum(abs(w) for w in weights)*2187
            require((amplitude**2+(2*abs(j)+1)*amplitude+abs(j*(j+1)))*2187**2<2**63,'integer localizer coefficient bound')
            rows=[]
            for a in range(8):
                for b0 in range(8):
                    row=j*(j+1)*radial[tuple(sorted((a,b0)))].copy()
                    for c,w in enumerate(weights):
                        if w:row-=(2*j+1)*w*radial[tuple(sorted((a,b0,c)))]
                        for e,v in enumerate(weights):
                            if w*v:row+=w*v*radial[tuple(sorted((a,b0,c,e)))]
                    rows.append(row)
            raw=csr_matrix(np.array(rows))
        elif kind=='fourier_pair':require(index==0,'Fourier pair support');raw=csr_matrix(fp[index])
        elif kind=='fourier_quadratic':
            require(0<=index<8,'Fourier quadratic frequency');raw=csr_matrix(np.column_stack([fq[index].toarray(),np.zeros(fq[index].shape[0],dtype=np.int64)]))
        else:raise ValueError('unexpected nonzero Gram family')
        contract(raw,f,o.V)
    require(nonzero_columns==33,'33 integer Gram columns')
    print('all33 Gram columns regenerated and contracted',time.monotonic()-start,flush=True)
    require([g['name'] for g in cert['equalities']]==['old','fifth'],'equality family names')
    weights=cert['equalities'][0]['weight_numerators'];require(len(weights)==95 and all(type(w)is int for w in weights),'old equality weights')
    zero=np.zeros((1,7),dtype=np.int64)
    for i,w in enumerate(weights):
        x,y=o.lower_representatives[i]
        for c,n in Counter(map(int,o.moments([zero,x[None,:],y[None,:],o.words]))).items():total[c]+=w*n
        total[i]-=M*w
    weights=cert['equalities'][1]['weight_numerators'];require(len(weights)==5 and all(type(w)is int for w in weights),'fifth equality weights')
    for i,(w,row,code) in enumerate(zip(weights,fixed,reps4)):
        for c,n in row.items():total[c]+=w*n
        total[lookup[code]]-=M*w
    singleton=cert['singleton_equality_weight_numerator'];require(type(singleton)is int,'singleton equality multiplier');total[0]+=singleton;total[-1]-=singleton
    require(total==cert['combined_integer_coefficients'],'all4295 exact aggregate coefficients match accepted certificate')
    require(total[-1]+sum(max(0,c) for c in total[:-1])==cert['strict_upper_bound_integer'],'unit-box arithmetic')
    degrees=[];sizes=[]
    for pp in o.representatives:
        unique=np.array(list(dict.fromkeys(map(tuple,pp))));degrees.append(len(unique));sizes.append(canonical.orbit_size(unique))
    for code in codes[4085:]:degrees.append(5);sizes.append(canonical.orbit_size(reps5[code]))
    for degree in range(1,5):require(sum(s for d,s in zip(degrees,sizes) if d==degree)==math.comb(2187,degree),'complete orbit-size total')
    bounds=[min(Fraction(1),Fraction(2187*math.comb(M,k),M*s)) for k,s in zip(degrees,sizes)]
    require([[b.numerator,b.denominator] for b in bounds]==box['bounds'],'all exact orbit bounds reconstructed')
    upper=Fraction(total[-1])+sum(c*b for c,b in zip(total,bounds) if c>0)
    require(upper.numerator==box['numerator'] and upper.denominator*2**120==box['denominator'] and upper<0,'strict exact rational contradiction')
    from check_cover import read_code,check_code
    _,words=read_code(HERE/'known34.txt');cover=check_code(words);require(cover['code_size']==34 and cover['is_radius_2_cover'] and cover['ambient_words_checked']==2187,'independent known cover check')
    report={'pass':True,'certificate_sha256':CERT_SHA,'orbit_box_sha256':BOX_SHA,'checker_sha256':sha(Path(__file__)),
      'source_file_sha256':{str(p.relative_to(HERE)).replace('\\','/'):sha(p) for p in sorted(HERE.rglob('*.py')) if 'negative-control-' not in str(p)},
      'variables':V,'nonzero_scalar_rows_reconstructed':4753,'nonzero_Gram_blocks_reconstructed':16,'nonzero_integer_Gram_columns':33,
      'equalities_reconstructed':101,'aggregate_coefficients_checked':len(total),'all_orbit_bounds_reconstructed':True,
      'strict_upper_bound_numerator':upper.numerator,'strict_upper_bound_denominator':upper.denominator*2**120,
      'proof_dependencies':'Python integer/fraction arithmetic; NumPy and SciPy for bounded integer enumeration and sparse arrays. No solver, floating optimization result, pickle, coefficient cache, or previous audit pass is used.',
      'known34_file_sha256':sha(HERE/'known34.txt'),'known34_exact_check':cover,
      'conclusion':'Excludes cardinality29. Any smaller covering code could be enlarged to29, so K_3(7,2)>=30. The independently checked known34 code gives K_3(7,2)<=34.',
      'limits':'Computational mathematical verification, not a proof-assistant formalization. Novelty and external scientific review remain separate.',
      'seconds':time.monotonic()-start}
    output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'verification.json');a=p.parse_args();run(a.output)
