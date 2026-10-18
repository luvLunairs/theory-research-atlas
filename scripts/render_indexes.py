"""Generate domain browsing, source discovery and candidate views from structured data."""
from html import escape
from research_records import records_for_problem
from render_cards import contribution_links
from render_verifications import ROOT, problem_verification_section, verification_summary

LABELS = {
    'literature_open': 'Literature-origin question',
    'curator_proposed': 'Curator proposal',
    'known_result_calibration': 'Known-result calibration',
    'source_reports_open': 'Source reports open',
    'open_after_scoped_check': 'Open after scoped check',
    'known_result': 'Known result in literature',
    'unverified': 'Unverified', 'resolved': 'Reported resolved',
    'disproved': 'Disproved', 'conditional': 'Conditional', 'conflicting': 'Conflicting evidence',
    'research_entry': 'Research entry', 'classification': 'Classification reference',
    'include_task_screened': 'Included; screen each task',
    'include_conditional': 'Included conditionally', 'exclude_current_index': 'Outside this index',
    'none_for_formal_task': 'No experiment for the formal task',
}


def label(value):
    return LABELS.get(value, value.replace('_', ' ').capitalize())


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def table(headers, rows):
    return ('| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join('---' for _ in headers)
            + ' |\n' + ''.join('| ' + ' | '.join(cell(v) for v in row) + ' |\n' for row in rows) + '\n')


def bullets(values):
    return ''.join(f'- {v}\n' for v in values) + '\n' if values else 'None recorded.\n\n'


def anchor(value):
    return value.lower().replace('.', '-')


def details(summary, body):
    return f'<details>\n<summary>{escape(summary)}</summary>\n\n{body}\n</details>\n\n'


def active_research(candidate):
    return (candidate['kind'] == 'literature_open'
            and candidate['status'] in {'source_reports_open', 'open_after_scoped_check'})


def render_indexes(d, root=ROOT):
    verification_root = root
    out = {}
    nodes = {n['id']: n for n in d['nodes']}
    sources = {s['id']: s for s in d['sources']}
    cards = {c['id']: c for c in d['cards']}
    profiles = {p['problem_id']: p for p in d['profiles']}
    checks = {p['problem_id']: p for p in d['checks']}
    literature_checks = {}
    for review in d.get('literature_checks', []):
        literature_checks.setdefault(review['problem_id'], []).append(review)
    roots = [n for n in d['nodes'] if n['parent_id'] is None]
    mappings = {m['source_id']: m for m in d['source_map']}

    def within(child, parent):
        while child in nodes:
            if child == parent:
                return True
            child = nodes[child]['parent_id']
        return False

    def root_of(node_id):
        while nodes[node_id]['parent_id'] is not None:
            node_id = nodes[node_id]['parent_id']
        return node_id

    def node_link(node_id, prefix='domains/'):
        node = nodes[node_id]
        fragment = f'#{anchor(node_id)}' if node['parent_id'] else ''
        return f'[{node["title"]}]({prefix}{root_of(node_id).lower()}.md{fragment})'

    def source_link(source_id, prefix='sources.md'):
        source_id = d['aliases'].get(source_id, source_id)
        return f'[{sources[source_id]["title"]}]({prefix}#{source_id.lower()})'

    def problem_link(c, prefix=''):
        target = f'cards/{c["id"]}.md' if c['id'] in cards else f'candidates/{c["id"]}.md'
        return f'[{c["title"]}]({prefix}{target})'

    def selected(node_id):
        primary = [c for c in d['candidates'] if within(c['primary_domain_id'], node_id)]
        cross = [c for c in d['candidates'] if not within(c['primary_domain_id'], node_id)
                 and any(within(x, node_id) for x in c['cross_domain_ids'])]
        source_ids = [s['id'] for s in d['sources']
                      if any(within(n, node_id) for n in mappings[s['id']]['domain_ids'])]
        return primary, cross, source_ids

    def counts(node_id):
        primary, cross, source_ids = selected(node_id)
        research = sum(sources[s]['role'] == 'research_entry' for s in source_ids)
        classification = len(source_ids) - research
        complete = sum(c['id'] in cards for c in primary)
        gap = ('Extend coverage and review these cards' if complete else
               'Develop detailed problem cards' if primary else
               'Identify well-specified questions' if research else 'Find specialist sources')
        return classification, research, len(primary), complete, len(cross), gap

    def nav(prefix=''):
        return (f'[Browse]({prefix}README.md) · [Results]({prefix}results.md) · '
                f'[Contribute]({prefix}../CONTRIBUTING.md)\n\n')

    def candidates_table(candidates, prefix=''):
        return table(['Task', 'Difficulty', 'Origin', 'Current evidence status', 'Entry'], [
            (problem_link(c, prefix), label(profiles[c['id']]['difficulty']), label(c['kind']), label(c['status']),
             f'Full card · {c["id"]}' if c['id'] in cards else f'Outline · {c["id"]}')
            for c in candidates])

    def source_table(source_ids, prefix=''):
        return table(['Source', 'Purpose', 'Year'], [
            (source_link(s, prefix + 'sources.md'), label(sources[s]['role']),
             sources[s]['year'] or 'Not verified') for s in source_ids])

    text = '# Browse the atlas\n\n'
    text += ('Choose a subject, then open a question to read its statement, sources and evidence limits. '
             'A **full card** also gives assumptions, possible methods, resource needs and a checking plan. '
             'You can browse and contribute through GitHub without installing anything.\n\n')
    text += (f'**{len(roots)} main domains · {len(nodes)} subjects and subfields · {len(sources)} source records · '
             f'{len(d["candidates"])} candidate records · {len(cards)} full cards.** '
             f'The cards are included in the {len(d["candidates"])} candidates.\n\n')
    text += '## Choose a domain\n\n'
    text += table(['Domain', 'Research sources', 'Questions', 'Full cards'], [
        (node_link(n['id']), counts(n['id'])[1], counts(n['id'])[2], counts(n['id'])[3]) for n in roots])
    text += ('Use your browser\'s **Find** command to look for a term on the current page. '
             'Expand any collapsed section you want to search.\n\n')
    text += '## Choose a way to help\n\n' + table(['If you want to…', 'Start here'], [
        ('Explore a research question', '[Open research candidates](research-candidates.md), with detailed tasks first; [difficulty view](difficulty.md) for a wider comparison.'),
        ('Check a source, clarify a statement or update a status', '[Questions awaiting checks](pending-checks.md). Each entry explains the missing information and links to a correction form.'),
        ('Share an idea, result or review', '[Contribute](../CONTRIBUTING.md). A concise explanation with sources is enough to start; a complete problem card is not required.'),
    ])
    text += ('Checking references and improving explanations are useful contributions in their own right. '
             '[Recorded progress](progress.md) includes unsuccessful work and partial results when available.\n\n')
    reference = bullets([
        '[Full subject outline](taxonomy.md) — scan the hierarchy before choosing a branch.',
        '[Problem cards by assessment and method](cards/README.md) — compare scoped tasks.',
        '[All candidate questions](candidates.md) — separate literature-origin questions, proposals and calibrations.',
        '[Source directory](sources.md) and [literature checks](literature-checks.md) — inspect evidence and its limits.',
        '[Millennium and Hilbert problems](landmark-problems.md) — distinguish open questions from historical resolutions.',
        '[Coverage and next actions](coverage.md) — find branches that need sources or deeper curation.',
        '[Evidence rules](evidence-policy.md) and [AI assessment rubric](ai-assessment.md) — interpret the labels.',
        '[Local search and export](catalog.md) and [data model](data-model.md) — optional tools for working with structured records.',
    ])
    reference += table(['Collection layer', 'What it provides', 'Limits'], [
        ('A · Sources', 'Papers, surveys, problem collections and research communities.', 'A collection has not necessarily been fully read or indexed.'),
        ('B · Candidates', 'A target, its origin, evidence status and brief difficulty profile.', 'An outline is not a full methods, resource or verification assessment.'),
        ('C · Full cards', 'Assumptions, methods, resources and a validation plan.', 'A card is not a solution or expert endorsement. AI forecasts still require testing.'),
    ])
    reference += ('Domain counts include their branches. Cross-links reuse existing questions; cards are included in question counts. '
                  'Source counts include separately cited versions and cannot be summed across domains. '
                  'Zero marks a coverage gap, not a field without useful research.\n')
    text += details('More indexes, evidence labels and optional tools', reference)
    text += '[Project overview](../README.md) · [Results](results.md) · [Contribute](../CONTRIBUTING.md)\n'
    out['docs/README.md'] = text

    text = '# Subject outline\n\n' + nav()
    text += ('Scan the hierarchy here; follow any branch for its definition, boundaries, sources and tasks. '
             'The map is an editorial adaptation, not an official crosswalk. See the [design rationale](classification-design.md).\n\n')
    text += ' · '.join(f'[{n["title"]}](#{anchor(n["id"])})' for n in roots) + '\n\n'
    for root in roots:
        text += f'<a id="{anchor(root["id"])}"></a>\n\n## {root["title"]}\n\n{root["definition"]}\n\n'
        text += f'[Explore this domain](domains/{root["id"].lower()}.md)\n\n'
        def tree(parent_id, level=0):
            content = ''
            for n in d['nodes']:
                if n['parent_id'] != parent_id:
                    continue
                content += '  ' * level + f'- {node_link(n["id"])} — {n["definition"]}\n'
                content += tree(n['id'], level + 1)
            return content
        text += tree(root['id']) + '\n'
    text += '[Back to the atlas](README.md) · [Coverage gaps](coverage.md)\n'
    out['docs/taxonomy.md'] = text

    for root in roots:
        root_id = root['id']
        branch_nodes = [n for n in d['nodes'] if within(n['id'], root_id)]
        primary, cross, source_ids = selected(root_id)
        cls, research, total, complete, _, gap = counts(root_id)
        text = f'# {root["title"]}\n\n' + nav('../')
        text += root['definition'] + '\n\n**Boundary:** ' + root['boundary'] + '\n\n'
        text += (f'**Research sources: {research} · Primary tasks: {total} · '
                 f'Full cards: {complete} · Cross-linked tasks: {len(cross)}.**\n\n')
        text += '**Further work:** ' + gap + '.\n\n'
        text += '[Tasks](#tasks) · [Sources](#sources) · [Branch guide](#branches) · [Cross-domain tasks](#cross-domain-tasks)\n\n'
        text += '<a id="tasks"></a>\n\n## Tasks in this domain\n\n'
        text += candidates_table(primary, '../') if primary else 'No primary candidate has been extracted yet. Start with the sources below; this is an area still to be developed.\n\n'
        text += '<a id="sources"></a>\n\n## Sources for this domain\n\n'
        text += ('These are mapped to this domain or a descendant. A source entry does not mean all of its questions have been extracted. '
                 'Follow it for the inspected location, supported claims and limits.\n\n')
        text += source_table(source_ids, '../') if source_ids else 'No dedicated source has been mapped yet.\n\n'
        text += '<a id="branches"></a>\n\n## Branch guide\n\n'
        text += table(['Branch', 'Primary tasks', 'Full cards', 'Next step'], [
            (f'[{n["title"]}](#{anchor(n["id"])})', counts(n['id'])[2], counts(n['id'])[3], counts(n['id'])[5])
            for n in branch_nodes])
        text += ('Branch counts include descendants. Source links inside each branch below are direct mappings; '
                 'umbrella sources remain available in the domain directory above.\n\n')
        for n in branch_nodes:
            text += f'<a id="{anchor(n["id"])}"></a>\n\n### {n["title"]}\n\n{n["definition"]}\n\n'
            text += '**Boundary:** ' + n['boundary'] + '\n\n'
            text += '**Representative objects:** ' + ', '.join(n['objects']) + '.\n\n'
            direct = [s for s in source_ids if n['id'] in mappings[s]['domain_ids']]
            text += '**Direct source entries:** ' + (', '.join(source_link(s, '../sources.md') for s in direct) or 'None mapped at this branch; see the domain sources above') + '.\n\n'
            if n['id'] == root_id:
                text += '[View all primary tasks](#tasks) · [View cross-domain tasks](#cross-domain-tasks)\n\n'
            else:
                branch_primary, branch_cross, _ = selected(n['id'])
                text += '**Primary tasks in this branch and its descendants**\n\n'
                text += (bullets(problem_link(c, '../') for c in branch_primary) if branch_primary
                         else 'No primary candidate is recorded yet.\n\n')
                if branch_cross:
                    text += '**Additional cross-linked tasks**\n\n' + bullets(problem_link(c, '../') for c in branch_cross)
                text += '[Back to domain tasks](#tasks) · [Branch guide](#branches)\n\n'
            text += '**Related branches:** ' + (', '.join(node_link(i, '') for i in n['related_ids']) or 'See the branches in this domain') + '.\n\n'
            body = f'**Reference:** `{n["id"]}`. **Parent:** ' + (node_link(n['parent_id'], '') if n['parent_id'] else 'Top-level domain') + '.\n\n'
            body += '**Methods:** ' + ', '.join(m.replace('_', ' ').capitalize() for m in n['methods']) + '.\n\n'
            body += '**Evidence and checking options:** ' + ', '.join(label(v) for v in n['validation_options']) + '.\n\n'
            body += '**Scope decision:** ' + label(n['disposition']) + '. ' + n['rationale'] + '\n\n'
            body += '**Coverage note:** ' + n['coverage_note'] + '\n\n'
            body += '**Classification basis:** ' + ', '.join(source_link(s, '../sources.md') for s in n['classification_source_ids']) + '.\n\n'
            body += '**External mapping:** ' + label(n['external_mapping']['relation']) + '; exact equivalence is not claimed.\n'
            text += details('Methods, scope and classification basis', body)
        text += '<a id="cross-domain-tasks"></a>\n\n## Cross-domain tasks\n\n'
        text += 'These retain their primary record in another domain and are not added to this domain\'s primary count.\n\n'
        text += candidates_table(cross, '../') if cross else 'No additional cross-linked candidate is recorded yet.\n\n'
        text += '[Back to all domains](../README.md) · [Full outline](../taxonomy.md) · [Coverage gaps](../coverage.md)\n'
        out[f'docs/domains/{root_id.lower()}.md'] = text

    text = '# Candidate questions\n\n' + nav()
    text += (f'Use this index to compare targets and their evidence status. **{len(d["candidates"])} records include {len(cards)} with full cards.** '
             'Every candidate has a brief research profile; a candidate without a card still needs a detailed methods and verification assessment. '
             '[Browse by domain](README.md) or [compare the full cards](cards/README.md).\n\n')
    text += ('**Origin and current status are separate.** A literature-origin question may since have been resolved. '
             'A known result is established in the literature; this project has not reproduced it. '
             'Read the status basis before treating any record as open.\n\n')
    text += ' · '.join(f'[{label(k)}](#{k.replace("_", "-")})' for k in ('literature_open', 'curator_proposed', 'known_result_calibration')) + '\n\n'
    for kind in ('literature_open', 'curator_proposed', 'known_result_calibration'):
        selected_candidates = [c for c in d['candidates'] if c['kind'] == kind]
        text += f'<a id="{kind.replace("_", "-")}"></a>\n\n## {label(kind)}\n\n'
        text += table(['Task', 'Primary branch', 'Difficulty', 'Current status', 'Details'], [
            (f'[{c["title"]}](#{c["id"].lower()})', node_link(c['primary_domain_id']), label(profiles[c['id']]['difficulty']), label(c['status']),
             f'[Full card](cards/{c["id"]}.md)' if c['id'] in cards else 'Outline') for c in selected_candidates])
    text += '## Record details\n\nEach record has its own page with the statement, source locator, information gaps and assessment. Dates refer to scoped literature checks, not proof approval.\n\n'
    for c in d['candidates']:
        text += f'<a id="{c["id"].lower()}"></a>\n\n'
        body = c['statement'] + '\n\n'
        body += f'**Origin:** {label(c["kind"])}. **Curator-designed scope:** {"Yes" if c["curator_origin"] else "No"}.\n\n'
        body += f'**Current status:** {label(c["status"])}. **Last checked:** {c["last_checked"]}.\n\n'
        body += '**Status basis:** ' + c['status_basis'] + '\n\n'
        check = checks[c['id']]
        body += '**Statement check:** ' + label(check['statement_check']) + '. **Status check:** ' + label(check['status_check']) + '.\n\n'
        body += '**Source date and freshness:** ' + check['source_date_note'] + '\n\n'
        body += '**Scope limits:** ' + check['scope_note'] + '\n\n'
        body += '**Information still needed**\n\n' + (bullets(check['missing_information']) if check['missing_information'] else 'No additional gap is recorded here; the evidence limits and human-review status still apply.\n\n')
        body += '**Primary branch:** ' + node_link(c['primary_domain_id'], '../domains/') + '. **Related branches:** ' + (', '.join(node_link(i, '../domains/') for i in c['cross_domain_ids']) or 'None recorded') + '.\n\n'
        body += '**Sources:** ' + '; '.join(source_link(s, '../sources.md') for s in c['source_ids']) + '.\n\n**Exact locator:** ' + c['source_locator'] + '\n\n'
        p = profiles[c['id']]
        body += f'**Potential difficulty:** {label(p["difficulty"])}. {p["difficulty_basis"]}\n\n'
        body += '**Possible AI role:** ' + p['ai_role'] + '\n\n'
        body += f'**Verification burden:** {label(p["verification_burden"])}. {p["verification_basis"]}\n\n'
        body += '**Resource expectations:** ' + p['resource_expectation'] + '\n\n'
        body += f'**Assessment:** {p["assessment_date"]}; untested forecast. **Uncertainty:** {p["uncertainty"]}\n\n'
        if c['id'] in cards:
            body += f'[Read the full card](../cards/{c["id"]}.md). '
        elif c['status'] in {'resolved', 'disproved', 'known_result'}:
            body += '**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. '
        elif c['status'] in {'unverified', 'conflicting'}:
            body += '**Further work:** resolve the statement and status questions above before planning an attempt. '
        else:
            body += '**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. '
        body += '**Human review:** ' + label(c['human_review_status']) + '.\n\n'
        attempts, reviews = records_for_problem(d, c['id'])
        if attempts or reviews:
            body += '## Research records\n\n'
            body += bullets([f'[{a["id"]}](../attempts/{a["id"]}.md) — {label(a["status"])}. {a["outcome"]}' for a in attempts]
                            + [f'[{r["id"]}](../reviews/{r["id"]}.md) — {label(r["verdict"])}. Scope: {"; ".join(r["scope"])}' for r in reviews])
        body += problem_verification_section(d, c['id'], root=verification_root)
        if c['id'] in literature_checks:
            body += '## Literature checks\n\nThese are editorial evidence checks, not signed expert reviews or independent proof verification.\n\n'
            for review in sorted(literature_checks[c['id']], key=lambda r: r['checked_on'], reverse=True):
                body += f'### {review["checked_on"]}\n\n'
                body += f'**Coverage:** {label(review["coverage"])}. **Statement:** {label(review["statement_assessment"])}.\n\n'
                body += f'**Recorded status:** {label(review["status_before"])} → {label(review["status_after"])}.\n\n'
                body += review['conclusion'] + '\n\n**Search scope:** ' + review['search_scope'] + '\n\n'
                if review.get('previous_statement'):
                    body += details('Previous indexed wording', review['previous_statement'] + '\n\nThe current statement appears at the top of this page.')
                body += '**Inspected evidence**\n\n' + bullets(f'{source_link(e["source_id"], "../sources.md")} — {e["locator"].rstrip(". ")}. {e["finding"]}' for e in review['evidence'])
                body += '**Limits and remaining work**\n\n' + bullets(review['limitations'])
                if review['search_queries']:
                    body += details('Search queries', bullets(review['search_queries']))
        body += details('Structured records', '[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)\n')
        body += '[Back to the index](../candidates.md)\n'
        out[f'docs/candidates/{c["id"]}.md'] = (f'# {c["title"]}\n\n' + nav('../') + f'**{c["id"]} · {"Full card available" if c["id"] in cards else "Candidate outline"}.**\n\n' + contribution_links(c) + body)
        text += f'[{c["id"]} · {c["title"]}](candidates/{c["id"]}.md) — {label(c["status"])}.\n\n'
    out['docs/candidates.md'] = text

    text = '# Literature checks\n\n' + nav()
    text += ('Each check records what was read, which formulation was compared, and what remains uncertain. '
             'A statement-only check does not establish present-day open status. A reported resolution is attributed to its source; '
             'it does not mean this project has independently verified the proof. Human review remains separate.\n\n')
    latest = [max(rs, key=lambda r: r['checked_on']) for rs in literature_checks.values()]
    text += f'**{len(latest)} distinct questions · {len(d.get("literature_checks", []))} dated literature checks.** Latest-check counts appear below; earlier findings remain in each question\'s history.\n\n'
    text += table(['Latest check coverage', 'Questions'], [(label(v), sum(r['coverage'] == v for r in latest)) for v in ['statement_and_later_literature', 'statement_only', 'access_limited']])
    text += table(['Resulting evidence status', 'Questions'], [(label(v), sum(r['status_after'] == v for r in latest)) for v in sorted({r['status_after'] for r in latest})])
    changed = [r for r in latest if r['status_after'] in {'resolved', 'disproved'}]
    if changed:
        text += '## Resolutions and counterexamples to review\n\nThese entries retain their original identities. Follow each record for the exact result and its acceptance basis.\n\n'
        text += table(['Question', 'Status', 'Finding'], [(f'[{r["problem_id"]}](candidates/{r["problem_id"]}.md#literature-checks)', label(r['status_after']), r['conclusion']) for r in changed])
    corrected = sorted([r for r in d.get('literature_checks', []) if r['statement_assessment'] == 'corrected'], key=lambda r: (r['checked_on'], r['problem_id']), reverse=True)
    if corrected:
        text += '## Corrected statements\n\nRead the source comparison before reusing these formulations.\n\n'
        text += table(['Question', 'Date', 'Scope of correction'], [(f'[{r["problem_id"]}](candidates/{r["problem_id"]}.md#literature-checks)', r['checked_on'], r['conclusion']) for r in corrected])
    for root in roots:
        group = [c for c in d['candidates'] if c['id'] in literature_checks and root_of(c['primary_domain_id']) == root['id']]
        if not group:
            continue
        text += f'## {root["title"]}\n\n'
        rows = []
        for c in group:
            r = max(literature_checks[c['id']], key=lambda r: r['checked_on'])
            rows.append((f'[{c["id"]} · {c["title"]}](candidates/{c["id"]}.md#literature-checks)', r['checked_on'], label(r['coverage']), label(r['statement_assessment']), label(r['status_after'])))
        text += table(['Question and evidence', 'Date', 'Coverage', 'Statement', 'Status'], rows)
    text += '[Structured literature checks](../data/literature-checks.json) · [Evidence policy](evidence-policy.md)\n'
    out['docs/literature-checks.md'] = text

    pending = [c for c in d['candidates'] if checks[c['id']]['missing_information']]
    text = '# Questions awaiting checks\n\n' + nav()
    text += ('An identifiable question can be useful before every detail has been verified. This page lists the remaining work explicitly. '
             'A literature source that described a question as open years ago does not establish its present status. '
             'Records marked unverified are excluded from the open research selection.\n\n')
    unresolved_ids = {c['id'] for c in pending if c['status'] in {'unverified', 'conflicting'}
                      or checks[c['id']]['statement_check'] == 'needs_clarification'}
    text += (f'**{len(pending)} records have information gaps:** '
             f'[{len(unresolved_ids)} need statement or status clarification](#statement-or-status-clarification); '
             f'[{len(pending) - len(unresolved_ids)} have other review or planning needs](#further-review-and-planning). '
             'A missing resource estimate or planned certificate format does not by itself call a sourced result into question.\n\n')
    text += ('Choose one entry and one question you can check. Follow its **Suggest a correction** link to share '
             'what you found, the source passage and anything you could not verify. You do not need to complete every gap.\n\n')
    for title, clarify in [('Statement or status clarification', True), ('Further review and planning', False)]:
        text += f'## {title}\n\n'
        for root in roots:
            group = [c for c in pending if root_of(c['primary_domain_id']) == root['id']
                     and (c['id'] in unresolved_ids) == clarify]
            if not group: continue
            text += f'### {root["title"]}\n\n'
            text += table(['Question', 'Current status', 'Statement check', 'Information still needed'], [
                (problem_link(c), label(c['status']), label(checks[c['id']]['statement_check']), '<br>'.join(checks[c['id']]['missing_information'])) for c in group])
    text += '[Structured check records](../data/candidate-checks.json) · [Evidence policy](evidence-policy.md) · [Coverage](coverage.md)\n'
    out['docs/pending-checks.md'] = text

    research = [c for c in d['candidates'] if active_research(c)]
    research_cards = [cards[c['id']] for c in research if c['id'] in cards]
    outlines = [c for c in research if c['id'] not in cards]
    calibrations = sum(c['kind'] == 'known_result_calibration' for c in d['candidates'])
    text = '# Open research candidates\n\n' + nav()
    text += ('This selection contains literature-origin questions whose recorded evidence still supports an open status. '
             'Follow each entry for the exact statement and the limits of its status check. '
             'An open label is dated evidence, not a guarantee that no solution exists elsewhere.\n\n')
    text += (f'**{len(research)} research candidates · {len(research_cards)} full research cards · '
             f'{len(outlines)} outlines awaiting detailed assessment.** '
             f'The broader atlas also retains {calibrations} known-result calibration records, listed separately in the '
             '[complete index](candidates.md#known-result-calibration).\n\n')
    text += ('A bounded first milestone can be proposed by the curator within a literature problem. '
             'Such a milestone is identified in the card and is not automatically a separately established open problem. '
             'Easy witness checking does not imply easy discovery. Resource ceilings are stopping limits unless explicitly supported by measurements.\n\n')
    text += '## Detailed research tasks\n\n'
    text += ('These cards include methods, resources and validation plans. All AI assessments are forecasts until supported by recorded trials. '
             'Priority applies to the scoped approach in the card, not to solving the unrestricted problem quickly.\n\n')
    for priority in ('priority_trial', 'preparation_required', 'exploratory', 'unassessed'):
        group = [c for c in research_cards if c['ai_assessment']['priority'] == priority]
        if not group:
            continue
        text += '### ' + label(priority) + '\n\n'
        text += table(['Task', 'Why consider it', 'Verification', 'Status checked'], [
            (problem_link(c), c['ai_assessment']['rationale'],
             f'[Resources and checks](cards/{c["id"]}.md#verification)', c['last_checked']) for c in group])
    text += '## Further research outlines\n\n'
    text += ('These questions have source-backed statements, status notes and brief research profiles, but have not received a full methods and resource assessment. '
             'Inclusion here is not a recommendation to begin an unrestricted attempt.\n\n')
    text += table(['Question', 'Primary branch', 'Difficulty', 'Evidence status', 'Checked'], [
        (problem_link(c), node_link(c['primary_domain_id']), label(profiles[c['id']]['difficulty']), label(c['status']), c['last_checked']) for c in outlines])
    text += ('[Curator proposals](candidates.md#curator-proposed), unverified questions and reported resolutions remain in the '
             '[complete index](candidates.md). [Coverage notes](coverage.md) identify subjects still missing from this selection.\n')
    out['docs/research-candidates.md'] = text

    text = '# Browse by difficulty\n\n' + nav()
    text += ('Difficulty concerns the stated target, not the ease of stating a question. A finite instance can be difficult to discover and easy to check. '
             'A high or frontier rating does not rule out useful partial progress. These are dated, untested editorial forecasts; no model success rate is implied. '
             'See the [assessment rubric](ai-assessment.md) for definitions.\n\n')
    provisional = [c for c in d['candidates'] if c['kind']=='literature_open' and c['status'] in {'unverified','conflicting','conditional'}]
    text += table(['Rating', 'Meaning', 'Open-status evidence', 'Provisional or conflicting status'], [
        (label(level), meaning, sum(profiles[c['id']]['difficulty']==level for c in research),
         sum(profiles[c['id']]['difficulty']==level for c in provisional)) for level, meaning in [
            ('low','A routine or tightly bounded task under stated prerequisites.'),
            ('medium','Substantial but structured work; feasibility still needs testing.'),
            ('high','Specialist research with significant unresolved obstacles.'),
            ('frontier','A major long-standing target or comparably deep general problem.'),
            ('unknown','Insufficient task-specific evidence for a defensible rating.')]])
    text += '## Candidates with open-status evidence\n\n'
    for level in ['low','medium','high','frontier','unknown']:
        group=[c for c in research if profiles[c['id']]['difficulty']==level]
        if not group: continue
        text += f'### {label(level)}\n\n'
        text += table(['Question','Verification burden','Possible AI role'],[(problem_link(c),label(profiles[c['id']]['verification_burden']),profiles[c['id']]['ai_role']) for c in group])
    text += '## Candidates awaiting statement or status checks\n\n'
    text += ('These source-defined questions remain provisional or have conflicting evidence. Their difficulty ratings do not establish that they are still open. '
             'Follow the record for missing assumptions, dated source claims and recent resolution notices.\n\n')
    for level in ['low','medium','high','frontier','unknown']:
        group=[c for c in provisional if profiles[c['id']]['difficulty']==level]
        if not group: continue
        text += details(label(level) + f' · {len(group)} provisional candidates', table(
            ['Question','Primary branch','Evidence status','Verification burden'],
            [(problem_link(c), node_link(c['primary_domain_id']), label(c['status']),
              label(profiles[c['id']]['verification_burden'])) for c in group]))
    text += ('[All candidate profiles](candidates.md) also cover calibrations, curator proposals and reported resolutions. '
             '[Historical collections](landmark-problems.md) provide context without adding solved problems to the open selection.\n')
    out['docs/difficulty.md']=text

    text = '# Millennium and Hilbert problems\n\n' + nav()
    text += ('These historical collections provide a map of influential research directions. Their entries are not all unsolved, '
             'and a broad research program may have no single yes-or-no resolution. Collection entries are not added to the candidate count; '
             'links reuse canonical problem records. Unlinked open components still need a precise statement and specialist assessment.\n\n')
    text += ('A reported resolution awaiting scrutiny is kept distinct from an accepted solution. '
             'For the Millennium collection, numbering below is a navigation convention, not an official problem number.\n\n')
    candidates_by_id={c['id']:c for c in d['candidates']}
    def landmark_status(value):
        return 'Resolved' if value=='resolved' else label(value)
    for collection,title in [('millennium','Millennium Prize Problems'),('hilbert',"Hilbert's 23 problems")]:
        group=sorted([p for p in d['landmarks'] if p['collection']==collection],key=lambda p:p['number'])
        text += f'## {title}\n\n'
        text += table(['No.','Problem','Status','Research records'],[(p['number'],f'[{p["title"]}](#{p["id"].lower()})',landmark_status(p['status']),'; '.join(problem_link(candidates_by_id[i]) for i in p['problem_ids']) or 'Historical context; no separate candidate yet') for p in group])
        for p in group:
            text += f'<a id="{p["id"].lower()}"></a>\n\n'
            body=p['scope']+'\n\n**Status:** '+landmark_status(p['status'])+'. '+p['status_basis']+'\n\n'
            body+='**Sources:** '+'; '.join(source_link(s) for s in p['source_ids'])+'.\n\n**Locator:** '+p['source_locator']+'\n\n'
            body+='**Checked:** '+p['last_checked']+'.\n'
            text += details(f'{p["number"]}. {p["title"]}',body)
    text += '[Structured collection records](../data/landmark-problems.json) · [Source notes](quality-checks.md)\n'
    out['docs/landmark-problems.md']=text

    text = '# Source directory\n\n' + nav()
    text += ('Find literature by [domain](README.md), or scan the complete directory below. '
             '**Opened** means the recorded location was inspected, not every page or linked question. '
             'An access date is not confirmation that a problem remained open on that date.\n\n')
    for role in ('research_entry', 'classification'):
        text += '## ' + ('Research entry points' if role == 'research_entry' else 'Classification references') + '\n\n'
        text += source_table([s['id'] for s in d['sources'] if s['role'] == role])
    text += '## Source notes\n\nExpand a source to see its authors, exact location, supported claims, limitations and linked candidates.\n\n'
    for s in d['sources']:
        text += f'<a id="{s["id"].lower()}"></a>\n\n'
        body = f'[{s["title"]}]({s["url"]})\n\n'
        body += '**Authors / responsible organization:** ' + '; '.join(s['authors']) + '.\n\n'
        body += f'**Publication year:** {s["year"] or "Not verified"}. **Access / attempt date:** {s["accessed"]}.\n\n'
        body += f'**Type:** {label(s["source_type"])}. **Purpose:** {label(s["role"])}. **Inspection:** {label(s["verification"])}.\n\n'
        body += '**Inspected location:** ' + s['locator'] + '\n\n'
        body += '**Supports**\n\n' + bullets(s['supports']) + '**Limits:** ' + s['limitations'] + '\n\n'
        body += '**Related subjects:** ' + ', '.join(node_link(i) for i in mappings[s['id']]['domain_ids']) + '.\n\n'
        body += '**Connection to these subjects:** ' + mappings[s['id']]['mapping_basis'] + '\n\n'
        referencing = [c for c in d['candidates'] if s['id'] in c['source_ids']]
        body += '**Indexed tasks using this source**\n\n' + (bullets(problem_link(c) for c in referencing) if referencing else 'No candidate has been extracted from this entry yet.\n\n')
        body += '[Structured source data](../data/sources.json) · [Back to the directory](#source-directory)\n'
        text += details(f'{s["id"]} · {s["title"]}', body)
    alias_body = table(['Earlier identifier', 'Canonical record'], [(a, source_link(s)) for a, s in d['aliases'].items()])
    text += details('Source aliases retained for provenance', alias_body)
    out['docs/sources.md'] = text

    text = '# Coverage and next steps\n\n' + nav()
    text += f'**Collection updated: {d["project"]["as_of"]}.** {len(roots)} domains, {len(nodes)} nodes, {len(sources)} source records, {len(d["candidates"])} candidates and {len(cards)} full cards. These counts do not estimate the fraction of science covered.\n\n'
    text += ('Research sources are directly mapped to the selected node or its descendants; ancestor mappings are not inherited. '
             'Cards are included in candidate counts. Cross-linked tasks keep one primary record. Source counts include separately cited versions and cannot be summed across domains. Each source and question retains its own inspection date.\n\n')
    headers = ['Domain / branch', 'A: research sources', 'B + C: primary tasks', 'C: full cards', 'Next action']
    def coverage_row(n):
        cls, research, total, complete, cross, gap = counts(n['id'])
        return node_link(n['id']), research, total, complete, gap
    text += '## Main domains\n\n' + table(headers, [coverage_row(n) for n in roots])
    text += ('Cross-links, full-card views and historical collection positions do not add records. '
             'The status breakdown shows where further source checks are needed.\n\n')
    text += table(['Domain', 'Primary records', 'Open-status evidence', 'Unverified'], [
        (node_link(n['id']), len(selected(n['id'])[0]), sum(active_research(c) for c in selected(n['id'])[0]),
         sum(c['status']=='unverified' for c in selected(n['id'])[0])) for n in roots])
    text += 'See [questions awaiting checks](pending-checks.md) for evidence gaps.\n\n'
    text += '## Branch detail\n\nExpand a domain to inspect its branches without scrolling through the entire taxonomy.\n\n'
    for root in roots:
        branch_nodes = [n for n in d['nodes'] if n['parent_id'] and within(n['id'], root['id'])]
        body = table(headers, [coverage_row(n) for n in branch_nodes])
        body += table(['Node', 'Classification references', 'Cross-linked candidates'], [
            (node_link(n['id']), counts(n['id'])[0], counts(n['id'])[4]) for n in [root, *branch_nodes]])
        text += details(root['title'], body)
    text += '## Areas for further coverage\n\nThese notes identify the remaining work; broad portals do not fill a specialist candidate or card gap. The tables above give current coverage.\n\n'
    for item in d['coverage_notes']:
        note = item['note']
        summary = item['area']
        body = ''
        if isinstance(note, dict):
            for key, value in note.items():
                if key == 'source_ids':
                    body += '**Sources:** ' + ', '.join(source_link(s) for s in value) + '.\n\n'
                else:
                    body += f'**{label(key)}:** {value}\n\n'
        else:
            body = str(note) + '\n\n'
        text += details(summary, body)
    text += '## Bias and missing evidence\n\nCoverage favors accessible English-language sources and exact discrete certificates. Many continuous, empirical-model and foundational branches have no full card. No new-experiment or public-data task has received a full data/protocol audit. Novelty searches are scoped, not systematic reviews.\n\n'
    text += '[Review priorities](review-guide.md) · [How to contribute](../CONTRIBUTING.md)\n'
    out['docs/coverage.md'] = text

    candidate_by_id = {c['id']: c for c in d['candidates']}
    attempts = [(candidate_by_id[a['problem_id']], a) for a in d['attempts']]
    reviews = [(candidate_by_id[r['problem_id']], r) for r in d['reviews']]
    text = '# Research progress\n\n' + nav()
    text += ('This page follows research recorded in the atlas. Results from the literature remain credited '
             'in the problem cards; they are not results produced by this project.\n\n')
    text += f'**Recorded attempts: {len(attempts)} · Recorded reviews: {len(reviews)}.**\n\n'
    if not attempts and not reviews:
        text += ('No research attempts or reviews have been recorded. The [collection and editorial contributions](results.md) are available to explore. '
                 'There are no problem-solving results or measured model-performance figures to report.\n\n')
    if attempts:
        text += '## Attempts\n\n'
        text += table(['Problem', 'Attempt', 'Execution status', 'Reported outcome', 'Machine verification and scope'], [
            (problem_link(c), f'[{a["id"]}](attempts/{a["id"]}.md)', label(a['status']), a['outcome'], verification_summary(d, a['id'], root=verification_root))
            for c, a in attempts])
        text += 'Execution status does not establish correctness. Follow each record for artifacts, limitations and review scope.\n\n'
    if reviews:
        text += '## Reviews\n\n'
        text += table(['Problem', 'Review', 'Verdict', 'Scope'], [
            (problem_link(c), f'[{r["id"]}](reviews/{r["id"]}.md)', label(r['verdict']), '; '.join(r['scope']))
            for c, r in reviews])
    text += '## Contribute a research record\n\n'
    text += ('A useful record can describe an unsuccessful approach, a reproduction, a partial result or a candidate answer. '
             'State the exact claim, credit contributors, provide reproducible evidence, and identify what remains unchecked. '
             'Reviews should specify their scope and the version examined.\n\n')
    text += ('[Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml) · '
             '[Review a claim](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=scoped-review.yml) · '
             '[Contribution guide](../CONTRIBUTING.md)\n\n')
    text += ('[Problem cards](cards/README.md) identify possible starting points. '
             '[Coverage](coverage.md) tracks the collection of sources and questions separately from research progress. '
             '[Machine verification records](verifications.md) retain scoped certificate checks without changing human review or problem status.\n')
    out['docs/progress.md'] = text
    return out
