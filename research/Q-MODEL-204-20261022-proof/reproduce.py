"""Replay the nine scientific checks in isolated copies; never edit this package."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse, datetime, hashlib, json, shutil, subprocess, sys, time, zipfile

p=argparse.ArgumentParser();p.add_argument('--jobs',type=int,default=2);p.add_argument('--only',nargs='+');a=p.parse_args()
assert 1<=a.jobs<=4
package=Path(__file__).resolve().parent;project=package.parents[1]
assert (project/'CONTRIBUTING.md').is_file()
replay=project/'work'/('qmodel204-proof-replay-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f'));replay.mkdir()
with zipfile.ZipFile(package/'evidence.zip') as archive:
    assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in archive.namelist())
    archive.extractall(replay/'frozen')
evidence=replay/'frozen/evidence'
tests=[
 ('root/check_residual_quota_independent.py',[],'root/check_residual_quota_independent.json'),
 ('root/verify_efx_nash_obstruction.py',['--input','three-agent-input.json','--output','verify_efx_nash_three_agents.json'],'root/verify_efx_nash_three_agents.json'),
 ('theory/check_modular_safe_capacity.py',[],'theory/check_modular_safe_capacity.json'),
 ('theory/check_efx_nash_family_analytic.py',[],'theory/check_efx_nash_family_analytic.json'),
 ('structure/check_rounded_phase_cores.py',[],'structure/check_rounded_phase_cores.json'),
 ('search/verify_three_agent_nash.py',[],'search/verify-three-agent-nash.json'),
 ('search/verify_candidate_ratio_cells.py',[],'search/verify-candidate-ratio-cells.json'),
 ('search/verify_one_guard_family.py',[],'search/verify-one-guard-family.json'),
 ('search/verify_two_guards.py',[],'search/verify-two-guards.json'),
]
def path(short):return 'qmodel204-v8-'+short
if a.only:
    assert set(a.only)<=set(t[2]for t in tests),'Unknown test output'
    tests=[t for t in tests if t[2]in a.only]
def scientific(x):
    if isinstance(x,dict):return {k:scientific(v)for k,v in x.items()if k not in {'seconds','elapsed_seconds'}}
    if isinstance(x,list):return list(map(scientific,x))
    return x
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(index,test):
    name,args,out=test;start=time.monotonic();job=replay/f'job-{index:02d}'
    shutil.copytree(evidence,job,ignore=shutil.ignore_patterns('__pycache__'))
    script=job/path(name)
    proc=subprocess.run([sys.executable,str(script),*args],cwd=script.parent,capture_output=True,text=True,encoding='utf-8')
    (job/(path(out)+'.log')).write_text(proc.stdout+proc.stderr,encoding='utf-8')
    assert proc.returncode==0,(name,proc.returncode,proc.stderr[-4000:])
    actual=json.loads((job/path(out)).read_text(encoding='utf-8'))
    expected=json.loads((evidence/path(out)).read_text(encoding='utf-8'))
    assert actual['status']=='PASS'
    assert scientific(actual)==scientific(expected),('Scientific output changed',out)
    return dict(script=path(name),arguments=args,output=path(out),status='PASS',
        script_sha256=digest(evidence/path(name)),output_sha256=digest(evidence/path(out)),
        seconds=round(time.monotonic()-start,3))
results=[]
with ThreadPoolExecutor(max_workers=a.jobs)as pool:
    for future in as_completed([pool.submit(run,k,t)for k,t in enumerate(tests)]):
        row=future.result();results.append(row);print(json.dumps(row),flush=True)
report=dict(status='PASS',python=sys.version,jobs=a.jobs,tests=sorted(results,key=lambda x:x['output']),
    comparison='Exact retained JSON equality, ignoring only seconds and elapsed_seconds. No project solver imported by any of the nine verification scripts. This is executable evidence, not formal certification or human review.')
(replay/'replay-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',tests=len(results),report=str(replay/'replay-report.json'))),flush=True)
