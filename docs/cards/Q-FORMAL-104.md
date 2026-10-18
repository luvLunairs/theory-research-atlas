# Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How dense must a network be to make identical phase oscillators synchronize from almost all starting phases? Three quarters of all possible neighbors is sufficient; proving that this universal threshold cannot be lowered remains open.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics) |
| Related fields | [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For finite simple undirected graphs with identical natural frequencies and unit positive edge coupling, let mu_c be the infimum of thresholds guaranteeing convergence to the all-in-phase state from almost every initial phase configuration whenever minimum degree/(n-1) exceeds the threshold. Determine whether mu_c = 3/4. This concerns nonlinear almost-everywhere global synchronization, not merely the absence of positive eigenvalues at selected equilibria.

**Required output:** Develop a proof of sharpness or a stronger universal synchronization theorem. A bounded first deliverable is a fully checkable stable nonsynchronized equilibrium certificate or a precisely delimited list of inconclusive or unstable cases.

**Scope:** The literature target ranges over all finite graphs. A curator-proposed first milestone explores connected circulants with 8≤n≤32 and twisted equilibria theta_j=2pi qj/n, 1≤q&lt;n. At most 1,000 declared (graph,q) pairs are considered. This family and cap are not asserted novel or sufficient to settle the threshold.

### Assumptions

- A finite simple undirected graph with n≥2, adjacency A_ij∈{0,1}, no loops, and minimum-degree density delta(G)/(n−1).
- Identical natural frequencies are removed by a rotating frame; theta_dot_i=sum_j A_ij sin(theta_j−theta_i). Coupling is positive and unweighted.
- Phases lie on a torus. Uniform phase rotation is a symmetry; stability statements must be interpreted after quotienting that direction.
- Global synchronization means convergence to equal phases from almost every initial phase, with respect to torus Lebesgue measure.

### Success criteria

1. Record the graph, connectivity, degree, phase pattern and exact equilibrium equations.
2. To certify a useful local obstruction, prove the Jacobian is strictly negative definite on the complement of the uniform-rotation vector. Explain why this gives an open basin and defeats almost-everywhere synchronization.
3. If any additional eigenvalue is zero, report nonlinear stability as unresolved unless a separate nonlinear argument is supplied.
4. Report the achieved degree density exactly and compare it with prior constructions. A finite example or failed search does not establish mu_c=3/4.

### Background needed

- Kuramoto gradient dynamics, equilibria and stability modulo a continuous symmetry.
- Circulant matrices, Fourier diagonalization and exact algebraic or certified interval arithmetic.
- The difference between an equilibrium, a local minimum, a second-order critical point and almost-everywhere convergence.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Suggested pilot cap: 1,000 (graph,q) pairs, n≤32, one CPU-hour and 8 GiB memory, with timeouts marked unresolved. These are proposed limits, not benchmarks. Small circulant spectra support inexpensive numerical filtering, but exact sign certificates and proofs about all graph sizes may be substantially harder.

**Data:** Explicit adjacency matrices and exact phase parameters; no observed time series is required.

**Experiments:** None for the homogeneous graph model. Testing real oscillator networks requires measured frequencies, coupling, noise and model adequacy.

**Theory and model requirements:** Identical frequencies, unit positive symmetric coupling, deterministic sine interaction, finite simple graphs and almost-everywhere initial phases.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Reconstruct A from the saved edge list, verify simplicity, symmetry and connectivity, and compute delta(G)/(n−1) exactly.
2. Check every equilibrium residual using exact trigonometric identities; floating-point cancellation is insufficient.
3. Construct J_ij=A_ij cos(theta_j−theta_i) off diagonal and J_ii=−sum_(j≠i)J_ij independently from the search routine.
4. Verify the rotation zero mode and exact strict negativity on its orthogonal complement with a separate algebraic or certified-interval implementation.
5. Explain the nonlinear implication of strict reduced stability, and have a dynamics specialist audit any extra-zero case.
6. Compare any claimed density improvement or graph family against the cited constructions and later literature before naming it new.

**Statement alignment:** Retain unit symmetric coupling, identical frequencies, density divided by n−1 and almost-everywhere convergence. Stable nonuniform equilibria are sufficient obstructions; marginal critical points alone are not.

**Human review difficulty:** Medium for a strict finite-dimensional certificate after conventions are fixed; high for marginal equilibria, graph-size limits or a universal threshold proof.

### Formal validity and empirical support

**What the formal task can establish:** Any certificate establishes a fact only for the specified homogeneous Kuramoto equations and graph. Strict reduced stability has a mathematical local-basin interpretation.

**Empirical support and limits:** Real synchronization depends on frequency mismatch, weights, noise and the adequacy of sine coupling. This formal task supplies no observational or experimental support for those assumptions.

### Methods and obstacles

**Proposed methods:**

- Symmetry-guided graph construction and twisted equilibria.
- Exact Fourier spectra over cyclotomic fields, or rigorous interval enclosures with justified sign separation.
- Independent rational or algebraic certificates for the reduced Jacobian.
- Minimal-obstruction analysis and nonlinear normal-form arguments when strict stability fails.

**Expected obstacles:**

- Absence of positive Jacobian eigenvalues does not establish nonlinear attraction when additional zero eigenvalues occur.
- A few stable examples cannot prove sharpness without a sequence approaching the threshold.
- A theorem about local minima needs careful comparison with the dynamical almost-everywhere definition.

### Checks still needed

- Establish whether a proposed finite family or density has already been classified.
- Determine nonlinear behavior separately whenever the reduced Jacobian is singular.
- Refresh lower-bound constructions before any bound-improvement claim; no historical lower bound is designated current.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The 2021 paper proves the upper bound; the August 2026 follow-up still calls sharpness conjectural. Targeted later-work searches found no resolution. This is a dated source-supported status, not an exhaustive novelty audit. No historical lower bound is asserted as current.

**Exact problem / theorem locator:** Kassabov et al., abstract and Sections I, VI; McRae (2026 v2), Section 3.4.3

### Sources

- [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104). Alex Townsend; Michael Stillman; Steven H. Strogatz. 2020. [Read source](https://arxiv.org/html/1906.10627v4).
  - **Relevant sections:** Section II, equations (1), (4), (5); Section II.1 Ring network; Section III.1
  - **Source limitations:** Year refers to the inspected 17 June 2020 version. Historical density bounds are not presented as current; the HTML typesetting date is not the research publication date.
- [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105). Martin Kassabov; Steven H. Strogatz; Alex Townsend. 2021. [Read source](https://arxiv.org/html/2105.11406v1).
  - **Relevant sections:** Abstract; Sections I, V and VI
  - **Source limitations:** The inspected arXiv version is dated 24 May 2021. Its lower-bound summary is historical; the 2026 follow-up is checked separately.
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106). Andrew D. McRae. 2026. [Read source](https://arxiv.org/html/2503.18801v2).
  - **Relevant sections:** Version 2 dated 21 August 2026; Section 1.2, Section 3.4.3 Dense graphs and Section 3.4.4
  - **Source limitations:** This preprint is evidence of the authors' reported results and status, not an independent verification of all proofs or a complete survey.

### Known results and partial progress

- Kassabov, Strogatz and Townsend prove the sufficient 3/4 density threshold.
- McRae's August 2026 Section 3.4.3 still describes sharpness as conjectural.
- Townsend, Stillman and Strogatz provide explicit circulant constructions and spectra. Examples approaching 3/4 with marginal second-order conditions are not automatically stable nonlinear obstructions.

**Research value:** A sharp threshold would connect graph density with a global nonlinear property. Small certified constructions can guide a structural argument, but duplicating a known family does not improve the bound.

### Related problems

- **Calibrated by:** [Check twisted-state spectra on Kuramoto cycle networks](../candidates.md#q-formal-103). The cycle-spectrum task checks phase conventions and treatment of zero eigenvalues before extending to general circulants.
- **Related to:** [Global synchronization of random cubic graphs](../candidates.md#q-model-207). Random cubic synchronization is a different asymptotic question; it does not follow from a high minimum-degree criterion.

### Scope of the status check

**Finding:** The 2021 paper proves the upper bound; the August 2026 follow-up still calls sharpness conjectural. Targeted later-work searches found no resolution. This is a dated source-supported status, not an exhaustive novelty audit. No historical lower bound is asserted as current.

**Search limits:** Dated primary-source checks and targeted later-work searches cannot establish that no unpublished or newly posted solution exists. Refresh the literature before claiming progress.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104)
- [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105)
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The 2020 circulant constructions, the 2021 density theorem and the 2026 normalized-Laplacian analysis are external records. No project search or simulation has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Alex Townsend
- Michael Stillman
- Steven H. Strogatz
- Martin Kassabov
- Andrew D. McRae

**Suggested citation:** Townsend, Stillman and Strogatz (2020), arXiv:1906.10627v4; Kassabov, Strogatz and Townsend (2021), arXiv:2105.11406v1; McRae (2026 revision), arXiv:2503.18801v2, Sections 3.4.3–3.4.4. The capped circulant pilot is curator-proposed.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

AI can suggest graph families and derive spectra while exact arithmetic checks stability. Expert review must prevent a marginal linear condition from being mistaken for a nonlinear obstruction.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions.

**Uncertainty:** The small circulant family may only recover known examples. No model has been tested and no likelihood of improving the bound is claimed.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The graph class, dynamics and degree normalization are explicit. |
| Decomposability | High | Graph generation, equilibrium verification and spectral certification are separate tasks. |
| Methods and literature | High | The sources give explicit circulant methods and sharp sufficient criteria. |
| Search / symbolic fit | High | Small structured graphs admit finite search and symbolic eigenvalue calculations. |
| Checkability | Medium | Strict spectral certificates are checkable; degenerate equilibria require nonlinear analysis. |
| Expertise needed | High | Dynamical systems and extremal graph expertise are needed. |
| Scholarly significance | High | The threshold is a meaningful global synchronization question. |
| Verification difficulty | High | Linear degeneracies and the all-graph quantifier are serious obstacles. |

**Correctness:** No project answer.

The literature supports the question; no project answer has been submitted for review.

**Novelty:** Requires future literature review.

Sharpness is source-reported open. Novelty of a small search family, finite obstruction or improved bound requires an independent literature comparison.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The complete target is an unresolved existence problem. A bounded search does not establish the general statement.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-104` |
| Duplicate key | `kuramoto-critical-connectivity-three-quarters` |
| Original domain label | Dynamics on networks and collective behavior |
| Original cross-domain labels | Dynamical systems; Extremal graph theory |
| Primary domain ID | `NET.DYNAMICS` |
| Cross-domain IDs | `MATH.DYN`, `MATH.COMB.EXT` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `finite_search`, `symbolic_derivation`, `exact_computation`, `proof`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-104.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
