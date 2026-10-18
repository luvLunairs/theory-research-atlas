# Check twisted-state spectra on Kuramoto cycle networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A ring of identical oscillators supports synchronized and twisted phase patterns. A known spectrum provides a compact test of instability, stability up to common rotation, and cases where linearization cannot decide.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-103%3A+Check+twisted-state+spectra+on+Kuramoto+cycle+networks&target=Q-FORMAL-103) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-103%3A+Check+twisted-state+spectra+on+Kuramoto+cycle+networks&target=Q-FORMAL-103)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics) |
| Related fields | [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Combinatorics and discrete mathematics](../domains/math.md#math-comb) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For the simple undirected cycle C_n, n &gt;= 3, consider theta_dot_j = sin(theta_(j-1)-theta_j) + sin(theta_(j+1)-theta_j), with indices modulo n and phases modulo 2 pi. Reproduce the equilibrium and Jacobian spectrum for theta_j = 2 pi q j/n, 0 &lt;= q &lt;= floor(n/2), and classify linear stability modulo uniform rotation. Build an exact sign table only for 3 &lt;= n &lt;= 20. Extra zero eigenvalues must be labeled inconclusive for nonlinear stability. The finite range is curator chosen.

**Required output:** The known spectral derivation, exact finite sign certificates and an explicit treatment of rotational symmetry.

**Scope:** Reproduce the general cycle formula, then classify signs only for 3 &lt;= n &lt;= 20 and 0 &lt;= q &lt;= floor(n/2). Other graphs, all-equilibrium classification and nonlinear degenerate-case analysis are outside scope.

### Assumptions

- Use a simple undirected cycle, n &gt;= 3, identical frequencies removed by a rotating frame, and unit positive edge coupling.
- The phase ODE has no noise, delay, inertia or frequency heterogeneity.
- Commonly rotated configurations represent the same relative-phase state.
- Use the dynamics Jacobian; a potential-Hessian sign convention must be translated explicitly.

### Success criteria

1. Verify that the proposed twisted configuration is an equilibrium for the stated edges.
2. Recover J_q = -cos(2 pi q/n) L_Cn and eigenvalues 2 cos(2 pi q/n)(cos(2 pi r/n)-1), r = 0,...,n-1.
3. Separate the rotational zero eigenvalue from any additional zeros.
4. Justify finite-table signs exactly, without treating near-zero floating values as certificates.
5. A positive eigenvalue establishes instability. All nonrotational eigenvalues negative support asymptotic stability modulo rotation; extra zeros remain inconclusive for nonlinear stability.

### Background needed

- Smooth ODE linearization and stability modulo symmetry.
- Cycle Laplacians and Fourier eigenvectors.
- Exact trigonometric signs or certified algebraic-number calculations.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Symbolic differentiation and matrices of order at most twenty for the finite table. Exact trigonometric reasoning avoids numerical optimization. The bounds are chosen for inspectability; no runtime, cost or success rate has been measured.

**Data:** Cycle edges, n and q; no empirical time series.

**Experiments:** None for the idealized ODE calculation. Physical or biological comparisons require separate observations or experiments.

**Theory and model requirements:** Homogeneous first-order phase coupling on a fixed unweighted undirected cycle. Unequal frequencies, amplitude dynamics, noise and delays are outside this model.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Check adjacency and derivative signs against the ODE.
2. Independently derive the Jacobian and compare it with the Laplacian.
3. Check Fourier eigenvalues and exact finite sign certificates.
4. Review every stability label and the limits for extra-zero cases.

**Statement alignment:** The result concerns only the stated twisted equilibria. It is not an all-equilibrium classification, empirical prediction or global synchronization guarantee.

**Human review difficulty:** Moderate: short symbolic work is inspectable, but local, orbital and global behavior require dynamics expertise.

### Formal validity and empirical support

**What the formal task can establish:** The spectrum and conditional stability labels concern the homogeneous phase model with the stated symmetry convention.

**Empirical support and limits:** The calculation does not establish behavior of measured physical, biological or social networks.

### Methods and obstacles

**Proposed methods:**

- Symbolic differentiation
- Fourier diagonalization
- Exact sign classification

**Expected obstacles:**

- Incorrect cycle edge counting at small n.
- Dropping or misinterpreting the rotational zero mode.
- Rounding an exact zero into a positive or negative value.
- Inferring global synchronization from selected twisted equilibria.

### Checks still needed

- Select a representation for exact trigonometric signs before implementation.
- Have a reviewer approve terminology for asymptotic stability modulo rotation.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The spectrum is a known result in the opened paper. Later work preserves the distinction between second-order criticality and nonlinear stability. No table or simulation has been produced by this project.

**Exact problem / theorem locator:** Townsend et al., equations (4)-(5) and Section II.1; McRae, Section 1.2

### Sources

- [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104). Alex Townsend; Michael Stillman; Steven H. Strogatz. 2020. [Read source](https://arxiv.org/html/1906.10627v4).
  - **Relevant sections:** Section II, equations (1), (4), (5); Section II.1 Ring network; Section III.1
  - **Source limitations:** Year refers to the inspected 17 June 2020 version. Historical density bounds are not presented as current; the HTML typesetting date is not the research publication date.
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106). Andrew D. McRae. 2026. [Read source](https://arxiv.org/html/2503.18801v2).
  - **Relevant sections:** Version 2 dated 21 August 2026; Section 1.2, Section 3.4.3 Dense graphs and Section 3.4.4
  - **Source limitations:** This preprint is evidence of the authors' reported results and status, not an independent verification of all proofs or a complete survey.

### Known results and partial progress

- The source supplies the twisted equilibria and circulant Jacobian, including the nearest-neighbor cycle specialization.
- Rotational symmetry contributes a necessary zero mode.
- Later work distinguishes second-order critical points from stable nonlinear equilibria.

**Research value:** Creates a transparent baseline for network stability studies and prevents local numerical spectra from being mistaken for global synchronization proofs.

### Related problems

- **Calibration for:** [Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](../candidates.md#q-formal-104). Cycle spectra prepare local-stability methods used in connectivity studies, but do not settle the dense-network threshold or nonlinear degenerate cases.

### Scope of the status check

**Finding:** The original spectrum and cycle specialization were checked alongside the 2026 distinction between stable equilibria and second-order critical points.

**Search limits:** This known-result calibration does not resolve degenerate nonlinear dynamics. Later-work searches are not a complete audit of all graph families.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104)
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Townsend, Stillman and Strogatz analyze these spectra in the literature. No independent atlas computation or AI trial is recorded.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Alex Townsend
- Michael Stillman
- Steven H. Strogatz
- Andrew D. McRae

**Suggested citation:** Townsend, A., Stillman, M., and Strogatz, S. H. (2020 version), Dense networks that do not synchronize and sparse ones that do, arXiv:1906.10627v4, Section II. Later context: McRae, A. D. (2026 version), arXiv:2503.18801v2, Sections 1.2 and 3.4.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The known formula and a bounded exact table independently check symbolic reasoning and symmetry handling without relying on trajectories as proof.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI that can read mathematical sources, produce inspectable symbolic work and code, and work with a human domain reviewer.

**Uncertainty:** No model calculation or simulation has been tested. Degenerate cases intentionally receive no nonlinear verdict.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The ODE, equilibria, spectral target and finite range are explicit. |
| Decomposability | High | Equilibrium checking, differentiation, diagonalization and sign classification are separate. |
| Methods and literature | High | The paper gives an explicit formula and standard circulant-matrix methods. |
| Search / symbolic fit | High | Differentiation and exact signs suit symbolic tools. |
| Checkability | High | The analytic formula and small cases allow independent review. |
| Expertise needed | Medium | A dynamics reviewer must handle the symmetry quotient and degenerate cases. |
| Scholarly significance | Medium | This is a verification baseline rather than a new synchronization result. |
| Verification difficulty | Medium | The algebra is compact, but a wrong stability interpretation would overstate the result. |

**Correctness:** No project answer.

The cited literature supports the calibration target. No project answer has been submitted for review.

**Novelty:** Not claimed.

This is a known-result calibration. The chosen bounds and presentation are not claims of scientific novelty.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-103` |
| Duplicate key | `homogeneous-kuramoto-cycle-twisted-state-spectrum` |
| Original domain label | Dynamics on networks and collective behavior |
| Original cross-domain labels | Dynamical systems; Spectral graph theory |
| Primary domain ID | `NET.DYNAMICS` |
| Cross-domain IDs | `MATH.DYN`, `MATH.COMB` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `symbolic_derivation`, `exact_computation`, `classification`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-103.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
