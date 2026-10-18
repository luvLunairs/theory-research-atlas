# AI-assisted contributions

AI assistance is welcome in both research and project maintenance. **Credit the assistance and check the work.** The [work types](../CONTRIBUTING.md#requirements-by-work-type) determine which requirements apply, across all submission channels. [Rights-concern reports](../LICENSE.md#rights-concerns) are exempt.

For routine maintenance, source curation and sensitive maintenance, a short note naming the tool or model if known, its role and actual checks is enough. Missing identity or configuration details do not block submission. These tasks have **no recommended-model requirement, full-text research screening or manual-only route**. Sensitive changes still receive targeted assessment in the existing PR review.

## Submission routes

The following routes apply to **scientific substance**: arguments, research ideas, counterexamples, research computations, results and scientific assessments, including their supporting code and evidence. Faithfully recording an attributed source claim is curation; supplying an independent argument or verdict is scientific work.

| AI contribution to scientific substance | Route |
| --- | --- |
| None | Ordinary scientific evidence and citation requirements; disclose any presentation-only assistance |
| Recommended configurations only, including recognized higher configurations | Human submission, or automation through an explicitly authorized channel; disclose assistance and complete the [agent recheck](../AGENTS.md#required-recheck) when applicable |
| Any non-recommended or unidentified configuration | **Full-text human review, then manual submission. Automated submission is prohibited, even after review.** |

Apply these routes to the scientific content and supporting material in mixed or delegated work. A submission containing scientific work that requires manual submission must be submitted manually; unrelated maintenance can be submitted separately. Rewriting, translation or review does not erase substantive provenance. AI used only for presentation that preserves meaning is disclosed but does not trigger these model restrictions. If substantive influence is uncertain, treat it as scientific assistance. Unused trials need no disclosure.

Supporting material means contributed reasoning, code or evidence for the claim. Existing third-party tools need attribution, versions and relevant trust checks, not full-text screening or inferred model provenance. General verification-tool changes are sensitive maintenance; claim-specific proof code or certificates are scientific contributions.

All automation needs an authorized channel and the [agent recheck](../AGENTS.md#required-recheck). Preparing a local draft is not submission. Manual submission means a human sends the reviewed version without delegating or scheduling that act to automation. Eligibility is not acceptance, merge permission or scientific approval. [Machine verification](machine-verification.md) does not waive applicable research submission rules.

## Recommended models

**Policy date: 18 October 2026; model recommendations dated 15 October 2026.** These preferences apply to scientific contributions, not maintenance or curation. They are not a benchmark ranking or a guarantee of availability, correctness or success.

| Model | Recommended configuration |
| --- | --- |
| Claude Opus 5.5 | Max, High |
| Gemini 4 Argon | High |
| Claude Sonnet 5.5 | Max |
| GPT-6 Astra | Max, High |
| Claude Fable 5.1 | Max, High |
| GPT-6.1 Sol | Max |
| Muse Wonder Full | Max |

Corresponding higher configurations and more capable successors qualify only when the relationship is documented and recognized by the maintainer; link that recognition. A higher version number, similar name or capability claim is insufficient.

For scientific assistance, use the actual service-supplied identity, available API identifier/version and reasoning or compute setting. Never infer identity from a model’s self-description or invent missing details. If identity and settings cannot establish eligibility, use the non-recommended research route.

## One assistance note

Use the form’s assistance field or link one note for the **same final version and attachments**. Maintenance and curation need only the short note above. For scientific assistance, include:

- Each contributing model’s provider, actual identity, available version, settings, date, role and affected material.
- Permitted retained inputs and outputs, material human changes and actual checks. Mark unavailable information; protect private material.
- Human screening and the agent recheck when required below.

A simple correction needs no research-attempt record. Models are tools, not human authors or reviewers. The [citation example](reuse-and-citation.md#acknowledge-ai-assistance) and [record locations](maintaining.md#record-assistance-and-submission-screening) are optional references.

## Full-text human review

For scientific work involving non-recommended or unidentified models, humans must read **the full scientific contribution and its supporting material**, including proofs, reasoning, code and evidence. Unrelated maintenance is outside this screening scope; label the boundary and include any dependencies that affect the claim. Sampling, summaries, changed-lines-only review and AI review are insufficient. Disclosed self-review is allowed; multiple readers may divide the work with complete combined coverage.

Check claims, assumptions, reasoning, relevant source passages and attribution. Add to the assistance note:

- Readers’ names or handles, relationship to the work and review dates.
- Exact final revision or retained snapshot, attachments and confirmation of complete coverage.
- Corrections, unresolved findings, verification or novelty limits, and the manual submitter’s name or handle.

Unread material within scope leaves the requirement unmet. Changes within that scope require renewed review before manual submission. This screening does not establish scientific correctness or change review status; scientific findings belong in a separate [scoped review](review-guide.md). Forms and repository checks cannot authenticate model identity or human review.

## Cite every proof and idea

Credit original papers, code, data and people alongside AI assistance, including for sketches, constructions and unsuccessful approaches. Open relevant source passages; a model-suggested citation is not evidence. Distinguish quotation, adaptation and original proposal, and leave unchecked novelty unverified. Share only material you may distribute.

## Automated recheck

Follow [AGENTS.md](../AGENTS.md#required-recheck), including for drafts awaiting human handoff. Keep one report for the exact version, intended action, actual checks and results, corrections and limits. Link it instead of repeating it. Repeat affected checks after changes; missing checks or authorization leave the action pending. Self-checking replaces neither human screening nor independent scientific review.

## Policy changes

Identify the policy date and any maintainer recognition used. Later changes do not erase provenance or retroactively verify work. Use the [assessment rubric](ai-assessment.md) for task-specific judgments; the atlas has not established success rates for these models.

[Contributing](../CONTRIBUTING.md) · [Citation examples](reuse-and-citation.md)
