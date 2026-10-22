"""Check package integrity and exact evidence bindings, not theorem validity.

Contributed under the repository MIT license.
"""
from pathlib import Path
import ast, hashlib, json, re, sys, zipfile

root=Path(__file__).resolve().parent
def sha(data): return hashlib.sha256(data).hexdigest()
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='manifest.json')
for path in files:
    if path.suffix=='.py': ast.parse(path.read_text(encoding='utf-8'))
    if path.suffix=='.json': json.loads(path.read_text(encoding='utf-8'))
    if path.suffix=='.md':
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            target=target.strip('<>').split('#')[0]
            if not target or '://' in target: continue
            if '--seal' in sys.argv and target=='manifest.json': continue
            assert (path.parent/target).exists(), ('Missing link',str(path),target)
proof=(root/'PROOF.md').read_text(encoding='utf-8')
assert proof.count('$$')%2==0
assert all(x not in proof for x in ('\\[','\\]','\\(','\\)'))
for label in ('Lemma 2.1','Theorem 3.1','Theorem 4.2','Theorem 5.1','Theorem 6.1','Theorem 7.1','Theorem N','Proposition 9.1'):
    assert label in proof, label
with zipfile.ZipFile(root/'evidence.zip') as archive:
    names=archive.namelist()
    assert len(names)==len(set(names))
    assert all(n.startswith('evidence/') and '..' not in Path(n).parts and not Path(n).is_absolute() for n in names)
    for name in names:
        content=archive.read(name)
        if name.endswith('.py'): ast.parse(content.decode('utf-8'))
        if name.endswith('.json'): json.loads(content)
    report=json.loads((root/'replay-report.json').read_text(encoding='utf-8'))
    assert report['status']=='PASS' and len(report['tests'])==9
    for test in report['tests']:
        assert test['status']=='PASS'
        assert sha(archive.read('evidence/'+test['script']))==test['script_sha256']
        assert sha(archive.read('evidence/'+test['output']))==test['output_sha256']
    for result,cert,key in (
        ('verify-candidate-ratio-cells.json','candidate-all-ratio-cells.json','certificate_sha256'),
        ('verify-one-guard-family.json','all-one-guard-family.json','certificate_sha256'),
        ('verify-two-guards.json','two-guards-n5m14.json','search_output_sha256')):
        prefix='evidence/qmodel204-v8-search/'
        assert json.loads(archive.read(prefix+result))[key]==sha(archive.read(prefix+cert))
audit=(root/'INDEPENDENT_AUDIT.md').read_text(encoding='utf-8')
assert sha((root/'PROOF.md').read_bytes()) in audit, 'Independent audit must identify exact manuscript bytes'
metadata=json.loads((root/'execution-metadata.json').read_text(encoding='utf-8'))
assert len(metadata['records'])==13
for record in metadata['records']:
    assert record['provider']=='openai'
    assert record['configurations'] and all(c['model']=='gpt-6-astra' and c['effort']=='ultra' for c in record['configurations'])
hashes={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files}
if '--seal' in sys.argv:
    (root/'manifest.json').write_text(json.dumps({'algorithm':'SHA-256','files':hashes},indent=2)+'\n',encoding='utf-8')
else:
    assert hashes==json.loads((root/'manifest.json').read_text(encoding='utf-8'))['files']
print(json.dumps({'status':'PASS','payload_files':len(files),'evidence_files':len(names),'scientific_replays':9,'manuscript_sha256':sha((root/'PROOF.md').read_bytes()),'manifest_sha256':sha((root/'manifest.json').read_bytes())}))
