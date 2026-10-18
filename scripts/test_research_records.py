"""Exercise record lifecycle rules using synthetic, in-memory fixtures only."""
import copy
import hashlib
import unittest

from validate import ROOT, load_dataset, validate_dataset
from render_cards import render_cards
from research_records import statement_digest, attempt_digest, current_attempt_reviews


def research_dataset_fixture():
    data = copy.deepcopy(load_dataset())
    # Isolate synthetic lifecycles from real records and their run counts.
    for key in ('attempts', 'reviews', 'verification_specs', 'verifications'):
        data[key] = []
    data['project']['research_attempts_run'] = 0
    data['project']['model_evaluations_run'] = 0
    return data


def artifact_fixture():
    return {'reference': 'README.md', 'version': 'Synthetic fixture using the current README bytes.',
            'sha256': 'sha256:' + hashlib.sha256((ROOT / 'README.md').read_bytes()).hexdigest()}


def attempt_fixture(pid):
    return {
        'id': 'ATT-TEST', 'problem_id': pid, 'statement_version': 'Synthetic test snapshot',
        'target': 'Test record, not a scientific result.', 'purpose': 'research',
        'assumptions': ['Synthetic assumptions.'], 'success_criteria': ['Synthetic target.'],
        'verification_plan': ['Independent fixture check.'],
        'requirements': {'experiment': 'None.', 'data': 'Synthetic data.', 'compute': 'No execution.'},
        'contributors': [{'name': 'Test contributor', 'roles': ['Test fixture']}],
        'model': {'provider': None, 'name': None, 'version': None, 'capabilities': []},
        'started_at': None, 'ended_at': None, 'status': 'planned',
        'environment': {'os': None, 'tools': [], 'versions': [], 'code_revision': None, 'seeds': []},
        'input_artifacts': [], 'process_artifacts': [], 'candidate_answer_artifacts': [],
        'artifact_manifest': [],
        'planned_budget': {'kind': 'cap', 'money': {'amount': None, 'currency': None, 'basis': 'Not estimated.'},
                           'compute_units': None, 'human_hours': None, 'notes': 'No execution has begun.'},
        'actual_use': {'kind': 'actual', 'money': {'amount': None, 'currency': None, 'basis': 'No run.'},
                       'compute_units': None, 'human_hours': None, 'notes': 'No run.'},
        'human_help': [], 'outcome_kind': 'not_yet_reported', 'outcome': 'No run.',
        'stopping_conditions': ['No execution.'], 'limitations': ['Synthetic fixture.'],
        'review_ids': [], 'revision_history': [{'date': '2026-10-13', 'change': 'Test fixture.'}],
    }


class ResearchRecordTests(unittest.TestCase):
    def setUp(self):
        self.data = research_dataset_fixture()
        self.card = self.data['cards'][0]
        self.attempt = attempt_fixture(self.card['id'])
        self.data['attempts'] = [self.attempt]

    def executed(self):
        self.attempt.update(status='completed', started_at='2026-10-13T10:00:00Z',
                            ended_at='2026-10-13T11:00:00Z', outcome_kind='unsuccessful',
                            outcome='Synthetic unsuccessful outcome.', process_artifacts=['README.md'],
                            artifact_manifest=[artifact_fixture()])
        self.data['project']['research_attempts_run'] = 1

    def review(self):
        r = {'id': 'REV-TEST', 'problem_id': self.card['id'], 'attempt_id': 'ATT-TEST',
             'review_type': 'research_record', 'statement_digest': statement_digest(self.card),
             'attempt_digest': attempt_digest(self.attempt),
             'reviewed_version': 'Synthetic test snapshot', 'reviewer': 'Test reviewer',
             'reviewer_role': 'Test fixture', 'date': '2026-10-14', 'scope': ['Code only'],
             'not_reviewed': ['Novelty'], 'verdict': 'inconclusive', 'comments': 'Synthetic review.',
             'evidence_artifacts': ['README.md'], 'artifact_manifest': [artifact_fixture()], 'supersedes': [],
             'conflicts_of_interest': 'Synthetic fixture.',
             'revision_history': [{'date': '2026-10-14', 'change': 'Test fixture.'}]}
        self.data['reviews'] = [r]
        self.attempt['review_ids'] = [r['id']]
        return r

    def entry_review(self):
        review = self.review()
        review.update(review_type='problem_entry', attempt_id=None, attempt_digest=None)
        self.attempt['review_ids'] = []
        return review

    def fails_with(self, fragment):
        self.assertTrue(any(fragment in e for e in validate_dataset(self.data)), validate_dataset(self.data))

    def test_planned_record_is_allowed_without_incrementing_runs(self):
        self.assertEqual(validate_dataset(self.data), [])

    def test_planned_record_cannot_claim_zero_actual_cost(self):
        self.attempt['actual_use']['money'].update(amount=0, currency='USD')
        self.fails_with('cannot report measured use')

    def test_failed_or_completed_run_is_not_a_claim_of_success(self):
        self.executed()
        self.review()
        self.assertEqual(validate_dataset(self.data), [])

    def test_terminal_run_needs_evidence_and_time(self):
        self.executed()
        self.attempt['process_artifacts'] = []
        self.attempt['ended_at'] = None
        self.fails_with('requires an end time')
        self.fails_with('observable research record')

    def test_inverted_time_is_rejected(self):
        self.executed()
        self.attempt['ended_at'] = '2026-10-13T09:00:00Z'
        self.fails_with('end precedes start')

    def test_project_counts_are_derived_from_executed_records(self):
        self.executed()
        self.data['project']['research_attempts_run'] = 0
        self.fails_with('differs from started attempt')

    def test_model_evaluation_needs_model_and_matching_count(self):
        self.executed()
        self.attempt['purpose'] = 'model_evaluation'
        self.fails_with('requires a model identifier')
        self.fails_with('differs from started model-evaluation')

    def test_outcome_needs_result_artifact(self):
        self.executed()
        self.attempt['outcome_kind'] = 'candidate_answer'
        self.fails_with('result requires an artifact')

    def test_review_needs_reciprocal_reference(self):
        self.executed()
        self.review()
        self.attempt['review_ids'] = []
        self.fails_with('must link back')

    def test_cross_problem_record_rejected(self):
        self.attempt['problem_id'] = 'Q-OTHER-000'
        self.fails_with('unknown problem reference')

    def test_duplicate_attempt_identity_rejected(self):
        self.data['attempts'].append(copy.deepcopy(self.attempt))
        self.fails_with('duplicate research record ID')

    def test_measurement_requires_completed_model_record(self):
        self.card['ai_assessment'].update(evidence_level='project_measured', evidence_refs=['ATT-TEST'])
        self.fails_with('unsupported measured')
        self.executed()
        self.attempt['model']['name'] = 'Synthetic model fixture'
        self.assertEqual(validate_dataset(self.data), [])
        page = render_cards(self.data)[f'docs/cards/{self.card["id"]}.md']
        self.assertIn('[ATT-TEST](#audit-trail)', page)

    def test_reviewed_label_needs_a_matching_scoped_review(self):
        self.card['human_review_status'] = 'reviewed_accepted'
        next(c for c in self.data['candidates'] if c['id'] == self.card['id'])['human_review_status'] = 'reviewed_accepted'
        self.fails_with('requires a matching scoped review')

    def test_future_date_and_unattributed_amount_rejected(self):
        self.executed()
        self.attempt['ended_at'] = '2099-01-01T10:00:00Z'
        self.attempt['actual_use']['money']['amount'] = 1
        self.fails_with('future execution')
        self.fails_with('amount needs a currency')

    def test_outlines_cannot_claim_a_review_without_record_storage(self):
        c = next(c for c in self.data['candidates'] if c['curation_level'] == 'B')
        c['human_review_status'] = 'reviewed_accepted'
        self.fails_with('requires a matching scoped review')

    def test_old_acceptance_cannot_override_later_rejection(self):
        self.executed()
        review = self.entry_review()
        review['verdict'] = 'accepted_within_scope'
        later = dict(review, id='REV-LATER', date='2026-10-15', verdict='rejected')
        self.data['reviews'].append(later)
        self.card['human_review_status'] = 'reviewed_accepted'
        next(c for c in self.data['candidates'] if c['id'] == self.card['id'])['human_review_status'] = 'reviewed_accepted'
        self.fails_with('current review conclusions')

    def test_changed_hypotheses_do_not_inherit_old_acceptance(self):
        self.executed()
        self.entry_review()['verdict'] = 'accepted_within_scope'
        self.card['human_review_status'] = 'reviewed_accepted'
        next(c for c in self.data['candidates'] if c['id'] == self.card['id'])['human_review_status'] = 'reviewed_accepted'
        self.assertEqual(validate_dataset(self.data), [])
        self.card['assumptions'].append('A new synthetic assumption.')
        self.fails_with('requires a matching scoped review')

    def test_review_of_plan_remains_valid_after_execution(self):
        review = self.review()
        review.update(review_type='planned_method', date='2026-10-12')
        self.executed()
        self.assertEqual(validate_dataset(self.data), [])

    def test_assessment_cannot_predate_measurement(self):
        self.executed()
        self.attempt['model']['name'] = 'Synthetic model fixture'
        self.card['ai_assessment'].update(evidence_level='project_measured', evidence_refs=['ATT-TEST'], assessment_date='2026-10-12')
        self.fails_with('assessment predates')


if __name__ == '__main__':
    unittest.main()
