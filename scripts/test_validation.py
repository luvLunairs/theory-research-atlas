"""Regression checks for data-integrity failures; these are not research trials."""
import copy
import json
import unittest
from validate import load_dataset, schema_check, validate_dataset

class ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.original=load_dataset()
    def setUp(self): self.d=copy.deepcopy(self.original)
    def test_current_dataset(self): self.assertEqual(validate_dataset(self.d),[])
    def test_missing_source(self):
        self.d['candidates'][0]['source_ids']=['SRC-UNKNOWN-999']
        self.assertTrue(any('unresolved reference' in e for e in validate_dataset(self.d)))
    def test_duplicate_problem(self):
        self.d['candidates'][1]['duplicate_key']=self.d['candidates'][0]['duplicate_key']
        self.assertTrue(any('duplicate canonical problem' in e for e in validate_dataset(self.d)))
    def test_taxonomy_cycle(self):
        self.d['nodes'][0]['parent_id']=self.d['nodes'][0]['id']
        self.assertTrue(any('cycle' in e for e in validate_dataset(self.d)))
    def test_card_drift(self):
        self.d['cards'][0]['statement']='A changed statement without candidate update.'
        self.assertTrue(any('card/candidate drift' in e for e in validate_dataset(self.d)))
    def test_unopened_card_source(self):
        sid=self.d['cards'][0]['source_ids'][0]
        next(s for s in self.d['sources'] if s['id']==sid)['verification']='pending'
        self.assertTrue(any('unopened source' in e for e in validate_dataset(self.d)))
    def test_false_measurement(self):
        self.d['cards'][0]['ai_assessment']['evidence_level']='project_measured'
        self.assertTrue(any('unsupported measured' in e for e in validate_dataset(self.d)))
    def test_missing_required_field(self):
        del self.d['cards'][0]['assumptions']
        self.assertTrue(any('missing assumptions' in e for e in validate_dataset(self.d)))
    def test_unsupported_schema_keyword_fails(self):
        errors=[]; schema_check('x',{'unexpectedKeyword':True},'test',errors)
        self.assertTrue(errors)
    def test_invalid_date_fails(self):
        errors=[]; schema_check('2026-02-30',{'type':'string','format':'date'},'test',errors)
        self.assertTrue(errors)
    def test_wrong_type_fails(self):
        errors=[]; schema_check(True,{'type':'integer'},'test',errors)
        self.assertTrue(errors)
    def test_nonfinite_numbers_fail(self):
        for value in [float('nan'), float('inf'), float('-inf')]:
            for schema in [{'type':'number'}, {'type':['number','null'],'minimum':0}]:
                with self.subTest(value=value,schema=schema):
                    errors=[]
                    schema_check(value,schema,'actual_use.money.amount',errors)
                    self.assertEqual(errors,['actual_use.money.amount: number must be finite'])
    def test_json_numeric_overflow_fails(self):
        for encoded in ['1e999','-1e999']:
            with self.subTest(encoded=encoded):
                errors=[]
                schema_check(json.loads(encoded),{'type':'number'},'measurement',errors)
                self.assertEqual(errors,['measurement: number must be finite'])
    def test_finite_and_nullable_numbers_remain_valid(self):
        for value in [None,0,10**400,0.0,0.25,1e308]:
            with self.subTest(value=value):
                errors=[]
                schema_check(value,{'type':['number','null'],'minimum':0},'measurement',errors)
                self.assertEqual(errors,[])
    def test_vocabulary_drift(self):
        self.d['vocabularies']['priority'].append('guaranteed_success')
        self.assertTrue(any('schema drift' in e for e in validate_dataset(self.d)))
    def test_invalid_coverage_notes(self):
        self.d['coverage_notes']=[{'unsupported':'not attributed'}]
        self.assertTrue(any('coverage notes' in e for e in validate_dataset(self.d)))
    def test_profile_coverage_is_required(self):
        self.d['profiles'].pop()
        self.assertTrue(any('missing or excess candidate profiles' in e for e in validate_dataset(self.d)))
    def test_duplicate_profile_fails(self):
        self.d['profiles'].append(copy.deepcopy(self.d['profiles'][0]))
        self.assertTrue(any('duplicate problem profile' in e for e in validate_dataset(self.d)))
    def test_historical_collection_cannot_lose_an_entry(self):
        self.d['landmarks'].pop()
        self.assertTrue(any('incomplete or duplicate' in e for e in validate_dataset(self.d)))
    def test_historical_links_use_real_problem_ids(self):
        self.d['landmarks'][0]['problem_ids']=['Q-NONE-999']
        self.assertTrue(any('unresolved reference' in e for e in validate_dataset(self.d)))
    def test_profile_forecasts_cannot_become_measurements(self):
        self.d['profiles'][0]['evidence_level']='project_measured'
        self.assertTrue(validate_dataset(self.d))
    def test_checks_cover_every_candidate(self):
        self.d['checks'].pop()
        self.assertTrue(any('missing or excess candidate checks' in e for e in validate_dataset(self.d)))
    def test_unchecked_status_cannot_be_open(self):
        candidate=next(c for c in self.d['candidates'] if c['status']=='source_reports_open')
        next(c for c in self.d['checks'] if c['problem_id']==candidate['id'])['status_check']='not_checked'
        self.assertTrue(any('unchecked status cannot support' in e for e in validate_dataset(self.d)))
    def test_unclear_statement_requires_a_gap(self):
        self.d['checks'][0]['statement_check']='needs_clarification'
        self.d['checks'][0]['missing_information']=[]
        self.assertTrue(any('unclear statement needs' in e for e in validate_dataset(self.d)))

if __name__=='__main__': unittest.main()
