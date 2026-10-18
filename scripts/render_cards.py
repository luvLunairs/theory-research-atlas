"""Render research cards and their index from structured records.

Return Markdown without writing files. Link the JSON records without duplicating
them in the research pages.
"""
from html import escape
from urllib.parse import urlencode
from research_records import records_for_problem


PRIORITIES = {
    'priority_trial': 'Priority for a later trial',
    'preparation_required': 'Preparation needed',
    'exploratory': 'Exploratory',
    'unassessed': 'Not yet assessed',
}
KINDS = {
    'known_result_calibration': 'Known-result calibration',
    'literature_open': 'Literature-origin question',
    'curator_proposed': 'Curator-proposed task',
}
STATUSES = {
    'known_result': 'Known result in literature',
    'source_reports_open': 'Source reports open',
    'open_after_scoped_check': 'Open after a scoped check',
    'resolved': 'Reported resolution in literature',
    'disproved': 'Sourced disproof',
    'conditional': 'Conditional status',
    'conflicting': 'Conflicting evidence',
    'unverified': 'Needs further verification',
}
EVIDENCE = {
    'untested_forecast': 'Untested forecast',
    'public_attempt_evidence': 'Evidence from a public attempt',
    'project_measured': 'Measured project evidence',
}
METHODS = {
    'proof': 'Proof', 'construction': 'Construction',
    'counterexample': 'Counterexample', 'classification': 'Classification',
    'bounds': 'Bounds', 'algorithm': 'Algorithms',
    'symbolic_derivation': 'Symbolic derivation', 'finite_search': 'Finite search',
    'exact_computation': 'Exact computation', 'numerical_computation': 'Numerical computation',
    'certificate_checking': 'Certificate checking', 'formalization': 'Formalization',
    'model_analysis': 'Model analysis', 'model_construction': 'Model construction',
}
VALIDATION = {
    'pure_proof': 'Proof', 'exact_computation': 'Exact computation',
    'numerical_evidence': 'Numerical evidence', 'public_data': 'Public data',
    'simple_experiment': 'Simple experiment', 'complex_experiment': 'Complex experiment',
}
DIMENSIONS = {
    'clarity': 'Statement clarity', 'decomposability': 'Decomposability',
    'methods': 'Methods and literature', 'search_or_symbolic': 'Search / symbolic fit',
    'checkability': 'Checkability', 'expertise': 'Expertise needed',
    'significance': 'Scholarly significance', 'verification_difficulty': 'Verification difficulty',
}
RELATIONS = {
    'calibrated_by': 'Calibrated by', 'calibrates': 'Calibrates',
    'calibration_for': 'Calibration for', 'depends_on': 'Depends on',
    'equivalent_to': 'Equivalent to', 'method_bridge': 'Method bridge to',
    'method_preparation': 'Method preparation for', 'prerequisite': 'Prerequisite for',
    'related_method': 'Related method', 'related_to': 'Related to',
    'subproblem_of': 'Subproblem of',
}
SECTIONS = (
    ('at-a-glance', 'At a glance'), ('problem', 'The task'),
    ('verification', 'Resources and verification'), ('evidence', 'Evidence and context'),
    ('assessment', 'AI trial assessment'), ('audit-trail', 'Research records'),
)
CARD_FIELDS = {
    'id', 'title', 'domain', 'cross_domains', 'kind', 'statement', 'source_ids',
    'source_locator', 'status', 'status_basis', 'last_checked', 'curator_origin',
    'duplicate_key', 'proposed_card', 'plain_summary', 'assumptions', 'scope',
    'target', 'success_criteria', 'known_results', 'prerequisites', 'significance',
    'relations', 'requirements', 'ai_assessment', 'methods', 'obstacles',
    'validation', 'known_attempts', 'unresolved_checks', 'attribution',
    'status_search', 'primary_domain_id', 'cross_domain_ids', 'curation_level',
    'human_review_status', 'method_tags', 'validation_tags', 'experimental_dependency',
    'epistemic_layers', 'judgments', 'revision_history',
}
NAV = '[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)'
ISSUE_BASE = 'https://github.com/luvLunairs/theory-research-atlas/issues/new'


def contribution_links(problem):
    """Open the relevant form with the problem identified, without submitting it."""
    links = []
    for template, prefix, label in (
        ('correction.yml', 'Correction', 'Suggest a correction'),
        ('research-progress.yml', 'Research', 'Share progress'),
    ):
        query = urlencode({
            'template': template,
            'title': f'[{prefix}] {problem["id"]}: {problem["title"]}',
            'target': problem['id'],
        })
        links.append(f'[{label}]({ISSUE_BASE}?{query})')
    return ' · '.join(links) + '\n\n'


def _human(value):
    return str(value).replace('_', ' ').capitalize()


def _text(value):
    return escape(str(value), quote=False)


def _label(value):
    return _text(value).replace('[', '\\[').replace(']', '\\]')


def _code(value):
    return '`' + str(value).replace('`', '&#96;') + '`'


def _table(headers, rows):
    def cell(value):
        return str(value).replace('|', '&#124;').replace('\n', '<br>')
    return ('| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join('---' for _ in headers) + ' |\n'
            + ''.join('| ' + ' | '.join(cell(v) for v in row) + ' |\n' for row in rows) + '\n')


def _list(values, ordered=False):
    if not values:
        return 'None recorded.\n\n'
    return ''.join(f'{i + 1}.' + ' ' + _text(v) + '\n' if ordered else '- ' + _text(v) + '\n'
                   for i, v in enumerate(values)) + '\n'


def _details(summary, body):
    return f'<details>\n<summary>{_text(summary)}</summary>\n\n{body.rstrip()}\n\n</details>\n\n'


def _section(anchor, title):
    return f'<a id="{anchor}"></a>\n\n## {title}\n\n'


def _value(value):
    """Render record/history extensions without dropping unfamiliar fields."""
    if value is None:
        return 'Not recorded.\n\n'
    if isinstance(value, bool):
        return ('Yes' if value else 'No') + '\n\n'
    if isinstance(value, dict):
        return ''.join(f'**{_text(_human(k))}:**\n\n' + _value(v) for k, v in value.items())
    if isinstance(value, list):
        if not value:
            return 'None recorded.\n\n'
        if all(isinstance(v, str) for v in value):
            return _list(value)
        return '\n'.join(_value(v) for v in value)
    return _text(value) + '\n\n'


def render_cards(d, root=None):
    """Return the index and one Markdown document per research problem."""
    from render_verifications import ROOT, problem_verification_section
    root = ROOT if root is None else root
    nodes = {n['id']: n for n in d['nodes']}
    sources = {s['id']: s for s in d['sources']}
    candidates = {c['id']: c for c in d['candidates']}
    cards = sorted(d['cards'], key=lambda c: c['id'])

    def domain_link(node_id):
        node = nodes[node_id]
        root = node
        while root['parent_id'] is not None:
            root = nodes[root['parent_id']]
        fragment = '' if node['parent_id'] is None else '#' + node_id.lower().replace('.', '-')
        return f'[{_label(node["title"])}](../domains/{root["id"].lower()}.md{fragment})'

    def source_link(source_id):
        source = sources[source_id]
        return f'[{_label(source["title"])}](../sources.md#{source_id.lower()})'

    def problem_link(problem_id):
        item = candidates[problem_id]
        return f'[{_label(item["title"])}](../candidates.md#{problem_id.lower()})'

    def priority_link(card):
        priority = card['ai_assessment']['priority']
        return f'[{PRIORITIES.get(priority, _human(priority))}](../ai-assessment.md)'

    def tags(values, labels):
        return ', '.join(labels.get(v, _human(v)) for v in values) or 'None recorded'

    out = {}
    index = '# Research problems\n\n' + NAV + '\n\n'
    index += (
        'Each entry brings together a precise task, its sources, prerequisites and ways to check a result. '
        'The priorities indicate which tasks may be worth trying; they are not measurements of AI performance. '
        'Known results are distinguished from open questions and proposed investigations.\n\n'
        '**Looking for new research? Start with [open research candidates](../research-candidates.md).** '
        'This complete card directory also retains calibrations and proposals.\n\n'
        '[Assessment rubric](../ai-assessment.md) · [Evidence policy](../evidence-policy.md)\n\n'
    )
    index += _table(['Entry type', 'Full cards', 'Broader index'], [
        (KINDS.get(kind, _human(kind)), sum(c['kind'] == kind for c in cards),
         f'[View candidates](../candidates.md#{kind.replace("_", "-")})')
        for kind in ('literature_open', 'curator_proposed', 'known_result_calibration')
    ])
    index += ('Origin is separate from current status. Reproductions help assess methods; '
              'their completion would not constitute a new solution to an open problem. '
              '[Research progress](../progress.md) records actual attempts and reviews.\n\n')
    present = [p for p in PRIORITIES if any(c['ai_assessment']['priority'] == p for c in cards)]
    present += sorted({c['ai_assessment']['priority'] for c in cards} - set(PRIORITIES))
    index += ' · '.join(f'[{PRIORITIES.get(p, _human(p))}](#{p.replace("_", "-")})' for p in present)
    index += ' · [Browse by method](#browse-by-method)\n\n'
    for priority in present:
        index += _section(priority.replace('_', '-'), PRIORITIES.get(priority, _human(priority)))
        ordered = sorted(cards, key=lambda c: c['kind'] == 'known_result_calibration')
        for c in (c for c in ordered if c['ai_assessment']['priority'] == priority):
            ai = c['ai_assessment']
            index += f'<a id="{c["id"].lower()}"></a>\n\n### [{_label(c["title"])}]({c["id"]}.md)\n\n'
            index += (f'{domain_link(c["primary_domain_id"])} · '
                      f'{KINDS.get(c["kind"], _human(c["kind"]))}\n\n')
            index += _text(c['plain_summary']) + '\n\n'
            index += f'**Status:** {STATUSES.get(c["status"], _human(c["status"]))}; checked {c["last_checked"]}. '
            index += f'**Assessment evidence:** {EVIDENCE.get(ai["evidence_level"], _human(ai["evidence_level"]))}.\n\n'
            index += '**Background:** ' + '; '.join(_text(x).rstrip('.') for x in c['prerequisites']) + '.\n\n'
            index += '**Verification:** ' + tags(c['validation_tags'], VALIDATION) + f'. [How to check a result]({c["id"]}.md#verification).\n\n'
            review_notes = '**Reason for this priority:** ' + _text(ai['rationale']) + '\n\n'
            review_notes += '**Computing requirements and limits:** ' + _text(c['requirements']['compute']) + '\n\n'
            review_notes += '**Human review:** ' + _text(c['validation']['human_review_difficulty']) + '\n\n'
            index += _details('Review notes and full computing requirements', review_notes)
    index += _section('browse-by-method', 'Browse by method')
    index += 'This table covers the detailed problem entries. Other candidates have not received an AI suitability assessment. The methods describe possible approaches, not measured capability.\n\n'
    method_ids = sorted({tag for c in cards for tag in c['method_tags']}, key=lambda tag: METHODS.get(tag, tag))
    index += _table(['Method', 'Cards'], [
        (METHODS.get(tag, _human(tag)), '<br>'.join(f'[{_label(c["title"])}]({c["id"]}.md)' for c in cards if tag in c['method_tags']))
        for tag in method_ids
    ])
    out['docs/cards/README.md'] = index

    for c in cards:
        ai, validation, requirements = c['ai_assessment'], c['validation'], c['requirements']
        text = f'# {_text(c["title"])}\n\n' + NAV + '\n\n'
        text += _text(c['plain_summary']) + '\n\n'
        text += contribution_links(c)
        text += ' · '.join(f'[{title}](#{anchor})' for anchor, title in SECTIONS) + '\n\n'
        text += _section('at-a-glance', 'At a glance')
        text += _table(['Field', 'Summary'], [
            ('Primary field', domain_link(c['primary_domain_id'])),
            ('Related fields', ', '.join(domain_link(i) for i in c['cross_domain_ids']) or 'None recorded'),
            ('Task origin', f'[{KINDS.get(c["kind"], _human(c["kind"]))}](../evidence-policy.md)'),
            ('Current status', f'[{STATUSES.get(c["status"], _human(c["status"]))}](../evidence-policy.md) · checked {c["last_checked"]}'),
            ('AI suitability', priority_link(c) + ' · ' + EVIDENCE.get(ai['evidence_level'], _human(ai['evidence_level']))),
            ('Scientific review', _human(c['human_review_status'])),
        ])
        text += _section('problem', 'The task')
        text += '### Precise statement\n\n' + _text(c['statement']) + '\n\n'
        text += '**Required output:** ' + _text(c['target']) + '\n\n'
        text += '**Scope:** ' + _text(c['scope']) + '\n\n'
        text += '### Assumptions\n\n' + _list(c['assumptions'])
        text += '### Success criteria\n\n' + _list(c['success_criteria'], ordered=True)
        text += '### Background needed\n\n' + _list(c['prerequisites'])
        text += _section('verification', 'Resources and verification')
        text += '### Resource requirements\n\n'
        for key, label in [('compute', 'Computing'), ('data', 'Data'), ('experiment', 'Experiments'), ('theoretical_assumptions', 'Theory and model requirements')]:
            text += f'**{label}:** ' + _text(requirements[key]) + '\n\n'
        text += '**Validation modes:** ' + tags(c['validation_tags'], VALIDATION) + '.\n\n'
        text += '### Verification steps\n\n' + _list(validation['steps'], ordered=True)
        text += '**Statement alignment:** ' + _text(validation['statement_alignment']) + '\n\n'
        text += '**Human review difficulty:** ' + _text(validation['human_review_difficulty']) + '\n\n'
        text += '### Formal validity and empirical support\n\n'
        text += '**What the formal task can establish:** ' + _text(c['epistemic_layers']['formal_validity']) + '\n\n'
        text += '**Empirical support and limits:** ' + _text(c['epistemic_layers']['empirical_support']) + '\n\n'
        text += '### Methods and obstacles\n\n**Proposed methods:**\n\n' + _list(c['methods'])
        text += '**Expected obstacles:**\n\n' + _list(c['obstacles'])
        text += '### Checks still needed\n\n' + _list(c['unresolved_checks'])
        text += _section('evidence', 'Evidence and context')
        text += '**Status basis:** ' + _text(c['status_basis']) + '\n\n'
        if any(r['problem_id'] == c['id'] for r in d.get('literature_checks', [])):
            text += f'[Dated literature checks and remaining limits](../candidates/{c["id"]}.md#literature-checks). These are editorial evidence checks, not signed expert reviews.\n\n'
        text += '**Exact problem / theorem locator:** ' + _text(c['source_locator']) + '\n\n'
        text += '### Sources\n\n'
        for source_id in c['source_ids']:
            source = sources[source_id]
            text += f'- {source_link(source_id)}. {_text("; ".join(source["authors"]))}. '
            text += f'{source["year"] if source["year"] is not None else "Year not verified"}. '
            text += f'[Read source]({source["url"]}).\n'
            text += '  - **Relevant sections:** ' + _text(source['locator']) + '\n'
            text += '  - **Source limitations:** ' + _text(source['limitations']) + '\n'
        text += '\n### Known results and partial progress\n\n' + _list(c['known_results'])
        text += '**Research value:** ' + _text(c['significance']) + '\n\n'
        text += '### Related problems\n\n'
        if c['relations']:
            for relation in c['relations']:
                label = RELATIONS.get(relation['type'], _human(relation['type']))
                text += f'- **{_text(label)}:** {problem_link(relation["target"])}. {_text(relation["explanation"])}\n'
            text += '\n'
        else:
            text += 'No formal dependency or equivalence is asserted.\n\n'
        search = c['status_search']
        text += '### Scope of the status check\n\n'
        text += '**Finding:** ' + _text(search['result']) + '\n\n'
        text += '**Search limits:** ' + _text(search['limitations']) + '\n\n'
        search_detail = ''
        if search['queries']:
            search_detail += '**Queries used:**\n\n' + _list(search['queries'])
        if search['checked_sources']:
            search_detail += '**Sources checked:**\n\n' + ''.join('- ' + source_link(i) + '\n' for i in search['checked_sources']) + '\n'
        if search_detail:
            text += _details('Literature references checked', search_detail)
        if c['known_attempts']:
            text += _details('Previous attempts and public records', _list(c['known_attempts']))
        attribution = c['attribution']
        credits = '**Original authors and credited contributors:**\n\n' + _list(attribution['original_authors'])
        credits += '**Suggested citation:** ' + _text(attribution['citation']) + '\n\n'
        credits += '**Editorial credit:** ' + _text(attribution['curator_credit']) + '\n\n'
        text += _details('Attribution and suggested citation', credits)
        text += _section('assessment', 'AI trial assessment')
        text += '**Label:** ' + priority_link(c) + '. **Evidence:** ' + EVIDENCE.get(ai['evidence_level'], _human(ai['evidence_level'])) + f'. **Assessed:** {ai["assessment_date"]}.\n\n'
        text += _text(ai['rationale']) + '\n\n'
        text += '**Model or capability conditions:** ' + _text(ai['model_scope']) + '\n\n'
        text += '**Uncertainty:** ' + _text(ai['uncertainty']) + '\n\n'
        if ai.get('evidence_refs'):
            text += '**Assessment evidence:** ' + ', '.join(source_link(ref) if ref in sources else f'[{ref}](#audit-trail)' for ref in ai['evidence_refs']) + '.\n\n'
        text += 'Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.\n\n'
        text += _table(['Dimension', 'Rating', 'Reason'], [
            (DIMENSIONS.get(key, _human(key)), _human(value['rating']), _text(value['reason']))
            for key, value in ai['dimensions'].items()
        ])
        judgments = ''
        for key, value in c['judgments'].items():
            judgment = f'**{_text(_human(key))}:** {_text(_human(value.get("rating", value.get("status", "Not recorded"))))}.\n\n'
            if key == 'difficulty' and value['basis'] == ai['rationale']:
                judgment += 'The reasons are given in the [AI trial assessment](#assessment).\n\n'
            elif key == 'significance' and value['basis'] == c['significance']:
                judgment += 'The reasons are given under [research value](#evidence).\n\n'
            else:
                judgment += _text(value['basis']) + '\n\n'
            if 'evidence' in value:
                judgment += '**Evidence type:** ' + _text(_human(value['evidence'])) + '.\n\n'
            if key in ('correctness', 'novelty'):
                text += judgment
            else:
                judgments += judgment
        if judgments:
            text += _details('Difficulty and significance', judgments)
        text += _section('audit-trail', 'Research records')
        attempts, reviews = records_for_problem(d, c['id'])
        if not attempts and not reviews:
            text += 'No project attempts or human reviews have been recorded.\n\n'
        elif not attempts:
            text += 'No project attempts have been recorded.\n\n'
        elif not reviews:
            text += 'No human reviews have been recorded.\n\n'
        for attempt in attempts:
            text += f'- [{attempt["id"]}](../attempts/{attempt["id"]}.md): {_human(attempt["status"])}. {_text(attempt["outcome"])}\n'
        for review in reviews:
            text += f'- [{review["id"]}](../reviews/{review["id"]}.md): {_human(review["verdict"])}. Scope: {_text("; ".join(review["scope"]))}\n'
        if attempts or reviews:
            text += '\n'
        text += problem_verification_section(d, c['id'], root=root, heading='###')
        if c['revision_history']:
            text += _details('Changes to this problem', _table(['Date', 'Change'], [(_text(r['date']), _text(r['change'])) for r in c['revision_history']]))
        metadata = _table(['Field', 'Recorded value'], [
            ('Stable ID', _code(c['id'])), ('Duplicate key', _code(c['duplicate_key'])),
            ('Original domain label', _text(c['domain'])), ('Original cross-domain labels', '; '.join(_text(v) for v in c['cross_domains']) or 'None'),
            ('Primary domain ID', _code(c['primary_domain_id'])), ('Cross-domain IDs', ', '.join(_code(v) for v in c['cross_domain_ids']) or 'None'),
            ('Origin code', _code(c['kind'])), ('Status code', _code(c['status'])),
            ('Curator-designed scope', 'Yes' if c['curator_origin'] else 'No'),
            ('Detailed entry', 'Yes' if c['proposed_card'] else 'No'), ('Record level', _code(c['curation_level'])),
            ('Human review status', _code(c['human_review_status'])), ('Trial-label code', _code(ai['priority'])),
            ('Assessment-evidence code', _code(ai['evidence_level'])),
            ('Method tags', ', '.join(_code(v) for v in c['method_tags'])),
            ('Validation tags', ', '.join(_code(v) for v in c['validation_tags'])),
            ('Experimental-dependency tag', _code(c['experimental_dependency'])),
        ])
        extra_fields = {key: value for key, value in c.items() if key not in CARD_FIELDS}
        if extra_fields:
            metadata += '**Additional record information:**\n\n' + _value(extra_fields)
        metadata += f'[JSON record](../../data/cards/{c["id"]}.json)\n\n'
        text += _details('Record information', metadata)
        text += '[Problem cards](README.md) · [Back to top](#at-a-glance)\n'
        out[f'docs/cards/{c["id"]}.md'] = text
    return out
