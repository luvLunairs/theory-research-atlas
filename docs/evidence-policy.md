# Evidence and problem status

## Levels of detail

| Level | Minimum content | Interpretation |
| --- | --- | --- |
| A: source directory | Research entry point, scope, provenance and limitations | A route into the literature; individual questions may not yet be indexed |
| B: candidate | Stable identity, identifiable statement, source locator, origin and provisional status | A problem requiring further assessment |
| C: full card | Precise scope, status evidence, background, resources and verification plan | A detailed research record, not a solution or expert endorsement |

Classification references organize the directory and are counted separately from research entry points. A source record must state which passages were inspected. An abstract or landing page supports only the claims it actually contains. Theorem claims need the theorem text or an authoritative statement of the result. An arXiv record establishes a public claim and its version history, not peer-review acceptance.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| `source_reports_open` | An identified source states openness at its own date; current resolution is not established |
| `open_after_scoped_check` | A source states openness and a recorded update search found no accepted resolution; the search is not exhaustive |
| `known_result` | The exact target is a documented result, normally used for calibration |
| `resolved` | A previously open candidate has a sourced resolution, with scope and acceptance basis recorded |
| `disproved` | A sourced counterexample or disproof addresses the exact statement |
| `conditional` | The result or status relies on explicitly recorded additional assumptions |
| `conflicting` | Material sources or claims disagree; both are retained |
| `unverified` | The statement, novelty, status or an announced resolution needs further checking |

Origin and status are separate. A curator proposal has `curator_origin: true` and `kind: curator_proposed`. It usually has `unverified` status: an open parent problem does not establish the novelty or openness of a proposed subproblem. A curator-designed task can instead have `known_result` status when it reproduces an established mathematical property. An older “open problems” title alone never establishes present openness.

Each candidate has a separate check record. `statement_check` says whether the source target is identifiable or still needs clarification; `status_check` says whether the evidence is a source report, a later-literature check, or an unfinished status check. These labels describe the work supporting the entry, not the truth of the conjecture. The [pending checks](pending-checks.md) collect missing assumptions, literature updates and assessment details in one place.

The complete index includes provisional research directions and historical questions whose present status is unknown. Its total is not a count of confirmed open problems or a measure of comprehensive coverage. Domain counts use each candidate's primary subject exactly once; cross-links, full cards and historical collection positions do not add extra problems.

## Check a status claim

Read the original or authoritative statement and identify its version. Search the exact name and close formulations alongside terms for resolutions, counterexamples, corrections and improved bounds. Inspect significant later results. Compare quantifiers, constants, dimensions, regularity conditions and model assumptions.

Record the queries, sources, findings, date and limits of the search. Distinguish a source's explicit claim from the absence of a result in a particular search. New evidence requires a fresh assessment of the affected record.

Dated [literature checks](literature-checks.md) preserve the statement assessment, before/after status, inspected passages and remaining limits. Their coverage is explicit: `statement_only` locates or corrects a question; `statement_and_later_literature` also compares later evidence within a recorded scope; `access_limited` records a substantive access barrier. None is a signed specialist review. A retained `unverified` label can therefore accompany useful, completed editorial work.

Keep a resolved or disproved question under its existing ID. Do not replace it silently with a stronger variant. A newly proposed variant needs its own provenance, novelty check and relation to the original. Broad empirical research programs require operational definitions before a single solved/open judgment is meaningful.

For a claimed solution, inspect the paper and relevant independent evaluation before treating acceptance as established. An institutional announcement may justify a status warning without establishing proof correctness. Credible updates must not be ignored to preserve a familiar open label.

## Keep four judgments separate

- **Difficulty:** estimated mathematical and implementation burden for the exact target.
- **Correctness:** whether an argument or certificate has been checked, and within what scope.
- **Novelty:** whether a claim adds to prior work; reproduction is deliberately non-novel.
- **Significance:** potential scientific value and the basis of that assessment.

These judgments do not collapse into model confidence. A short statement can be difficult; a long certificate may be easy to check but costly to discover.

## AI assistance and provenance

Apply the [AI policy](ai-contributions.md) to the [type of work](../CONTRIBUTING.md#requirements-by-work-type). Maintenance and source curation need a short assistance note; scientific contributions need detailed provenance and applicable submission screening. Cite every proof and idea. For research, supply relevant inputs, observable outputs and human changes once, or link the record for that exact version. The [citation guide](reuse-and-citation.md#acknowledge-ai-assistance) provides a format.

Model output is a contribution artifact, not an authoritative source for a theorem or an open-status claim. Inspect the original source and check that it supports the assertion. A recommended model does not supply evidence of correctness, novelty or likely success merely by generating an answer. An idea without a proof remains an idea, regardless of its origin.

Full-text submission screening is distinct from mathematical verification and independent review. Record checks actually performed and leave unexamined claims unresolved.

Optional [preliminary-screening stages](review-guide.md#preliminary-screening) describe the checks recorded for a particular result version. Recommended-AI contributor checks and a reported human preliminary pass can be displayed together, with their scope and limitations. These are procedural descriptions, not calibrated confidence levels or scientific verdicts. They do not change problem status, human-review status, submission eligibility or machine verification. Specialist academic review remains a separate, attributable scoped review; neither model identity nor preliminary screening establishes it.

## Match validation to the claim

Universal claims need a proof with explicit premises. Finite computational claims need exact arithmetic and independent checks; an exhaustive search also needs a complete instance generator, justified symmetry reductions and a defined search space.

Interval arithmetic or controlled error bounds can sometimes certify a numerical result. Ordinary floating-point tests remain numerical evidence. Statistical validation needs a specified design, model assumptions, leakage controls and uncertainty. Public data requires provenance and appropriate access rights.

Formal verification also requires agreement between the formal statement and the source problem, inspection of axioms and trusted code, and disclosure of admitted lemmas. For physical, biological and social models, formal validity and empirical support are separate questions. Mathematical consistency does not confirm a model of nature.

The [machine verification policy](machine-verification.md) permits correctness acceptance for exact certificates under a previously human-approved claim and checking procedure. A retained independent pass earns **Machine checked** for the exact certified claim; a contributor's self-report does not. This is separate from human review, novelty, rights and empirical support, and does not automatically change the candidate's status. Ordinary repository consistency checks are not certificate verification.

## Review and freshness

Recheck status when expanding a candidate into a full card, starting an attempt or preparing a publication. Revisit an entry when a relevant new claim appears. Active candidates may warrant quarterly checks; directory links can usually be reviewed annually. Historical sources remain useful, but their dates and limits must remain visible.

Preserve conflicting evidence, corrections and negative results. Scientific reviews should identify the version examined, the reviewer's scope and any unresolved objections. An unrelated later acceptance cannot dismiss an earlier objection. The [maintenance reference](maintaining.md#review-and-credit) explains explicit review replacements and separates current result reviews from reviews of plans or earlier versions. Local evidence files carry checksums; remote references identify the retained version and require separate inspection. Offline integrity checks do not inspect remote evidence or validate a proof.
