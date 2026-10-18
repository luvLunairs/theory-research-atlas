"""Check evidence retention using temporary files confined to the project."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from artifact_integrity import validate_record_artifacts


class ArtifactIntegrityTests(unittest.TestCase):
    def setUp(self):
        work = Path(__file__).resolve().parents[1] / 'work'
        work.mkdir(exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(prefix='artifact-tests-', dir=work)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.record = {'id': 'ATT-TEST', 'process_artifacts': [], 'artifact_manifest': []}

    def retain(self, reference='evidence/proof.txt', content=b'Synthetic evidence.\n'):
        path = self.root / reference
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        item = {'reference': reference, 'version': 'Synthetic retained snapshot v1',
                'sha256': 'sha256:' + hashlib.sha256(content).hexdigest()}
        self.record['process_artifacts'].append(reference)
        self.record['artifact_manifest'].append(item)
        return path, item

    def errors(self):
        return validate_record_artifacts(self.record, self.root)

    def test_empty_plan_has_no_artifacts(self):
        self.assertEqual(self.errors(), [])

    def test_retained_bytes_match_manifest(self):
        self.retain()
        self.assertEqual(self.errors(), [])

    def test_editing_evidence_invalidates_its_manifest(self):
        path, _ = self.retain()
        path.write_bytes(b'A different claim.\n')
        self.assertTrue(any('differs from retained bytes' in e for e in self.errors()))

    def test_deleted_artifact_is_rejected(self):
        path, _ = self.retain()
        path.unlink()
        self.assertTrue(any('does not exist' in e for e in self.errors()))

    def test_local_digest_is_required(self):
        _, item = self.retain()
        item['sha256'] = None
        self.assertTrue(any('requires a SHA-256' in e for e in self.errors()))

    def test_all_artifact_fields_require_manifests(self):
        for field in ('input_artifacts', 'process_artifacts', 'candidate_answer_artifacts', 'evidence_artifacts'):
            with self.subTest(field=field):
                record = {'id': 'REV-TEST', field: ['evidence/missing.txt'], 'artifact_manifest': []}
                self.assertTrue(any('lacks a manifest' in e for e in validate_record_artifacts(record, self.root)))

    def test_duplicate_and_unused_manifest_entries_are_rejected(self):
        _, item = self.retain()
        self.record['artifact_manifest'].append(dict(item))
        self.assertTrue(any('duplicate artifact' in e for e in self.errors()))
        self.record['process_artifacts'] = []
        self.assertTrue(any('not referenced' in e for e in self.errors()))

    def test_same_file_can_support_multiple_artifact_fields(self):
        _, item = self.retain()
        self.record['candidate_answer_artifacts'] = [item['reference']]
        self.assertEqual(self.errors(), [])

    def test_paths_cannot_escape_or_use_temporary_directories(self):
        for reference in ('../outside.txt', '/absolute.txt', 'C:\\outside.txt', 'C:outside.txt',
                          '\\\\server\\share\\proof.txt', 'work/proof.txt', '.git/proof.txt',
                          'evidence/../work/proof.txt'):
            with self.subTest(reference=reference):
                self.record['process_artifacts'] = [reference]
                self.record['artifact_manifest'] = [{'reference': reference, 'version': 'v1',
                                                     'sha256': 'sha256:' + '0' * 64}]
                self.assertTrue(self.errors())

    def test_remote_version_is_declared_without_fetching(self):
        reference = 'https://example.invalid/archive/proof-v1.pdf'
        self.record['process_artifacts'] = [reference]
        self.record['artifact_manifest'] = [{'reference': reference, 'version': 'Archive version 1', 'sha256': None}]
        self.assertEqual(self.errors(), [])
        self.record['artifact_manifest'][0]['version'] = ' '
        self.assertTrue(any('retained version' in e for e in self.errors()))

    def test_incomplete_or_unsupported_remote_scheme_is_rejected(self):
        for reference in ('https:///proof.pdf', 'ftp://example.invalid/proof.pdf', 'file:///proof.pdf'):
            with self.subTest(reference=reference):
                self.record['process_artifacts'] = [reference]
                self.record['artifact_manifest'] = [{'reference': reference, 'version': 'v1', 'sha256': None}]
                self.assertTrue(self.errors())


if __name__ == '__main__':
    unittest.main()
