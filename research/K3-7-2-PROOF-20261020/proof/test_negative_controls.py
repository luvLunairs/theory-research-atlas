"""Corrupt valid proof inputs and ensure semantic checks reject them.

The original input files are never modified. For the Gram mutation only,
the initial file-digest check is bypassed in memory so that rejection must
come from the complete rebuilt exact aggregate, not merely a checksum.
"""
import copy,contextlib,io,json,shutil,tempfile,time
from pathlib import Path
import verify
from check_shell28_certificate import Orbits
from rebuild_scalar_products import Rebuilder

HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic();original=json.loads((HERE/'certificate.json').read_text());controls=[]
    # Full witness grammar check, beyond a file fingerprint.
    o=Orbits();rebuilder=Rebuilder(o)
    for bad in [['3000000'],['000000'],['00000000']]:
        try:rebuilder.points(bad)
        except ValueError as e:controls.append({'mutation':'invalid literal word '+bad[0],'rejected':True,'reason':str(e)})
        else:raise ValueError('invalid word accepted')
    with tempfile.TemporaryDirectory(prefix='negative-control-',dir=HERE) as directory:
        temp=Path(directory)
        for name in ['orbit-box.json','known34.txt']:shutil.copyfile(HERE/name,temp/name)
        shutil.copytree(HERE/'data',temp/'data')
        # Leave every claimed aggregate coefficient unchanged, but alter one
        # raw integer Gram factor. The new factor is still PSD by construction.
        changed=copy.deepcopy(original)
        block=next(b for b in changed['psd_factors'] if any(any(row) for row in b['factor_numerators']))
        block['factor_numerators'][0][0]+=1
        (temp/'certificate.json').write_text(json.dumps(changed))
        original_here=verify.HERE;original_sha=verify.sha
        verify.HERE=temp
        verify.sha=lambda p:verify.CERT_SHA if p.name=='certificate.json' else original_sha(p)
        try:
            with (HERE/'negative-control.log').open('w',encoding='utf-8') as stream,contextlib.redirect_stdout(stream):
                try:verify.run(temp/'must-not-be-created.json')
                except ValueError as e:
                    if str(e)!='all4295 exact aggregate coefficients match accepted certificate':raise
                    controls.append({'mutation':'one integer Gram-factor entry +1, initial certificate digest bypassed','rejected':True,'reason':str(e)})
                else:raise ValueError('changed Gram factor was accepted')
            if (temp/'must-not-be-created.json').exists():raise ValueError('failed run emitted a pass report')
        finally:verify.HERE=original_here;verify.sha=original_sha
    result={'pass':True,'controls':controls,'original_certificate_unchanged':verify.sha(HERE/'certificate.json')==verify.CERT_SHA,
      'scope':'Malformed word witnesses and full exact aggregation with a changed PSD factor. These tests do not substitute for the positive full replay.',
      'seconds':time.monotonic()-start}
    (HERE/'negative-controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
