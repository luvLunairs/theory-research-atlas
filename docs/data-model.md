# Data model

Data-format version: **0.11.0**. Collection version: **0.1.0-dev**. These identify the data contract and the collection edition respectively. JSON records are authoritative; Markdown indexes and cards are generated. The schemas use JSON Schema Draft 2020-12. The local validator implements the subset used by these schemas and rejects unsupported keywords.

For reading, start at [Browse the atlas](README.md). Subject pages and backlinks are views of the same records, not additional sources or problems.

## Files

| File | Contract | Purpose |
| --- | --- | --- |
| `data/project.json` | `schemas/project.schema.json` | Collection identity, versions, date and research counts |
| `data/taxonomy.json` | Array of `taxonomy-node.schema.json` | Stable hierarchy, definitions and cross-links |
| `data/sources.json` | Array of `source.schema.json` | Bibliography, evidence scope and access limits |
| `data/source-map.json` | Array of `source-map.schema.json` | Source-to-subject associations |
| `data/source-aliases.json` | Alias-to-canonical-ID object | References retained when duplicate sources are merged |
| `data/candidates.json` | Array of `candidate.schema.json` | Problem identity, statement, origin and status |
| `data/research-profiles.json` | Array of `research-profile.schema.json` | One dated difficulty, AI-role, resource and verification profile per candidate |
| `data/candidate-checks.json` | Array of `candidate-check.schema.json` | One statement check, status-check scope, source-date note and list of information gaps per candidate |
| `data/literature-checks.json` | Array of `literature-check.schema.json` | Dated editorial checks with search scope, inspected evidence, conclusions and limitations |
| `data/landmark-problems.json` | Array of `landmark-problem.schema.json` | Seven Millennium and 23 Hilbert collection entries, linked to canonical candidates |
| `data/cards/Q-*.json` | `card.schema.json` | Detailed records extending matching candidates |
| `data/attempts/ATT-*.json` | `attempt.schema.json` | One research plan or attempt per file, linked to any candidate |
| `data/reviews/REV-*.json` | `review.schema.json` | One scoped review per file, linked to a candidate and, when applicable, an attempt |
| `data/verification-specs/VSPEC-*.json` | `verification-spec.schema.json` | Fixed claims, checking protocols and version-bound human approval |
| `data/verifications/VER-*.json` | `verification.schema.json` | Actual certificate-checking runs, evidence and derived eligibility |
| `data/vocabularies.json` | Controlled lists | Methods, evidence, status and assessment labels |
| `data/scope-decisions.json` | Array of `scope-decision.schema.json` | Inclusion, deferral and exclusion rules |
| `data/coverage-notes.json` | Observations by subject area | Qualitative gaps alongside computed coverage counts |

Core schemas reject unknown fields. Source aliases, coverage notes and vocabulary containers receive integrity checks. A data-model change needs an intentional version update and migration; do not relax constraints merely to make an invalid record pass.

## Collection metadata

`data/project.json` identifies the collection and its recorded research activity.

| Field | Meaning |
| --- | --- |
| `schema_version` | Version of the data format and validation contract |
| `collection_version` | Edition of the collection |
| `title` | Project title used by the reading pages |
| `as_of` | Latest date covered by the collection's metadata |
| `research_attempts_run` | Number of attempts with recorded execution, including unfinished and unsuccessful work |
| `model_evaluations_run` | Number of executed attempts whose purpose is model evaluation |

The counts are derived from attempt records and checked for consistency. They measure recorded activity, not the number of solved problems or verified results.

## Candidate identity and provenance

| Field group | Meaning |
| --- | --- |
| Identity | `id`, `title`, `duplicate_key`; ID remains stable after renaming or reclassification |
| Placement | `primary_domain_id`, `cross_domain_ids`; `domain` and `cross_domains` provide readable labels |
| Origin | `kind` distinguishes literature-open problems, curator proposals and known-result calibrations; `curator_origin` identifies curator-designed tasks |
| Statement | `statement`, `source_locator`, `source_ids` |
| Status | `status`, `status_basis`, `last_checked` |
| Detail level | `curation_level` is B or C; `proposed_card` must match the presence of a card |
| Review | `human_review_status` records the actual review state |

`literature_open` describes a problem's origin, not necessarily its present status. A historical question may be `resolved`. A `curator_proposed` task may have `known_result` status when its mathematical property is established and the proposal concerns an artifact or reproduction.

A card uses the candidate's ID; set `curation_level: C` and `proposed_card: true` in both records. Shared fields must match exactly. Relations have a type, an existing target ID and an explanation; an equivalence claim needs its assumptions. Use cross-links for secondary subjects. Never delete or reuse a duplicate ID silently: preserve it through a documented redirect or tombstone migration.

Research profiles are keyed by `problem_id`. Their difficulty and verification labels require reasons; `ai_role` states the assumed capability and possible contribution. `resource_expectation` is qualitative unless a justified estimate is explicitly given. Profile coverage is complete, but an `unknown` rating identifies an assessment gap. A profile cannot substitute for the full card's assumptions, methods and checking plan.

Historical collection entries use `problem_ids` to link existing questions. A problem shared by two collections keeps one candidate ID. Collection status can be open, resolved, partly open, formulation dependent, a broad program, independent of specified axioms, or a claimed resolution under review. Historical entries do not contribute to candidate or open-problem counts. All 30 collection positions must be present exactly once.

## Complete card fields

Every candidate also has a check record. `statement_check` distinguishes a located statement from a direction that still needs precise assumptions. `status_check` distinguishes a source report, a scoped later-literature check and an unperformed status search. The source-date note prevents an access date from being mistaken for recent evidence. `missing_information` lists concrete unresolved work; `scope_note` identifies formulation and empirical limits. A missing status search cannot support an open label. The [questions awaiting checks](pending-checks.md) view makes these gaps searchable without promoting incomplete entries to full cards.

| Content | Fields |
| --- | --- |
| Accessible and precise framing | `plain_summary`, inherited `statement`, `assumptions`, `scope`, `target`, `success_criteria` |
| Sources and attribution | `source_ids` link to authors, dates and URLs; `source_locator` and `attribution` give specific credit and locations |
| Status and freshness | Status fields and `status_search.queries`, `checked_sources`, `result`, `limitations` |
| Background and prior work | `known_results`, `prerequisites`, `known_attempts` |
| Value and relationships | `significance`, `relations` |
| Independent resource requirements | `requirements.experiment`, `data`, `compute`, `theoretical_assumptions` |
| Formal and empirical claims | `epistemic_layers.formal_validity`, `empirical_support` |
| AI suitability | `ai_assessment`: priority, rationale, eight explained dimensions, evidence level, evidence references, uncertainty, date and capability scope |
| Separate scientific judgments | `judgments.difficulty`, `correctness`, `novelty`, `significance` |
| Methods | `methods`, `method_tags` |
| Obstacles and verification | `obstacles`, `validation.steps`, `human_review_difficulty`, `statement_alignment`, `validation_tags` |
| Experimental dependence | `experimental_dependency`, supplemented by the prose requirements |
| Unresolved questions | `unresolved_checks` |
| Material revisions | `revision_history`; attempts and reviews are separate records linked by `problem_id` |

The absence of attempt or review files for a problem means none are recorded; it does not represent a successful zero-cost attempt or an implicit review. An empty card revision history means no substantive revision is recorded.

## Attempt contract

[attempt.schema.json](../schemas/attempt.schema.json) defines:

- attempt ID, parent problem ID, exact target, statement version and contributors with their roles;
- explicit `assumptions`, `success_criteria`, `verification_plan`, and separate experiment, data and compute `requirements`;
- purpose: research, method calibration or model evaluation;
- model provider, name, version and capability profile;
- start/end timestamps and run status;
- operating system, tools, package versions, code revision and randomness seeds;
- research inputs and reproducibility artifacts, including code and relevant outputs;
- an `artifact_manifest` identifying each artifact reference, retained version and checksum;
- planned estimates or limits and actual use, with units, currency and a stated basis;
- human assistance, stopping conditions, candidate-answer artifacts, classified outcomes and limitations;
- related review IDs and material revisions.

Store each attempt in `data/attempts/<attempt-id>.json`. Any level B or C candidate can receive an attempt; a full card is not required. The attempt itself must state a precise target, assumptions, success criteria, verification plan and resource requirements, including any narrower scope than its parent problem. `statement_version` identifies a retained snapshot, checksum or repository revision; a mutable title is insufficient. An attempt may be planned, running, completed, stopped or failed. Execution status is separate from `outcome_kind`: an unsuccessful attempt can be completed.

Unknown measurements remain null with an explanation. Planned records have no execution timestamps or measured use. A started record needs a start time; terminal records also need an end time and an observable process artifact. Reported reproductions, results, corrections and retractions need their supporting artifacts. Monetary amounts require a currency. Examples and software-test fixtures never belong in actual research records.

Artifact manifests use `reference`, `version` and `sha256` to describe the evidence behind links. Local artifact references must resolve to existing files and match their recorded checksums. External references need a description of the retained version and may use `sha256: null` when a checksum is unavailable. The offline validator does not fetch remote contents or establish that an external URL still serves the examined bytes. Keep a stable copy or an independently retrievable version when the evidence is necessary to evaluate a claim.

Incomplete drafts belong in `work/`. Fields beginning with `TODO:` cannot enter the research collection. An accepted plan may still contain explicitly unknown measurements, provided its target, intended checks and limitations are clear.

Project counts are checked against the records. `research_attempts_run` counts started attempts of all purposes, including unfinished and unsuccessful work; `model_evaluations_run` counts the subset whose purpose is `model_evaluation`. Planned work contributes to neither count.

The brief candidate profiles remain forecasts. A full card's AI assessment can cite `public_attempt_evidence` using inspected source IDs and described public attempts, or `project_measured` using terminal local attempt IDs with model identifiers and process artifacts. Put those references in `evidence_refs`; leave it empty for `untested_forecast`. Evidence links establish traceability, not scientific correctness or a general success rate.

## Preliminary-screening contract

An attempt may include `preliminary_screening`; omission means no structured preliminary screening is recorded. This optional object is separate from `review_ids`, `human_review_status` and machine verification. It contains:

- `recorded_by`, `date`, nonempty `scope` and `limitations`, plus nonempty `evidence_artifacts`. Each evidence reference must already be a `process_artifacts` entry with a SHA-256 in the attempt's `artifact_manifest`. The evidence identifies the humans, actual AI configurations, roles, checks and any unreported details; these declarations require maintainer assessment.
- `ai_basis`: `recommended_only`, `other_or_unknown` or `no_ai`; `ai_check_status`: `completed` or `not_recorded`; `human_preliminary_status`: `passed`, `changes_requested` or `not_recorded`. Recommended-only means all substantive AI contributors meet the cited policy, including delegated work and any documented maintainer recognition. The validator does not infer eligibility from a model name. `no_ai` cannot accompany completed AI checks.
- `target_digest`, computed by `screening_target_digest` in [research_records.py](../scripts/research_records.py). It hashes the canonical JSON object containing exactly `problem_id`, `statement_version`, `target`, `assumptions`, `success_criteria`, `outcome_kind`, `outcome`, `model`, `environment` and `candidate_answer_artifacts`, using the SHA-256 serialization convention below. It excludes the screening metadata and therefore does not hash itself.
- Nonempty `result_artifacts`, containing the examined `reference`, `version` and nonnull `sha256` for every candidate-answer artifact, every `evidence_artifacts` reference and every supporting artifact within screening scope. For a current stage, these must exactly match the current artifact manifest. This also binds the preliminary-screening note itself; do not put that note's own digest inside the note. List relevant proof dependencies explicitly. A bound package manifest is useful evidence, but this feature does not recursively inspect files named inside that manifest.

An executed attempt with result artifacts is required. Changed target fields, new unbound candidate artifacts, or changed/missing bound result or supporting manifest entries yield an earlier-version stage. Retained older bindings are allowed as history. Invalid evidence associations fail validation; missing or altered local bytes prevent a current positive display. Remote hashes remain declarations and are not fetched or authenticated. A report requesting changes never yields a positive preliminary stage. The renderer displays the declaration, scope, limitations and evidence separately from actual scoped reviews; no numeric confidence or academic-review tier is inferred. See the [screening vocabulary](review-guide.md#preliminary-screening).

Changing screening metadata changes the ordinary `attempt_digest`, conservatively making existing attempt reviews earlier-version reviews. It does not alter the existing review or verification contracts. Keep previous screening reports and explain replacements in `revision_history`.

## Review contract

Editorial literature checks are stored separately in `data/literature-checks.json`. Each records its date, problem ID, statement assessment, before/after status, coverage, actual search queries, inspected source passages, conclusion and limitations. A correction preserves the previous indexed wording in `previous_statement`. Multiple checks accumulate over time; combine evidence from the same date into one record. Successive before/after statuses must agree, and the latest check must match the candidate's status and not postdate its check date. A resolution or disproof requires a later-literature check with inspected evidence. These records do not populate the signed human-review collection.

[review.schema.json](../schemas/review.schema.json) defines reviewer identity and role, date, problem/attempt IDs, `reviewed_version`, target and attempt digests, review type, exact scope, exclusions, verdict, comments, evidence, an `artifact_manifest`, conflicts of interest, revisions and explicitly superseded reviews. Store each review in `data/reviews/<review-id>.json`. Any level B or C candidate can receive a review. A `problem_entry` review has `attempt_id: null` and `attempt_digest: null`. A `planned_method` or `research_record` review links to an attempt, records its `attempt_digest`, and is linked back through the attempt's `review_ids`. A review of a plan may predate execution; a review of research evidence cannot. Completed reviews need evidence references and the corresponding manifest entries.

The `statement_digest` identifies the reviewed problem target and hypotheses. The [catalog's JSON output](catalog.md) supplies the current digest for every candidate, using its full card when available. It is SHA-256 of the UTF-8 JSON object containing the available fields among `statement`, `assumptions`, `scope`, `target` and `success_criteria`, with sorted keys, no ASCII escaping, and separators `,` and `:` without surrounding whitespace. A level B candidate currently contributes only its `statement`; the absence of fuller assumptions does not mean that they have been checked. Adding a full card changes the digest when it adds these fields.

The `attempt_digest` uses the same serialization and hash, applied to all attempt fields except `review_ids` and `revision_history`. Excluding those fields avoids circular review references. Changes to the attempt's target, assumptions, execution record, outcome, artifact references or manifest change its digest. A digest binds the recorded fields; artifact checksums and `reviewed_version` identify the retained evidence to which those fields refer.

An accepted or changes-requested problem-entry label needs a corresponding `problem_entry` review of the current target. Applicable, unsuperseded conclusions must support the label; changing the statement, hypotheses or success criteria invalidates an inherited label. An attempt review does not endorse the whole problem entry. Result views use completed `research_record` reviews matching the current attempt digest; a review of an earlier plan or superseded result cannot support the current result's label. Acceptance always remains limited to the recorded scope. Editorial literature checks remain separate at either curation level.

`supersedes` lists review IDs that the reviewer explicitly replaces. A replacement must concern the same reviewer, scope, review type, problem and attempt. A later review does not silently remove another reviewer's objection. Keep independent conclusions visible and resolve conflicting findings through further evidence and attributable review.

A person may check code without assessing mathematics or novelty. Record only the review that actually occurred, and retain unresolved objections. Source-specific limitations are documented in [source notes](quality-checks.md).

## Machine verification contract

Machine verification uses two separate contracts: [verification-spec.schema.json](../schemas/verification-spec.schema.json) for the fixed claim and checking procedure, and [verification.schema.json](../schemas/verification.schema.json) for each actual execution. Their [policy](machine-verification.md) defines when a certificate may establish correctness. They do not populate human review records or change problem status.

| Record | Required content |
| --- | --- |
| `VSPEC-...` specification | Problem ID and `statement_digest`; method, exact `claim` and `scope`; target and definitions, checker sources/version, environment and protocol artifacts; arithmetic and axiom policy; human approval and retained evidence |
| `VER-...` execution | Specification ID and digest; problem/attempt IDs and `attempt_digest`; actual timestamp, runner identity/provenance and command arguments; submitted result, certificate and logs; named checks, observed axioms/native evaluation, outcome and limitations |

Every artifact used in a role must also appear in `evidence_artifacts` with one matching `artifact_manifest` entry. Run `result_artifacts` must identify the linked attempt's candidate-answer artifacts with the same retained version and checksum when the attempt digest is current. Certificate and log files have distinct roles even if an exact witness is itself the result and certificate. Failed or interrupted runs may have no certificate; they still need their submitted result and execution evidence.

A specification's `approval` is separate from its scientific content. An approved decision names a human reviewer, role, date, examined specification digest and evidence, covering `target_correspondence`, `checker_protocol` and `trust_basis`. Pending approval may leave the reviewer and date null. Rejected or withdrawn decisions retain their attribution and evidence. Repository checks cannot authenticate these declarations; maintainer intake must establish that the review and independent execution occurred.

`specification_digest` uses the same canonical JSON encoding and SHA-256 convention as the other digests. It excludes `approval` and `revision_history`, and excludes references and manifest entries used only as approval evidence, avoiding a circular hash. An artifact serving any target, checker, environment or protocol role always remains included. Changing a scientific field or its retained artifact metadata changes the digest. Preserve the previous specification and evidence when introducing a revised protocol.

Every run requires `target_match`, `environment_match`, `protocol_match`, `independent_rerun` and `certificate_check` to pass before qualifying. Method-specific checks are:

| Method | Additional successful checks |
| --- | --- |
| `exact_counterexample` | `domain_membership`, `negated_conclusion` |
| `lean_proof` | `kernel_check`, `axiom_audit` |
| `finite_construction` | `constraints_check` |
| `finite_exhaustion` | `enumeration_complete` |

Each named check cites retained evidence and explains its findings. The protocol supplies the detailed acceptance criteria; these names are not substitutes for performing the checks. A passing outcome cannot contain a failed or inconclusive check.

The displayed `verification_state` is derived, never stored as an asserted approval field:

| State | Interpretation |
| --- | --- |
| `machine_checked` | Passed an approved, current specification in a recorded project or independent rerun, with required checks, permitted trust assumptions and local evidence whose hashes match |
| `reported_pass` | A pass was reported, but independent execution, evidence or strict eligibility requirements are incomplete |
| `pending_approval` | The specification is not currently approved |
| `stale` | The problem, attempt, specification or approval digest no longer matches |
| `failed`, `inconclusive`, `error` | The recorded check did not pass; the outcome remains visible |
| `conflicting` | Runs of the same bound result and certificate under the same specification disagree; a newer timestamp does not choose a winner |
| `invalid` | The records or retained artifacts fail integrity checks; repair the record before relying on it |

Only the approved claim and scope receive the `machine_checked` label. It does not endorse every claim in the attempt. Changed target statements, attempts, specification content or withdrawn approval prevent a current label. Contributor-only logs and remote artifact declarations cannot establish it. Unresolved conflicting runs remain visible; retain the evidence and obtain an attributable resolution and any necessary protocol revision before seeking a new qualifying run.

The strict Lean route permits only the declared subset of `propext`, `Classical.choice` and `Quot.sound`, with no admitted proofs or native-evaluation trust extension. Exact or approved interval arithmetic is required for the other methods. Local repository validation checks the contract and retained bytes; it does not execute a scientific checker or certify the truth of a submitted log.

Use the draft helper described in [research records](maintaining.md#record-machine-verification). Drafts deliberately leave missing execution and approval information unset and cannot enter the canonical collection until complete. A specification or verification run does not count as a new research attempt or model evaluation; those counts still follow the linked attempt records.

## Editing and rendering

1. Edit the relevant JSON records and source mappings.
2. Synchronize candidate/card fields and record material scientific revisions.
3. Run `python scripts/check.py --render` to validate data, refresh reading pages and run all checks. The separate `python scripts/render.py` and `python scripts/check.py` commands remain available.

The renderer coordinates index, card, attempt, review, verification and results views; `--check` detects stale files without writing them. Each check can also run separately as defined in [check.py](../scripts/check.py). Use UTF-8 and ISO dates. Preserve null for unverified bibliographic dates. Access dates refer to actual inspection of the relevant source content, not a successful automated link check.

See [Contributing](../CONTRIBUTING.md) for the editing workflow.

