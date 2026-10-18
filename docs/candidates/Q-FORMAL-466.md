# Boolean conditional combinatory logic

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-466 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-466%3A+Boolean+conditional+combinatory+logic&target=Q-FORMAL-466) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-466%3A+Boolean+conditional+combinatory+logic&target=Q-FORMAL-466)

Is CL-pc1 confluent? Its rules are I x → x, K x y → x, S x y z → x z (y z), C T x y → x, C F x y → y, and C z x y → x when x and y are convertible in CL-pc1 itself. Application associates to the left; T and F denote the Boolean constants.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-10-15.

**Status basis:** Czajka's FSCD 2017 paper proves confluence of the same asymmetric semi-equational conditional extension, explicitly resolving RTA Problem 15. Section 1, footnote 1 confirms that the accompanying formalization includes the I rule used in the original question.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Original 1991 question; FSCD 2017 resolution.

**Scope limits:** The condition is convertibility in the same conditional system, not syntactic equality of branches. The I rule is included in the author's formalization. The original confluence question is resolved.

**Information still needed**

- Retrieve the exact formalization revision and toolchain before attempting a reproduction; neither has been executed here.

**Primary branch:** [Programming languages and verification theory](../domains/cs.md#cs-semantics). **Related branches:** [Proof theory and constructive logic](../domains/logic.md#logic-proof).

**Sources:** [RTA Problem 15: Boolean conditional combinatory logic](../sources.md#src-formal-455); [Confluence of an extension of Combinatory Logic by Boolean constants](../sources.md#src-formal-601).

**Exact locator:** RTA Problem 15; Czajka, FSCD 2017, §1 and footnote 1, Theorem 32.

**Potential difficulty:** Unknown. Czajka's FSCD 2017 paper proves confluence for the indexed asymmetric Boolean extension; the original question is historical. Proof-audit and formalization effort remain unestimated.

**Possible AI role:** Help align the original conditional rules with the published theorem and reconstruct its confluence argument. Work on this record should review or reproduce the existing result rather than seek a new resolution of the original question.

**Verification burden:** High. Check the relation used in the side condition and compare the formalized statement with every listed rule. Finite reduction examples cannot establish confluence.

**Resource expectations:** No empirical data or experiment is required. Reproduction needs the proof files and compatible proof-assistant version; setup and expert review remain unestimated.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** No model has been evaluated and the confluence proof has not been formally reproduced by this project.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Reported resolved → Reported resolved.

Czajka proves confluence for CL-pc1 with the listed rules and the convertibility condition. The unconditional and symmetric conditional systems are different targets.

**Search scope:** Reopened the full FSCD manuscript and compared the rules, side condition, I-rule note and final theorem.

<details>
<summary>Previous indexed wording</summary>

Is combinatory logic with I, K, S, true, false and the source's asymmetric semi-equational conditional operator confluent?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Confluence of an extension of Combinatory Logic by Boolean constants](../sources.md#src-formal-601) — §1, footnote 1 and Theorem 32. The theorem proves confluence; its conditional equality is defined by the system's own convertibility relation.

**Limits and remaining work**

- The Coq development was not executed. This check concerns statement alignment, not an independent formal verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Reported resolved.

Czajka's FSCD 2017 paper proves confluence of the same asymmetric semi-equational conditional extension, explicitly resolving RTA Problem 15. Section 1, footnote 1 confirms that the accompanying formalization includes the I rule used in the original question.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [RTA Problem 15: Boolean conditional combinatory logic](../sources.md#src-formal-455) — Problem 15; full question and all displayed remarks. The asymmetric Boolean conditional is the original target; the page's extra symmetric rule yields a different known confluent system.
- [Confluence of an extension of Combinatory Logic by Boolean constants](../sources.md#src-formal-601) — Abstract; section 1, rules and footnote 1. The published result answers the original question affirmatively, including the I-rule convention.

**Limits and remaining work**

- The project has not rerun the Coq formalization or independently re-proved the theorem.

<details>
<summary>Search queries</summary>

- "combinatory logic" "Boolean" "confluence" conditional


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
