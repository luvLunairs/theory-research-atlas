"""Protect evidence scope, source attribution and status history."""
import copy
import unittest

from render_indexes import render_indexes
from validate import load_dataset, validate_dataset


class LiteratureCheckTests(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(load_dataset())
        candidate = self.data['candidates'][0]
        candidate['last_checked'] = self.data['project']['as_of']
        for card in self.data['cards']:
            if card['id'] == candidate['id']:
                card['last_checked'] = candidate['last_checked']
        self.record = {
            'id': 'LC-TEST', 'problem_id': candidate['id'],
            'checked_on': self.data['project']['as_of'],
            'status_before': 'unverified', 'status_after': candidate['status'],
            'statement_assessment': 'matched', 'coverage': 'statement_only',
            'search_queries': [], 'search_scope': 'Original statement only.',
            'evidence': [{'source_id': candidate['source_ids'][0],
                          'locator': 'Exact source passage.', 'finding': 'Statement identified.'}],
            'conclusion': 'A bounded editorial assessment.',
            'limitations': ['No independent proof audit.'],
        }
        self.data['literature_checks'].append(self.record)

    def test_valid_statement_only_record(self):
        self.assertEqual(validate_dataset(self.data), [])

    def test_latest_check_must_match_candidate(self):
        self.record['status_after'] = 'unverified'
        self.assertTrue(any('differs from candidate status' in e for e in validate_dataset(self.data)))

    def test_resolution_requires_later_literature(self):
        self.record['status_after'] = 'resolved'
        self.assertTrue(any('requires a later-literature check' in e for e in validate_dataset(self.data)))

    def test_conclusion_requires_inspected_evidence(self):
        self.record['coverage'] = 'statement_and_later_literature'
        self.record['evidence'] = []
        self.assertTrue(any('requires evidence' in e for e in validate_dataset(self.data)))

    def test_unknown_source_is_rejected(self):
        self.record['evidence'][0]['source_id'] = 'SRC-MISSING-999'
        self.assertTrue(any('unresolved reference' in e for e in validate_dataset(self.data)))

    def test_history_and_limits_are_visible(self):
        self.record['previous_statement'] = 'An earlier formulation with incomplete assumptions.'
        pages = render_indexes(self.data)
        page = pages[f'docs/candidates/{self.record["problem_id"]}.md']
        for field in ['conclusion', 'search_scope']:
            self.assertIn(self.record[field], page)
        self.assertIn(self.record['limitations'][0], page)
        self.assertIn(self.record['evidence'][0]['locator'], page)
        self.assertIn(self.record['previous_statement'], page)
        self.assertIn('#literature-checks', pages['docs/literature-checks.md'])

    def test_correction_requires_original_wording(self):
        self.record['statement_assessment'] = 'corrected'
        self.assertTrue(any('requires previous wording' in e for e in validate_dataset(self.data)))

    def test_same_day_checks_must_be_combined(self):
        duplicate = dict(self.record, id='LC-SECOND')
        self.data['literature_checks'].append(duplicate)
        self.assertTrue(any('duplicate literature-check date' in e for e in validate_dataset(self.data)))

    def test_status_history_cannot_skip_a_change(self):
        earlier = dict(self.record, id='LC-EARLIER', checked_on='2026-10-12')
        self.data['literature_checks'].append(earlier)
        self.assertTrue(any('discontinuous literature status history' in e for e in validate_dataset(self.data)))

    def test_later_matched_check_does_not_hide_correction(self):
        earlier = dict(self.record, id='LC-EARLIER', checked_on='2026-10-12',
                       statement_assessment='corrected', previous_statement='Earlier incomplete target.',
                       conclusion='An important historical correction.')
        self.data['literature_checks'].append(earlier)
        self.assertIn(earlier['conclusion'], render_indexes(self.data)['docs/literature-checks.md'])


if __name__ == '__main__':
    unittest.main()
