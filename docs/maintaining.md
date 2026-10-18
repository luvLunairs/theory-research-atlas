# Maintaining the collection

This reference is for maintainers and contributors who edit structured records. For an ordinary suggestion or research update, use [Contributing](../CONTRIBUTING.md); no local tools or JSON are required. Consult the sections below only when they apply to your change.

JSON records are authoritative. The [data model](data-model.md#files) maps each file to its schema; generated indexes and pages are views of those records. Any indexed problem may have attempts and reviews without a full problem card. Source suggestions and editorial corrections do not need a research attempt.

## Intake and inclusion

1. **Check the essentials.** Identify the target, [work type](../CONTRIBUTING.md#requirements-by-work-type) and any existing discussion; check the applicable evidence, credit and reuse rights. Apply the [scientific AI submission route](ai-contributions.md#submission-routes) to scientific arguments, evidence and conclusions. Ask only for missing information that affects inclusion or the claim. Reuse the contribution's evidence, disclosure and check report for the same version.
2. **Assess and retain the claim.** Apply the [evidence policy](evidence-policy.md), retain objections and missing checks, and edit the authoritative records. An unverified proposal may be included with that status. Verify the provenance of claimed human approvals and independent runs; forms and automated checks cannot authenticate them.
3. **Explain the decision.** Link the retained record or explain why the contribution was deferred or declined. Keep substantive corrections, failures and disagreements visible. Merging a change or closing an issue is an editorial action, not a scientific verdict.

These responsibilities do not require separate approval rounds. One assessment may cover several checks when its scope and evidence are explicit. [CODEOWNERS](../.github/CODEOWNERS) identifies the responsible maintainer; [Governance](../GOVERNANCE.md) defines editorial responsibility. A maintainer's own work follows the same standards and is independently reviewed only when another reviewer performs and records that assessment.

Accept useful prose without asking the contributor to repeat it in JSON or another template. Maintainers assign IDs, preserve the examined version and attachments, calculate required checksums and link the records. Confirm any material change to the contributor's claim or credit. Related corrections may share a pull request; a source suggestion or typo does not need a research attempt or scientific review. An exact reviewed target is still required before retaining a review verdict.

Treat form fields as prompts, not enforcement: [GitHub's required-field validation](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) is not available in every repository context. Check required evidence and declarations during intake even when the form was accepted.

## Prepare a record

Use Python 3.10 or later from the repository root. Choose an unused ID and replace `YOUR_NAME_OR_HANDLE` with the contributor's preferred attribution. The helper checks references, supplies current digests and writes an incomplete draft to `work/drafts/`.

Create an attempt:

```sh
python scripts/new_record.py attempt Q-CODE-201 --id ATT-CODE-201-01 --author YOUR_NAME_OR_HANDLE
```

Create a review of a problem entry:

```sh
python scripts/new_record.py review Q-CODE-201 --id REV-CODE-201-ENTRY-01 --author YOUR_NAME_OR_HANDLE --review-type problem_entry
```

Create a review of an attempt already in `data/attempts/`:

```sh
python scripts/new_record.py review Q-CODE-201 --id REV-CODE-201-RESULT-01 --author YOUR_NAME_OR_HANDLE --attempt ATT-CODE-201-01 --review-type research_record
```

Use `--review-type planned_method` to review a proposed method. The [attempt contract](data-model.md#attempt-contract) and [review contract](data-model.md#review-contract) define the fields. An attempt should retain:

| Include | Necessary detail |
| --- | --- |
| Target | Problem ID, exact claim and assumptions, scope, success criteria and sources; distinguish an original proposed subproblem |
| Method and evidence | Argument or procedure, tools and versions, relevant inputs and outputs, and result artifacts; seeds, precision and stopping conditions where relevant |
| Credit | People's actual roles, material human changes and checks, and model assistance |
| Resources | Experiment, data and computing needs; planned limits separately from actual use |
| Outcome and limits | What happened, how to check it, checks performed and what remains unresolved |

For failures, state the failure point and limits of the negative finding. For reproductions, cite the known result and match its hypotheses. For partial results or candidate answers, identify the exact contribution and outstanding checks. A reviewed result links to the review of that version; a correction or retraction identifies the affected version, consequences and any replacement statement.

Use unknown rather than zero for unavailable measurements. Claims about speed need a defined time measure, model/tool conditions, human and checking time, and a suitable comparison. A completed run may have no useful result; reproducing known work does not demonstrate a new solution. Retain reproducible arguments and observable evidence rather than a narrative of how an idea occurred.

To add a record:

1. Resolve every `TODO:` field. Check the target, evidence, credit, rights and submission eligibility. Reuse versioned disclosures and check reports when they cover the same material.
2. Save under the record's ID in `data/attempts/`, `data/reviews/`, `data/verification-specs/` or `data/verifications/`. Link an attempt review through the attempt's `review_ids`. Keep stable IDs and the original `problem_id` when titles or classifications change.
3. Update `data/project.json`: `as_of` must cover the latest actual record date; `research_attempts_run` counts attempts with non-null `started_at`; `model_evaluations_run` counts that subset whose purpose is `model_evaluation`. Plans, specifications and verification runs do not add research runs.
4. Run `python scripts/check.py --render`, then inspect the changed records and generated pages. Use the [check matrix](#check-a-pull-request) for other changes.

The helper creates record drafts; it does not conduct research, reviews or certificate checks. Record only execution, approvals, outcomes and axiom audits that actually occurred. Edit the source records, not the generated attempt, review, specification or verification pages.

## Record assistance and submission screening

Keep one assistance note for the exact submitted version and link it wherever needed. Maintenance and source curation need only the role, tool or model if known, and actual checks; they do not require recommended-model eligibility, full-text human screening or manual submission. Scientific contributions follow the [AI policy](ai-contributions.md), including screening and manual submission when required. Scientific content within a mixed change retains those requirements. Screening does not establish scientific correctness or change `human_review_status`.

Structured research records use these locations; their schemas reject extra properties:

| Information | Location |
| --- | --- |
| Primary model | `model.provider`, `model.name`, `model.version`; null for unavailable details, explained in `limitations` or an assistance note |
| Configuration and software | `environment.tools`, `environment.versions`; exact displayed settings in a process artifact |
| Each contributing model's date, role and affected material | Assistance note in `process_artifacts`; the primary `model` object cannot describe a mixed workflow |
| Inputs, observable outputs and final argument | `input_artifacts`, `process_artifacts`, `candidate_answer_artifacts`, with matching manifest entries |
| Human changes and checks | `human_help`, with actual roles in `contributors` |
| Required submission screening | Linked cover note or process artifact covering readers, dates, exact final version, complete coverage and limits; summarize in `human_help` where applicable |

See the [citation example](reuse-and-citation.md#acknowledge-ai-assistance) for acknowledgment wording. Scientific findings belong in a separate scoped review, even when the same person also screens the submission.

## Preserve the evidence

Each referenced input, process record, result or review-evidence artifact needs an `artifact_manifest` entry:

| Field | Content |
| --- | --- |
| `reference` | The repository-relative path or external URL used in the artifact list |
| `version` | Retained immutable revision, dated snapshot or versioned release |
| `sha256` | `sha256:` followed by 64 lowercase hexadecimal digits; required for local files, or null when an external checksum is unavailable |

Keep local evidence in [research/](../research/README.md), outside `work/` and `.git/`, with appropriate rights and attribution. For remote evidence, identify an exact retained version and checksum when available; otherwise state the limitation. A mutable landing page alone does not preserve a proof, dataset or certificate. Offline validation checks local files and hashes, but does not fetch or authenticate remote content.

Preserve earlier evidence when introducing a replacement. Update its reference or version and obtain any necessary review; changing a manifest changes the attempt digest, so old findings do not silently transfer. A version identifier does not grant permission to copy material. Protect private communications and identifying information, and retain only material you may share.

## Review and credit

Retain scientific verdicts as separate records identifying the reviewer, date, exact version, scope, exclusions, findings and evidence. Use the [review guide](review-guide.md) for the assessment itself.

| Review type | Target |
| --- | --- |
| `problem_entry` | Candidate or card; `attempt_id` and `attempt_digest` are null |
| `planned_method` | Proposed method in an identified attempt; may precede execution |
| `research_record` | Evidence and claims in an identified attempt |

Each review binds the target by `statement_digest`; attempt reviews also bind `attempt_digest`, which excludes `review_ids` and `revision_history`. The helper supplies both; [catalogue JSON](catalog.md) also provides statement digests. Retain the examined content as well as its digest. A plan review does not certify a later result; changed claims or evidence need a new review. See the [review contract](data-model.md#review-contract) for label eligibility.

Keep applicable reviews and objections visible. To replace your own completed conclusion, create a new review and list the earlier ID in `supersedes`. Reviewer, problem, attempt, review type, scope and exclusions must match; the date cannot be earlier. A pending replacement does not retire a completed conclusion. Other reviewers or scopes add evidence rather than replacing it.

Credit actual contributions and preserve original researchers' authorship. Models are tools, not human reviewers. Correctness within a scope does not establish novelty, significance or empirical validity; record those assessments separately. Validation checks the record, not whether a person performed the review.

## Record machine verification

Use the [machine verification template](../templates/machine-verification.md) and first look for a suitable approved specification in the [verification index](verifications.md). Reuse it unchanged when possible. Otherwise prepare a draft for human approval:

```sh
python scripts/new_record.py verification-spec Q-CODE-201 --id VSPEC-CODE-201-01 --author YOUR_NAME_OR_HANDLE --method exact_counterexample
```

Other methods are `lean_proof`, `finite_construction` and `finite_exhaustion`. Once the attempt and specification are in the collection, prepare a run record:

```sh
python scripts/new_record.py verification Q-CODE-201 --id VER-CODE-201-01 --author YOUR_NAME_OR_HANDLE --attempt ATT-CODE-201-01 --specification VSPEC-CODE-201-01
```

Keep the specification and each actual run separate. Retain certificates, logs, versions, hashes, operator, outcome and limits under the [machine verification contract](data-model.md#machine-verification-contract). Drafts leave missing approval and execution information unset.

The [machine verification policy](machine-verification.md) controls approval, independent execution, trust assumptions and eligibility for **Machine checked**. A self-check or compilation report is insufficient. Changed targets, procedures or trust assumptions need renewed approval; changed artifacts need another check. Preserve failures and earlier evidence. The label does not populate human review status, settle broader claims or waive AI submission screening.

## Check a pull request

Use the [contribution check table](../CONTRIBUTING.md#edit-and-check-files) to match local checks to the change. Issues, comments and read-only investigations need no repository tool run. Before integrating structured changes, run `python scripts/check.py --render` and inspect the affected records and pages.

`--render` validates the data, refreshes generated pages and runs the full suite. Without it, `check.py` leaves pages unchanged. The suite checks records, regression tests, generated-page consistency and documentation. It does not inspect external evidence, authenticate declarations, run research models or certify scientific claims. Perform the applicable proof, exact-computation, certificate or reproducibility check separately. Automated contributors also follow the [required recheck](../AGENTS.md#required-recheck).

[GitHub Actions](../.github/workflows/checks.yml) runs the full read-only check on pull requests and updates to `main`; topic-branch pushes do not start duplicate runs. Local commands use Python's standard library and run offline. The workflow uses pinned actions and read-only repository access; review upstream changes before updating pins, following GitHub's [workflow security guidance](https://docs.github.com/en/actions/reference/security/secure-use). Keep external action permissions limited to the components in use, currently `actions/checkout` and `actions/setup-python`; this restriction does not sandbox workflow scripts.

Link displayed outcomes in [progress](progress.md) and [results](results.md) to versioned evidence and applicable reviews. Keep failures, corrections, missing checks and unresolved objections visible.

## Merge a pull request

Use a topic branch and pull request for changes to `main`. Before merging:

1. Read the final diff, apply the requirements for each [work type](../CONTRIBUTING.md#requirements-by-work-type) and address substantive objections. For sensitive maintenance, assess affected behavior, trust assumptions, permissions, terms and checks within this PR; no separate approval round or research-model eligibility check is needed. Changed verification specifications still follow the [approval requirements](machine-verification.md#approve-the-specification). [CODEOWNERS](../.github/CODEOWNERS) maps responsibility; request that review manually when automatic assignment is unavailable.
2. Confirm that both Linux and Windows jobs in **Repository checks** succeeded for the current PR and its integration with the latest `main`. A successful run on an earlier revision or an unrelated branch is insufficient. Missing, skipped or unavailable checks leave the merge pending. After changes to either branch, refresh the integration checks and any affected review.
3. Record the maintainer's decision in the PR, including any remaining limits. A maintainer may assess their own work, but must not describe that assessment as independent review. Passing checks alone does not authorize a merge or establish a scientific verdict.

Immediately before merging, recheck both branch revisions. Automated merges need authorization for that action and an expected-head SHA to reject new PR commits; also recheck the base revision and avoid concurrent merges. Preserve history: do not force-push or delete `main`.

Where GitHub cannot enforce branch protection or owner review, these conventions do not block someone with write access from bypassing them. Limit write access to trusted maintainers and keep decisions and checks in the PR history.
