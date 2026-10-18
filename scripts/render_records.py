"""Render attributable research records and a collection-wide results view."""
from urllib.parse import quote

from render_cards import _value, _table, _list, _human, _text
from research_records import (attempt_digest, current_attempt_reviews, unsuperseded_reviews,
                              statement_digest, preliminary_screening_label)
from render_verifications import ROOT, verification_summary


def render_records(dataset, root=ROOT):
    out = {}
    candidates = {c['id']: c for c in dataset['candidates']}
    cards = {c['id'] for c in dataset['cards']}
    targets = {c['id']: c for c in [*dataset['candidates'], *dataset['cards']]}
    attempts = {a['id']: a for a in dataset['attempts']}
    retained_reviews = {r['id'] for r in unsuperseded_reviews(dataset)}
    screening_labels = {a['id']: preliminary_screening_label(a, root) for a in dataset['attempts']}

    def review_version(r):
        if r['id'] not in retained_reviews:
            return 'Superseded; retained as history'
        if r['attempt_id']:
            matches = r['attempt_digest'] == attempt_digest(attempts[r['attempt_id']])
        else:
            matches = r['statement_digest'] == statement_digest(targets[r['problem_id']])
        return 'Matches the current recorded target' if matches else 'Earlier or different target version'

    def artifacts(record, field):
        rows = []
        manifest = {item['reference']: item for item in record['artifact_manifest']}
        for ref in record[field]:
            target = ref if ref.lower().startswith(('https://', 'http://')) else '../../' + quote(ref.replace('\\', '/'), safe='/')
            rows.append((f'[{_text(ref)}](<{target}>)', manifest[ref]['version']))
        return _table(['Artifact', 'Retained version'], rows) if rows else 'None recorded.\n\n'

    def problem_link(pid, prefix=''):
        folder = 'cards' if pid in cards else 'candidates'
        return f'[{candidates[pid]["title"]}]({prefix}{folder}/{pid}.md)'

    for a in dataset['attempts']:
        text = f'# {a["id"]}: {candidates[a["problem_id"]]["title"]}\n\n'
        text += f'[Research progress](../progress.md) · {problem_link(a["problem_id"], "../")} · [Project contributions](../results.md)\n\n'
        text += f'**Execution:** {_human(a["status"])}. **Outcome:** {_human(a["outcome_kind"])}. **Purpose:** {_human(a["purpose"])}.\n\n'
        text += '## Reported outcome\n\n' + a['outcome'] + '\n\n'
        text += '**Limitations**\n\n' + _list(a['limitations'])
        text += '## Preliminary screening\n\n' + screening_labels[a['id']] + '.\n\n'
        screening = a.get('preliminary_screening')
        if screening:
            text += f'**Recorded by:** {_text(screening["recorded_by"])}. **Date:** {screening["date"]}.\n\n'
            text += _table(['Declaration', 'Recorded value'], [
                ('AI basis', _human(screening['ai_basis'])),
                ('AI contributor checks', _human(screening['ai_check_status'])),
                ('Human preliminary screening', _human(screening['human_preliminary_status']))])
            text += '**Scope**\n\n' + _list(screening['scope'])
            text += '**Screening limitations**\n\n' + _list(screening['limitations'])
            text += '**Evidence**\n\n' + artifacts({
                'artifact_manifest': a['artifact_manifest'],
                'evidence_artifacts': screening['evidence_artifacts']}, 'evidence_artifacts')
            text += (f'**Bound result, supporting and screening artifacts:** {len(screening["result_artifacts"])}. '
                     f'Exact references, versions and hashes are retained in the [structured record](../../data/attempts/{a["id"]}.json).\n\n')
            text += '**Examined target digest:** `' + screening['target_digest'] + '`.\n\n'
        text += ('This procedural stage is not a correctness probability, independent review or scientific approval. '
                 'See the scoped reviews and machine verification below. [Screening policy](../review-guide.md#preliminary-screening).\n\n')
        text += '## Target and verification\n\n' + a['target'] + '\n\n'
        text += '**Statement version:** ' + a['statement_version'] + '\n\n'
        for field in ['assumptions', 'success_criteria', 'verification_plan', 'stopping_conditions']:
            text += f'### {_human(field)}\n\n' + (_list(a[field]) if a[field] else 'No additional assumptions recorded.\n\n')
        text += '## Contributors\n\n' + _table(['Contributor', 'Roles'], [(p['name'], '; '.join(p['roles'])) for p in a['contributors']])
        text += '## Reproducibility\n\n'
        for field in ['started_at', 'ended_at', 'model', 'environment', 'input_artifacts', 'process_artifacts', 'human_help', 'candidate_answer_artifacts', 'artifact_manifest']:
            body = artifacts(a, field) if field.endswith('_artifacts') else _value(a[field])
            text += f'### {_human(field)}\n\n' + body
        text += '## Resources\n\n'
        for field in ['requirements', 'planned_budget', 'actual_use']:
            text += f'### {_human(field)}\n\n' + _value(a[field])
        text += '## Reviews\n\n'
        linked = [r for r in dataset['reviews'] if r['attempt_id'] == a['id']]
        if linked:
            text += _table(['Review', 'Date', 'Type', 'Verdict', 'Scope', 'Version'], [
                (f'[{r["id"]}](../reviews/{r["id"]}.md)', r['date'], _human(r['review_type']), _human(r['verdict']), '; '.join(r['scope']), review_version(r)) for r in linked])
        else:
            text += 'No review has been recorded.\n\n'
        text += 'Each verdict applies only to the recorded scope and version. A review of a plan is not a review of its results.\n\n'
        text += '## Machine verification\n\n' + verification_summary(dataset, a['id'], '../', root) + '.\n\n'
        text += 'Verification applies only to the certified scope and versions; human review and novelty remain separate. [Policy](../machine-verification.md).\n\n'
        text += f'**Current attempt digest:** `{attempt_digest(a)}`.\n\n'
        text += '## Revisions\n\n' + _table(['Date', 'Change'], [(r['date'], r['change']) for r in a['revision_history']])
        text += f'[Structured record](../../data/attempts/{a["id"]}.json)\n'
        out[f'docs/attempts/{a["id"]}.md'] = text
    for r in dataset['reviews']:
        text = f'# {r["id"]}: review of {candidates[r["problem_id"]]["title"]}\n\n'
        text += f'[Research progress](../progress.md) · {problem_link(r["problem_id"], "../")}\n\n'
        text += f'**Reviewer:** {r["reviewer"]}. **Role:** {r["reviewer_role"]}. **Date:** {r["date"]}.\n\n'
        text += f'**Type:** {_human(r["review_type"])}. **Verdict:** {_human(r["verdict"])}.\n\n'
        text += f'**Version relationship:** {review_version(r)}. This identifies the recorded target; it does not establish correctness or verify remote artifacts.\n\n'
        if r['attempt_id']:
            text += f'**Attempt:** [{r["attempt_id"]}](../attempts/{r["attempt_id"]}.md).\n\n'
        text += '**Reviewed version:** ' + r['reviewed_version'] + '\n\n'
        for field in ['scope', 'not_reviewed', 'comments', 'evidence_artifacts', 'artifact_manifest', 'conflicts_of_interest', 'statement_digest', 'attempt_digest', 'supersedes', 'revision_history']:
            if field == 'evidence_artifacts':
                body = artifacts(r, field)
            elif field == 'supersedes':
                body = _list([f'[{rid}]({rid}.md)' for rid in r[field]]) if r[field] else 'No earlier review is replaced.\n\n'
            else:
                body = _value(r[field])
            text += f'## {_human(field)}\n\n' + body
        text += f'[Structured record](../../data/reviews/{r["id"]}.json)\n'
        out[f'docs/reviews/{r["id"]}.md'] = text

    text = '# Project contributions\n\n'
    text += '[Project overview](../README.md) · [Research progress](progress.md) · [Contributors and credit](../AUTHORS.md)\n\n'
    text += f'**Edition:** {dataset["project"]["collection_version"]}.\n\n'
    text += '## The collection\n\n'
    text += ('The atlas contributes an organized research directory: original summaries, subject placement, source comparisons and explicit verification requirements. '
             'The underlying questions and published results remain credited to their original authors.\n\n')
    text += _table(['Resource', 'Contents'], [
        ('[Subject directory](README.md)', f'{sum(n["parent_id"] is None for n in dataset["nodes"])} main domains and {len(dataset["nodes"])} subjects and subfields'),
        ('[Problem index](candidates.md)', f'{len(candidates)} identified questions, including {len(cards)} full cards'),
        ('[Sources](sources.md)', f'{len(dataset["sources"])} bibliographic and research-entry records'),
        ('[Literature checks](literature-checks.md)', f'{len(dataset["literature_checks"])} dated checks, with findings and limitations')])
    text += '## Research findings\n\n'
    findings = [a for a in dataset['attempts'] if a['outcome_kind'] in {'partial_result', 'candidate_answer', 'correction', 'retraction'}]
    if not findings:
        text += 'No original research findings have been recorded. Source curation and documentation checks are not counted as solutions to the indexed problems.\n\n'
    else:
        rows = []
        for a in sorted(findings, key=lambda a: max(r['date'] for r in a['revision_history']), reverse=True):
            reviews = current_attempt_reviews(dataset, a)
            review_text = '; '.join(f'[{r["id"]}](reviews/{r["id"]}.md): {_human(r["verdict"])} ({"; ".join(r["scope"])})' for r in reviews) or 'No formal review of the current result recorded'
            credit = '; '.join(person['name'] for person in a['contributors'])
            rows.append((f'[{a["id"]}](attempts/{a["id"]}.md)', problem_link(a['problem_id']), credit, _human(a['outcome_kind']), a['outcome'], screening_labels[a['id']], review_text, verification_summary(dataset, a['id'], root=root)))
        text += _table(['Record', 'Question', 'Contributors', 'Contribution', 'Reported finding', 'Preliminary screening', 'Current formal human review scope', 'Machine verification and scope'], rows)
        text += 'Preliminary screening describes attributed checks, not correctness confidence or specialist academic acceptance. [Screening policy](review-guide.md#preliminary-screening).\n\n'
        text += 'A scoped acceptance does not establish novelty or all aspects of correctness. Corrections and retractions remain visible alongside the affected records.\n\n'
    text += ('[All attempts and reviews](progress.md) include unsuccessful work and known-result reproductions. '
             'Every candidate can receive a research record; a full card is optional.\n\n')
    text += '[Machine verification records](verifications.md) track certificate checks separately; they do not add research findings or human review verdicts.\n\n'
    text += '## Contribute\n\n'
    text += '[Propose or correct an entry](../templates/entry-change.md), [report an attempt](../templates/research-update.md), or [review a claim](../templates/review.md). '
    text += 'Give the problem ID, exact target, contributor roles, supporting evidence and remaining limits. Follow the [contribution terms](../CONTRIBUTING.md).\n'
    out['docs/results.md'] = text
    return out
