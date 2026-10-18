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

## Review machine-checkable work

The [machine verification policy](machine-verification.md) separates approval of the claim and checker from checking each certificate. For a new specification, assess statement alignment, definitions, assumptions, trusted components, acceptance rules and invalid-input handling. Record the approved version and limits. A changed target, procedure or trust basis needs renewed approval.

For a certificate under an approved specification, confirm that the independent run and retained artifacts match its scope and versions. An eligible pass can establish the certified claim without repeating a line-by-line human proof review. It does not establish novelty, a human verdict or the resolution of a broader problem. Preserve unresolved objections and verifier defects.

## State the scope of a review

Record the problem ID, examined version, reviewer and role, date, scope, exclusions, findings, evidence and relevant conflicts. Choose **accepted within scope**, **changes requested**, **rejected with reasons** or **inconclusive**. A brief, precise conclusion is enough:

> The cited theorem settles the indexed claim under its regularity assumption. I checked statement alignment, not the proof.

Preserve the examined version, evidence and unresolved objections. Follow the [record rules](maintaining.md#review-and-credit) when evidence changes or a reviewer revises a conclusion; a newer positive review does not erase another reviewer's objection. Existing evidence can be linked rather than repeated.

Credit only checks actually performed and identify the responsible human for a human review. A model critique, automated test or full-text submission screening is not an independent human proof review. Keep correctness, novelty, significance, empirical support and editorial acceptance separate.

[Contributing](../CONTRIBUTING.md) · [Record maintenance](maintaining.md) · [Evidence policy](evidence-policy.md)
