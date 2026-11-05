# Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How dense must a network be to make identical phase oscillators synchronize from almost all starting phases? The historical target is whether three quarters is sharp for this dynamical guarantee. A weaker condition, absence of nonsynchronous local minima, must be assessed separately.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics) |
| Related fields | [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-11-05 |
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

**Computing:** Suggested pilot cap: 1,000 (graph,q) pairs, n≤32, one CPU-hour and 8 GiB memory, with timeouts marked unresolved. These are proposed limits, not benchmarks. Small circulant spectra support inexpensive numerical filtering, but exact sign certificates and proofs about all graph sizes may be substantially harder. SRC-FORMAL-620, Section V, describes an existence construction with more than 9×10^84 vertices; the pilot is not a direct reproduction of those graphs.

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
- Compare proposed improvements with SRC-FORMAL-620 and subsequent work; independently review its proof and obtain the supporting scripts before claiming a reproduction.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The dynamical 3/4 conjecture remains source-reported open. Later papers distinguish it from a local-minimum conjecture and report new bounds; see the dated literature check. These preprint claims have not received independent review here.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-104.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Kassabov et al., abstract and Sections I, VI; McRae (2026 v2), Section 3.4.3; Lepsveridze and Zhang (2026), Theorem 1, footnote 1 and Remark 1; O'Keeffe (2026), Section I, footnotes 1–2 and Theorem 1

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
- [Graphs with connectivity 3/4 - epsilon are globally synchronizing](../sources.md#src-formal-619). Saba Lepsveridze; Sam Zhang. 2026. [Read source](https://arxiv.org/html/2608.20010v1).
  - **Relevant sections:** 20 August 2026; Section 1, footnote 1, Theorem 1 and Section 6, Remark 1
  - **Source limitations:** Primary claim only; proof correctness and independent acceptance were not assessed.
- [Beyond 11/16: dense Kuramoto networks that resist synchrony](../sources.md#src-formal-620). Kevin P. O'Keeffe. 2026. [Read source](https://arxiv.org/html/2610.21271v1).
  - **Relevant sections:** 15 October 2026; Section I, equations (2)–(3), footnotes 1–2; Section V, Theorem 1, Proposition 1 and Lemmas 1–2
  - **Source limitations:** Proofs and interval certificates were not independently checked; the cited scripts were not obtained or run.

### Known results and partial progress

- Kassabov, Strogatz and Townsend prove the sufficient 3/4 density threshold.
- McRae's August 2026 Section 3.4.3 records the historical sharpness conjecture; later sources below distinguish its formulations.
- Townsend, Stillman and Strogatz provide explicit circulant constructions and spectra. Examples approaching 3/4 with marginal second-order conditions are not automatically stable nonlinear obstructions.
- Lepsveridze and Zhang (SRC-FORMAL-619) report a strict upper bound below 3/4 for the local-minimum threshold, refuting that version of the conjecture. Their normalization is (delta+1)/n; Remark 1 leaves the dynamical extension unfinished.
- O'Keeffe (SRC-FORMAL-620) reports a lower bound mu_0=(4+2q*)/(7+q*)=0.6929077063... for both thresholds. Here q* is the unique root in (0,1) of 9q^8+72q^7+288q^6+448q^5+470q^4+88q^3−208q^2−128q−15. Section I retains 3/4 as the dynamical upper bound.

**Research value:** A sharp threshold would connect graph density with a global nonlinear property. Small certified constructions can guide a structural argument, but duplicating a known family does not improve the bound.

### Related problems

- **Calibrated by:** [Check twisted-state spectra on Kuramoto cycle networks](../candidates.md#q-formal-103). The cycle-spectrum task checks phase conventions and treatment of zero eigenvalues before extending to general circulants.
- **Related to:** [Global synchronization of random cubic graphs](../candidates.md#q-model-207). Random cubic synchronization is a different asymptotic question; it does not follow from a high minimum-degree criterion.

### Scope of the status check

**Finding:** The scoped update supports retaining the exact dynamical question. It does not certify any new proof or establish an exhaustive current status.

**Search limits:** Checked identified primary passages and targeted update searches. No independent proof audit, certificate replay or exhaustive novelty review was performed.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- Kuramoto "dynamical" "3/4" "2026"
- "2608.20010" correction OR dynamical OR synchronization
- "2610.21271" correction OR synchronization

**Sources checked:**

- [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105)
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106)
- [Graphs with connectivity 3/4 - epsilon are globally synchronizing](../sources.md#src-formal-619)
- [Beyond 11/16: dense Kuramoto networks that resist synchrony](../sources.md#src-formal-620)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The 2020 circulant constructions, the 2021 density theorem and the 2026 normalized-Laplacian analysis are external records. No project search or simulation has been run.
- The 2026 preprints SRC-FORMAL-619 and SRC-FORMAL-620 supply later external results. O'Keeffe reports AI-assisted research; its proofs and computations have not been reproduced here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Alex Townsend
- Michael Stillman
- Steven H. Strogatz
- Martin Kassabov
- Andrew D. McRae
- Saba Lepsveridze
- Sam Zhang
- Kevin P. O'Keeffe

**Suggested citation:** Townsend, Stillman and Strogatz (2020), arXiv:1906.10627v4; Kassabov, Strogatz and Townsend (2021), arXiv:2105.11406v1; McRae (2026 revision), arXiv:2503.18801v2, Sections 3.4.3–3.4.4. The capped circulant pilot is curator-proposed. Later results: Lepsveridze and Zhang (20 August 2026), arXiv:2608.20010v1; O'Keeffe (15 October 2026), arXiv:2610.21271v1.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-11-05.

AI can suggest graph families and derive spectra while exact arithmetic checks stability. Expert review must prevent a marginal linear condition from being mistaken for a nonlinear obstruction.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions.

**Uncertainty:** The small circulant family may only recover known examples. The pilot has not been evaluated; external AI-assisted work does not establish its likely success.

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

The exact dynamical target is retained. Novelty of any proposed family, obstruction or improvement requires comparison with the later sources and subsequent work.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The historical dynamical sharpness question is still source-reported open. A bounded search does not establish its all-graph statement.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-11-05 | Added later sources and clarified their distinct threshold definitions; preserved the original dynamical statement and pending human review. |

</details>

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
