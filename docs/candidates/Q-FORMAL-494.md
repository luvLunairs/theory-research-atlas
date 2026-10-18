# Word problem for the S combinator

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-494 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-494%3A+Word+problem+for+the+S+combinator&target=Q-FORMAL-494) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-494%3A+Word+problem+for+the+S+combinator&target=Q-FORMAL-494)

Is convertibility decidable for closed applicative terms built only from S, with reduction S x y z to (x z)(y z)?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** Manzonetto's 2023 FSCD survey explicitly restates this question as open. A targeted keyword search found no inspected later resolution; this remains a dated source report, not proof that no resolution exists.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Historical question reaffirmed in the 2023 survey.

**Scope limits:** The original calculus and decision/existence question are preserved; related normalization results do not answer it.

**Information still needed**

- A specialist citation-chain search after 2023 remains outstanding.

**Primary branch:** [Programming languages and verification theory](../domains/cs.md#cs-semantics). **Related branches:** None recorded.

**Sources:** [RTA Problem 97: Word problem for the S combinator](../sources.md#src-formal-483); [A Lambda Calculus Satellite (Invited Talk)](../sources.md#src-formal-602).

**Exact locator:** Problem 97

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

Manzonetto's 2023 FSCD survey explicitly restates this question as open. A targeted keyword search found no inspected later resolution; this remains a dated source report, not proof that no resolution exists.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [RTA Problem 97: Word problem for the S combinator](../sources.md#src-formal-483) — Problem 97; full question and all displayed remarks. The page distinguishes the word problem from the cited decidability of normalization of S-terms.
- [A Lambda Calculus Satellite (Invited Talk)](../sources.md#src-formal-602) — Section 6.4, Problem 4. The survey explicitly identifies the original question as an unresolved problem.

**Limits and remaining work**

- A specialist citation-chain search after 2023 remains outstanding.

<details>
<summary>Search queries</summary>

- "S-combinator" "word problem" 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
