"""Prepare a research or verification draft without executing a research task."""
import argparse
import datetime as dt
import json
import re
import sys

from research_records import statement_digest, attempt_digest
from machine_verification import specification_digest
from validate import ROOT, load_dataset


def draft_record(dataset, kind, problem_id, record_id, author, *, attempt_id=None, review_type=None,
                 specification_id=None, method=None, date=None):
    prefixes = {'attempt': 'ATT', 'review': 'REV', 'verification-spec': 'VSPEC', 'verification': 'VER'}
    if kind not in prefixes:
        raise ValueError('Choose an attempt, review, verification-spec or verification draft.')
    date = date or dt.date.today().isoformat()
    candidate = next((c for c in dataset['candidates'] if c['id'] == problem_id), None)
    if not candidate:
        raise ValueError('Unknown problem ID: ' + problem_id)
    card = next((c for c in dataset['cards'] if c['id'] == problem_id), candidate)
    prefix = prefixes[kind]
    if not re.fullmatch(prefix + r'-[A-Za-z0-9][A-Za-z0-9_-]*', record_id):
        raise ValueError('Use a safe, stable ' + prefix + '- ID containing letters, digits, underscores or hyphens.')
    if any(r['id'] == record_id for k in ('attempts', 'reviews', 'verification_specs', 'verifications') for r in dataset.get(k, [])):
        raise ValueError('Record ID already exists: ' + record_id)
    if not author.strip():
        raise ValueError('Provide an agreed contributor name or handle.')
    if review_type and kind != 'review':
        raise ValueError('--review-type applies only to reviews.')
    if specification_id and kind != 'verification':
        raise ValueError('--specification applies only to verification runs.')
    if method and kind != 'verification-spec':
        raise ValueError('--method applies only to verification specifications.')
    if attempt_id and kind not in {'review', 'verification'}:
        raise ValueError('--attempt applies only to reviews and verification runs.')
    if kind == 'verification-spec':
        if method not in {'exact_counterexample', 'lean_proof', 'finite_construction', 'finite_exhaustion'}:
            raise ValueError('Choose an explicit --method for the verification specification.')
        return {
            'id': record_id, 'problem_id': problem_id, 'statement_digest': statement_digest(card),
            'method': method, 'claim': 'TODO: state the precise claim this protocol can establish.',
            'scope': ['TODO: specify definitions, assumptions, quantifiers, limits and correspondence to the problem.'],
            'target_artifacts': [],
            'checker': {'name': 'TODO: identify the checker.', 'version': 'TODO: pin the checker version.', 'source_artifacts': []},
            'environment_artifacts': [], 'protocol_artifacts': [],
            'trust': {'arithmetic': 'not_applicable' if method == 'lean_proof' else 'exact',
                      'allowed_axioms': [], 'allow_native_decide': False},
            'approval': {'status': 'pending', 'reviewer': None, 'reviewer_role': None, 'date': None,
                         'specification_digest': None, 'scope': [], 'evidence_artifacts': [],
                         'notes': 'No human approval recorded.'},
            'evidence_artifacts': [], 'artifact_manifest': [],
            'revision_history': [{'date': date, 'change': f'Verification specification proposed by {author}.'}],
        }
    if kind == 'verification':
        attempt = next((a for a in dataset['attempts'] if a['id'] == attempt_id), None)
        specification = next((s for s in dataset.get('verification_specs', []) if s['id'] == specification_id), None)
        if not attempt or attempt['problem_id'] != problem_id:
            raise ValueError('A verification draft requires an existing attempt for this problem.')
        if not specification or specification['problem_id'] != problem_id:
            raise ValueError('A verification draft requires an existing specification for this problem.')
        return {
            'id': record_id, 'problem_id': problem_id, 'specification_id': specification_id,
            'specification_digest': specification_digest(specification), 'attempt_id': attempt_id,
            'attempt_digest': attempt_digest(attempt), 'executed_at': None,
            'runner': {'name': author, 'role': 'TODO: identify who actually performed the check.', 'provenance': 'contributor'},
            'command': [], 'outcome': None, 'result_artifacts': [], 'certificate_artifacts': [],
            'log_artifacts': [], 'checks': [], 'axioms_used': None, 'native_decide_used': None,
            'evidence_artifacts': [], 'artifact_manifest': [],
            'limitations': ['TODO: record the actual execution, evidence, axiom audit and checking limits.'],
            'revision_history': [{'date': date, 'change': 'Prepared a verification draft; no check recorded.'}],
        }
    if kind == 'attempt':
        return {
            'id': record_id, 'problem_id': problem_id,
            'statement_version': 'TODO: identify a retained statement snapshot or repository revision.',
            'target': candidate['statement'],
            'assumptions': ['TODO: specify the assumptions of this particular attempt.'],
            'success_criteria': ['TODO: define what this attempt would establish.'],
            'verification_plan': ['TODO: describe independent checks of that claim.'],
            'requirements': {k: 'TODO: specify the requirement or explain why none is needed.' for k in ['experiment', 'data', 'compute']},
            'purpose': 'research', 'contributors': [{'name': author, 'roles': ['Research planning']}],
            'model': {'provider': None, 'name': None, 'version': None, 'capabilities': []},
            'started_at': None, 'ended_at': None, 'status': 'planned',
            'environment': {'os': None, 'tools': [], 'versions': [], 'code_revision': None, 'seeds': []},
            'input_artifacts': [], 'process_artifacts': [], 'candidate_answer_artifacts': [],
            'artifact_manifest': [],
            'planned_budget': {'kind': 'cap', 'money': {'amount': None, 'currency': None, 'basis': 'No budget agreed.'},
                               'compute_units': None, 'human_hours': None, 'notes': 'TODO: record agreed limits and their basis.'},
            'actual_use': {'kind': 'actual', 'money': {'amount': None, 'currency': None, 'basis': 'No execution.'},
                           'compute_units': None, 'human_hours': None, 'notes': 'No execution.'},
            'human_help': [], 'outcome_kind': 'not_yet_reported', 'outcome': 'No execution or result recorded.',
            'stopping_conditions': ['TODO: record explicit stopping conditions.'],
            'limitations': ['TODO: identify uncertainty and known limitations.'], 'review_ids': [],
            'revision_history': [{'date': date, 'change': 'Prepared a research plan.'}],
        }
    attempt = next((a for a in dataset['attempts'] if a['id'] == attempt_id), None) if attempt_id else None
    if attempt_id and (not attempt or attempt['problem_id'] != problem_id):
        raise ValueError('The attempt must exist and belong to this problem.')
    review_type = review_type or ('research_record' if attempt_id else 'problem_entry')
    if review_type not in {'problem_entry', 'planned_method', 'research_record'}:
        raise ValueError('Unknown review type.')
    if (review_type == 'problem_entry') != (attempt_id is None):
        raise ValueError('A problem-entry review has no attempt; other reviews require one.')
    return {
        'id': record_id, 'problem_id': problem_id, 'attempt_id': attempt_id,
        'review_type': review_type, 'statement_digest': statement_digest(card),
        'attempt_digest': attempt_digest(attempt) if attempt else None,
        'reviewed_version': 'TODO: identify the exact statement and artifact versions examined.',
        'reviewer': author, 'reviewer_role': 'TODO: describe the reviewer role.', 'date': date,
        'scope': ['TODO: specify what will be checked.'],
        'not_reviewed': ['TODO: specify exclusions.'], 'verdict': 'pending',
        'comments': 'TODO: record findings and supporting reasons.', 'evidence_artifacts': [],
        'artifact_manifest': [], 'supersedes': [],
        'conflicts_of_interest': 'TODO: disclose relevant interests or state none.',
        'revision_history': [{'date': date, 'change': 'Prepared a scoped review.'}],
    }


def save_draft(record, root=ROOT):
    if not re.fullmatch(r'(ATT|REV|VSPEC|VER)-[A-Za-z0-9][A-Za-z0-9_-]*', record['id']):
        raise ValueError('Unsafe record ID.')
    directory = root / 'work' / 'drafts'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / (record['id'] + '.json')
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['attempt', 'review', 'verification-spec', 'verification'])
    parser.add_argument('problem_id')
    parser.add_argument('--id', required=True, dest='record_id')
    parser.add_argument('--author', required=True, help='Contributor or reviewer name/handle with agreed attribution')
    parser.add_argument('--attempt', dest='attempt_id')
    parser.add_argument('--review-type', choices=['problem_entry', 'planned_method', 'research_record'])
    parser.add_argument('--specification', dest='specification_id', help='Existing VSPEC- ID for a verification run draft')
    parser.add_argument('--method', choices=['exact_counterexample', 'lean_proof', 'finite_construction', 'finite_exhaustion'])
    args = parser.parse_args()
    try:
        record = draft_record(load_dataset(), **vars(args))
        path = save_draft(record)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(f'Draft saved: {path}')
    print('Complete missing fields and review the target, evidence and rights before submitting. No research, certificate check or approval was performed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
