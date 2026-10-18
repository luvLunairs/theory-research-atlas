"""Guard evidence preservation and navigation across changes to the atlas hierarchy."""
import copy
import re
import unittest

from render_indexes import active_research, render_indexes
from render_cards import contribution_links
from validate import load_dataset


class IndexRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataset = load_dataset()
        cls.pages = render_indexes(cls.dataset)

    def test_every_branch_has_one_definition_destination(self):
        domain_pages = [text for path, text in self.pages.items() if path.startswith('docs/domains/')]
        for node in self.dataset['nodes']:
            target = f'<a id="{node["id"].lower().replace(".", "-")}"></a>'
            self.assertEqual(sum(text.count(target) for text in domain_pages), 1, node['id'])
            destination = next(text for text in domain_pages if target in text)
            for field in ('definition', 'boundary', 'rationale', 'coverage_note'):
                self.assertIn(node[field], destination, (node['id'], field))

    def test_source_evidence_survives_disclosure_layout(self):
        page = self.pages['docs/sources.md']
        for source in self.dataset['sources']:
            for field in ('locator', 'limitations', 'url'):
                self.assertIn(source[field], page, (source['id'], field))
            for support in source['supports']:
                self.assertIn(support, page, source['id'])

    def test_candidate_statements_and_status_basis_survive(self):
        for candidate in self.dataset['candidates']:
            page = self.pages[f'docs/candidates/{candidate["id"]}.md']
            self.assertIn(candidate['statement'], page, candidate['id'])
            self.assertIn(candidate['status_basis'], page, candidate['id'])
            self.assertIn(candidate['source_locator'], page, candidate['id'])

    def test_pending_page_separates_unresolved_status_from_planning(self):
        page = self.pages['docs/pending-checks.md']
        first, later = page.split('## Further review and planning\n', 1)
        self.assertIn('Q-LAND-305.md)', first)
        self.assertNotIn('Q-LAND-305.md)', later)
        self.assertIn('Q-MATH-001.md)', later)
        self.assertNotIn('Q-MATH-001.md)', first)
        linked = re.findall(r'\]\((?:cards|candidates)/(Q-[A-Z]+-\d+)\.md\)', page)
        expected = {c['problem_id'] for c in self.dataset['checks'] if c['missing_information']}
        self.assertEqual(set(linked), expected)
        self.assertEqual(len(linked), len(expected))

    def test_reparenting_uses_hierarchy_not_id_prefix(self):
        data = copy.deepcopy(self.dataset)
        node = next(n for n in data['nodes'] if n['id'] == 'MATH.COMB')
        node['parent_id'] = 'CS'
        pages = render_indexes(data)
        self.assertIn('domains/cs.md#math-comb-ext', pages['docs/candidates.md'])
        self.assertIn('<a id="math-comb-ext"></a>', pages['docs/domains/cs.md'])
        self.assertNotIn('<a id="math-comb-ext"></a>', pages['docs/domains/math.md'])

    def test_root_links_open_domain_overview(self):
        home = self.pages['docs/README.md']
        self.assertIn('[Mathematics](domains/math.md)', home)
        self.assertNotIn('(domains/math.md#math)', home)

    def test_browsing_keeps_human_routes_visible_and_tools_optional(self):
        home = self.pages['docs/README.md']
        expanded = re.sub(r'<details>.*?</details>', '', home, flags=re.S)
        for node in self.dataset['nodes']:
            if node['parent_id'] is None:
                self.assertIn(f'](domains/{node["id"].lower()}.md)', expanded)
        for destination in ('research-candidates.md', 'pending-checks.md', '../CONTRIBUTING.md'):
            self.assertIn(f']({destination})', expanded)
        for destination in ('catalog.md', 'data-model.md', 'taxonomy.md', 'sources.md'):
            self.assertIn(f']({destination})', home)
            self.assertNotIn(f']({destination})', expanded)

    def test_candidate_routes_identify_target_and_keep_data_accessible(self):
        for candidate in self.dataset['candidates']:
            page = self.pages[f'docs/candidates/{candidate["id"]}.md']
            expanded = re.sub(r'<details>.*?</details>', '', page, flags=re.S)
            self.assertIn(contribution_links(candidate), expanded)
            for destination in ('../../data/candidates.json', '../../data/candidate-checks.json'):
                self.assertIn(f']({destination})', page)
                self.assertNotIn(f']({destination})', expanded)
            navigation = page.split('\n\n')[1]
            self.assertEqual(len(re.findall(r'\]\(', navigation)), 3)
            for destination in ('../README.md', '../results.md', '../../CONTRIBUTING.md'):
                self.assertIn(f']({destination})', navigation)

    def test_coverage_source_aliases_link_to_retained_records(self):
        page = self.pages['docs/coverage.md']
        for item in self.dataset['coverage_notes']:
            if not isinstance(item['note'], dict):
                continue
            for source_id in item['note'].get('source_ids', []):
                target = self.dataset['aliases'].get(source_id, source_id)
                self.assertIn(f'](sources.md#{target.lower()})', page)
                if target != source_id:
                    self.assertNotIn(f'](sources.md#{source_id.lower()})', page)

    def test_disclosures_and_explicit_ids_are_well_formed(self):
        for path, text in self.pages.items():
            self.assertEqual(text.count('<details>'), text.count('</details>'), path)
            self.assertEqual(text.count('<details>'), text.count('<summary>'), path)
            ids = re.findall(r'<a id="([^"]+)"></a>', text)
            self.assertEqual(len(ids), len(set(ids)), path)
            for body in re.findall(r'<summary>(.*?)</summary>', text, re.S):
                self.assertNotIn('<', body, path)

    def test_progress_does_not_treat_curation_as_research(self):
        data = copy.deepcopy(self.dataset)
        data['attempts'] = []
        data['reviews'] = []
        page = render_indexes(data)['docs/progress.md']
        self.assertIn('Recorded attempts: 0', page)
        self.assertIn('No research attempts or reviews have been recorded.', page)
        self.assertNotIn('## Attempts', page)

    def test_research_selection_requires_origin_and_current_open_evidence(self):
        for kind in ('literature_open', 'curator_proposed', 'known_result_calibration'):
            for status in self.dataset['vocabularies']['status']:
                expected = kind == 'literature_open' and status in {'source_reports_open', 'open_after_scoped_check'}
                self.assertEqual(active_research(dict(kind=kind, status=status)), expected)

    def test_research_page_has_no_calibration_or_resolved_problem_links(self):
        page = self.pages['docs/research-candidates.md']
        cards = {c['id'] for c in self.dataset['cards']}
        for c in self.dataset['candidates']:
            target = f'cards/{c["id"]}.md' if c['id'] in cards else f'candidates/{c["id"]}.md'
            self.assertEqual(f']({target})' in page, active_research(c), c['id'])

    def test_progress_preserves_attempt_and_review_scope(self):
        data = copy.deepcopy(self.dataset)
        card = data['cards'][0]
        data['attempts'] = [{'id': 'ATT-test', 'problem_id': card['id'], 'status': 'completed', 'outcome': 'No proof found.'}]
        data['reviews'] = [{'id': 'REV-test', 'problem_id': card['id'], 'verdict': 'inconclusive', 'scope': ['Code only.']}]
        page = render_indexes(data)['docs/progress.md']
        self.assertIn('Recorded attempts: 1', page)
        self.assertIn('Recorded reviews: 1', page)
        self.assertIn('No proof found.', page)
        self.assertIn('Code only.', page)
        self.assertIn(f'cards/{card["id"]}.md', page)
        self.assertIn('attempts/ATT-test.md', page)
        self.assertIn('reviews/REV-test.md', page)
        self.assertNotIn('No research attempts or reviews have been recorded.', page)

    def test_candidate_profiles_preserve_reasons_and_uncertainty(self):
        for profile in self.dataset['profiles']:
            page=self.pages[f'docs/candidates/{profile["problem_id"]}.md']
            for key in ['difficulty_basis','ai_role','verification_basis','resource_expectation','uncertainty']:
                self.assertIn(profile[key],page,(profile['problem_id'],key))

    def test_difficulty_view_labels_provisional_questions_and_excludes_resolved(self):
        page=self.pages['docs/difficulty.md']
        cards={c['id'] for c in self.dataset['cards']}
        for c in self.dataset['candidates']:
            target=f'cards/{c["id"]}.md' if c['id'] in cards else f'candidates/{c["id"]}.md'
            expected = active_research(c) or (c['kind']=='literature_open' and c['status'] in {'unverified','conflicting','conditional'})
            self.assertEqual(f']({target})' in page,expected,c['id'])
        self.assertIn('Candidates awaiting statement or status checks',page)
        self.assertIn('Their difficulty ratings do not establish that they are still open.',page)

    def test_landmark_status_scope_and_source_limits_are_visible(self):
        page=self.pages['docs/landmark-problems.md']
        for entry in self.dataset['landmarks']:
            for key in ['scope','status_basis','source_locator']:
                self.assertIn(entry[key],page,(entry['id'],key))
    def test_information_gaps_remain_visible(self):
        pending=self.pages['docs/pending-checks.md']
        for check in self.dataset['checks']:
            page=self.pages[f'docs/candidates/{check["problem_id"]}.md']
            for field in ['source_date_note','scope_note']:
                self.assertIn(check[field],page,check['problem_id'])
            for gap in check['missing_information']:
                self.assertIn(gap,page,check['problem_id'])
                self.assertIn(gap.replace('|','\\|').replace('\n',' '),pending,check['problem_id'])
    def test_index_retains_each_stable_anchor_and_detail_link(self):
        page=self.pages['docs/candidates.md']
        for c in self.dataset['candidates']:
            self.assertIn(f'<a id="{c["id"].lower()}"></a>',page)
            self.assertIn(f'](candidates/{c["id"]}.md)',page)


if __name__ == '__main__':
    unittest.main()
