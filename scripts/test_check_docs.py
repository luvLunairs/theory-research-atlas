"""Check references in the context where contributors will read them."""
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from check_docs import (issue_form_errors, main, repository_link_errors,
                        submission_reference_errors)


class SubmissionReferenceTests(unittest.TestCase):
    def test_relative_links_are_rejected_in_all_submission_formats(self):
        for name in ('.github/ISSUE_TEMPLATE/correction.yml',
                     '.github/PULL_REQUEST_TEMPLATE.md', 'templates/review.md'):
            with self.subTest(name=name):
                errors = submission_reference_errors(
                    Path(name), 'Read [the policy](../../docs/ai-contributions.md).')
                self.assertEqual(len(errors), 1)

    def test_repository_file_navigation_remains_relative(self):
        self.assertEqual(submission_reference_errors(
            Path('docs/review-guide.md'), '[Contributing](../CONTRIBUTING.md)'), [])

    def test_portable_references_are_accepted(self):
        text = ('See `CONTRIBUTING.md` and '
                '[the source](https://example.org/paper). [Scope](#scope)\n\n'
                '```md\n[example](relative.md)\n```')
        self.assertEqual(submission_reference_errors(Path('templates/review.md'), text), [])


class RepositoryLinkTests(unittest.TestCase):
    url = 'https://github.com/luvLunairs/theory-research-atlas'
    source = Path('CONTRIBUTING.md')

    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / 'docs').mkdir()
        (self.root / 'docs/guide.md').write_text(
            '# Guide\n\n## Evidence and attribution\n', encoding='utf-8')
        (self.root / '.github/ISSUE_TEMPLATE').mkdir(parents=True)
        (self.root / '.github/ISSUE_TEMPLATE/correction.yml').write_text(
            'name: Correction\n', encoding='utf-8')

    def check(self, suffix):
        return repository_link_errors(self.source, self.url + suffix, self.root)

    def test_main_branch_files_and_encoded_fragments_resolve_locally(self):
        self.assertEqual(self.check('/blob/main/docs/guide.md'), [])
        self.assertEqual(self.check(
            '/blob/main/docs/guide.md#evidence%2Dand%2Dattribution'), [])

    def test_missing_files_and_fragments_are_reported(self):
        self.assertIn('missing target', self.check('/blob/main/missing.md')[0])
        self.assertIn('missing fragment', self.check('/blob/main/docs/guide.md#missing')[0])

    def test_form_url_accepts_encoded_title_and_prefilled_text(self):
        self.assertEqual(self.check(
            '/issues/new?template=correction%2Eyml&title=Q%3A%20%28example%29'
            '&target=Q-MATH-001%20%23%20evidence%20%26%20notes'), [])

    def test_unknown_and_ambiguous_forms_are_reported(self):
        self.assertIn('missing target', self.check('/issues/new?template=missing.yml')[0])
        self.assertIn('expected one issue form', self.check(
            '/issues/new?template=correction.yml&template=missing.yml')[0])
        self.assertIn('invalid issue form name', self.check('/issues/new?template=')[0])
        self.assertIn('invalid issue form name', self.check('/issues/new?template=config.yml')[0])

    def test_encoded_paths_cannot_escape_the_checkout_or_forms_directory(self):
        for name in ('%2E%2E/outside.md', '%2Foutside.md', '%5C%5Cserver/share.md',
                     'C%3A/outside.md'):
            with self.subTest(name=name):
                self.assertIn('escapes project', self.check('/blob/main/' + name)[0])
        for selector in ('..%2Fcorrection.yml', '..%5Ccorrection.yml', '%2Fcorrection.yml'):
            with self.subTest(selector=selector):
                self.assertIn('invalid issue form name', self.check(
                    '/issues/new?template=' + selector)[0])

    def test_unrelated_external_and_generic_github_routes_remain_uninspected(self):
        for target in ('https://github.com/another/repository/blob/main/missing.md',
                       'https://example.org/paper', self.url + '/issues/new/choose',
                       self.url + '/issues/new?title=Example',
                       self.url + '/blob/other-branch/missing.md'):
            with self.subTest(target=target):
                self.assertIsNone(repository_link_errors(self.source, target, self.root))

    def test_main_checks_absolute_links_in_markdown_and_yaml(self):
        for name in ('README.md', 'templates/review.md', '.github/ISSUE_TEMPLATE/report.yml'):
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(
                '[Guide](' + self.url + '/blob/main/docs/guide.md#missing)', encoding='utf-8')
        output = StringIO()
        with patch('check_docs.ROOT', self.root), redirect_stdout(output):
            self.assertTrue(main())
        report = output.getvalue()
        for name in ('README.md', 'templates/review.md', '.github/ISSUE_TEMPLATE/report.yml'):
            self.assertIn(name + ': missing fragment', report)


class IssueFormTests(unittest.TestCase):
    path = Path('.github/ISSUE_TEMPLATE/correction.yml')

    def dropdown(self, option):
        return ('body:\n  - type: dropdown\n    attributes:\n'
                '      label: AI assistance\n      options:\n'
                f'        - {option}\n    validations:\n      required: true\n')

    def test_reserved_choice_is_rejected_with_or_without_quotes(self):
        for option in ('None', 'none', 'NONE', '"None"', "'none'", '"None" # choice'):
            with self.subTest(option=option):
                errors = issue_form_errors(self.path, self.dropdown(option))
                self.assertEqual(len(errors), 1)
                self.assertIn('correction.yml:6:', errors[0])
                self.assertIn('reserved', errors[0])

    def test_descriptive_choice_and_prose_are_allowed(self):
        text = self.dropdown('"No AI assistance"') + (
            '  - type: markdown\n    attributes:\n      value: |\n'
            '        None of these examples establishes a proof.\n'
            '        - type: dropdown\n          attributes:\n'
            '            options:\n              - None\n'
            '  - type: textarea\n    attributes:\n'
            '      label: Notes\n      value: "None"\n')
        self.assertEqual(issue_form_errors(self.path, text), [])

    def test_checkbox_labels_and_other_yaml_files_are_out_of_scope(self):
        checkboxes = ('body:\n  - type: checkboxes\n    attributes:\n'
                      '      label: Examples\n      options:\n'
                      '        - label: "None"\n')
        self.assertEqual(issue_form_errors(self.path, checkboxes), [])
        self.assertEqual(issue_form_errors(Path('docs/example.yml'), self.dropdown('None')), [])

    def test_options_do_not_leak_into_another_field(self):
        text = self.dropdown('"No AI assistance"') + (
            '  - type: textarea\n    attributes:\n      label: Notes\n'
            '      description: |\n        options:\n          - None\n')
        self.assertEqual(issue_form_errors(self.path, text), [])

    def test_yaml_extension_and_indentless_options_are_checked(self):
        text = self.dropdown('None').replace('        - None', '      - None')
        self.assertEqual(len(issue_form_errors(
            Path('.github/ISSUE_TEMPLATE/example.yaml'), text)), 1)


if __name__ == '__main__':
    unittest.main()
