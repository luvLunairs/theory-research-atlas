# Optimal reduced-order H-infinity approximation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-405 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-405%3A+Optimal+reduced-order+H-infinity+approximation&target=Q-CROSS-405) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-405%3A+Optimal+reduced-order+H-infinity+approximation&target=Q-CROSS-405)

Given a continuous-time scalar real-rational transfer function G of McMillan degree N, analytic in the right half-plane and bounded on the imaginary axis, and an integer n < N, find a stable real-rational A of degree n minimizing sup over real ω of |G(iω) − A(iω)|. The source accepts an exact minimizer or an algorithm proved to converge to one.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The 2002 source states the scalar continuous-time problem and requires global optimality. It distinguishes finding the approximant from computing the distance or a suboptimal model. The later discrete-time construction cited here has a prescribed order drop tied to the smallest Hankel singular value.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-26 literature check identifies the publications, versions and limits covered.

**Scope limits:** Use H-infinity error on the imaginary axis, the source's exact degree convention, and the scalar real-rational continuous-time class.

**Information still needed**

- Check general global algorithms and attainment for the source's exact-degree class.
- A restricted-order construction needs a proof of applicability and convergence before it can answer the general question.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [On H-Infinity Model Reduction for Discrete-Time LTI Systems Using LMIs](../sources.md#src-phys-910).

**Exact locator:** Antoulas and Astolfi, MTNS Problem 2, section 2.1, equation (2.1) and footnotes 1–2. Ebihara, Hirai and Hagiwara (2006), abstract and section I.

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could search rational approximants and derive independently checkable lower bounds. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Restore the input class and success criterion and distinguish the restricted-order result.

**Search scope:** Use H-infinity error on the imaginary axis, the source's exact degree convention, and the scalar real-rational continuous-time class.

<details>
<summary>Previous indexed wording</summary>

Find a globally optimal stable rational approximation of prescribed lower McMillan degree in H-infinity norm.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 2, equation (2.1), footnotes 1 and 2. Explicitly defines the scalar continuous-time problem and accepts a convergent algorithm.
- [On H-Infinity Model Reduction for Discrete-Time LTI Systems Using LMIs](../sources.md#src-phys-910) — Abstract and section I. Reports construction of an optimal discrete-time approximant for an order reduction equal to the multiplicity of the smallest Hankel singular value.

**Limits and remaining work**

- This search did not settle the current general status. A frequency-grid error or a Hankel-norm optimum does not certify the required H-infinity optimum.

<details>
<summary>Search queries</summary>

- optimal H infinity model reduction global minimizer model reduction fixed order H infinity optimal approximant discrete time SISO globally optimal H infinity norm model reduction MTNS 2002 problem


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source asks for global H-infinity optimality at fixed reduced McMillan degree. A local optimization method or an error bound does not meet this target. No matching general resolution was established by the scoped search.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 2, section 2.1, pp. 73–76; A. C. Antoulas and A. Astolfi. Identifies the historical target.

**Limits and remaining work**

- Review later global rational-approximation results and specify input representation and attainment assumptions.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "optimal" "H-infinity" "model reduction" "global" 2024 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
