# Exact optimal attenuation in general H-infinity control

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-406 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-406%3A+Exact+optimal+attenuation+in+general+H-infinity+control&target=Q-CROSS-406) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-406%3A+Exact+optimal+attenuation+in+general+H-infinity+control&target=Q-CROSS-406)

For the continuous-time generalized plant in MTNS equation (14.1), with D11=D22=0, compute exactly the infimum gamma* of the disturbance-to-controlled-output H-infinity norm over proper internally stabilizing dynamic measurement-feedback controllers.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The exact infimum target is stated in equation (14.4), with proper internally stabilizing measurement feedback. Ordinary gamma-iteration is not an exact symbolic answer. Later exact and noniterative formulations still require comparison.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** The exact infimum target is stated in equation (14.4), with proper internally stabilizing measurement feedback. Ordinary gamma-iteration is not an exact symbolic answer. Later exact and noniterative formulations still require comparison.

**Information still needed**

- Inspect the later noniterative-computation literature and distinguish exact algebraic characterization from approximation.
- Specialist assessment of the exact formulation and remaining novelty is pending.

**Primary branch:** [Robust design and verification](../domains/eng.md#eng-robust). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401).

**Exact locator:** Problem 14, section 14.1, pp. 77–79; Ben M. Chen

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could investigate symbolic special cases and degeneracies in optimal-control equations. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The exact infimum target is stated in equation (14.4), with proper internally stabilizing measurement feedback. Ordinary gamma-iteration is not an exact symbolic answer. Later exact and noniterative formulations still require comparison.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

<details>
<summary>Previous indexed wording</summary>

Compute the exact infimum of closed-loop H-infinity disturbance gain under internally stabilizing measurement feedback.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 14, section 14.1, pp. 77–79; Ben M. Chen. Identifies the historical target.

**Limits and remaining work**

- Inspect the later noniterative-computation literature and distinguish exact algebraic characterization from approximation.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "Ben M. Chen" "optimal" "attenuation" open problem 2002 H infinity


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
