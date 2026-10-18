# Termination of a single linear rewrite rule

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-468 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-468%3A+Termination+of+a+single+linear+rewrite+rule&target=Q-FORMAL-468) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-468%3A+Termination+of+a+single+linear+rewrite+rule&target=Q-FORMAL-468)

Is termination decidable for a term-rewriting system consisting of one rule that is both left-linear and right-linear?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The inspected 2005 survey matches the historical variant and distinguishes nearby solved cases. No verified current resolution was established in the scoped search; present openness is not asserted.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The entry was first dated 1991; later references on the page do not constitute a current-status audit.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- A post-2005 citation-chain review and current specialist status check remain incomplete.

**Primary branch:** [Programming languages and verification theory](../domains/cs.md#cs-semantics). **Related branches:** None recorded.

**Sources:** [RTA Problem 21: Termination of a single linear rewrite rule](../sources.md#src-formal-457); [Open. Closed. Open.](../sources.md#src-formal-618).

**Exact locator:** Problem 21

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

The inspected 2005 survey matches the historical variant and distinguishes nearby solved cases. No verified current resolution was established in the scoped search; present openness is not asserted.

**Search scope:** Compared the RTA entry with the 2005 survey's exact problem and nearby results; targeted searches did not establish a later resolution.

**Inspected evidence**

- [RTA Problem 21: Termination of a single linear rewrite rule](../sources.md#src-formal-457) — Problem 21; full question and all displayed remarks. The Remark records partial string-rule results and the 2005 history, while distinguishing termination from confluence.
- [Open. Closed. Open.](../sources.md#src-formal-618) — Section 3, Problem 21a, printed pages 383–384. The question requires one rule that is both left- and right-linear; undecidability for a merely left-linear rule does not settle it.

**Limits and remaining work**

- A post-2005 citation-chain review and current specialist status check remain incomplete.

<details>
<summary>Search queries</summary>

- "one-rule" "linear" "termination" "open"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
