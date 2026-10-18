# Exact Gaussian interference-channel capacity

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-458 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-458%3A+Exact+Gaussian+interference-channel+capacity&target=Q-FORMAL-458) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-458%3A+Exact+Gaussian+interference-channel+capacity&target=Q-FORMAL-458)

Determine the exact capacity region of the two-user Gaussian interference channel for arbitrary gains and input power constraints, with independent messages and each receiver decoding its intended message.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** A 2025 preprint claims Gaussian signaling optimality for weak interference, with fixed component power constraints. This does not by itself settle the indexed arbitrary-gain capacity region; the broader status remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The inspected paper is the 2007 preprint.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- Independent review and reception of the 2025 signaling-optimality claim are not established.
- No complete later-literature review of arbitrary channel gains and power-allocation convexification was completed.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [Gaussian Interference Channel Capacity to Within One Bit](../sources.md#src-formal-447); [On the Optimality of Gaussian Code-books for Signaling over a Two-Users Weak Gaussian Interference Channel](../sources.md#src-formal-616).

**Exact locator:** Abstract; section II

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After operational conventions are fixed, explore small-alphabet examples, compare inner and outer bounds and assist with entropy calculations. Numerical optimization cannot establish a capacity formula.

**Verification burden:** High. Achievability and converse arguments must match channel, coding, error and asymptotic conventions; local numerical extrema are insufficient.

**Resource expectations:** No physical channel experiment is required for the formal question. Alphabet optimization and symbolic calculations may be costly; no resource bound is established.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

A 2025 preprint claims Gaussian signaling optimality for weak interference, with fixed component power constraints. This does not by itself settle the indexed arbitrary-gain capacity region; the broader status remains unverified.

**Search scope:** Compared the original general-channel target with a 2025 preprint's abstract, model and explicit power-allocation limitation.

**Inspected evidence**

- [Gaussian Interference Channel Capacity to Within One Bit](../sources.md#src-formal-447) — Abstract; section II. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [On the Optimality of Gaussian Code-books for Signaling over a Two-Users Weak Gaussian Interference Channel](../sources.md#src-formal-616) — Section 1, Remark 1; Section 3. The stated weak-interference result omits optimization over component-channel power allocations and does not address arbitrary gains.

**Limits and remaining work**

- Independent review and reception of the 2025 signaling-optimality claim are not established.
- No complete later-literature review of arbitrary channel gains and power-allocation convexification was completed.

<details>
<summary>Search queries</summary>

- "Gaussian interference channel" "capacity region" "2026"
- "Gaussian interference" "capacity" "Khandani" correction


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
