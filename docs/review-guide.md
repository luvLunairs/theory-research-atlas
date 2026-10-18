# Research and editorial review

A useful review can check one citation or one claim. Identify the version examined, what you checked, your finding and any limits. Add a comment to the existing discussion or open the [review form](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=scoped-review.yml); no local tools or full problem card are required. The [contribution guide](../CONTRIBUTING.md#examples-and-versions) explains how to retain a version in the browser. A maintainer handles the structured record.

## Choose the scope

Choose a specific task and check only what is needed to support your conclusion:

| Task | Check |
| --- | --- |
| Citation or correction | The exact passage, relevant assumptions and proposed change |
| Problem status | The indexed statement, equivalent formulations and later results under the [status policy](evidence-policy.md#check-a-status-claim) |
| Method or result | The fixed target, evidence, applicable verification and unresolved steps |
| Reproducibility | Versions, inputs, procedure and whether the retained result can be reproduced |
| Novelty, significance or empirical interpretation | Relevant prior work or empirical evidence, assessed separately from correctness |

A narrow review need not assess every category. Say which ones you did not check. Open the relevant passages and compare the actual assumptions and conclusion, not only the title or abstract. Use the [assessment rubric](ai-assessment.md) for AI suitability judgments; confidence or a model's identity is not evidence of correctness.

Disclose AI assistance under the [AI policy](ai-contributions.md). Checking what a cited passage says is source curation; an independent assessment of an argument or result is a scientific contribution. Model eligibility and full-text screening apply to scientific substance, not editorial checks or presentation-only help. Applicable submission screening covers the complete scientific contribution, even when that contribution reviews only one claim. Link notes for the same final version rather than repeating them.

Find a bounded task in [pending checks](pending-checks.md). Consult the [source notes and examples](quality-checks.md) only when they help with your target.

## Preliminary screening

An attempt may record a preliminary-screening note before specialist academic review. Attribute the report, identify the exact target and result files, describe what was checked and retain the evidence. State whether AI checks came from the contributing team. A human preliminary pass must identify the human and the reported scope in the evidence; do not infer full-text coverage, independence or professional expertise. If those details were not supplied, say so.

The displayed stage is derived from the optional record and its current version bindings:

| Stage | Meaning |
| --- | --- |
| Preliminary screening not recorded | No structured record is available, or it records no completed checks or human preliminary conclusion |
| Limited preliminary screening recorded | Checks are recorded, but the recommended-AI or human-pass conditions below are not established |
| Recommended-model contributor checks recorded | Completed checks and recommended configurations for all substantive AI assistance are documented, including delegated work |
| Recommended-model contributor checks + reported human preliminary pass | The preceding contributor checks and an attributed human preliminary pass are recorded for the same bound result |
| Human preliminary pass reported | A human preliminary pass is recorded without asserting recommended-AI checks |
| Preliminary screening: changes requested | The preliminary report requests changes; no positive preliminary stage is displayed |

Earlier or different versions and evidence needing attention receive explicit labels instead of a current positive stage. Preserve previous reports when revising screening. These stages describe review progress, not low, medium or high probabilities of correctness. A non-recommended or unidentified model is not evidence that an argument is wrong. Model provenance and applicable submission restrictions remain governed by the [AI policy](ai-contributions.md).

**Specialist academic review** is shown through the existing scoped-review records, separately from preliminary screening. Record the responsible human's expertise, relationship to the work, scope, verdict, examined version and evidence. A generic acceptance, code review or professional title does not automatically establish academic acceptance of the argument. Same-team checks remain same-team checks; preliminary screening never creates an independent-review claim, changes `human_review_status` or earns a machine-verification label. Repository checks validate bindings and declarations, not the authenticity or adequacy of a reported review.

## Review machine-checkable work

The [machine verification policy](machine-verification.md) separates approval of the claim and checker from checking each certificate. For a new specification, assess statement alignment, definitions, assumptions, trusted components, acceptance rules and invalid-input handling. Record the approved version and limits. A changed target, procedure or trust basis needs renewed approval.

For a certificate under an approved specification, confirm that the independent run and retained artifacts match its scope and versions. An eligible pass can establish the certified claim without repeating a line-by-line human proof review. It does not establish novelty, a human verdict or the resolution of a broader problem. Preserve unresolved objections and verifier defects.

## State the scope of a review

Record the problem ID, examined version, reviewer and role, date, scope, exclusions, findings, evidence and relevant conflicts. Choose **accepted within scope**, **changes requested**, **rejected with reasons** or **inconclusive**. A brief, precise conclusion is enough:

> The cited theorem settles the indexed claim under its regularity assumption. I checked statement alignment, not the proof.

Preserve the examined version, evidence and unresolved objections. Follow the [record rules](maintaining.md#review-and-credit) when evidence changes or a reviewer revises a conclusion; a newer positive review does not erase another reviewer's objection. Existing evidence can be linked rather than repeated.

Credit only checks actually performed and identify the responsible human for a human review. A model critique, automated test or full-text submission screening is not an independent human proof review. Keep correctness, novelty, significance, empirical support and editorial acceptance separate.

[Contributing](../CONTRIBUTING.md) · [Record maintenance](maintaining.md) · [Evidence policy](evidence-policy.md)
