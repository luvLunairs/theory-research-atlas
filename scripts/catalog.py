"""Search the local atlas and export matching records without network access."""
import argparse
import datetime as dt
import json
import shlex
import sys

from validate import load_dataset
from research_records import statement_digest, records_for_problem
from machine_verification import specification_digest, verification_state, validate_machine_records


def descendant(node_id, ancestor, nodes):
    seen = set()
    while node_id in nodes and node_id not in seen:
        if node_id == ancestor:
            return True
        seen.add(node_id)
        node_id = nodes[node_id]['parent_id']
    return False


def records(dataset):
    errors = validate_machine_records(dataset)
    if errors:
        raise ValueError('Invalid machine-verification records: ' + '; '.join(errors))
    profiles = {p['problem_id']: p for p in dataset['profiles']}
    checks = {p['problem_id']: p for p in dataset['checks']}
    cards = {p['id']: p for p in dataset['cards']}
    sources = {s['id']: s for s in dataset['sources']}
    history = {}
    for item in dataset['literature_checks']:
        history.setdefault(item['problem_id'], []).append(item)
    result = []
    for candidate in dataset['candidates']:
        pid = candidate['id']
        literature = sorted(history.get(pid, []), key=lambda x: (x['checked_on'], x['id']), reverse=True)
        cited = set(candidate['source_ids'])
        for check in literature:
            cited.update(e['source_id'] for e in check['evidence'])
        result.append({
            'candidate': candidate, 'profile': profiles[pid], 'check': checks[pid],
            'literature_checks': literature,
            'sources': [sources[s] for s in sorted(cited)],
            'card': cards.get(pid),
            'statement_digest': statement_digest(cards.get(pid, candidate)),
            'attempts': records_for_problem(dataset, pid)[0],
            'reviews': records_for_problem(dataset, pid)[1],
            'verification_specs': [dict(s, current_specification_digest=specification_digest(s))
                                   for s in dataset.get('verification_specs', []) if s['problem_id'] == pid],
            'verifications': [dict(v, verification_state=verification_state(dataset, v))
                              for v in dataset.get('verifications', []) if v['problem_id'] == pid],
            'reading_path': f'docs/{"cards" if pid in cards else "candidates"}/{pid}.md',
        })
    return result


def select(dataset, *, query='', domain=None, include_cross_links=False,
           statuses=(), difficulties=(), kind=None, level=None,
           statement_check=None, coverage=None, checked_before=None,
           research=False, problem_id=None):
    """Combine filters with AND; repeated status/difficulty values use OR."""
    nodes = {n['id']: n for n in dataset['nodes']}
    lexer = shlex.shlex(query, posix=True)
    lexer.whitespace_split = True
    lexer.quotes = '"'
    lexer.commenters = ''
    lexer.escape = ''
    terms = [t.casefold() for t in lexer]
    selected = []
    for row in records(dataset):
        c, p = row['candidate'], row['profile']
        if problem_id and c['id'] != problem_id:
            continue
        placements = [c['primary_domain_id']]
        if include_cross_links:
            placements += c['cross_domain_ids']
        if domain and not any(descendant(x, domain, nodes) for x in placements):
            continue
        if statuses and c['status'] not in statuses:
            continue
        if difficulties and p['difficulty'] not in difficulties:
            continue
        if kind and c['kind'] != kind:
            continue
        if level and c['curation_level'] != level:
            continue
        if statement_check and row['check']['statement_check'] != statement_check:
            continue
        latest = row['literature_checks'][0] if row['literature_checks'] else None
        if coverage and (latest['coverage'] if latest else 'no_record') != coverage:
            continue
        if checked_before and c['last_checked'] >= checked_before:
            continue
        if research and not (c['kind'] == 'literature_open' and c['status'] in
                             {'source_reports_open', 'open_after_scoped_check'}):
            continue
        searchable = json.dumps(row, ensure_ascii=False).casefold()
        if not all(t in searchable for t in terms):
            continue
        selected.append(row)
    return sorted(selected, key=lambda r: r['candidate']['id'])


def iso_date(value):
    try:
        date = dt.date.fromisoformat(value)
        if date.isoformat() != value:
            raise ValueError
        return value
    except ValueError:
        raise argparse.ArgumentTypeError('Use an ISO date: YYYY-MM-DD.')


def markdown(rows):
    def cell(value):
        return value.replace('|', '\\|').replace('\n', ' ')
    lines = ['| ID | Question | Domain | Status | Difficulty | Checked |',
             '| --- | --- | --- | --- | --- | --- |']
    for r in rows:
        c = r['candidate']
        lines.append('| ' + ' | '.join(cell(v) for v in [c['id'], c['title'],
            c['primary_domain_id'], c['status'], r['profile']['difficulty'], c['last_checked']]) + ' |')
    return '\n'.join(lines)


def main(argv=None):
    dataset = load_dataset()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='', help='Words or quoted phrases; all must match')
    parser.add_argument('--id', dest='problem_id', help='Exact stable problem ID')
    parser.add_argument('--domain', metavar='ID', choices=[n['id'] for n in dataset['nodes']], help='Branch and descendants; IDs: --list-domains')
    parser.add_argument('--include-cross-links', action='store_true', help='Also match secondary subject placements')
    parser.add_argument('--status', dest='statuses', action='append', default=[], choices=dataset['vocabularies']['status'])
    parser.add_argument('--difficulty', dest='difficulties', action='append', default=[], choices=sorted({p['difficulty'] for p in dataset['profiles']}))
    parser.add_argument('--kind', choices=sorted({c['kind'] for c in dataset['candidates']}))
    parser.add_argument('--level', choices=['B', 'C'])
    parser.add_argument('--statement-check', choices=sorted({c['statement_check'] for c in dataset['checks']}))
    parser.add_argument('--coverage', choices=['statement_only', 'statement_and_later_literature', 'access_limited', 'no_record'])
    parser.add_argument('--checked-before', type=iso_date, help='Candidate check date strictly before YYYY-MM-DD')
    parser.add_argument('--research', action='store_true', help='Literature-origin entries with recorded open evidence; not a readiness rating')
    parser.add_argument('--list-domains', action='store_true', help='List subject IDs and titles, then exit')
    parser.add_argument('--format', choices=['text', 'json', 'markdown'], default='text')
    parser.add_argument('--limit', type=int, help='Show at most this many matches; total count remains visible')
    args = parser.parse_args(argv)
    if args.limit is not None and args.limit < 1:
        parser.error('--limit must be positive')
    if args.problem_id and args.problem_id not in {c['id'] for c in dataset['candidates']}:
        parser.error(f'Unknown problem ID: {args.problem_id}')
    if args.list_domains:
        print(json.dumps(dataset['nodes'], ensure_ascii=False, indent=2) if args.format == 'json'
              else '\n'.join(f'{n["id"]:20} {n["title"]}' for n in dataset['nodes']))
        return 0
    filters = {k: v for k, v in vars(args).items() if k not in {'format', 'limit', 'list_domains'}}
    try:
        matches = select(dataset, **filters)
    except ValueError as exc:
        parser.error(str(exc))
    shown = matches[:args.limit] if args.limit else matches
    if args.format == 'json':
        print(json.dumps({'as_of': dataset['project']['as_of'], 'filters': filters,
                         'total_matches': len(matches), 'returned': len(shown), 'records': shown},
                         ensure_ascii=False, indent=2))
    else:
        print(f'{len(matches)} matches; showing {len(shown)}. Collection date: {dataset["project"]["as_of"]}.')
        print('Status is dated evidence. Read the statement, sources and limits before selecting a task.\n')
        if args.format == 'markdown':
            print(markdown(shown))
        else:
            for row in shown:
                c = row['candidate']
                print(f'{c["id"]}  {c["title"]}\n'
                      f'  {c["primary_domain_id"]} | {c["status"]} | difficulty: {row["profile"]["difficulty"]} | {c["last_checked"]}\n'
                      f'  {row["reading_path"]}\n')
    return 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
