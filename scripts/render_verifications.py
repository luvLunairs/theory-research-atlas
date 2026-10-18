"""Render verification specifications and scoped execution evidence."""
from pathlib import Path
from urllib.parse import quote

from machine_verification import specification_digest, verification_state
from render_cards import _human, _label, _table, _text, _value
from research_records import statement_digest


ROOT = Path(__file__).resolve().parents[1]
STATE_LABELS = {
    'machine_checked': 'Machine checked',
    'reported_pass': 'Reported pass',
    'pending_approval': 'Pending approval',
    'stale': 'Stale',
    'failed': 'Failed',
    'inconclusive': 'Inconclusive',
    'error': 'Execution error',
    'conflicting': 'Conflicting evidence',
    'invalid': 'Invalid verification record',
}
STATE_NOTES = {
    'machine_checked': 'The retained independent run qualifies for the approved claim and recorded versions. Human review, novelty and problem status remain separate.',
    'reported_pass': 'Success was reported, but this run does not meet all independent-execution, evidence or strict eligibility requirements.',
    'pending_approval': 'The specification does not have a current qualifying approval. This run cannot establish acceptance through the machine verification route.',
    'stale': 'The checked versions no longer match the current target, specification or attempt. The historical result does not certify the changed work.',
    'failed': 'The recorded verification failed. No correctness acceptance follows from this run.',
    'inconclusive': 'The run does not settle the certified claim.',
    'error': 'Verification encountered an execution error; no pass is established.',
    'conflicting': 'Conflicting verification evidence prevents reliance on a pass until the conflict is resolved.',
    'invalid': 'This record does not satisfy the verification requirements; its reported outcome is not an acceptance.',
}


def state_label(dataset, record, root=ROOT):
    """Always derive eligibility; never promote a recorded outcome directly."""
    state = verification_state(dataset, record, root=root)
    return STATE_LABELS.get(state, STATE_LABELS['invalid'])


def _specifications(dataset):
    return {spec['id']: spec for spec in dataset.get('verification_specs', [])}


def _problem_link(dataset, problem_id, prefix=''):
    candidate = next((c for c in dataset['candidates'] if c['id'] == problem_id), None)
    if candidate is None:
        return _text(problem_id) + ' (entry unavailable)'
    folder = 'cards' if any(c['id'] == problem_id for c in dataset['cards']) else 'candidates'
    return f'[{_label(candidate["title"])}]({prefix}{folder}/{problem_id}.md)'


def _scope(spec):
    return '; '.join(spec['scope']) if spec else 'Specification unavailable'


def _approval_label(dataset, spec):
    approval = spec['approval']
    if approval['status'] != 'approved':
        return _human(approval['status'])
    if approval['specification_digest'] != specification_digest(spec):
        return 'Approved for an earlier specification'
    target = next((c for c in [*dataset['cards'], *dataset['candidates']] if c['id'] == spec['problem_id']), None)
    if target is None or spec['statement_digest'] != statement_digest(target):
        return 'Approved for an earlier problem statement'
    return 'Approved for the recorded version'


def verification_summary(dataset, attempt_id, prefix='', root=ROOT):
    """Compact run links and their certified scope for an attempt table."""
    specs = _specifications(dataset)
    runs = sorted((r for r in dataset.get('verifications', []) if r['attempt_id'] == attempt_id),
                  key=lambda r: (r['executed_at'], r['id']), reverse=True)
    return '; '.join(
        f'[{r["id"]}]({prefix}verifications/{r["id"]}.md): {state_label(dataset, r, root)}. '
        f'Current specification scope: {_text(_scope(specs.get(r["specification_id"])))}' for r in runs
    ) or 'No verification recorded'


def _runs_table(dataset, runs, prefix='', root=ROOT):
    specs = _specifications(dataset)
    return _table(['Run', 'Attempt', 'State', 'Executed', 'Current specification scope'], [
        (f'[{r["id"]}]({prefix}verifications/{r["id"]}.md)',
         f'[{r["attempt_id"]}]({prefix}attempts/{r["attempt_id"]}.md)',
         state_label(dataset, r, root), r['executed_at'],
         _text(_scope(specs.get(r['specification_id']))))
        for r in sorted(runs, key=lambda r: (r['executed_at'], r['id']), reverse=True)])


def problem_verification_section(dataset, problem_id, prefix='../', root=ROOT, heading='##'):
    """Do not add empty verification sections to hundreds of problem pages."""
    specs = [s for s in dataset.get('verification_specs', []) if s['problem_id'] == problem_id]
    runs = [r for r in dataset.get('verifications', []) if r['problem_id'] == problem_id]
    if not specs and not runs:
        return ''
    text = f'{heading} Machine verification\n\n'
    if specs:
        text += _table(['Specification', 'Claim', 'Recorded approval'], [
            (f'[{s["id"]}]({prefix}verification-specs/{s["id"]}.md)', _text(s['claim']),
             _approval_label(dataset, s)) for s in sorted(specs, key=lambda s: s['id'])])
    if runs:
        text += _runs_table(dataset, runs, prefix, root)
    else:
        text += 'No verification run has been recorded.\n\n'
    text += (f'Each state applies only to its certified scope and versions. '
             f'[Machine verification]({prefix}machine-verification.md) is separate from human review and problem status.\n\n')
    return text


def _artifacts(record):
    rows = []
    for item in record['artifact_manifest']:
        ref = item['reference']
        target = ref if ref.lower().startswith(('https://', 'http://')) else '../../' + quote(ref.replace('\\', '/'), safe='/')
        rows.append((f'[{_label(ref)}](<{target}>)', _text(item['version']),
                     '`' + item['sha256'] + '`' if item['sha256'] else 'Not recorded'))
    return _table(['Artifact', 'Retained version', 'SHA-256'], rows) if rows else 'No artifact manifest recorded.\n\n'


def render_verifications(dataset, root=ROOT):
    """Return pages without executing any checker or writing artifacts."""
    specs = _specifications(dataset)
    runs = dataset.get('verifications', [])
    out = {}
    text = '# Machine verification records\n\n'
    text += '[Verification policy](machine-verification.md) · [Research progress](progress.md) · [Project contributions](results.md)\n\n'
    text += ('Specifications fix the claim and checking procedure; runs retain the evidence for individual certificates. '
             '**Machine checked** applies only to an approved scope and matching versions. It is separate from human review, novelty and problem status.\n\n')
    text += f'**Specifications: {len(specs)} · Recorded runs: {len(runs)}.** Verification records are not additional research findings.\n\n'
    if not specs and not runs:
        text += ('No verification specifications or runs have been recorded. '
                 'Use the [policy](machine-verification.md#start-here) and [machine verification template](../templates/machine-verification.md) '
                 'to propose a fixed target and checking procedure, or submit evidence for an approved specification.\n\n')
    if specs:
        text += '## Specifications\n\n'
        text += _table(['Specification', 'Question', 'Method', 'Claim', 'Recorded approval'], [
            (f'[{s["id"]}](verification-specs/{s["id"]}.md)', _problem_link(dataset, s['problem_id']),
             _human(s['method']), _text(s['claim']), _approval_label(dataset, s))
            for s in sorted(specs.values(), key=lambda s: s['id'])])
    if runs:
        text += '## Runs\n\n' + _runs_table(dataset, runs, root=root)
    text += ('Repository checks validate records and local hashes; they do not execute the certificate checker or authenticate an approval or runner. '
             'The maintainer must verify provenance at intake. The derived run state does not replace this responsibility.\n')
    out['docs/verifications.md'] = text

    for spec in sorted(specs.values(), key=lambda s: s['id']):
        text = f'# {spec["id"]}: verification specification\n\n'
        text += f'[Verification records](../verifications.md) · {_problem_link(dataset, spec["problem_id"], "../")}\n\n'
        text += f'**Method:** {_human(spec["method"])}. **Recorded approval:** {_approval_label(dataset, spec)}.\n\n'
        text += 'Approval applies only to the recorded specification digest and supporting human review; the run pages show current eligibility.\n\n'
        text += '## Certified claim\n\n' + _text(spec['claim']) + '\n\n'
        text += f'**Current specification digest:** `{specification_digest(spec)}`.\n\n'
        for field, value in spec.items():
            if field in {'id', 'problem_id', 'method', 'claim'}:
                continue
            text += f'## {_human(field)}\n\n' + (_artifacts(spec) if field == 'artifact_manifest' else _value(value))
        linked = [r for r in runs if r['specification_id'] == spec['id']]
        text += '## Verification runs\n\n'
        text += _runs_table(dataset, linked, '../', root) if linked else 'No verification run has been recorded.\n\n'
        text += f'[Structured specification](../../data/verification-specs/{spec["id"]}.json)\n'
        out[f'docs/verification-specs/{spec["id"]}.md'] = text

    for run in sorted(runs, key=lambda r: r['id']):
        state = verification_state(dataset, run, root=root)
        spec = specs.get(run['specification_id'])
        text = f'# {run["id"]}: verification run\n\n'
        text += f'[Verification records](../verifications.md) · {_problem_link(dataset, run["problem_id"], "../")}\n\n'
        text += f'**Verification state:** {STATE_LABELS.get(state, STATE_LABELS["invalid"])}.\n\n'
        text += STATE_NOTES.get(state, STATE_NOTES['invalid']) + '\n\n'
        text += f'**Attempt:** [{run["attempt_id"]}](../attempts/{run["attempt_id"]}.md). '
        text += f'**Specification:** [{run["specification_id"]}](../verification-specs/{run["specification_id"]}.md).\n\n'
        if spec:
            text += '## Certified claim and scope\n\n' + _text(spec['claim']) + '\n\n' + _value(spec['scope'])
            if state == 'stale':
                text += 'This is the current specification wording. Consult the retained target artifacts and digests for the historical wording checked by this run.\n\n'
        for field, value in run.items():
            if field in {'id', 'problem_id', 'specification_id', 'attempt_id'}:
                continue
            title = 'Recorded outcome' if field == 'outcome' else _human(field)
            text += f'## {title}\n\n' + (_artifacts(run) if field == 'artifact_manifest' else _value(value))
        text += f'[Structured run](../../data/verifications/{run["id"]}.json)\n'
        out[f'docs/verifications/{run["id"]}.md'] = text
    return out
