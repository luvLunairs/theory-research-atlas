"""Test attributed screening stages without granting scientific approval."""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from render_records import render_records
from research_records import (SCREENING_TARGET_FIELDS, attempt_digest,
                              current_attempt_reviews, preliminary_screening_label,
                              preliminary_screening_state, screening_target_digest,
                              statement_digest)
from test_research_records import attempt_fixture, research_dataset_fixture
from validate import ROOT, validate_dataset


class PreliminaryScreeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = research_dataset_fixture()

    def setUp(self):
        self.data = copy.deepcopy(self.base)
        self.card = self.data['cards'][0]
        self.attempt = attempt_fixture(self.card['id'])
        self.attempt.update(
            status='completed', started_at='2026-10-13T10:00:00Z',
            ended_at='2026-10-13T11:00:00Z', outcome_kind='candidate_answer',
            outcome='Synthetic candidate, not a scientific claim.',
            candidate_answer_artifacts=['README.md'],
            process_artifacts=['AGENTS.md', 'CONTRIBUTING.md'],
            model={'provider': 'Test', 'name': 'Recorded test model', 'version': None,
                   'capabilities': []},
            artifact_manifest=[self.artifact(ref) for ref in
                               ['README.md', 'AGENTS.md', 'CONTRIBUTING.md']])
        self.data['attempts'] = [self.attempt]
        self.data['project']['research_attempts_run'] = 1
        self.screening = {
            'target_digest': screening_target_digest(self.attempt),
            'result_artifacts': copy.deepcopy(self.attempt['artifact_manifest']),
            'evidence_artifacts': ['CONTRIBUTING.md'],
            'ai_basis': 'recommended_only', 'ai_check_status': 'completed',
            'human_preliminary_status': 'not_recorded',
            'recorded_by': 'Synthetic maintainer', 'date': '2026-10-13',
            'scope': ['Synthetic contributor-check declaration.'],
            'limitations': ['No scientific or independent review.'],
        }
        self.attempt['preliminary_screening'] = self.screening

    @staticmethod
    def artifact(ref):
        return {'reference': ref, 'version': 'Synthetic current bytes.',
                'sha256': 'sha256:' + hashlib.sha256((ROOT / ref).read_bytes()).hexdigest()}

    def fails_with(self, fragment):
        errors = validate_dataset(self.data)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_optional_absence_is_not_screened(self):
        self.attempt.pop('preliminary_screening')
        self.assertEqual(preliminary_screening_state(self.attempt), 'not_recorded')
        self.assertEqual(validate_dataset(self.data), [])

    def test_recommended_checks_and_human_pass_are_separate(self):
        self.assertEqual(validate_dataset(self.data), [])
        self.assertEqual(preliminary_screening_state(self.attempt), 'recommended_ai')
        self.screening['human_preliminary_status'] = 'passed'
        self.assertEqual(preliminary_screening_state(self.attempt), 'recommended_ai_human')
        self.assertEqual(preliminary_screening_label(self.attempt),
                         'Recommended-model contributor checks + reported human preliminary pass')
        self.assertEqual(self.attempt['review_ids'], [])
        self.assertEqual(self.data['verifications'], [])

    def test_incomplete_or_other_ai_checks_do_not_get_recommended_label(self):
        for basis, checked in [('recommended_only', 'not_recorded'),
                               ('other_or_unknown', 'completed'),
                               ('no_ai', 'not_recorded')]:
            with self.subTest(basis=basis, checked=checked):
                self.screening.update(ai_basis=basis, ai_check_status=checked)
                self.assertEqual(preliminary_screening_state(self.attempt),
                                 'limited' if checked == 'completed' else 'not_recorded')
                self.screening['human_preliminary_status'] = 'passed'
                self.assertEqual(preliminary_screening_state(self.attempt), 'human_preliminary')
                self.screening['human_preliminary_status'] = 'not_recorded'

    def test_changes_requested_overrides_completed_ai_checks(self):
        self.screening['human_preliminary_status'] = 'changes_requested'
        self.assertEqual(preliminary_screening_state(self.attempt), 'changes_requested')
        self.assertNotIn('pass', preliminary_screening_label(self.attempt))

    def test_contradictory_ai_declarations_are_invalid(self):
        self.screening['ai_basis'] = 'no_ai'
        self.fails_with('cannot report AI checks')
        self.assertEqual(preliminary_screening_state(self.attempt), 'invalid')
        self.screening['ai_basis'] = 'recommended_only'
        self.attempt['model']['name'] = None
        self.fails_with('requires recorded model identity')

    def test_every_target_field_is_bound_and_metadata_does_not_hash_itself(self):
        original = screening_target_digest(self.attempt)
        for field in SCREENING_TARGET_FIELDS:
            changed = copy.deepcopy(self.attempt)
            value = changed[field]
            if isinstance(value, str):
                changed[field] += ' changed'
            elif isinstance(value, list):
                changed[field].append('changed')
            else:
                changed[field]['name' if field == 'model' else 'os'] = 'changed'
            with self.subTest(field=field):
                self.assertNotEqual(screening_target_digest(changed), original)
                self.assertIn(preliminary_screening_state(changed), {'stale', 'invalid'})
        old_attempt_digest = attempt_digest(self.attempt)
        self.screening['human_preliminary_status'] = 'passed'
        self.assertEqual(screening_target_digest(self.attempt), original)
        self.assertNotEqual(attempt_digest(self.attempt), old_attempt_digest)

    def test_stale_target_is_preserved_as_history(self):
        self.attempt['target'] += ' Revised target.'
        self.assertEqual(validate_dataset(self.data), [])
        self.assertEqual(preliminary_screening_state(self.attempt), 'stale')

    def test_candidate_list_addition_removal_and_reordering_are_stale(self):
        self.attempt['candidate_answer_artifacts'].append('AGENTS.md')
        self.screening['target_digest'] = screening_target_digest(self.attempt)
        for refs in [['README.md'], ['AGENTS.md', 'README.md'],
                     ['README.md', 'AGENTS.md', 'CONTRIBUTING.md']]:
            changed = copy.deepcopy(self.attempt)
            changed['candidate_answer_artifacts'] = refs
            with self.subTest(refs=refs):
                self.assertEqual(preliminary_screening_state(changed), 'stale')

    def test_new_digest_alone_cannot_hide_an_unbound_candidate(self):
        self.attempt['candidate_answer_artifacts'].append('CONTRIBUTING.md')
        self.screening['result_artifacts'].pop()
        self.screening['target_digest'] = screening_target_digest(self.attempt)
        self.assertEqual(preliminary_screening_state(self.attempt), 'stale')

    def test_screening_evidence_versions_are_bound_as_well_as_results(self):
        original = copy.deepcopy(self.attempt)
        for key, value in [('version', 'Replacement report.'), ('sha256', 'sha256:' + '1' * 64)]:
            changed = copy.deepcopy(original)
            changed['artifact_manifest'][2][key] = value
            with self.subTest(key=key):
                self.assertEqual(preliminary_screening_state(changed), 'stale')
        self.screening['result_artifacts'].pop()
        self.assertEqual(preliminary_screening_state(self.attempt), 'stale')

    def test_supporting_artifact_change_or_removal_is_stale(self):
        original = copy.deepcopy(self.attempt)
        for key, value in [('version', 'Revised version.'), ('sha256', 'sha256:' + '0' * 64)]:
            changed = copy.deepcopy(original)
            changed['artifact_manifest'][1][key] = value
            with self.subTest(key=key):
                self.assertEqual(preliminary_screening_state(changed), 'stale')
        self.attempt['artifact_manifest'].pop(1)
        self.assertEqual(preliminary_screening_state(self.attempt), 'stale')

    def test_bound_local_bytes_are_checked_even_during_direct_render(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for item in self.attempt['artifact_manifest']:
                ref = item['reference']
                (root / ref).write_bytes((ROOT / ref).read_bytes())
            self.assertEqual(preliminary_screening_state(self.attempt, root), 'recommended_ai')
            (root / 'AGENTS.md').write_text('Changed dependency.', encoding='utf-8')
            self.assertEqual(preliminary_screening_state(self.attempt, root), 'invalid')
            rendered = render_records(self.data, root)
            self.assertIn('Preliminary-screening evidence needs attention', rendered['docs/results.md'])
            self.assertNotIn('Recommended-model contributor checks recorded', rendered['docs/results.md'])

    def test_evidence_must_be_manifested_process_material(self):
        self.screening['evidence_artifacts'] = ['README.md']
        self.fails_with('evidence must be a manifested process artifact')
        self.assertEqual(preliminary_screening_state(self.attempt), 'invalid')
        self.screening['evidence_artifacts'] = ['CONTRIBUTING.md']
        self.attempt['artifact_manifest'][2]['sha256'] = None
        self.fails_with('evidence requires a SHA-256 digest')

    def test_missing_or_changed_evidence_bytes_prevent_positive_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for item in self.attempt['artifact_manifest']:
                ref = item['reference']
                (root / ref).write_bytes((ROOT / ref).read_bytes())
            (root / 'CONTRIBUTING.md').unlink()
            self.assertEqual(preliminary_screening_state(self.attempt, root), 'invalid')

    def test_schema_rejects_unbound_or_invented_screening_fields(self):
        self.screening['confidence'] = 'high'
        self.fails_with('unknown field confidence')
        self.screening.pop('confidence')
        self.screening['result_artifacts'][0]['sha256'] = None
        self.fails_with('expected string')

    def test_duplicate_binding_and_future_date_are_rejected(self):
        self.screening['result_artifacts'].append(copy.deepcopy(self.screening['result_artifacts'][0]))
        self.fails_with('repeats a bound result reference')
        self.screening['result_artifacts'].pop()
        self.screening['date'] = '2099-01-01'
        self.fails_with('future date')
        self.screening['date'] = '2026-10-12'
        self.fails_with('predates the attempt')

    def test_planned_attempt_cannot_claim_preliminary_result_screening(self):
        self.attempt.update(status='planned', started_at=None, ended_at=None,
                            outcome_kind='not_yet_reported')
        self.data['project']['research_attempts_run'] = 0
        self.fails_with('requires an executed attempt')

    def test_human_pass_does_not_satisfy_existing_human_review_gate(self):
        self.screening['human_preliminary_status'] = 'passed'
        self.card['human_review_status'] = 'reviewed_accepted'
        candidate = next(c for c in self.data['candidates'] if c['id'] == self.card['id'])
        candidate['human_review_status'] = 'reviewed_accepted'
        self.fails_with('review status requires a matching scoped review')

    def test_generic_scoped_review_never_promotes_to_academic_stage(self):
        review = {
            'id': 'REV-TEST', 'problem_id': self.card['id'], 'attempt_id': self.attempt['id'],
            'review_type': 'research_record', 'statement_digest': statement_digest(self.card),
            'attempt_digest': attempt_digest(self.attempt), 'reviewed_version': 'Synthetic version.',
            'reviewer': 'Test reviewer', 'reviewer_role': 'Code reviewer', 'date': '2026-10-14',
            'scope': ['Code only'], 'not_reviewed': ['Mathematics'],
            'verdict': 'accepted_within_scope', 'comments': 'Synthetic code review.',
            'evidence_artifacts': ['CONTRIBUTING.md'],
            'artifact_manifest': [self.artifact('CONTRIBUTING.md')], 'supersedes': [],
            'conflicts_of_interest': 'Synthetic same-team fixture.',
            'revision_history': [{'date': '2026-10-14', 'change': 'Synthetic fixture.'}],
        }
        self.attempt['review_ids'] = [review['id']]
        self.data['reviews'] = [review]
        self.assertEqual(validate_dataset(self.data), [])
        self.assertEqual(len(current_attempt_reviews(self.data, self.attempt)), 1)
        self.assertEqual(preliminary_screening_state(self.attempt), 'recommended_ai')
        self.screening['human_preliminary_status'] = 'passed'
        self.assertEqual(current_attempt_reviews(self.data, self.attempt), [])

    def test_render_keeps_preliminary_and_formal_scopes_separate(self):
        self.screening['human_preliminary_status'] = 'passed'
        rendered = render_records(self.data)
        self.assertIn('Preliminary screening', rendered['docs/results.md'])
        self.assertIn('Current formal human review scope', rendered['docs/results.md'])
        self.assertIn('No formal review of the current result recorded', rendered['docs/results.md'])
        self.assertIn('Recommended-model contributor checks + reported human preliminary pass',
                      rendered['docs/attempts/ATT-TEST.md'])
        self.assertIn('No review has been recorded', rendered['docs/attempts/ATT-TEST.md'])
        self.assertEqual(self.attempt['outcome_kind'], 'candidate_answer')


if __name__ == '__main__':
    unittest.main()
