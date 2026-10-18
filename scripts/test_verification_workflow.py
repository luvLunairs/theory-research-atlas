"""Check draft and catalogue boundaries without running a scientific verifier."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from catalog import records
from machine_verification import specification_digest
from new_record import draft_record, save_draft
from research_records import attempt_digest
from test_research_records import attempt_fixture
from validate import ROOT, load_dataset, schema_check, validate_dataset


class VerificationWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.data = load_dataset()
        self.problem = next(c for c in self.data['candidates'] if c['curation_level'] == 'B')
        self.pid = self.problem['id']

    def specification(self, method='exact_counterexample'):
        return draft_record(self.data, 'verification-spec', self.pid, 'VSPEC-DRAFT',
                            'Test contributor', method=method, date='2026-10-16')

    def test_specification_requires_a_deliberate_method_and_cannot_approve_itself(self):
        with self.assertRaisesRegex(ValueError, 'explicit --method'):
            draft_record(self.data, 'verification-spec', self.pid, 'VSPEC-DRAFT', 'Test contributor')
        for method in ('exact_counterexample', 'lean_proof', 'finite_construction', 'finite_exhaustion'):
            with self.subTest(method=method):
                record = self.specification(method)
                self.assertEqual(record['approval']['status'], 'pending')
                self.assertIsNone(record['approval']['reviewer'])
                self.assertIsNone(record['approval']['date'])
                self.assertIsNone(record['approval']['specification_digest'])

    def test_run_draft_binds_existing_records_without_inventing_an_execution(self):
        spec = self.specification()
        attempt = attempt_fixture(self.pid)
        self.data['verification_specs'] = [spec]
        self.data['attempts'] = [attempt]
        before = copy.deepcopy(self.data)
        run = draft_record(self.data, 'verification', self.pid, 'VER-DRAFT', 'Test contributor',
                           attempt_id=attempt['id'], specification_id=spec['id'])
        self.assertEqual(self.data, before)
        self.assertEqual(run['specification_digest'], specification_digest(spec))
        self.assertEqual(run['attempt_digest'], attempt_digest(attempt))
        self.assertEqual(run['runner']['provenance'], 'contributor')
        for field in ('executed_at', 'outcome', 'axioms_used', 'native_decide_used'):
            self.assertIsNone(run[field], field)
        errors = []
        schema = json.loads((ROOT / 'schemas/verification.schema.json').read_text(encoding='utf-8'))
        schema_check(run, schema, 'draft', errors)
        self.assertTrue(errors)
        self.assertEqual(self.data['project']['research_attempts_run'], 0)

    def test_missing_and_cross_problem_links_are_rejected(self):
        with self.assertRaises(ValueError):
            draft_record(self.data, 'verification', self.pid, 'VER-DRAFT', 'Test contributor')
        self.data['attempts'] = [attempt_fixture(self.pid)]
        spec = self.specification()
        spec['problem_id'] = next(c['id'] for c in self.data['candidates'] if c['id'] != self.pid)
        self.data['verification_specs'] = [spec]
        with self.assertRaisesRegex(ValueError, 'specification for this problem'):
            draft_record(self.data, 'verification', self.pid, 'VER-DRAFT', 'Test contributor',
                         attempt_id='ATT-TEST', specification_id=spec['id'])

    def test_incomplete_specification_cannot_enter_the_canonical_collection(self):
        self.data['verification_specs'] = [self.specification()]
        self.assertTrue(validate_dataset(self.data))
        self.assertEqual(self.problem['human_review_status'], 'pending')

    def test_machine_draft_ids_are_safe_and_no_existing_file_is_overwritten(self):
        (ROOT / 'work').mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / 'work') as directory:
            root = Path(directory)
            record = self.specification()
            path = save_draft(record, root)
            self.assertEqual(path.parent, root / 'work/drafts')
            with self.assertRaises(FileExistsError):
                save_draft(record, root)
            with self.assertRaises(ValueError):
                save_draft(dict(record, id='VSPEC-../../escape'), root)

    def test_irrelevant_helper_options_are_not_silently_ignored(self):
        with self.assertRaisesRegex(ValueError, '--specification'):
            draft_record(self.data, 'attempt', self.pid, 'ATT-DRAFT', 'Test contributor',
                         specification_id='VSPEC-UNKNOWN')
        with self.assertRaisesRegex(ValueError, '--method'):
            draft_record(self.data, 'review', self.pid, 'REV-DRAFT', 'Test contributor', method='lean_proof')

    def test_catalogue_rejects_malformed_verification_records_with_a_clear_error(self):
        self.data['verification_specs'] = [{'id': 'VSPEC-BROKEN', 'problem_id': self.pid}]
        with self.assertRaisesRegex(ValueError, 'Invalid machine-verification records'):
            records(self.data)


if __name__ == '__main__':
    unittest.main()
