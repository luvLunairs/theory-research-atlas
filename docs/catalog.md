# Search the collection

The [subject directory](README.md) and [difficulty index](difficulty.md) provide reading paths through the atlas. For a more specific selection, the local catalog combines text search with subject, evidence and difficulty filters. It reads the JSON records, makes no network requests and does not modify files.

Run the commands below from the project directory with Python 3.10 or later. No additional packages are required.

## Find a question

```powershell
python scripts/catalog.py "covering code"
python scripts/catalog.py --id Q-CODE-201 --format json
python scripts/catalog.py --list-domains
```

Search is case-insensitive. All words must match somewhere in the record, including its statement, source metadata, information gaps or literature history. A match in an older check may concern a previous formulation; read the current statement before using it. To search a phrase, put double quotes inside the query, for example `'"sample compression"'`.

The default output lists every match with a reading path. `--format json` includes complete candidate, profile, check, source and literature records, plus the full card where one exists and any linked attempts, reviews, verification specifications and verification runs. Every entry has a `statement_digest`: it covers the candidate statement, or the statement, assumptions, scope, target and success criteria of a full card. Specifications include their current digest; runs include a derived `verification_state`. These export-only fields must not be copied into canonical JSON files. Stable IDs provide the join keys for other tools. See [research records](maintaining.md) for versioned evidence and [machine verification](machine-verification.md) for the scope of its labels.

## Narrow the selection

```powershell
python scripts/catalog.py --domain CS --research --level C
python scripts/catalog.py --domain MATH.COMB --include-cross-links
python scripts/catalog.py --status unverified --statement-check needs_clarification
python scripts/catalog.py --coverage access_limited
python scripts/catalog.py --checked-before 2026-10-14 --limit 20
```

| Filter | Meaning |
| --- | --- |
| `--domain ID` | Primary placement in this subject or any descendant |
| `--include-cross-links` | Also include secondary placements; each problem appears once |
| `--research` | Literature-origin questions with `source_reports_open` or `open_after_scoped_check` status |
| `--status VALUE` | Current recorded evidence status; repeat for alternatives |
| `--difficulty VALUE` | Estimated difficulty; repeat for alternatives |
| `--level B` or `--level C` | Candidate outline or full card |
| `--statement-check VALUE` | Current assessment of statement completeness |
| `--coverage VALUE` | Coverage of the latest dated literature check; `no_record` selects entries without one |
| `--checked-before DATE` | Candidate check date strictly before the supplied date |
| `--limit N` | Limit displayed records while retaining the total match count |

Different filters are combined with AND. Repeated statuses or difficulties are combined with OR. Use `--help` for the accepted values. Dates describe recorded checks, not a guarantee that all later literature has been considered. A source's open label and a manageable verification burden do not establish that a problem is easy to solve.

## Export a selection

```powershell
New-Item -ItemType Directory -Force work | Out-Null
python scripts/catalog.py --domain INFO --format json | Set-Content -Encoding utf8 work/information-theory.json
python scripts/catalog.py --status resolved --status disproved --format markdown
```

JSON output records the collection date, filters, total matches and number returned. Keep those fields with a shared selection so that omissions and filtering remain visible. Markdown output is a compact comparison table. Preserve the record IDs, source attribution and collection citation when sharing an extract.

[Browse subjects](README.md) · [Evidence labels](evidence-policy.md) · [Contributing](../CONTRIBUTING.md)
