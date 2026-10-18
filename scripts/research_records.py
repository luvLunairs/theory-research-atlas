"""Validate recorded attempts, scoped reviews and evidence links."""
import datetime as dt
import hashlib
import json
from pathlib import Path

from artifact_integrity import validate_record_artifacts


ROOT = Path(__file__).resolve().parents[1]
SCREENING_TARGET_FIELDS = (
    'problem_id', 'statement_version', 'target', 'assumptions', 'success_criteria',
    'outcome_kind', 'outcome', 'model', 'environment', 'candidate_answer_artifacts',
)
SCREENING_LABELS = {
    'not_recorded': 'Preliminary screening not recorded',
    'stale': 'Preliminary screening concerns an earlier or different version',
    'invalid': 'Preliminary-screening evidence needs attention',
    'changes_requested': 'Preliminary screening: changes requested',
    'limited': 'Limited preliminary screening recorded',
    'recommended_ai': 'Recommended-model contributor checks recorded',
    'recommended_ai_human': 'Recommended-model contributor checks + reported human preliminary pass',
    'human_preliminary': 'Human preliminary pass reported',
}


def screening_target_digest(attempt):
    """Bind screening to its claim and AI provenance, without hashing itself."""
    value = {key: attempt[key] for key in SCREENING_TARGET_FIELDS}
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return 'sha256:' + hashlib.sha256(encoded).hexdigest()


def _screening_errors(attempt, cutoff=None):
    """Check declarations; old target/artifact bindings are valid retained history."""
    screening = attempt.get('preliminary_screening')
    if screening is None:
        return []
    errors = []
    prefix = f'{attempt["id"]}: preliminary screening'
    manifest = {item['reference']: item for item in attempt['artifact_manifest']}
    if cutoff and screening['date'] > cutoff:
        errors.append(f'{prefix} has a future date')
    if attempt['started_at'] and screening['date'] < dt.datetime.fromisoformat(
            attempt['started_at'].replace('Z', '+00:00')).astimezone(dt.timezone.utc).date().isoformat():
        errors.append(f'{prefix} predates the attempt')
    if attempt['status'] == 'planned' or not attempt['candidate_answer_artifacts']:
        errors.append(f'{prefix} requires an executed attempt and result artifacts')
    refs = [item['reference'] for item in screening['result_artifacts']]
    if len(refs) != len(set(refs)):
        errors.append(f'{prefix} repeats a bound result reference')
    for ref in screening['evidence_artifacts']:
        if ref not in attempt['process_artifacts'] or ref not in manifest:
            errors.append(f'{prefix} evidence must be a manifested process artifact: {ref}')
        elif manifest[ref]['sha256'] is None:
            errors.append(f'{prefix} evidence requires a SHA-256 digest: {ref}')
    if screening['ai_basis'] == 'no_ai' and screening['ai_check_status'] == 'completed':
        errors.append(f'{prefix} cannot report AI checks with no AI basis')
    if screening['ai_basis'] == 'recommended_only' and not attempt['model']['name']:
        errors.append(f'{prefix} recommended-AI basis requires recorded model identity')
    return errors


def preliminary_screening_state(attempt, root=ROOT):
    """Describe recorded screening, never scientific correctness or approval.

    Callers validate record schemas first. Local retained bytes are checked here
    as well so direct rendering cannot inherit a positive label from changed files.
    Remote hashes remain declarations, as in ordinary artifact validation.
    """
    screening = attempt.get('preliminary_screening')
    if screening is None:
        return 'not_recorded'
    if _screening_errors(attempt):
        return 'invalid'
    manifest = {item['reference']: item for item in attempt['artifact_manifest']}
    bound = {item['reference']: item for item in screening['result_artifacts']}
    if (screening['target_digest'] != screening_target_digest(attempt)
            or not set(attempt['candidate_answer_artifacts']).issubset(bound)
            or not set(screening['evidence_artifacts']).issubset(bound)
            or any(manifest.get(ref) != item for ref, item in bound.items())):
        return 'stale'
    references = set(bound) | set(screening['evidence_artifacts'])
    retained = {'id': attempt['id'], 'process_artifacts': sorted(references),
                'artifact_manifest': [manifest[ref] for ref in sorted(references)]}
    if validate_record_artifacts(retained, root):
        return 'invalid'
    if screening['human_preliminary_status'] == 'changes_requested':
        return 'changes_requested'
    recommended = (screening['ai_basis'] == 'recommended_only'
                   and screening['ai_check_status'] == 'completed')
    if recommended:
        return ('recommended_ai_human' if screening['human_preliminary_status'] == 'passed'
                else 'recommended_ai')
    if screening['human_preliminary_status'] == 'passed':
        return 'human_preliminary'
    return 'limited' if screening['ai_check_status'] == 'completed' else 'not_recorded'


def preliminary_screening_label(attempt, root=ROOT):
    return SCREENING_LABELS[preliminary_screening_state(attempt, root)]


def statement_digest(card):
    """Identify the target and hypotheses, independently of display formatting."""
    fields = ['statement', 'assumptions', 'scope', 'target', 'success_criteria']
    value = {key: card[key] for key in fields if key in card}
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return 'sha256:' + hashlib.sha256(encoded).hexdigest()


def attempt_digest(attempt):
    """Bind a review to observable attempt content without circular review links."""
    value = {key: value for key, value in attempt.items() if key not in {'review_ids', 'revision_history'}}
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return 'sha256:' + hashlib.sha256(encoded).hexdigest()


def records_for_problem(dataset, problem_id):
    return ([a for a in dataset['attempts'] if a['problem_id'] == problem_id],
            [r for r in dataset['reviews'] if r['problem_id'] == problem_id])


def unsuperseded_reviews(dataset):
    replaced = {rid for r in dataset['reviews'] if r['verdict'] != 'pending' for rid in r['supersedes']}
    return [r for r in dataset['reviews'] if r['id'] not in replaced]


def current_attempt_reviews(dataset, attempt):
    """Exclude reviews of plans and superseded attempt versions from result views."""
    return [r for r in unsuperseded_reviews(dataset) if r['attempt_id'] == attempt['id']
               and r['review_type'] == 'research_record' and r['verdict'] != 'pending'
               and r['attempt_digest'] == attempt_digest(attempt)]


def validate_research_records(dataset):
    errors = []
    attempts, reviews = {}, {}
    cutoff = dataset['project']['as_of']
    sources = {s['id']: s for s in dataset['sources']}
    candidates = {c['id']: c for c in dataset['candidates']}

    def timestamp(value):
        return dt.datetime.fromisoformat(value.replace('Z', '+00:00')) if value else None

    def unfinished(value):
        if isinstance(value, str):
            return value.startswith('TODO:')
        if isinstance(value, dict):
            return any(unfinished(v) for v in value.values())
        if isinstance(value, list):
            return any(unfinished(v) for v in value)
        return False

    for field, target in [('attempts', attempts), ('reviews', reviews)]:
        for record in dataset[field]:
            rid = record['id']
            if rid in target:
                errors.append(f'{rid}: duplicate research record ID')
            target[rid] = record
            if unfinished(record):
                errors.append(f'{rid}: unfinished draft fields belong in work/, not the research collection')
            if record['problem_id'] not in candidates:
                errors.append(f'{rid}: unknown problem reference')
            if any(rev['date'] > cutoff for rev in record['revision_history']):
                errors.append(f'{rid}: future record revision')
    if attempts.keys() & reviews.keys():
        errors.append('attempt and review IDs must be distinct')

    for aid, attempt in attempts.items():
        errors.extend(_screening_errors(attempt, cutoff))
        start, end = timestamp(attempt['started_at']), timestamp(attempt['ended_at'])
        status = attempt['status']
        terminal = status in {'completed', 'stopped', 'failed'}
        if status == 'planned' and (start or end):
            errors.append(f'{aid}: planned attempt has execution timestamps')
        if status != 'planned' and not start:
            errors.append(f'{aid}: executed attempt requires a start time')
        if terminal and not end:
            errors.append(f'{aid}: terminal attempt requires an end time')
        if status == 'running' and end:
            errors.append(f'{aid}: running attempt has an end time')
        if start and end and end < start:
            errors.append(f'{aid}: end precedes start')
        for moment in (start, end):
            if moment and moment.astimezone(dt.timezone.utc).date().isoformat() > cutoff:
                errors.append(f'{aid}: future execution timestamp')
        actual = attempt['actual_use']
        if status == 'planned' and any(actual[key] is not None for key in ['compute_units', 'human_hours']):
            errors.append(f'{aid}: planned attempt cannot report measured use')
        if status == 'planned' and actual['money']['amount'] is not None:
            errors.append(f'{aid}: planned attempt cannot report measured use')
        for field in ['planned_budget', 'actual_use']:
            money = attempt[field]['money']
            if money['amount'] is not None and not money['currency']:
                errors.append(f'{aid}: {field} amount needs a currency')
        if attempt['purpose'] == 'model_evaluation' and not attempt['model']['name']:
            errors.append(f'{aid}: model evaluation requires a model identifier')
        if status == 'planned' and attempt['outcome_kind'] != 'not_yet_reported':
            errors.append(f'{aid}: planned attempt cannot report a research outcome')
        if terminal and attempt['outcome_kind'] == 'not_yet_reported':
            errors.append(f'{aid}: terminal attempt needs an outcome classification')
        if terminal and not attempt['process_artifacts']:
            errors.append(f'{aid}: terminal attempt requires an observable research record')
        if attempt['outcome_kind'] in {'reproduction', 'partial_result', 'candidate_answer', 'correction', 'retraction'} and not attempt['candidate_answer_artifacts']:
            errors.append(f'{aid}: reported result requires an artifact')
        for rid in attempt['review_ids']:
            if rid not in reviews or reviews[rid]['attempt_id'] != aid:
                errors.append(f'{aid}: missing or inconsistent review reference {rid}')

    for rid, review in reviews.items():
        if review['date'] > cutoff:
            errors.append(f'{rid}: future review')
        aid = review['attempt_id']
        if review['review_type'] == 'problem_entry' and aid is not None:
            errors.append(f'{rid}: problem-entry review must not identify an attempt')
        if review['review_type'] == 'problem_entry' and review['attempt_digest'] is not None:
            errors.append(f'{rid}: problem-entry review must not identify an attempt digest')
        if review['review_type'] != 'problem_entry' and aid is None:
            errors.append(f'{rid}: attempt review requires an attempt reference')
        if review['review_type'] != 'problem_entry' and not review['attempt_digest']:
            errors.append(f'{rid}: attempt review requires the examined attempt digest')
        if aid is not None:
            attempt = attempts.get(aid)
            if not attempt or attempt['problem_id'] != review['problem_id']:
                errors.append(f'{rid}: missing or inconsistent attempt reference {aid}')
            elif rid not in attempt['review_ids']:
                errors.append(f'{rid}: attempt must link back to its review')
            elif review['review_type'] == 'research_record' and attempt['started_at'] and review['date'] < timestamp(attempt['started_at']).astimezone(dt.timezone.utc).date().isoformat():
                errors.append(f'{rid}: review predates the attempt')
        if review['verdict'] != 'pending' and not review['evidence_artifacts']:
            errors.append(f'{rid}: completed review requires evidence references')
        if (review['review_type'] == 'research_record' and review['verdict'] != 'pending'
                and aid in attempts and not attempts[aid]['started_at']):
            errors.append(f'{rid}: result review requires an executed attempt')
        for replaced_id in review['supersedes']:
            replaced = reviews.get(replaced_id)
            if not replaced or replaced_id == rid:
                errors.append(f'{rid}: superseded review must be a distinct existing record')
                continue
            same = all(review[key] == replaced[key] for key in
                       ['problem_id', 'attempt_id', 'reviewer', 'review_type'])
            same = same and set(review['scope']) == set(replaced['scope']) and set(review['not_reviewed']) == set(replaced['not_reviewed'])
            if not same or review['date'] < replaced['date']:
                errors.append(f'{rid}: supersession must preserve reviewer, scope and target and cannot predate the earlier review')

    def cycle(rid, visiting, visited):
        if rid in visiting:
            return True
        if rid in visited or rid not in reviews:
            return False
        visiting.add(rid)
        found = any(cycle(previous, visiting, visited) for previous in reviews[rid]['supersedes'])
        visiting.remove(rid)
        visited.add(rid)
        return found
    visited = set()
    if any(cycle(rid, set(), visited) for rid in reviews):
        errors.append('reviews: supersession cycle')

    for card in dataset['cards']:
        assessment = card['ai_assessment']
        level, refs = assessment['evidence_level'], assessment['evidence_refs']
        if level == 'untested_forecast' and refs:
            errors.append(f'{card["id"]}: forecast must not present measured evidence references')
        if level == 'project_measured':
            if not refs:
                errors.append(f'{card["id"]}: unsupported measured AI evidence')
            for aid in refs:
                a = attempts.get(aid)
                if not a or a['problem_id'] != card['id'] or a['status'] not in {'completed', 'stopped', 'failed'} or not a['model']['name'] or not a['process_artifacts']:
                    errors.append(f'{card["id"]}: unsupported measured AI evidence {aid}')
                elif a['ended_at'] and timestamp(a['ended_at']).astimezone(dt.timezone.utc).date().isoformat() > assessment['assessment_date']:
                    errors.append(f'{card["id"]}: assessment predates its measured evidence')
        if level == 'public_attempt_evidence':
            if not refs or not card['known_attempts']:
                errors.append(f'{card["id"]}: public-attempt assessment needs described and cited evidence')
            for sid in refs:
                if sid not in sources or sources[sid]['verification'] != 'opened' or sid not in card['source_ids']:
                    errors.append(f'{card["id"]}: public-attempt evidence needs an inspected card source {sid}')
    cards = {card['id']: card for card in dataset['cards']}
    for candidate in dataset['candidates']:
        state = candidate['human_review_status']
        verdict = {'reviewed_accepted': 'accepted_within_scope', 'reviewed_changes_requested': 'changes_requested'}.get(state)
        if not verdict:
            continue
        target = cards.get(candidate['id'], candidate)
        current = [r for r in unsuperseded_reviews(dataset) if r['problem_id'] == candidate['id']
                   and r['review_type'] == 'problem_entry'
                   and r['statement_digest'] == statement_digest(target) and r['verdict'] != 'pending']
        if not current or not any(r['verdict'] == verdict for r in current):
            errors.append(f'{candidate["id"]}: review status requires a matching scoped review of the current target')
        elif state == 'reviewed_accepted' and any(r['verdict'] != verdict for r in current):
            errors.append(f'{candidate["id"]}: current review conclusions do not support an accepted label')

    executed = [a for a in attempts.values() if a['started_at'] is not None]
    if dataset['project']['research_attempts_run'] != len(executed):
        errors.append('project: research_attempts_run differs from started attempt records')
    evaluations = sum(a['purpose'] == 'model_evaluation' for a in executed)
    if dataset['project']['model_evaluations_run'] != evaluations:
        errors.append('project: model_evaluations_run differs from started model-evaluation records')
    return errors
