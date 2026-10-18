"""Presentation regression checks; these do not execute research tasks."""
import copy
from html import unescape
import re
import unittest
from urllib.parse import parse_qs, urlsplit

from render_cards import CARD_FIELDS, SECTIONS, contribution_links, render_cards
from validate import load_dataset


def normalized(value):
    """Compare displayed content after Markdown/HTML presentation escaping."""
    text = unescape(str(value)).replace('\\[', '[').replace('\\]', ']')
    return ' '.join(text.replace('_', ' ').lower().split())


def string_leaves(value, path=()):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from string_leaves(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from string_leaves(child, path + (index,))


class CardPresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_dataset()
        cls.outputs = render_cards(cls.data)

    def test_expected_paths_and_input_unchanged(self):
        original = copy.deepcopy(self.data)
        render_cards(self.data)
        self.assertEqual(original, self.data)
        expected = {'docs/cards/README.md'} | {
            f'docs/cards/{card["id"]}.md' for card in self.data['cards']
        }
        self.assertEqual(expected, set(self.outputs))

    def test_contribution_urls_preserve_form_target_and_title(self):
        problem = {'id': 'Q-TEST-001', 'title': 'Bounds (n > 0) & A/B? [draft] #1 + α'}
        links = re.findall(r'\]\((https://[^)]+)\)', contribution_links(problem))
        self.assertEqual(len(links), 2)
        for link, template, prefix in zip(links, ['correction.yml', 'research-progress.yml'], ['Correction', 'Research']):
            parsed = urlsplit(link)
            self.assertEqual(parsed.scheme, 'https')
            self.assertEqual(parsed.netloc, 'github.com')
            self.assertEqual(parsed.path, '/luvLunairs/theory-research-atlas/issues/new')
            self.assertFalse(parsed.fragment)
            self.assertEqual(parse_qs(parsed.query), {
                'template': [template], 'target': [problem['id']],
                'title': [f'[{prefix}] {problem["id"]}: {problem["title"]}'],
            })

    def test_each_card_has_its_own_contribution_routes(self):
        for card in self.data['cards']:
            text = self.outputs[f'docs/cards/{card["id"]}.md']
            expanded = re.sub(r'<details>.*?</details>', '', text, flags=re.S)
            self.assertIn(contribution_links(card), expanded)
            navigation = text.split('\n\n')[1]
            self.assertEqual(len(re.findall(r'\]\(', navigation)), 3)
            for destination in ('../README.md', '../results.md', '../../CONTRIBUTING.md'):
                self.assertIn(f']({destination})', navigation)

    def test_all_card_content_remains_accessible(self):
        # Metadata codes may be expanded into words, but no statement, qualifier,
        # resource warning, attribution, query, or revision text may disappear.
        for card in self.data['cards']:
            text = normalized(self.outputs[f'docs/cards/{card["id"]}.md'])
            for path, value in string_leaves(card):
                with self.subTest(card=card['id'], path=path):
                    self.assertIn(normalized(value), text)
            self.assertEqual(set(card), CARD_FIELDS)

    def test_six_sections_have_explicit_stable_anchors(self):
        for card in self.data['cards']:
            text = self.outputs[f'docs/cards/{card["id"]}.md']
            anchors = re.findall(r'<a id="([^"]+)"></a>', text)
            with self.subTest(card=card['id']):
                self.assertEqual([anchor for anchor, _ in SECTIONS], anchors)
                self.assertEqual(6, len(re.findall(r'^## ', text, re.M)))
                for anchor, _ in SECTIONS:
                    self.assertIn(f'](#{anchor})', text)

    def test_science_and_resource_constraints_are_not_collapsed(self):
        for card in self.data['cards']:
            text = self.outputs[f'docs/cards/{card["id"]}.md']
            expanded = normalized(re.sub(r'<details>.*?</details>', '', text, flags=re.S))
            required = [card['statement'], card['scope'], card['target'], card['status_basis'],
                        card['status_search']['limitations'], *card['assumptions'],
                        *card['success_criteria'], *card['requirements'].values(),
                        *card['epistemic_layers'].values()]
            for value in required:
                with self.subTest(card=card['id'], value=value):
                    self.assertIn(normalized(value), expanded)

    def test_index_keeps_full_compute_warnings_and_only_card_targets(self):
        index = self.outputs['docs/cards/README.md']
        for card in self.data['cards']:
            self.assertIn(normalized(card['requirements']['compute']), normalized(index))
            self.assertIn(f']({card["id"]}.md)', index)
        card_ids = {card['id'] for card in self.data['cards']}
        linked_ids = set(re.findall(r'\]\((Q-[A-Z]+-\d+)\.md(?:#[^)]+)?\)', index))
        self.assertEqual(card_ids, linked_ids)
        self.assertIn('detailed problem entries', index)
        self.assertIn('Other candidates have not received an AI suitability assessment', index)

    def test_disclosures_and_labels_preserve_interpretation(self):
        for path, text in self.outputs.items():
            with self.subTest(path=path):
                self.assertEqual(text.count('<details>'), text.count('</details>'))
                self.assertRegex(text, r'<summary>[^\n]+</summary>\n\n')
                self.assertNotIn('```json', text)
                self.assertIn('Untested forecast', text)
                if path != 'docs/cards/README.md':
                    self.assertIn('larger burden', text)
                    self.assertIn('Scientific review', text)
                    self.assertIn('[JSON record]', text)

    def test_sources_and_domains_use_named_stable_links(self):
        sources = {source['id']: source for source in self.data['sources']}
        nodes = {node['id']: node for node in self.data['nodes']}
        for card in self.data['cards']:
            text = self.outputs[f'docs/cards/{card["id"]}.md']
            for source_id in card['source_ids']:
                self.assertIn(f'](../sources.md#{source_id.lower()})', text)
                self.assertIn(f'[Read source]({sources[source_id]["url"]})', text)
            for node_id in [card['primary_domain_id'], *card['cross_domain_ids']]:
                root = nodes[node_id]
                while root['parent_id'] is not None:
                    root = nodes[root['parent_id']]
                fragment = '' if nodes[node_id]['parent_id'] is None else '#' + node_id.lower().replace('.', '-')
                self.assertIn(f'](../domains/{root["id"].lower()}.md{fragment})', text)

    def test_root_domain_links_open_overviews(self):
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        card['primary_domain_id'] = 'MATH'
        card['cross_domain_ids'] = ['CS']
        views = render_cards(data)
        text = views[f'docs/cards/{card["id"]}.md']
        self.assertIn('](../domains/math.md)', text)
        self.assertIn('](../domains/cs.md)', text)
        self.assertNotIn('](../domains/math.md#math)', text)
        self.assertNotIn('](../domains/cs.md#cs)', text)
        self.assertIn('](../domains/math.md)', views['docs/cards/README.md'])

    def test_prerequisite_and_dependency_labels_preserve_direction(self):
        text = self.outputs['docs/cards/Q-MODEL-002.md']
        self.assertRegex(text, r'\*\*Prerequisite for:\*\* \[[^\n]+\]\(../candidates.md#q-model-012\)')
        self.assertNotIn('**Prerequisite:**', text)
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        card['relations'] = [{'type': 'depends_on', 'target': 'Q-MODEL-002',
                              'explanation': 'The source task requires the target task.'}]
        text = render_cards(data)[f'docs/cards/{card["id"]}.md']
        self.assertRegex(text, r'\*\*Depends on:\*\* \[[^\n]+\]\(../candidates.md#q-model-002\)')

    def test_additional_record_fields_are_not_silently_lost(self):
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        card['future_note'] = 'An additional audited field must stay accessible.'
        text = render_cards(data)[f'docs/cards/{card["id"]}.md']
        self.assertIn(card['future_note'], text)

    def test_empty_research_records_are_concise(self):
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        data['attempts'] = []
        data['reviews'] = []
        card['revision_history'] = []
        text = render_cards(data)[f'docs/cards/{card["id"]}.md']
        records = text.split('## Research records\n\n', 1)[1]
        self.assertIn('No project attempts or human reviews have been recorded.', records)
        self.assertNotIn('<summary>Project attempts</summary>', records)
        self.assertNotIn('<summary>Scientific reviews</summary>', records)
        self.assertNotIn('<summary>Changes to this problem</summary>', records)
        self.assertNotIn('None recorded.', records)

    def test_scientific_records_remain_when_present(self):
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        data['attempts'] = [{'id': 'ATT-TEST', 'problem_id': card['id'], 'status': 'completed',
                             'outcome': 'The bounded calculation found a counterexample.'}]
        data['reviews'] = [{'id': 'REV-TEST', 'problem_id': card['id'], 'verdict': 'inconclusive',
                            'scope': ['The certificate checks only the stated finite case.']}]
        card['revision_history'] = [{'date': '2026-10-14', 'change': 'Restricted the statement to finite alphabets.'}]
        text = render_cards(data)[f'docs/cards/{card["id"]}.md']
        self.assertIn(data['attempts'][0]['outcome'], text)
        self.assertIn(data['reviews'][0]['scope'][0], text)
        self.assertIn('](../attempts/ATT-TEST.md)', text)
        self.assertIn('](../reviews/REV-TEST.md)', text)
        self.assertIn(card['revision_history'][0]['change'], text)
        self.assertNotIn('No project attempts or human reviews have been recorded.', text)

    def test_empty_literature_queries_are_not_shown(self):
        data = copy.deepcopy(self.data)
        card = data['cards'][0]
        card['status_search']['queries'] = []
        text = render_cards(data)[f'docs/cards/{card["id"]}.md']
        self.assertNotIn('**Queries used:**', text)
        self.assertIn('<summary>Literature references checked</summary>', text)
        for source_id in card['status_search']['checked_sources']:
            self.assertIn(f'](../sources.md#{source_id.lower()})', text)

    def test_correctness_novelty_and_uncertainty_are_visible(self):
        for card in self.data['cards']:
            text = self.outputs[f'docs/cards/{card["id"]}.md']
            expanded = normalized(re.sub(r'<details>.*?</details>', '', text, flags=re.S))
            self.assertIn(normalized(card['judgments']['correctness']['basis']), expanded)
            self.assertIn(normalized(card['judgments']['novelty']['basis']), expanded)
            self.assertIn(normalized(card['ai_assessment']['uncertainty']), expanded)


if __name__ == '__main__':
    unittest.main()
