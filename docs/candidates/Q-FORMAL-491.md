# Exact complexity of word equations

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-491 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-491%3A+Exact+complexity+of+word+equations&target=Q-FORMAL-491) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-491%3A+Exact+complexity+of+word+equations&target=Q-FORMAL-491)

Determine the exact complexity of satisfiability of finite word equations over a free monoid.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** A primary paper first published online in September 2025 explicitly says the precise complexity of word-equation satisfiability remains open. Its PSPACE upper bound and NP-hardness concern ordinary equations; adding regular constraints changes the problem.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The entry was first dated 1998; later references on the page do not constitute a current-status audit.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- A complete post-September-2025 complexity literature review remains outstanding.

**Primary branch:** [Programming languages and verification theory](../domains/cs.md#cs-semantics). **Related branches:** None recorded.

**Sources:** [RTA Problem 92: Exact complexity of word equations](../sources.md#src-formal-480); [When GNNs Met a Word Equations Solver: Learning to Rank Equations](../sources.md#src-formal-613).

**Exact locator:** Problem 92

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After definitions and present status are checked, enumerate bounded terms and reduction peaks, search for finite counterexamples, and help formalize candidate lemmas. Bounded enumeration cannot certify general confluence or decidability.

**Verification burden:** High. Check the exact reduction relation, variable conventions and all quantifiers; confluence and decision procedures need proofs beyond finite examples.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Term enumeration can grow exponentially; proof-assistant and expert-review effort are unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

A primary paper first published online in September 2025 explicitly says the precise complexity of word-equation satisfiability remains open. Its PSPACE upper bound and NP-hardness concern ordinary equations; adding regular constraints changes the problem.

**Search scope:** Read a recent primary paper's explicit complexity statement; separated pure equations from regular and length constraints in the search results.

**Inspected evidence**

- [RTA Problem 92: Exact complexity of word equations](../sources.md#src-formal-480) — Problem 92; full question and all displayed remarks. The Remark updates the original upper bound to PSPACE; the exact complexity question is distinct from decidability.
- [When GNNs Met a Word Equations Solver: Learning to Rank Equations](../sources.md#src-formal-613) — Introduction, first paragraph. The exact complexity is explicitly left open with NP-hard and PSPACE bounds.

**Limits and remaining work**

- A complete post-September-2025 complexity literature review remains outstanding.

<details>
<summary>Search queries</summary>

- "word equations" "PSPACE" "2026" complexity
- "word equations" PSPACE NP 2025 open
- "word equations" "complexity" "open" 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
