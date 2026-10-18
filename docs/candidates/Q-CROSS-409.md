# Computing the best achievable delay margin

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-409 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-409%3A+Computing+the+best+achievable+delay+margin&target=Q-CROSS-409) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-409%3A+Computing+the+best+achievable+delay+margin&target=Q-CROSS-409)

When the supremum of achievable delay margins over stabilizing LTI controllers for a specified plant is finite, compute it to a prescribed accuracy.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The requested object is the supremum over all admissible LTI controllers. Published bounds or optimizations within PID or fixed-order classes would not establish the unrestricted algorithm. No matching resolution was confirmed.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** The requested object is the supremum over all admissible LTI controllers. Published bounds or optimizations within PID or fixed-order classes would not establish the unrestricted algorithm. No matching resolution was confirmed.

**Information still needed**

- Inspect general delay-margin interpolation results and their guaranteed error or completeness properties.
- Specialist assessment of the exact formulation and remaining novelty is pending.

**Primary branch:** [Robust design and verification](../domains/eng.md#eng-robust). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401).

**Exact locator:** Problem 18, section 18.1, Problem 2, pp. 112–114; Daniel E. Davison and Daniel E. Miller

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could derive low-order analytic bounds and certify optimization calculations. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

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
