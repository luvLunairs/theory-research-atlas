# Noninteractive one-bit mean estimation over finite-moment classes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-438 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-438%3A+Noninteractive+one-bit+mean+estimation+over+finite-moment+classes&target=Q-FORMAL-438) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-438%3A+Noninteractive+one-bit+mean+estimation+over+finite-moment+classes&target=Q-FORMAL-438)

For every fixed k>1, can fully nonadaptive arbitrary measurable one-bit quantizers achieve, within constants depending only on k, the adaptive rate r_k in Lau–Scarlett equation (1), uniformly over distributions with mean in [-lambda,lambda] and E|X-mu|^k<=sigma^k, where lambda>=sigma>0 are known? Use independent samples, accuracy epsilon<=c_k sigma, and failure probability delta in (0,1/2).

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-11-06.

**Status basis:** Resolved affirmatively in the subsequent literature: Lau and Scarlett give the matching nonadaptive theorem and explicitly recognize concurrent solutions, including Hu and Zhong. The acceptance basis is acknowledgement by the original problem authors and their own construction; this is not independent proof certification by the project.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Original problem: July 2026. Hu-Zhong v1: 3 August 2026. Lau-Scarlett follow-up v1: 8 September 2026.

**Scope limits:** The historical target is preserved: arbitrary measurable nonadaptive quantizers, independent samples, the same central-moment class and all three k regimes. A two-stage decoder is not adaptive query selection.

**Information still needed**

- A specialist proof review and any later journal version remain to be recorded.

**Primary branch:** [Inference and decision theory](../domains/stat.md#stat-infer). **Related branches:** None recorded.

**Sources:** [Open Problem: Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?](../sources.md#src-formal-436); [Open Problem: Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?](../sources.md#src-formal-611); [Interaction Is Not Necessary for Order-Optimal 1-Bit Mean Estimation](../sources.md#src-model-700); [Non-Adaptive 1-Bit Mean Estimation: Minimax Rates and the Sample-Interval Tradeoff](../sources.md#src-model-701).

**Exact locator:** Lau-Scarlett (July 2026), Section 2, equation (1), Open Problem 1; Lau-Scarlett (September 2026), Sections 1.1 and 1.3, Theorem 1.

**Potential difficulty:** Unknown. The historical question now has a sourced affirmative resolution; original-research difficulty is no longer the appropriate selection criterion.

**Possible AI role:** Compare or reproduce the published estimators and proofs; identify any extension separately from this resolved target.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No project model experiment or independent proof audit was performed. Bibliographic resolution does not certify implementation correctness.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Reported resolved.

Resolved affirmatively in the subsequent literature: Lau and Scarlett give the matching nonadaptive theorem and explicitly recognize concurrent solutions, including Hu and Zhong. The acceptance basis is acknowledgement by the original problem authors and their own construction; this is not independent proof certification by the project.

**Search scope:** Compared July Open Problem 1 with the August construction and September original-authors follow-up, including its parameter class, main theorem and acknowledgement of concurrent solutions. Targeted later-correction searches found no relevant correction within this scope.

**Inspected evidence**

- [Open Problem: Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?](../sources.md#src-formal-611) — Section 2, equation (1), Open Problem 1. Defines the unrestricted finite-central-moment target and adaptive benchmark.
- [Interaction Is Not Necessary for Order-Optimal 1-Bit Mean Estimation](../sources.md#src-model-700) — Abstract and Section 1.1. Reports an affirmative fully nonadaptive construction.
- [Non-Adaptive 1-Bit Mean Estimation: Minimax Rates and the Sample-Interval Tradeoff](../sources.md#src-model-701) — Section 1.3; Theorem 1. The original problem authors acknowledge concurrent answers and establish the same minimax rates with queries fixed before all responses.

**Limits and remaining work**

- This records a sourced resolution, not a project proof review, implementation test or verified publication venue.

<details>
<summary>Search queries</summary>

- "one-bit mean estimation" noninteractive 2026 Lau Scarlett
- "2609.08564" correction OR erratum OR withdrawn


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Unverified → Source reports open.

The July 2026 full text explicitly poses this uniform question as Open Problem 1. Known lower bounds for thresholds and intervals do not settle arbitrary measurable quantizers.

**Search scope:** Read the full model and Open Problem 1, distinguishing general quantizers from thresholds and finite-moment classes from parametric families. A later-resolution search was not completed and no independent later status source was inspected.

<details>
<summary>Previous indexed wording</summary>

Can arbitrary nonadaptive one-bit quantizers attain the order-optimal adaptive minimax rate for mean estimation over the source's nonparametric finite-moment classes, or is one adaptive transition necessary?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?](../sources.md#src-formal-436) — Abstract. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Open Problem: Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?](../sources.md#src-formal-611) — Section 2, equation (1), Open Problem 1. The statement explicitly asks for a nonadaptive protocol achieving the adaptive rate.

**Limits and remaining work**

- Check later publications after July 2026; lower bounds limited to particular quantizer families do not resolve the stated question.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "Is Interaction Necessary for Order-Optimal"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
