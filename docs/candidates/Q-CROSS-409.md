# Computing the best achievable delay margin

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-409 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-409%3A+Computing+the+best+achievable+delay+margin&target=Q-CROSS-409) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-409%3A+Computing+the+best+achievable+delay+margin&target=Q-CROSS-409)

For the unity-feedback plant P(s)=P0(s) exp(-s tau), define each LTI controller's delay margin by internal stability for every constant delay in [0,tau_bar]. When the supremum of these margins over all LTI controllers internally stabilizing P0 is finite, give a computationally feasible algorithm that computes this supremum to prescribed accuracy.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Ringh, Karlsson and Lindquist (2020 revision) explicitly leave the exact general maximum open while improving lower bounds. Their numerical tolerance is not a general optimum-error certificate. No matching general resolution was confirmed in this scoped search; present status remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The original problem is from 2002. The dated literature check identifies the later version inspected; neither access date nor a related theorem establishes current openness.

**Scope limits:** The delay is an uncertain constant in the original continuous-time feedback model, and one controller must stabilize an interval of delays. Fixed-order, PID, discrete-time or internally delayed alternatives require separate statements.

**Information still needed**

- Check later general results for a guaranteed error bound against the unrestricted supremum.
- Confirm admissible plant and controller conventions before comparing bounds or proposing a restricted instance.

**Primary branch:** [Robust design and verification](../domains/eng.md#eng-robust). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [An analytic interpolation approach to stability margins with emphasis on time delay](../sources.md#src-cross-801).

**Exact locator:** Problem 18, section 18.1, Problem 2, pp. 112–114; Daniel E. Davison and Daniel E. Miller

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could derive low-order analytic bounds and certify optimization calculations. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Verify internal stability for the whole delay interval and certify the distance to the all-controller supremum. Bisection convergence for a sufficient test and simulation over a delay grid do not provide that certificate.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Ringh, Karlsson and Lindquist (2020 revision) explicitly leave the exact general maximum open while improving lower bounds. Their numerical tolerance is not a general optimum-error certificate. No matching general resolution was confirmed in this scoped search; present status remains unverified.

**Search scope:** Inspected the original formulation in the editor-hosted MTNS collection and the identified later paper. Targeted searches compared model assumptions and the claimed output; this is not an exhaustive status review.

<details>
<summary>Previous indexed wording</summary>

When the supremum of achievable delay margins over stabilizing LTI controllers for a specified plant is finite, compute it to a prescribed accuracy.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 18, section 18.1, Problem 2, pp. 112–114; Daniel E. Davison and Daniel E. Miller. Checked the original assumptions and target.
- [An analytic interpolation approach to stability margins with emphasis on time delay](../sources.md#src-cross-801) — 27 October 2020 revision; abstract, Sections I-III, Algorithm 1 and Section IX. Algorithm 1 yields a lower bound; Section IX retains the general unresolved target. Near-coincident bounds for examples do not prove a complete prescribed-accuracy algorithm.

**Limits and remaining work**

- Check later general results for a guaranteed error bound against the unrestricted supremum.
- Confirm admissible plant and controller conventions before comparing bounds or proposing a restricted instance.
- No independent proof audit or comprehensive present-status assessment was performed.

<details>
<summary>Search queries</summary>

- "maximum delay margin" "Davison" Miller algorithm open problem
- "maximum delay margin" "2025" "general"
- "maximum delay margin" "2026" Ringh


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The requested object is the supremum over all admissible LTI controllers. Published bounds or optimizations within PID or fixed-order classes would not establish the unrestricted algorithm. No matching resolution was confirmed.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 18, section 18.1, Problem 2, pp. 112–114; Daniel E. Davison and Daniel E. Miller. Identifies the historical target.

**Limits and remaining work**

- Inspect general delay-margin interpolation results and their guaranteed error or completeness properties.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "maximum delay margin" "Davison" Miller algorithm open problem


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
