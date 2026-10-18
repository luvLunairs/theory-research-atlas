"""Validate structured records, relationships and research evidence metadata.

The schema evaluator implements only the explicitly listed JSON Schema keywords
used in this repository and fails on unsupported keywords. A general Draft 2020-12
validator may also consume the schema files. This is not a general validator.
"""
import argparse
import json
import sys
from pathlib import Path

from research_records import validate_research_records
from artifact_integrity import validate_record_artifacts
from machine_verification import validate_machine_records
from schema_validation import read, schema_check

ROOT=Path(__file__).resolve().parents[1]
def read_records(directory):
    records=[]
    for path in sorted(directory.glob('*.json')):
        record=read(path)
        if isinstance(record,dict) and record.get('id') and path.stem!=record['id']:
            raise ValueError(f'{path}: filename must match the record ID')
        records.append(record)
    return records

def load_dataset(root=ROOT):
    return {key:read(root/'data'/path) for key,path in {'project':'project.json','nodes':'taxonomy.json','sources':'sources.json',
        'candidates':'candidates.json','source_map':'source-map.json','scope':'scope-decisions.json','aliases':'source-aliases.json',
        'vocabularies':'vocabularies.json','coverage_notes':'coverage-notes.json',
        'profiles':'research-profiles.json','checks':'candidate-checks.json','landmarks':'landmark-problems.json',
        'literature_checks':'literature-checks.json'}.items()}|{
        key:read_records(root/'data'/directory)
        for key,directory in [('cards','cards'),('attempts','attempts'),('reviews','reviews'),
                              ('verification_specs','verification-specs'),('verifications','verifications')]}

def validate_dataset(d,root=ROOT):
    errors=[]
    v=d['vocabularies']
    if not isinstance(v,dict): return ['vocabularies: expected an object']
    for key in ['methods','validation','experiment','status','priority','relations','evidence']:
        values=v.get(key)
        if not isinstance(values,list) or not values or not all(isinstance(x,str) and x for x in values):
            errors.append(f'vocabularies: invalid list {key}')
        elif len(values)!=len(set(values)): errors.append(f'vocabularies: duplicate value in {key}')
    notes=d['coverage_notes']
    if not isinstance(notes,list) or not all(isinstance(x,dict) and isinstance(x.get('area'),str) and x['area'].strip() and isinstance(x.get('note'),(str,dict)) for x in notes):
        errors.append('coverage notes: expected subject-area text or object records')
    if errors: return errors
    cp=read(root/'schemas/card.schema.json')['properties']
    schema_enums={'methods':cp['method_tags']['items']['enum'],'validation':cp['validation_tags']['items']['enum'],
        'experiment':cp['experimental_dependency']['enum'],'status':cp['status']['enum'],
        'priority':cp['ai_assessment']['properties']['priority']['enum'],'relations':cp['relations']['items']['properties']['type']['enum'],
        'evidence':cp['ai_assessment']['properties']['evidence_level']['enum']}
    for key,values in schema_enums.items():
        if set(values)!=set(v[key]): errors.append(f'vocabularies: schema drift in {key}')
    for key,schema_name in [('nodes','taxonomy-node'),('sources','source'),('candidates','candidate'),('cards','card'),('source_map','source-map'),('scope','scope-decision'),('profiles','research-profile'),('checks','candidate-check'),('landmarks','landmark-problem'),('literature_checks','literature-check'),('attempts','attempt'),('reviews','review'),('verification_specs','verification-spec'),('verifications','verification')]:
        schema=read(root/'schemas'/f'{schema_name}.schema.json')
        for i,x in enumerate(d[key]): schema_check(x,schema,f'{key}[{i}]',errors,root/'schemas')
    schema_check(d['project'],read(root/'schemas/project.schema.json'),'project',errors,root/'schemas')
    if errors: return errors
    for record in [*d['attempts'], *d['reviews']]:
        errors.extend(validate_record_artifacts(record, root))
    ids={}
    for key in ['nodes','sources','candidates','cards']:
        items=[x['id'] for x in d[key]]
        if len(items)!=len(set(items)): errors.append(f'{key}: duplicate stable ID')
        ids[key]=set(items)
    nodes={n['id']:n for n in d['nodes']}; sources={s['id']:s for s in d['sources']}; candidates={c['id']:c for c in d['candidates']}
    def refs(values,allowed,where):
        for x in values:
            if x not in allowed: errors.append(f'{where}: unresolved reference {x}')
    cutoff=d['project']['as_of']
    review_ids=[r['id'] for r in d['literature_checks']]
    if len(review_ids)!=len(set(review_ids)): errors.append('literature checks: duplicate record ID')
    latest={}; history={}
    for r in d['literature_checks']:
        refs([r['problem_id']],ids['candidates'],r['id'])
        if r['checked_on']>cutoff: errors.append(f'{r["id"]}: future literature check')
        for field in ('status_before','status_after'):
            if r[field] not in v['status']: errors.append(f'{r["id"]}: invalid {field}')
        for e in r['evidence']:
            refs([e['source_id']],ids['sources'],r['id'])
            if e['source_id'] in sources and sources[e['source_id']]['verification']!='opened':
                errors.append(f'{r["id"]}: evidence requires an inspected source')
        if r['coverage']=='statement_and_later_literature' and not r['evidence']:
            errors.append(f'{r["id"]}: literature conclusion requires evidence')
        if r['status_after'] in {'resolved','disproved','open_after_scoped_check'} and r['coverage']!='statement_and_later_literature':
            errors.append(f'{r["id"]}: status requires a later-literature check')
        prior=latest.get(r['problem_id'])
        if not prior or r['checked_on']>=prior['checked_on']: latest[r['problem_id']]=r
        history.setdefault(r['problem_id'],[]).append(r)
        if r['statement_assessment']=='corrected' and not r.get('previous_statement'):
            errors.append(f'{r["id"]}: correction requires previous wording')
    for pid,records in history.items():
        ordered=sorted(records,key=lambda r:r['checked_on'])
        if len({r['checked_on'] for r in ordered})!=len(ordered):
            errors.append(f'{pid}: duplicate literature-check date; combine same-day evidence')
        for before,after in zip(ordered,ordered[1:]):
            if before['status_after']!=after['status_before']:
                errors.append(f'{pid}: discontinuous literature status history')
    for pid,r in latest.items():
        if pid in candidates and r['status_after']!=candidates[pid]['status']:
            errors.append(f'{pid}: latest literature check differs from candidate status')
        if pid in candidates and candidates[pid]['last_checked']<r['checked_on']:
            errors.append(f'{pid}: candidate check date precedes latest literature check')
    check_ids=[p['problem_id'] for p in d['checks']]
    if len(check_ids)!=len(set(check_ids)): errors.append('checks: duplicate candidate check')
    if set(check_ids)!=ids['candidates']: errors.append('checks: missing or excess candidate checks')
    for p in d['checks']:
        c=candidates.get(p['problem_id'])
        if not c: continue
        if p['status_check']=='not_checked' and c['status'] in {'source_reports_open','open_after_scoped_check'}:
            errors.append(f'{c["id"]}: unchecked status cannot support an open label')
        if p['statement_check']=='needs_clarification' and not p['missing_information']:
            errors.append(f'{c["id"]}: unclear statement needs an explicit information gap')
    profile_ids=[p['problem_id'] for p in d['profiles']]
    if len(profile_ids)!=len(set(profile_ids)): errors.append('profiles: duplicate problem profile')
    if set(profile_ids)!=ids['candidates']: errors.append('profiles: missing or excess candidate profiles')
    for p in d['profiles']:
        if p['assessment_date']>cutoff: errors.append(f'{p["problem_id"]}: future profile assessment')
    landmark_ids=[p['id'] for p in d['landmarks']]
    if len(landmark_ids)!=len(set(landmark_ids)): errors.append('landmarks: duplicate ID')
    for collection,total in [('millennium',7),('hilbert',23)]:
        numbers=[p['number'] for p in d['landmarks'] if p['collection']==collection]
        if sorted(numbers)!=list(range(1,total+1)): errors.append(f'landmarks: incomplete or duplicate {collection} registry')
    for p in d['landmarks']:
        refs(p['source_ids'],ids['sources'],p['id'])
        refs(p['problem_ids'],ids['candidates'],p['id'])
        if p['last_checked']>cutoff: errors.append(f'{p["id"]}: future landmark check')
        if p['status']=='open' and p['problem_ids'] and all(candidates[x]['status'] in {'known_result','resolved','disproved'} for x in p['problem_ids'] if x in candidates):
            errors.append(f'{p["id"]}: open landmark links only resolved questions')
    for n in d['nodes']:
        refs(n['related_ids'],ids['nodes'],n['id'])
        refs(n['classification_source_ids'],ids['sources'],n['id'])
        if n['parent_id'] is not None: refs([n['parent_id']],ids['nodes'],n['id'])
        visited={n['id']}; p=n['parent_id']
        while p in nodes:
            if p in visited: errors.append(f'{n["id"]}: taxonomy cycle'); break
            visited.add(p); p=nodes[p]['parent_id']
    for s in d['sources']:
        if s['accessed']>cutoff: errors.append(f'{s["id"]}: access date exceeds cutoff')
        if s['year'] and s['year']>int(cutoff[:4]): errors.append(f'{s["id"]}: publication year exceeds cutoff')
    urls=[s['url'].rstrip('/') for s in d['sources']]
    if len(urls)!=len(set(urls)): errors.append('sources: duplicate canonical URL; use source aliases')
    dup=[c['duplicate_key'] for c in d['candidates']]
    if len(dup)!=len(set(dup)): errors.append('candidates: duplicate canonical problem key')
    for c in d['candidates']:
        refs(c['source_ids'],ids['sources'],c['id']); refs([c['primary_domain_id']]+c['cross_domain_ids'],ids['nodes'],c['id'])
        if c['primary_domain_id'] in c['cross_domain_ids']: errors.append(f'{c["id"]}: primary domain repeated as cross-link')
        if c['kind']=='curator_proposed' and not c['curator_origin']: errors.append(f'{c["id"]}: curator origin not disclosed')
        if c['kind']=='known_result_calibration' and c['status']!='known_result': errors.append(f'{c["id"]}: calibration needs known-result status')
        if c['last_checked']>cutoff: errors.append(f'{c["id"]}: future status check')
        if c['proposed_card'] != (c['id'] in ids['cards']): errors.append(f'{c["id"]}: promotion/card mismatch')
        if (c['curation_level']=='C') != (c['id'] in ids['cards']): errors.append(f'{c["id"]}: layer/card mismatch')
    for c in d['cards']:
        if c['id'] not in candidates: errors.append(f'{c["id"]}: missing candidate'); continue
        for key,value in candidates[c['id']].items():
            if c.get(key)!=value: errors.append(f'{c["id"]}: card/candidate drift in {key}')
        refs(c['status_search']['checked_sources'],ids['sources'],c['id'])
        refs([r['target'] for r in c['relations']],ids['candidates'],c['id'])
        for src in c['source_ids']:
            if src in sources and sources[src]['verification']!='opened': errors.append(f'{c["id"]}: card relies on unopened source {src}')
        if c['ai_assessment']['assessment_date']>cutoff: errors.append(f'{c["id"]}: future AI assessment')
    errors.extend(validate_research_records(d))
    errors.extend(validate_machine_records(d,root))
    for m in d['source_map']:
        refs([m['source_id']],ids['sources'],'source map'); refs(m['domain_ids'],ids['nodes'],'source map')
    mapped=[m['source_id'] for m in d['source_map']]
    if len(mapped)!=len(set(mapped)): errors.append('source map: duplicate source row')
    if set(mapped)!=ids['sources']: errors.append('source map: missing or excess source mappings')
    for alias,target in d['aliases'].items():
        if alias in ids['sources']: errors.append(f'{alias}: alias also has a canonical record')
        refs([target],ids['sources'],'source alias')
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true',help='Print a machine-readable result')
    args=parser.parse_args()
    try:
        d=load_dataset(); errors=validate_dataset(d)
        report={'status':'fail' if errors else 'pass','as_of':d['project']['as_of'],
            'counts':{k:len(d[k]) for k in ['nodes','sources','candidates','cards']},'errors':errors,
            'scope':'Schema, references, identity and research-record consistency; mathematical claims and current literature status require separate review.'}
    except (ValueError,KeyError,OSError,TypeError) as exc:
        report={'status':'fail','errors':[str(exc)]}
    print(json.dumps(report,indent=2) if args.json else '\n'.join([report['status'].upper(),*report.get('errors',[]),report.get('scope','')]))
    return 1 if report['status']=='fail' else 0

if __name__=='__main__': sys.exit(main())
