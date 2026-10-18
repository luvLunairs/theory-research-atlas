# Strong sequentiality for general rewrite systems

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-486 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-486%3A+Strong+sequentiality+for+general+rewrite+systems&target=Q-FORMAL-486) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-486%3A+Strong+sequentiality+for+general+rewrite+systems&target=Q-FORMAL-486)

Is strong sequentiality decidable for arbitrary finite term-rewriting systems?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The RTA question concerns unrestricted term-rewriting systems. Durand's inspected decidability results assume orthogonality or left-linearity and do not answer that scope. No current resolution of the unrestricted question was verified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The entry was first dated 1995; later references on the page do not constitute a current-status audit.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- An unrestricted-system decision theorem or undecidability reduction has not been verified.

**Primary branch:** [Programming languages and verification theory](../domains/cs.md#cs-semantics). **Related branches:** None recorded.

**Sources:** [RTA Problem 80: Strong sequentiality for general rewrite systems](../sources.md#src-formal-475); [Call-by-need computations in orthogonal TRSs](../sources.md#src-formal-606).

**Exact locator:** Problem 80

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After definitions and present status are checked, enumerate bounded terms and reduction peaks, search for finite counterexamples, and help formalize candidate lemmas. Bounded enumeration cannot certify general confluence or decidability.

**Verification burden:** High. Check the exact reduction relation, variable conventions and all quantifiers; confluence and decision procedures need proofs beyond finite examples.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Term enumeration can grow exponentially; proof-assistant and expert-review effort are unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The RTA question concerns unrestricted term-rewriting systems. Durand's inspected decidability results assume orthogonality or left-linearity and do not answer that scope. No current resolution of the unrestricted question was verified.

**Search scope:** Checked the hypotheses of later call-by-need decidability statements against the unrestricted RTA question.

**Inspected evidence**

- [RTA Problem 80: Strong sequentiality for general rewrite systems](../sources.md#src-formal-475) — Problem 80; full question and all displayed remarks. The page cites restricted decidability results and separately asks about arbitrary systems.
- [Call-by-need computations in orthogonal TRSs](../sources.md#src-formal-606) — Slides 13 and 21. The decision theorems inspected concern orthogonal or left-linear systems, not arbitrary systems.

**Limits and remaining work**

- An unrestricted-system decision theorem or undecidability reduction has not been verified.

<details>
<summary>Search queries</summary>

- rewriting "strong sequentiality" complexity decidability NP complete


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
