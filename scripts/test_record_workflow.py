"""Check contribution drafts, independent reviews and visible result boundaries."""
import json
from pathlib import Path
import tempfile
import unittest

from new_record import draft_record, save_draft
from render_indexes import render_indexes
from render_records import render_records
from research_records import attempt_digest, current_attempt_reviews, statement_digest
from test_research_records import artifact_fixture, attempt_fixture, research_dataset_fixture
from validate import ROOT, read_records, schema_check, validate_dataset


class RecordWorkflowTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'work').mkdir(exist_ok=True)
        self.data = research_dataset_fixture()
        self.candidate = next(c for c in self.data['candidates'] if c['curation_level'] == 'B')
        self.attempt = attempt_fixture(self.candidate['id'])
        self.data['attempts'] = [self.attempt]

    def execute(self):
        self.attempt.update(status='completed', started_at='2026-10-13T10:00:00Z',
                            ended_at='2026-10-13T11:00:00Z', outcome_kind='partial_result',
                            outcome='Synthetic bounded result; no general theorem.',
                            process_artifacts=['README.md'], candidate_answer_artifacts=['README.md'],
                            artifact_manifest=[artifact_fixture()])
        self.data['project']['research_attempts_run'] = 1

    def review(self, rid='REV-TEST', verdict='accepted_within_scope', review_type='research_record'):
        record = {
            'id': rid, 'problem_id': self.candidate['id'],
            'attempt_id': self.attempt['id'] if review_type != 'problem_entry' else None,
            'review_type': review_type, 'statement_digest': statement_digest(self.candidate),
            'attempt_digest': attempt_digest(self.attempt) if review_type != 'problem_entry' else None,
            'reviewed_version': 'Synthetic fixture version.', 'reviewer': 'Test reviewer',
            'reviewer_role': 'Synthetic reviewer', 'date': '2026-10-14',
            'scope': ['Finite certificate only'], 'not_reviewed': ['Novelty and general case'],
            'verdict': verdict, 'comments': 'Synthetic review, not a research finding.',
            'evidence_artifacts': ['README.md'], 'artifact_manifest': [artifact_fixture()],
            'conflicts_of_interest': 'Synthetic fixture.', 'supersedes': [],
            'revision_history': [{'date': '2026-10-14', 'change': 'Synthetic review.'}],
        }
        self.data['reviews'].append(record)
        if record['attempt_id']:
            self.attempt['review_ids'].append(rid)
        return record

    def test_outline_supports_a_complete_attempt_and_review(self):
        self.execute()
        self.review()
        self.assertEqual(validate_dataset(self.data), [])
        self.assertFalse(any(c['id'] == self.candidate['id'] for c in self.data['cards']))
        page = render_indexes(self.data)[f'docs/candidates/{self.candidate["id"]}.md']
        self.assertIn('../attempts/ATT-TEST.md', page)
        self.assertIn('../reviews/REV-TEST.md', page)

    def test_outline_entry_can_receive_an_attributed_review(self):
        self.review(review_type='problem_entry')
        self.candidate['human_review_status'] = 'reviewed_accepted'
        self.assertEqual(validate_dataset(self.data), [])

    def test_attempt_acceptance_does_not_endorse_the_problem_entry(self):
        self.execute()
        self.review()
        self.candidate['human_review_status'] = 'reviewed_accepted'
        self.assertTrue(any('requires a matching scoped review' in e for e in validate_dataset(self.data)))

    def test_completed_review_of_an_unexecuted_result_is_rejected(self):
        self.review()
        self.assertTrue(any('requires an executed attempt' in e for e in validate_dataset(self.data)))

    def test_changed_attempt_does_not_inherit_acceptance(self):
        self.execute()
        self.review()
        self.attempt['outcome'] = 'Changed synthetic claim.'
        self.assertEqual(current_attempt_reviews(self.data, self.attempt), [])
        self.assertEqual(validate_dataset(self.data), [])
        self.assertIn('No review of the current result recorded', render_records(self.data)['docs/results.md'])

    def test_later_different_scope_does_not_erase_an_objection(self):
        self.execute()
        objection = self.review(verdict='rejected')
        newer = self.review('REV-NEW')
        newer.update(date='2026-10-15', reviewer='Other reviewer', scope=['Formatting only'])
        current = current_attempt_reviews(self.data, self.attempt)
        self.assertEqual({r['id'] for r in current}, {objection['id'], newer['id']})
        page = render_records(self.data)['docs/results.md']
        self.assertIn('Rejected', page)
        self.assertIn('Formatting only', page)

    def test_unrelated_entry_review_cannot_hide_an_objection(self):
        self.review(verdict='rejected', review_type='problem_entry')
        newer = self.review('REV-NEW', review_type='problem_entry')
        newer.update(date='2026-10-15', reviewer='Other reviewer', scope=['Formatting only'])
        self.candidate['human_review_status'] = 'reviewed_accepted'
        self.assertTrue(any('current review conclusions' in e for e in validate_dataset(self.data)))

    def test_explicit_replacement_preserves_the_earlier_record(self):
        self.execute()
        earlier = self.review(verdict='rejected')
        newer = self.review('REV-NEW')
        newer.update(date='2026-10-15', supersedes=[earlier['id']])
        self.assertEqual(validate_dataset(self.data), [])
        self.assertEqual([r['id'] for r in current_attempt_reviews(self.data, self.attempt)], [newer['id']])
        self.assertIn('docs/reviews/REV-TEST.md', render_records(self.data))

    def test_pending_replacement_does_not_suppress_concluded_review(self):
        self.execute()
        earlier = self.review(verdict='rejected')
        newer = self.review('REV-NEW', verdict='pending')
        newer.update(date='2026-10-15', supersedes=[earlier['id']])
        self.assertEqual([r['id'] for r in current_attempt_reviews(self.data, self.attempt)], [earlier['id']])

    def test_different_reviewer_cannot_supersede_an_objection(self):
        self.execute()
        self.review(verdict='rejected')
        newer = self.review('REV-NEW')
        newer.update(reviewer='Another reviewer', supersedes=['REV-TEST'])
        self.assertTrue(any('supersession must preserve' in e for e in validate_dataset(self.data)))

    def test_review_supersession_cycles_are_rejected(self):
        self.execute()
        earlier = self.review()
        newer = self.review('REV-NEW')
        earlier['supersedes'] = ['REV-NEW']
        newer['supersedes'] = ['REV-TEST']
        self.assertTrue(any('supersession cycle' in e for e in validate_dataset(self.data)))

    def test_result_views_keep_scope_and_exclude_reproductions(self):
        self.execute()
        self.review()
        pages = render_records(self.data)
        result = pages['docs/results.md']
        self.assertIn('Finite certificate only', result)
        self.assertIn('does not establish novelty', result)
        self.assertIn('Synthetic bounded result', pages['docs/attempts/ATT-TEST.md'])
        self.assertIn('Novelty and general case', pages['docs/reviews/REV-TEST.md'])
        self.attempt['outcome_kind'] = 'reproduction'
        self.assertIn('No original research findings', render_records(self.data)['docs/results.md'])

    def test_drafts_have_schema_shape_but_cannot_enter_the_collection_unfinished(self):
        self.data['attempts'] = []
        for kind, rid in [('attempt', 'ATT-DRAFT'), ('review', 'REV-DRAFT')]:
            with self.subTest(kind=kind):
                record = draft_record(self.data, kind, self.candidate['id'], rid, 'Test author', date='2026-10-15')
                errors = []
                schema_check(record, json.loads((ROOT / 'schemas' / f'{kind}.schema.json').read_text()), 'draft', errors)
                self.assertEqual(errors, [])
                self.data['attempts' if kind == 'attempt' else 'reviews'] = [record]
                self.assertTrue(any('unfinished draft' in e for e in validate_dataset(self.data)))
        self.assertEqual(self.data['project']['research_attempts_run'], 0)

    def test_draft_writer_stays_in_work_and_does_not_overwrite(self):
        record = draft_record(self.data, 'attempt', self.candidate['id'], 'ATT-DRAFT', 'Test author')
        with tempfile.TemporaryDirectory(dir=ROOT / 'work') as folder:
            path = save_draft(record, Path(folder))
            self.assertEqual(path.parent, Path(folder) / 'work' / 'drafts')
            with self.assertRaises(FileExistsError):
                save_draft(record, Path(folder))
            with self.assertRaises(ValueError):
                save_draft(dict(record, id='../escape'), Path(folder))

    def test_draft_rejects_unknown_ids_and_cross_problem_reviews(self):
        with self.assertRaises(ValueError):
            draft_record(self.data, 'attempt', 'Q-UNKNOWN', 'ATT-DRAFT', 'Test author')
        with self.assertRaises(ValueError):
            draft_record(self.data, 'attempt', self.candidate['id'], 'ATT-TEST', 'Test author')
        other = next(c for c in self.data['candidates'] if c['id'] != self.candidate['id'])
        with self.assertRaises(ValueError):
            draft_record(self.data, 'review', other['id'], 'REV-DRAFT', 'Test author', attempt_id='ATT-TEST')

    def test_statement_and_attempt_digests_have_distinct_roles(self):
        self.execute()
        review = draft_record(self.data, 'review', self.candidate['id'], 'REV-DRAFT', 'Test author', attempt_id='ATT-TEST')
        self.assertEqual(review['statement_digest'], statement_digest(self.candidate))
        self.assertEqual(review['attempt_digest'], attempt_digest(self.attempt))
        original = attempt_digest(self.attempt)
        self.attempt['review_ids'].append('REV-DRAFT')
        self.attempt['revision_history'].append({'date': '2026-10-15', 'change': 'Added review link.'})
        self.assertEqual(attempt_digest(self.attempt), original)
        self.attempt['target'] += ' Changed target.'
        self.assertNotEqual(attempt_digest(self.attempt), original)

    def test_record_filename_is_its_stable_identity(self):
        with tempfile.TemporaryDirectory(dir=ROOT / 'work') as folder:
            path = Path(folder) / 'ATT-WRONG.json'
            path.write_text(json.dumps(self.attempt), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'filename must match'):
                read_records(Path(folder))


if __name__ == '__main__':
    unittest.main()
