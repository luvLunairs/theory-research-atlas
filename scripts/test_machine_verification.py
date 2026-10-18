"""Exercise eligibility with synthetic records and temporary retained artifacts."""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from machine_verification import (
    APPROVAL_SCOPE, COMMON_CHECKS, METHOD_CHECKS, ROOT, specification_digest,
    validate_machine_records, verification_state,
)
from research_records import attempt_digest, statement_digest


def fixture_dataset(root, method='exact_counterexample'):
    """Create a synthetic checked run; never write project research records."""
    root = Path(root)
    artifact_dir = root / 'research'
    artifact_dir.mkdir(parents=True, exist_ok=True)
    paths = ['target.txt', 'checker.py', 'environment.txt', 'protocol.txt',
             'approval.txt', 'result.txt', 'certificate.txt', 'log.txt']
    for name in paths:
        (artifact_dir / name).write_text(f'Synthetic fixture: {name}.\n', encoding='utf-8')

    def manifest(refs):
        return [{'reference': ref, 'version': 'Synthetic fixture version 1',
                 'sha256': 'sha256:' + hashlib.sha256((root / ref).read_bytes()).hexdigest()}
                for ref in refs]

    problem = {'id': 'Q-TEST', 'statement': 'Synthetic target; not a research claim.'}
    spec_refs = [f'research/{name}' for name in paths[:5]]
    spec = {
        'id': 'VSPEC-TEST', 'problem_id': problem['id'], 'statement_digest': statement_digest(problem),
        'method': method, 'claim': 'Synthetic bounded claim.', 'scope': ['Synthetic fixture only.'],
        'target_artifacts': ['research/target.txt'],
        'checker': {'name': 'Fixture checker', 'version': '1', 'source_artifacts': ['research/checker.py']},
        'environment_artifacts': ['research/environment.txt'], 'protocol_artifacts': ['research/protocol.txt'],
        'trust': {'arithmetic': 'not_applicable' if method == 'lean_proof' else 'exact',
                  'allowed_axioms': ['propext', 'Classical.choice', 'Quot.sound'] if method == 'lean_proof' else [],
                  'allow_native_decide': False},
        'approval': {'status': 'approved', 'reviewer': 'Synthetic human reviewer',
                     'reviewer_role': 'human_maintainer', 'date': '2026-10-15',
                     'specification_digest': None, 'scope': sorted(APPROVAL_SCOPE),
                     'evidence_artifacts': ['research/approval.txt'], 'notes': 'Synthetic approval fixture.'},
        'evidence_artifacts': spec_refs, 'artifact_manifest': manifest(spec_refs),
        'revision_history': [{'date': '2026-10-15', 'change': 'Synthetic fixture.'}],
    }
    spec['approval']['specification_digest'] = specification_digest(spec)
    attempt_refs = ['research/result.txt', 'research/log.txt']
    attempt = {
        'id': 'ATT-TEST', 'problem_id': problem['id'], 'statement_version': 'Synthetic fixture version 1',
        'target': 'Synthetic bounded claim.', 'purpose': 'research', 'assumptions': ['Synthetic fixture.'],
        'success_criteria': ['Synthetic fixture.'], 'verification_plan': ['Synthetic fixture.'],
        'requirements': {'experiment': 'None.', 'data': 'Synthetic.', 'compute': 'Synthetic.'},
        'contributors': [{'name': 'Synthetic contributor', 'roles': ['Fixture']}],
        'model': {'provider': None, 'name': None, 'version': None, 'capabilities': []},
        'started_at': '2026-10-15T10:00:00Z', 'ended_at': '2026-10-15T11:00:00Z', 'status': 'completed',
        'environment': {'os': 'Synthetic', 'tools': [], 'versions': [], 'code_revision': None, 'seeds': []},
        'input_artifacts': [], 'process_artifacts': ['research/log.txt'],
        'candidate_answer_artifacts': ['research/result.txt'], 'artifact_manifest': manifest(attempt_refs),
        'planned_budget': {'kind': 'cap', 'money': {'amount': None, 'currency': None, 'basis': 'Synthetic.'},
                           'compute_units': None, 'human_hours': None, 'notes': 'Synthetic.'},
        'actual_use': {'kind': 'actual', 'money': {'amount': None, 'currency': None, 'basis': 'Synthetic.'},
                       'compute_units': None, 'human_hours': None, 'notes': 'Synthetic.'},
        'human_help': [], 'outcome_kind': 'candidate_answer', 'outcome': 'Synthetic.',
        'stopping_conditions': ['Synthetic.'], 'limitations': ['Synthetic.'], 'review_ids': [],
        'revision_history': [{'date': '2026-10-15', 'change': 'Synthetic fixture.'}],
    }
    run_refs = [f'research/{name}' for name in paths[5:]]
    run = {
        'id': 'VER-TEST', 'specification_id': spec['id'], 'specification_digest': specification_digest(spec),
        'problem_id': problem['id'], 'attempt_id': attempt['id'], 'attempt_digest': attempt_digest(attempt),
        'executed_at': '2026-10-16T10:00:00Z',
        'runner': {'name': 'Synthetic verifier', 'role': 'Fixture runner', 'provenance': 'project'},
        'command': ['fixture-checker', '--certificate', 'research/certificate.txt'], 'outcome': 'passed',
        'result_artifacts': ['research/result.txt'], 'certificate_artifacts': ['research/certificate.txt'],
        'log_artifacts': ['research/log.txt'],
        'checks': [{'name': name, 'result': 'passed', 'evidence_artifacts': ['research/log.txt'],
                    'notes': 'Synthetic fixture check.'} for name in sorted(COMMON_CHECKS | METHOD_CHECKS[method])],
        'axioms_used': ['propext'] if method == 'lean_proof' else [], 'native_decide_used': False,
        'limitations': ['Synthetic fixture; no scientific execution.'],
        'evidence_artifacts': run_refs, 'artifact_manifest': manifest(run_refs),
        'revision_history': [{'date': '2026-10-16', 'change': 'Synthetic fixture.'}],
    }
    return {'project': {'as_of': '2026-10-16'}, 'candidates': [problem], 'cards': [],
            'attempts': [attempt], 'verification_specs': [spec], 'verifications': [run]}


class MachineVerificationTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'work').mkdir(exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(prefix='machine-verification-', dir=ROOT / 'work')
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.data = fixture_dataset(self.root)

    @property
    def spec(self):
        return self.data['verification_specs'][0]

    @property
    def record(self):
        return self.data['verifications'][0]

    @property
    def attempt(self):
        return self.data['attempts'][0]

    def state(self):
        return verification_state(self.data, self.record, self.root)

    def rebind(self):
        self.spec['approval']['specification_digest'] = specification_digest(self.spec)
        self.record['specification_digest'] = specification_digest(self.spec)
        self.record['attempt_digest'] = attempt_digest(self.attempt)

    def test_all_four_methods_can_qualify(self):
        for method in METHOD_CHECKS:
            with self.subTest(method=method):
                self.data = fixture_dataset(self.root, method)
                self.assertEqual(validate_machine_records(self.data, self.root), [])
                self.assertEqual(self.state(), 'machine_checked')

    def test_pending_rejected_and_withdrawn_approval_block_badge(self):
        for status in ['pending', 'rejected', 'withdrawn']:
            self.spec['approval']['status'] = status
            self.assertEqual(self.state(), 'pending_approval')

    def test_pending_approval_may_be_unassigned(self):
        self.spec['approval'].update(status='pending', reviewer=None, reviewer_role=None,
                                     date=None, specification_digest=None, scope=[])
        self.assertEqual(validate_machine_records(self.data, self.root), [])
        self.assertEqual(self.state(), 'pending_approval')

    def test_approved_requires_named_human_scope_and_evidence(self):
        self.spec['approval']['scope'] = ['target_correspondence']
        self.assertEqual(self.state(), 'invalid')
        self.spec['approval']['scope'] = sorted(APPROVAL_SCOPE)
        self.spec['approval']['reviewer'] = None
        self.assertEqual(self.state(), 'invalid')

    def test_scientific_change_invalidates_approval_and_run(self):
        self.spec['scope'].append('Changed scope.')
        self.assertEqual(self.state(), 'stale')
        self.record['specification_digest'] = specification_digest(self.spec)
        self.assertEqual(self.state(), 'stale')

    def test_approval_evidence_is_not_circularly_hashed(self):
        old_digest = specification_digest(self.spec)
        self.spec['approval']['notes'] = 'Updated review note.'
        self.spec['revision_history'].append({'date': '2026-10-16', 'change': 'Review note.'})
        self.assertEqual(specification_digest(self.spec), old_digest)
        self.spec['checker']['version'] = '2'
        self.assertNotEqual(specification_digest(self.spec), old_digest)

    def test_target_artifact_cannot_be_removed_from_digest_by_approval_role(self):
        self.spec['approval']['evidence_artifacts'].append('research/target.txt')
        prior = specification_digest(self.spec)
        self.spec['artifact_manifest'][0]['version'] = 'Changed target.'
        self.assertNotEqual(specification_digest(self.spec), prior)

    def test_problem_and_attempt_drift_are_stale(self):
        self.data['candidates'][0]['statement'] = 'Different problem.'
        self.assertEqual(self.state(), 'stale')
        self.spec['statement_digest'] = statement_digest(self.data['candidates'][0])
        self.rebind()
        self.attempt['target'] = 'Changed result target.'
        self.assertEqual(self.state(), 'stale')

    def test_contributor_only_logs_do_not_qualify(self):
        self.record['runner']['provenance'] = 'contributor'
        self.assertEqual(self.state(), 'reported_pass')

    def test_no_executed_attempt_cannot_qualify(self):
        self.attempt.update(status='planned', started_at=None, ended_at=None)
        self.rebind()
        self.assertEqual(self.state(), 'reported_pass')

    def test_future_execution_and_pre_attempt_execution_are_invalid(self):
        self.record['executed_at'] = '2026-10-17T10:00:00Z'
        self.assertEqual(self.state(), 'invalid')
        self.record['executed_at'] = '2026-10-15T09:00:00Z'
        self.assertEqual(self.state(), 'invalid')

    def test_run_before_specification_approval_does_not_qualify(self):
        self.record['executed_at'] = '2026-10-15T12:00:00Z'
        self.spec['approval']['date'] = '2026-10-16'
        self.assertEqual(self.state(), 'reported_pass')

    def test_missing_method_specific_check_blocks_badge(self):
        self.record['checks'] = [item for item in self.record['checks'] if item['name'] != 'negated_conclusion']
        self.assertEqual(self.state(), 'reported_pass')

    def test_failed_or_duplicated_checks_cannot_support_pass(self):
        self.record['checks'][0]['result'] = 'failed'
        self.assertEqual(self.state(), 'invalid')
        self.record['checks'][0]['result'] = 'passed'
        self.record['checks'].append(copy.deepcopy(self.record['checks'][0]))
        self.assertEqual(self.state(), 'invalid')

    def test_lean_holes_custom_axioms_and_native_computation_are_not_eligible(self):
        self.data = fixture_dataset(self.root, 'lean_proof')
        for axiom in ['sorryAx', 'myUnprovedLemma']:
            self.spec['trust']['allowed_axioms'].append(axiom)
            self.record['axioms_used'].append(axiom)
            self.rebind()
            self.assertEqual(self.state(), 'reported_pass')
            self.spec['trust']['allowed_axioms'].remove(axiom)
            self.record['axioms_used'].remove(axiom)
        self.record['native_decide_used'] = True
        self.rebind()
        self.assertEqual(self.state(), 'reported_pass')
        self.record['native_decide_used'] = False
        self.spec['trust']['allow_native_decide'] = True
        self.rebind()
        self.assertEqual(self.state(), 'reported_pass')

    def test_ordinary_floating_point_is_not_exact_evidence(self):
        self.spec['trust']['arithmetic'] = 'ordinary_floating_point'
        self.rebind()
        self.assertEqual(self.state(), 'reported_pass')

    def test_modified_or_missing_retained_artifact_is_invalid(self):
        (self.root / 'research/log.txt').write_text('Changed bytes.', encoding='utf-8')
        self.assertEqual(self.state(), 'invalid')
        (self.root / 'research/log.txt').unlink()
        self.assertEqual(self.state(), 'invalid')

    def test_remote_evidence_declaration_does_not_qualify(self):
        old, new = 'research/certificate.txt', 'https://example.org/certificate.txt'
        self.record['certificate_artifacts'] = [new]
        self.record['evidence_artifacts'] = [new if ref == old else ref for ref in self.record['evidence_artifacts']]
        item = next(item for item in self.record['artifact_manifest'] if item['reference'] == old)
        item['reference'] = new
        self.assertEqual(self.state(), 'reported_pass')
        item['sha256'] = None
        self.assertEqual(self.state(), 'reported_pass')

    def test_local_evidence_requires_exact_hashes(self):
        self.record['artifact_manifest'][0]['sha256'] = None
        self.assertEqual(self.state(), 'invalid')

    def test_manifest_role_and_attempt_correspondence_are_enforced(self):
        self.record['result_artifacts'] = ['research/certificate.txt']
        self.assertEqual(self.state(), 'invalid')
        self.record['result_artifacts'] = ['research/result.txt']
        self.record['log_artifacts'] = ['research/unlisted.txt']
        self.assertEqual(self.state(), 'invalid')

    def test_missing_certificate_can_record_error_but_not_success(self):
        self.record['certificate_artifacts'] = []
        self.assertEqual(self.state(), 'reported_pass')
        self.record['outcome'] = 'error'
        self.assertEqual(self.state(), 'error')

    def test_conflicting_reruns_cannot_be_overridden_by_newer_pass(self):
        earlier = copy.deepcopy(self.record)
        earlier.update(id='VER-EARLIER', outcome='failed', executed_at='2026-10-16T09:00:00Z')
        earlier['checks'][0]['result'] = 'failed'
        self.data['verifications'].append(earlier)
        self.assertEqual(self.state(), 'conflicting')
        self.assertEqual(verification_state(self.data, earlier, self.root), 'conflicting')

    def test_other_certificate_does_not_create_same_certificate_conflict(self):
        other = copy.deepcopy(self.record)
        other.update(id='VER-OTHER', outcome='failed')
        other['certificate_artifacts'] = ['research/result.txt']
        self.data['verifications'].append(other)
        self.assertEqual(self.state(), 'machine_checked')

    def test_renaming_the_same_certificate_does_not_hide_conflict(self):
        other = copy.deepcopy(self.record)
        other.update(id='VER-RENAMED', outcome='failed')
        old, new = 'research/certificate.txt', 'research/renamed-certificate.txt'
        (self.root / new).write_bytes((self.root / old).read_bytes())
        other['certificate_artifacts'] = [new]
        other['evidence_artifacts'] = [new if ref == old else ref for ref in other['evidence_artifacts']]
        next(item for item in other['artifact_manifest'] if item['reference'] == old)['reference'] = new
        self.data['verifications'].append(other)
        self.assertEqual(self.state(), 'conflicting')

    def test_inconclusive_and_error_outcomes_are_preserved(self):
        for outcome in ['failed', 'inconclusive', 'error']:
            self.record['outcome'] = outcome
            self.assertEqual(self.state(), outcome)

    def test_duplicate_ids_and_unregistered_records_fail_closed(self):
        self.data['verifications'].append(copy.deepcopy(self.record))
        self.assertEqual(self.state(), 'invalid')
        self.data['verifications'].pop()
        detached = copy.deepcopy(self.record)
        detached['id'] = 'VER-UNREGISTERED'
        self.assertEqual(verification_state(self.data, detached, self.root), 'invalid')

    def test_unknown_fields_and_malformed_attempts_fail_closed(self):
        self.record['accepted'] = True
        self.assertEqual(self.state(), 'invalid')
        del self.record['accepted']
        del self.attempt['contributors']
        self.rebind()
        self.assertEqual(self.state(), 'invalid')

    def test_unfinished_canonical_records_are_rejected(self):
        self.spec['checker']['version'] = 'TODO: choose a version.'
        self.rebind()
        self.assertEqual(self.state(), 'invalid')

    def test_unfinished_linked_attempt_cannot_receive_badge(self):
        self.attempt['limitations'].append('TODO: inspect evidence.')
        self.rebind()
        self.assertEqual(self.state(), 'invalid')


if __name__ == '__main__':
    unittest.main()
