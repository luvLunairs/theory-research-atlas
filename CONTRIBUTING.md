# Contributing

**One form is enough.** You can contribute in ordinary prose, entirely in the browser. No code, JSON, complete problem card or prior approval is needed. A maintainer handles the records and credits your work.

## Choose a contribution

Find the relevant entry and check for an existing discussion. Add a comment there for follow-up work; otherwise open one of these forms:

| I want to… | Open a form | Include |
| --- | --- | --- |
| Fix or clarify something | [Correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml) | Entry link, proposed change and evidence for factual claims |
| Suggest a question or source | [Proposal](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=problem-proposal.yml) | Question or source, link and why it belongs here |
| Share an attempt or result | [Research progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml) | Exact target, method, result or failure, evidence and limits |
| Check someone’s claim or source | [Review](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=scoped-review.yml) | Version examined, checks, findings and what you did not check |
| Submit an exact or formal check | [Machine verification](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=machine-verification.yml) | Fixed claim and checker, or certificate for an approved specification |

Give information **once** and link it from later updates. Mark missing details as unknown or pending. A typo needs no literature search; an uninspected source can be suggested as pending inspection. A review may cover one citation. You do not need to solve a problem to contribute.

## Requirements by work type

Use the requirements for what your change does, regardless of its file or submission form. No separate application or approval round is needed.

| Work | Requirements |
| --- | --- |
| **Routine maintenance:** navigation, formatting, wording that preserves meaning, forms, ordinary tools and tests | Explain the change and run the [applicable checks](#edit-and-check-files). Research model restrictions and full-text submission screening do not apply. |
| **Source curation:** citations, classification, and faithful records of published questions, assumptions or reported status | Cite and inspect the relevant passages; preserve credit, conflicting evidence and uncertainty. Uninspected suggestions may remain pending. Research model restrictions and full-text submission screening do not apply. |
| **Scientific contributions:** proofs, research ideas, counterexamples, research computations, results and scientific assessments | State the target, assumptions, evidence and limits; credit sources and AI assistance. Apply the [research submission rules](docs/ai-contributions.md#submission-routes) and appropriate scientific verification. |
| **Sensitive maintenance:** verification tools, acceptance rules, workflows, permissions, licenses and research standards | Explain the effect and check affected behavior. The maintainer assesses these changes explicitly within the existing PR review. Research model restrictions apply only to any scientific content included. |

Recording what a source reports is curation; supplying an argument, result or independent scientific verdict is a scientific contribution. Changed scientific meaning requires source checks or scientific verification as appropriate, even in a wording or generator change. For mixed work, apply each requirement to the relevant content and its dependencies; do not relabel research as maintenance.

## Evidence and attribution

- **Make claims checkable.** Cite authors, a link and the relevant page or theorem, with dates when known. Open sources before relying on them; distinguish a source’s open-problem label from a current status check. State assumptions, checks and uncertainty.
- **Describe the result honestly.** Separate proposals, reproductions, partial results and proofs. Mark an original research target “Curator-proposed; pending review.” Numerical evidence is not a general proof; correctness does not establish novelty or empirical support. Keep conflicting evidence visible.
- **Credit and respect rights.** Cite every proof and idea, including AI assistance. Share only material you may distribute; protect private information. Original text/data use [CC BY 4.0 and code uses MIT](LICENSE.md). Contributors retain authorship. Name project collaborators or reviewers only with their agreement and accurate roles.
- **Keep discussion useful.** Preserve entry IDs, earlier findings and objections. Group related minor fixes, avoid duplicate submissions and communicate respectfully.

## AI-assisted contributions

For maintenance or source curation, a short note naming the tool or model if known, its role and actual checks is enough; missing model details do not block submission. Scientific content follows the [AI policy](docs/ai-contributions.md): a non-recommended or unidentified model contributing to its substance requires **full-text human review and manual submission**. AI used only for formatting or wording that preserves meaning does not trigger that restriction. Disclose its role nonetheless.

Automation always needs an authorized channel and the [agent recheck](AGENTS.md#required-recheck). Machine verification does not waive applicable research submission rules.

## What happens next

A maintainer checks the essentials, retains useful work with its stated limits, and links the resulting record or explains what is missing. Inclusion is an editorial decision, not scientific certification. You need not repeat your submission in another format.

<a id="examples-and-versions"></a>
<details>
<summary>Examples, attachments and identifying a version</summary>

An illustrative wording suggestion:

> Entry: [paste the entry link]. Please explain “UNSAT” as “unsatisfiable” at first use. This is a wording suggestion; I have not checked the mathematical claim.

For a source correction, add its authors, link, page or theorem and the passage’s relevance. For a proof or review, state the exact claim and assumptions being examined.

You can [attach a PDF or notes](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files) in a form’s text area. Date and name your document; retain earlier versions when revising it. To identify an existing entry exactly, open its file on GitHub, press **Y** and copy the resulting [permanent link](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files). If that is unavailable, attach the examined text with its URL and access date. An access date alone does not preserve a version. Maintainers handle record IDs and checksums.

</details>

<details>
<summary>Edit and check files — optional for contributors</summary>

## Edit and check files

Use a topic branch and pull request; an issue first is optional. Edit source records or guides, rather than generated pages. With Python 3.10 or later, run only the checks appropriate to your change:

| Change | Check |
| --- | --- |
| Guide or template text | Reread it and run `python scripts/check_docs.py` |
| Structured records or generated pages | `python scripts/check.py --render`, then inspect the pages |
| Code, schemas or validation | `python scripts/check.py`; add `--render` if pages need refreshing |

These checks establish repository consistency, not scientific correctness. Report actual checks and limits in the pull request. The [maintenance reference](docs/maintaining.md) covers record editing and integration.

</details>

<details>
<summary>Specialist references and plain-text alternatives</summary>

Use a form **or** its plain-text alternative: [entry change](templates/entry-change.md), [research update](templates/research-update.md), [review](templates/review.md) or [machine verification](templates/machine-verification.md).

Consult [evidence and status rules](docs/evidence-policy.md), [review scope](docs/review-guide.md), [machine verification](docs/machine-verification.md) or [citation examples](docs/reuse-and-citation.md) when your task needs them. [Governance](GOVERNANCE.md) covers decisions and disagreements.

</details>

For permission or infringement concerns, use the separate [rights reporting process](LICENSE.md#rights-concerns); research-submission requirements do not apply.
