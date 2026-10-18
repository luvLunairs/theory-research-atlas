"""Check that verification views preserve scope, evidence and derived states."""
import copy
import tempfile
import unittest
from pathlib import Path

from machine_verification import ROOT, specification_digest
from render import outputs
from render_verifications import render_verifications, verification_summary
from research_records import attempt_digest, statement_digest
from test_machine_verification import fixture_dataset
from validate import load_dataset


class VerificationRenderingTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'work').mkdir(exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix='verification-render-', dir=ROOT / 'work')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.data = fixture_dataset(self.root)
        self.data['candidates'][0]['title'] = 'Synthetic verification target'

    @property
    def spec(self):
        return self.data['verification_specs'][0]

    @property
    def verification(self):
        return self.data['verifications'][0]

    def run_page(self):
        return render_verifications(self.data, self.root)['docs/verifications/VER-TEST.md']

    def test_empty_index_is_useful_without_claiming_research(self):
        self.data['verification_specs'] = []
        self.data['verifications'] = []
        pages = render_verifications(self.data, self.root)
        self.assertEqual(set(pages), {'docs/verifications.md'})
        self.assertIn('Specifications: 0 · Recorded runs: 0', pages['docs/verifications.md'])
        self.assertIn('No verification specifications or runs', pages['docs/verifications.md'])
        self.assertIn('machine-verification.md#start-here', pages['docs/verifications.md'])

    def test_current_pass_preserves_exact_claim_and_artifacts(self):
        original = copy.deepcopy(self.data)
        pages = render_verifications(self.data, self.root)
        page = pages['docs/verifications/VER-TEST.md']
        spec_page = pages['docs/verification-specs/VSPEC-TEST.md']
        self.assertIn('**Verification state:** Machine checked.', page)
        self.assertIn(self.spec['claim'], page)
        self.assertIn(self.spec['scope'][0], page)
        self.assertIn(self.verification['attempt_digest'], page)
        self.assertIn(self.verification['specification_digest'], page)
        self.assertIn(specification_digest(self.spec), spec_page)
        for record, rendered in [(self.spec, spec_page), (self.verification, page)]:
            for item in record['artifact_manifest']:
                self.assertIn(item['reference'], rendered)
                self.assertIn(item['version'], rendered)
                self.assertIn(item['sha256'], rendered)
        self.assertEqual(self.data, original)

    def test_reported_pass_does_not_inherit_recorded_success(self):
        self.verification['runner']['provenance'] = 'contributor'
        page = self.run_page()
        self.assertIn('**Verification state:** Reported pass.', page)
        self.assertNotIn('**Verification state:** Machine checked.', page)
        self.assertIn('Reported pass', verification_summary(self.data, 'ATT-TEST', root=self.root))

    def test_stale_claim_is_not_presented_as_the_checked_version(self):
        self.spec['claim'] = 'Changed synthetic claim.'
        page = self.run_page()
        self.assertIn('**Verification state:** Stale.', page)
        self.assertIn('historical wording checked by this run', page)
        self.assertNotIn('**Verification state:** Machine checked.', page)
        spec_page = render_verifications(self.data, self.root)['docs/verification-specs/VSPEC-TEST.md']
        self.assertIn('Approved for an earlier specification', spec_page)

    def test_failed_run_and_conflicting_rerun_remain_visible(self):
        self.verification['outcome'] = 'failed'
        self.assertIn('**Verification state:** Failed.', self.run_page())
        other = copy.deepcopy(self.verification)
        other.update(id='VER-OTHER', outcome='passed')
        self.data['verifications'].append(other)
        pages = render_verifications(self.data, self.root)
        self.assertIn('**Verification state:** Conflicting evidence.', pages['docs/verifications/VER-TEST.md'])
        self.assertIn('**Verification state:** Conflicting evidence.', pages['docs/verifications/VER-OTHER.md'])
        self.assertIn('VER-OTHER', pages['docs/verifications.md'])

    def test_invalid_artifact_cannot_display_a_machine_pass(self):
        (self.root / 'research' / 'certificate.txt').write_text('Changed bytes.', encoding='utf-8')
        self.assertIn('**Verification state:** Invalid verification record.', self.run_page())

    def test_full_views_keep_human_review_and_research_counts_separate(self):
        data = copy.deepcopy(load_dataset())
        card = data['cards'][0]
        for record in [self.spec, self.verification, self.data['attempts'][0]]:
            record['problem_id'] = card['id']
        self.spec['statement_digest'] = statement_digest(card)
        self.spec['approval']['specification_digest'] = specification_digest(self.spec)
        self.verification['specification_digest'] = specification_digest(self.spec)
        self.verification['attempt_digest'] = attempt_digest(self.data['attempts'][0])
        for field in ['attempts', 'verification_specs', 'verifications']:
            data[field] = self.data[field]
        data['project']['as_of'] = self.data['project']['as_of']
        original = copy.deepcopy(data)
        pages = outputs(data, root=self.root)
        self.assertIn('Machine checked', pages[f'docs/cards/{card["id"]}.md'])
        self.assertIn('Machine checked', pages[f'docs/candidates/{card["id"]}.md'])
        self.assertIn('Machine checked', pages['docs/attempts/ATT-TEST.md'])
        self.assertIn('Machine verification and scope', pages['docs/results.md'])
        self.assertIn('Current human review scope', pages['docs/results.md'])
        self.assertIn('Recorded attempts: 1 · Recorded reviews: 0', pages['docs/progress.md'])
        other = next(c for c in data['candidates'] if c['id'] != card['id'])
        self.assertNotIn('## Machine verification', pages[f'docs/candidates/{other["id"]}.md'])
        self.assertEqual(data, original)


if __name__ == '__main__':
    unittest.main()
