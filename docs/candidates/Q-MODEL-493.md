# Three-copy undistillability of the Werner endpoint

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-493 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493)

For every integer d >= 3, is rho = (I - F/2)/(d^2 - d/2) three-copy undistillable, where F swaps the two C^d factors? Equivalently, is <psi|(rho^Gamma)^(tensor 3)|psi> >= 0 for every unit vector psi of Schmidt rank at most two across A1A2A3:B1B2B3, with Gamma the partial transpose on B?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Tomar (23 October 2026), Theorems 1.1-1.2, now claims the exact three-copy endpoint for every d>=3. The full proof and certificates have not been independently assessed here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The dated literature check records the exact source versions inspected on 2026-11-06.

**Scope limits:** The target quantifies over every d >= 3. A d=4 study is Curator-proposed; pending review. Its novelty requires a separate check, and a positive answer there is only partial progress.

**Information still needed**

- Obtain a fixed version and assess the new full-scope claim before asserting novelty.
- Inspect the analytic reductions, complete certificates and independent evaluations.

**Primary branch:** [Quantum information theory](../domains/info.md#info-quant). **Related branches:** [Functional and operator analysis](../domains/math.md#math-anal-func), [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Sharp Plücker Geometry for Three-Copy Werner Distillation](../sources.md#src-phys-011); [Three-copy undistillability of the boundary qutrit Werner state](../sources.md#src-phys-012); [A solution to 2-copy distillability of Werner states](../sources.md#src-formal-604); [Undistillability of Werner states from three, four and five copies](../sources.md#src-phys-707).

**Exact locator:** Wu and Zou, Section 1.1; Fu et al., Section 4; qutrit candidate description; Tomar, PDF p.2, Theorems 1.1-1.2.

**Potential difficulty:** High. The recent full-scope claim needs review; the previous description of remaining sectors is out of date.

**Possible AI role:** Review and reproduction of the new claim take priority over treating this target as untouched. No model has been evaluated.

**Verification burden:** High. High for a general proof; an explicit small witness is more localized but still requires statement alignment.

**Resource expectations:** Experiment: None for the formal distillability question. Data: Source definitions and any future exact candidate coefficients. Computation: Unmeasured. At d=4 the coefficient matrix has 64 rows and columns; low-rank parameterization reduces storage but does not make global optimization easy. No runtime or cost is forecast. Assumptions: Standard finite-dimensional quantum mechanics and ideal LOCC; all stated complex vectors are allowed.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No project AI attempt measured; correctness of the new claim and novelty of further work remain unresolved.

[Read the full card](../cards/Q-MODEL-493.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Unverified.

Keep the exact target unverified pending assessment of the new full-scope claim.

**Search scope:** Targeted web searches through 2026-11-06 and inspection of the listed primary statements or survey passages. This is not an exhaustive literature or acceptance audit.

**Inspected evidence**

- [Undistillability of Werner states from three, four and five copies](../sources.md#src-phys-707) — PDF p.2, Theorems 1.1-1.2. The claimed all-dimension threshold includes alpha=-1/2 and exactly three copies.

**Limits and remaining work**

- Obtain a fixed version and assess the new full-scope claim before asserting novelty.
- Inspect the analytic reductions, complete certificates and independent evaluations.
- No independent proof review or certificate execution was performed.

<details>
<summary>Search queries</summary>

- "NPT bound entanglement" "2026" solved
- "three-copy" "Werner" "2026" November
- "2607.21367" correction OR withdrawn
- "Undistillability of Werner states from three, four and five copies" correction


</details>

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
