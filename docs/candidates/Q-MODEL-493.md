# Three-copy undistillability of the Werner endpoint

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-493 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493)

For every integer d >= 3, is rho = (I - F/2)/(d^2 - d/2) three-copy undistillable, where F swaps the two C^d factors? Equivalently, is <psi|(rho^Gamma)^(tensor 3)|psi> >= 0 for every unit vector psi of Schmidt rank at most two across A1A2A3:B1B2B3, with Gamma the partial transpose on B?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** The primary sources leave the unrestricted three-copy question open. A later unreviewed d=3 candidate is retained as a claim, not an established answer. The scoped search found no resolution covering all d >= 3.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Wu and Zou, Section 1.1, equations (1)-(3); Fu, Gao and Park, Section 4; Zenodo candidate description. Source versions and dates appear in the source catalog.

**Scope limits:** The target quantifies over every d >= 3. A d=4 study is Curator-proposed; pending review. Its novelty requires a separate check, and a positive answer there is only partial progress.

**Information still needed**

- Audit the recent sector proofs.
- Inspect the d=3 candidate and its certificate.
- Refresh later literature before research or submission.

**Primary branch:** [Quantum information theory](../domains/info.md#info-quant). **Related branches:** [Functional and operator analysis](../domains/math.md#math-anal-func), [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Sharp Plücker Geometry for Three-Copy Werner Distillation](../sources.md#src-phys-011); [Three-copy undistillability of the boundary qutrit Werner state](../sources.md#src-phys-012); [A solution to 2-copy distillability of Werner states](../sources.md#src-formal-604).

**Exact locator:** Wu and Zou, Section 1.1, equations (1)-(3); Fu, Gao and Park, Section 4; Zenodo candidate description.

**Potential difficulty:** High. Global nonconvex inequalities remain beyond the reported sectors.

**Possible AI role:** The explicit algebra permits symbolic checks and candidate generation, but the unresolved nonnormal sector and recent claims require careful preparation. No model evaluated. Assumes tool-using AI able to inspect literature, manipulate mathematical expressions and retain reproducible calculations.

**Verification burden:** High. High for a general proof; an explicit small witness is more localized but still requires statement alignment.

**Resource expectations:** Experiment: None for the formal distillability question. Data: Source definitions and any future exact candidate coefficients. Computation: Unmeasured. At d=4 the coefficient matrix has 64 rows and columns; low-rank parameterization reduces storage but does not make global optimization easy. No runtime or cost is forecast. Assumptions: Standard finite-dimensional quantum mechanics and ideal LOCC; all stated complex vectors are allowed.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** No AI attempt measured; feasible search size and novelty of restrictions remain uncertain.

[Read the full card](../cards/Q-MODEL-493.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The primary sources leave the unrestricted three-copy question open. A later unreviewed d=3 candidate is retained as a claim, not an established answer. The scoped search found no resolution covering all d >= 3.

**Search scope:** Opened the cited primary passages and metadata, then searched for subsequent results through 2026-10-20.

**Inspected evidence**

- [Sharp Plücker Geometry for Three-Copy Werner Distillation](../sources.md#src-phys-011) — Section 1.1, equations (1)-(3), Sections 6-7. The unrestricted endpoint remains separate from the reported sectors.
- [Three-copy undistillability of the boundary qutrit Werner state](../sources.md#src-phys-012) — Version 1.1.0-candidate landing-page description. A d=3 candidate is reported; its proof and certificate were not inspected.
- [A solution to 2-copy distillability of Werner states](../sources.md#src-formal-604) — Theorem 1.1 and Section 4, v3. The reported two-copy threshold does not settle higher copies.

**Limits and remaining work**

- Searches are bounded; the anonymous deposit's attachments could not be inspected. No independent proof review was performed.

<details>
<summary>Search queries</summary>

- "three-copy" "Werner" "2026"
- "three-copy" "Werner" "four" 2026
- "Werner" "2608.02647" solution
- "Werner" "three-copy" "undistillability" October 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
