"""Derive bounded machine-check labels from retained, human-curated evidence.

This module never runs a checker or authenticates a person's identity. Its output
depends on the accuracy of the admitted execution and approval records.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

from artifact_integrity import validate_record_artifacts
from research_records import attempt_digest, statement_digest
from schema_validation import read, schema_check


ROOT = Path(__file__).resolve().parents[1]
STANDARD_LEAN_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
COMMON_CHECKS = {'target_match', 'environment_match', 'independent_rerun',
                 'certificate_check', 'protocol_match'}
METHOD_CHECKS = {
    'exact_counterexample': {'domain_membership', 'negated_conclusion'},
    'lean_proof': {'kernel_check', 'axiom_audit'},
    'finite_construction': {'constraints_check'},
    'finite_exhaustion': {'enumeration_complete'},
}
APPROVAL_SCOPE = {'target_correspondence', 'checker_protocol', 'trust_basis'}


def _digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True,
                         separators=(',', ':'), allow_nan=False).encode('utf-8')
    return 'sha256:' + hashlib.sha256(encoded).hexdigest()


def _spec_roles(spec):
    return (spec['target_artifacts'] + spec['checker']['source_artifacts']
            + spec['environment_artifacts'] + spec['protocol_artifacts'])


def specification_digest(spec):
    """Bind scientific content without circularly hashing its approval evidence.

    Approval-only references and their manifest entries are excluded. An artifact
    used for a scientific role is always included, even if also cited in approval.
    """
    approval_only = set(spec['approval']['evidence_artifacts']) - set(_spec_roles(spec))
    value = {key: value for key, value in spec.items()
             if key not in {'approval', 'revision_history', 'evidence_artifacts', 'artifact_manifest'}}
    value['evidence_artifacts'] = [ref for ref in spec['evidence_artifacts'] if ref not in approval_only]
    value['artifact_manifest'] = [item for item in spec['artifact_manifest']
                                  if item['reference'] not in approval_only]
    return _digest(value)


def _shape_errors(record, schema_name):
    """Use the same fail-closed schema evaluator as collection validation."""
    errors = []
    schema_check(record, read(ROOT / 'schemas' / f'{schema_name}.schema.json'),
                 record.get('id', schema_name) if isinstance(record, dict) else schema_name,
                 errors, ROOT / 'schemas')
    return errors


def _timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def _all_roles(record, spec=False):
    if spec:
        return _spec_roles(record) + record['approval']['evidence_artifacts']
    return (record['result_artifacts'] + record['certificate_artifacts'] + record['log_artifacts']
            + [ref for check in record['checks'] for ref in check['evidence_artifacts']])


def _manifest(record):
    return {item['reference']: item for item in record['artifact_manifest']}


def _local_evidence(record):
    """Remote hash declarations alone do not establish retained local bytes."""
    return all(not urlsplit(item['reference']).scheme and item['sha256']
               for item in record['artifact_manifest'])


def _unfinished(value):
    if isinstance(value, str):
        return value.startswith('TODO:')
    if isinstance(value, dict):
        return any(_unfinished(item) for item in value.values())
    if isinstance(value, list):
        return any(_unfinished(item) for item in value)
    return False


def validate_machine_records(dataset, root=ROOT):
    """Validate declarations and evidence integrity, without scientific execution.

    Stale records and non-passing outcomes remain valid historical records. They do
    not confer a current badge. Missing references or contradictory metadata fail
    validation rather than being silently repaired.
    """
    errors = []
    specifications = dataset.get('verification_specs', [])
    records = dataset.get('verifications', [])
    for collection, schema in [(specifications, 'verification-spec'), (records, 'verification')]:
        if not isinstance(collection, list):
            return ['machine verification: expected record lists']
        for record in collection:
            errors.extend(_shape_errors(record, schema))
    if errors:
        return errors
    candidates = {item['id']: item for item in dataset['candidates']}
    attempts = {item['id']: item for item in dataset['attempts']}
    specs = {item['id']: item for item in specifications}
    cutoff = dataset['project']['as_of']
    for collection, name in [(specifications, 'verification specifications'), (records, 'verification runs')]:
        if len({record['id'] for record in collection}) != len(collection):
            errors.append(f'{name}: duplicate stable ID')
        for record in collection:
            rid = record['id']
            if _unfinished(record):
                errors.append(f'{rid}: unfinished drafts belong in work/, not the verification collection')
            if record['problem_id'] not in candidates:
                errors.append(f'{rid}: unknown problem reference')
            if any(item['date'] > cutoff for item in record['revision_history']):
                errors.append(f'{rid}: future record revision')
            errors.extend(validate_record_artifacts(record, root))
            roles = _all_roles(record, collection is specifications)
            if set(roles) - set(record['evidence_artifacts']):
                errors.append(f'{rid}: every artifact role must appear in evidence_artifacts')
    for spec in specifications:
        approval = spec['approval']
        if approval['date'] and approval['date'] > cutoff:
            errors.append(f'{spec["id"]}: future specification approval')
        if approval['status'] != 'pending':
            if not all(approval[key] for key in ['reviewer', 'reviewer_role', 'date',
                                                 'specification_digest', 'evidence_artifacts']):
                errors.append(f'{spec["id"]}: recorded approval decision requires named human and retained evidence')
        if approval['status'] == 'approved' and set(approval['scope']) != APPROVAL_SCOPE:
            errors.append(f'{spec["id"]}: approval must cover target correspondence, checker protocol and trust basis')
    for record in records:
        rid = record['id']
        spec = specs.get(record['specification_id'])
        attempt = attempts.get(record['attempt_id'])
        if not spec or spec['problem_id'] != record['problem_id']:
            errors.append(f'{rid}: missing or inconsistent specification reference')
        if not attempt or attempt['problem_id'] != record['problem_id']:
            errors.append(f'{rid}: missing or inconsistent attempt reference')
        moment = _timestamp(record['executed_at'])
        if moment.astimezone(dt.timezone.utc).date().isoformat() > cutoff:
            errors.append(f'{rid}: future verification execution')
        if attempt and attempt.get('started_at') and moment < _timestamp(attempt['started_at']):
            errors.append(f'{rid}: verification predates the attempt')
        if attempt and record['attempt_digest'] == attempt_digest(attempt):
            manifest = _manifest(attempt)
            result_manifest = _manifest(record)
            for ref in record['result_artifacts']:
                if (ref not in attempt['candidate_answer_artifacts'] or ref not in manifest
                        or ref not in result_manifest or manifest[ref] != result_manifest[ref]):
                    errors.append(f'{rid}: result artifact must match the linked attempt manifest')
        names = [check['name'] for check in record['checks']]
        if len(set(names)) != len(names):
            errors.append(f'{rid}: duplicate named verification check')
        if record['outcome'] == 'passed' and any(check['result'] != 'passed' for check in record['checks']):
            errors.append(f'{rid}: passed outcome contradicts a non-passing check')
    return errors


def _trust_eligible(spec, record):
    trust = spec['trust']
    if spec['method'] == 'lean_proof':
        return (not trust['allow_native_decide'] and not record['native_decide_used']
                and set(trust['allowed_axioms']) <= STANDARD_LEAN_AXIOMS
                and set(record['axioms_used']) <= set(trust['allowed_axioms']))
    return (trust['arithmetic'] in {'exact', 'certified_interval'}
            and not trust['allowed_axioms'] and not record['axioms_used']
            and not trust['allow_native_decide'] and not record['native_decide_used'])


def _conflict_key(record):
    manifest = _manifest(record)

    def identities(references):
        return tuple(sorted({manifest[ref]['sha256'] or f'unverified:{ref}:{manifest[ref]["version"]}'
                             for ref in references}))

    results = identities(record['result_artifacts'])
    certificates = identities(record['certificate_artifacts'])
    return (record['specification_id'], record['specification_digest'],
            record['attempt_id'], record['attempt_digest'], results, certificates)


def verification_state(dataset, record, root=ROOT):
    """Derive a current evidence label; never execute or accept a submission.

    All records must be structurally sound. A passing declaration becomes
    machine_checked only for an approved, current target with retained evidence of
    an independent run and the prescribed successful checks. Conflicting reruns of
    the same certificate remain visible; timestamps do not select a winner.
    """
    try:
        if validate_machine_records(dataset, root):
            return 'invalid'
        matches = [item for item in dataset.get('verifications', []) if item['id'] == record['id']]
        if len(matches) != 1 or matches[0] != record:
            return 'invalid'
        spec = next(item for item in dataset['verification_specs'] if item['id'] == record['specification_id'])
        attempts = [item for item in dataset['attempts'] if item['id'] == record['attempt_id']]
        if len(attempts) != 1:
            return 'invalid'
        attempt = attempts[0]
        target = next((item for item in dataset.get('cards', []) if item['id'] == record['problem_id']), None)
        target = target or next(item for item in dataset['candidates'] if item['id'] == record['problem_id'])
        digest = specification_digest(spec)
        approval = spec['approval']
        if (spec['statement_digest'] != statement_digest(target)
                or record['specification_digest'] != digest
                or record['attempt_digest'] != attempt_digest(attempt)
                or (approval['status'] == 'approved' and approval['specification_digest'] != digest)):
            return 'stale'
        peers = [item for item in dataset['verifications'] if _conflict_key(item) == _conflict_key(record)]
        outcomes = {item['outcome'] for item in peers}
        if 'passed' in outcomes and len(outcomes) > 1:
            return 'conflicting'
        if record['outcome'] != 'passed':
            return record['outcome']
        if approval['status'] != 'approved':
            return 'pending_approval'
        if _shape_errors(attempt, 'attempt') or _unfinished(attempt):
            return 'invalid'
        if (not attempt.get('started_at') or attempt.get('status') not in
                {'running', 'completed', 'stopped', 'failed'}):
            return 'reported_pass'
        terminal = attempt['status'] in {'completed', 'stopped', 'failed'}
        if (terminal and not attempt['ended_at']) or not attempt['process_artifacts']:
            return 'reported_pass'
        if attempt['ended_at'] and _timestamp(attempt['ended_at']) < _timestamp(attempt['started_at']):
            return 'invalid'
        if _timestamp(record['executed_at']).astimezone(dt.timezone.utc).date().isoformat() < approval['date']:
            return 'reported_pass'
        if record['runner']['provenance'] not in {'project', 'independent'}:
            return 'reported_pass'
        required = COMMON_CHECKS | METHOD_CHECKS[spec['method']]
        completed = {check['name'] for check in record['checks'] if check['result'] == 'passed'}
        if not required <= completed or not _trust_eligible(spec, record) or not record['certificate_artifacts']:
            return 'reported_pass'
        if not _local_evidence(spec) or not _local_evidence(record):
            return 'reported_pass'
        if validate_record_artifacts(attempt, root):
            return 'invalid'
        return 'machine_checked'
    except (KeyError, TypeError, ValueError, OSError, StopIteration):
        return 'invalid'
