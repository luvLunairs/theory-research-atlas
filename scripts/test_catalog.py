"""Keep local selections reproducible and evidence-complete."""
import copy
import io
import json
import unittest
from contextlib import redirect_stdout

from catalog import main, select
from validate import load_dataset


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_dataset()

    def test_default_returns_every_id_once(self):
        rows = select(self.data)
        self.assertEqual({r['candidate']['id'] for r in rows}, {c['id'] for c in self.data['candidates']})
        self.assertEqual(len(rows), len(self.data['candidates']))

    def test_research_filter_excludes_resolved_and_calibrations(self):
        for row in select(self.data, research=True):
            self.assertEqual(row['candidate']['kind'], 'literature_open')
            self.assertIn(row['candidate']['status'], {'source_reports_open', 'open_after_scoped_check'})

    def test_domain_uses_tree_and_crosslinks_do_not_duplicate(self):
        data = copy.deepcopy(self.data)
        next(n for n in data['nodes'] if n['id'] == 'MATH.COMB')['parent_id'] = 'CS'
        ids = [r['candidate']['id'] for r in select(data, domain='CS', include_cross_links=True)]
        self.assertIn('Q-MATH-001', ids)
        self.assertEqual(len(ids), len(set(ids)))

    def test_repeated_statuses_are_or_filters(self):
        rows = select(self.data, statuses=['resolved', 'disproved'])
        self.assertEqual(len(rows), sum(c['status'] in {'resolved', 'disproved'} for c in self.data['candidates']))

    def test_export_keeps_full_evidence_and_card(self):
        row = select(self.data, problem_id='Q-CODE-201')[0]
        self.assertIsNotNone(row['card'])
        self.assertTrue(row['sources'])
        self.assertIn('missing_information', row['check'])
        checked = next(r for r in select(self.data) if r['literature_checks'])
        cited = {s['id'] for s in checked['sources']}
        self.assertTrue(all(e['source_id'] in cited for lc in checked['literature_checks'] for e in lc['evidence']))

    def test_phrase_search_finds_scientific_statement(self):
        rows = select(self.data, query='"covering code"')
        self.assertIn('Q-CODE-201', {r['candidate']['id'] for r in rows})

    def test_latest_coverage_not_any_historical_coverage(self):
        data = copy.deepcopy(self.data)
        item = data['literature_checks'][0]
        data['literature_checks'].append(dict(item, id='LC-NEW', checked_on='2099-01-01', coverage='access_limited'))
        self.assertIn(item['problem_id'], {r['candidate']['id'] for r in select(data, coverage='access_limited')})

    def test_limited_json_keeps_total_count_and_filters(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(['--status', 'unverified', '--limit', '2', '--format', 'json']), 0)
        result = json.loads(output.getvalue())
        self.assertEqual(result['returned'], 2)
        self.assertGreater(result['total_matches'], 2)
        self.assertEqual(result['filters']['statuses'], ['unverified'])

    def test_checked_before_is_strict(self):
        date = min(c['last_checked'] for c in self.data['candidates'])
        self.assertEqual(select(self.data, checked_before=date), [])

    def test_apostrophes_are_literal_search_characters(self):
        data = copy.deepcopy(self.data)
        data['candidates'][0]['title'] = "Erdős's test question"
        rows = select(data, query="Erdős's")
        self.assertEqual(rows[0]['candidate']['id'], data['candidates'][0]['id'])


if __name__ == '__main__':
    unittest.main()
