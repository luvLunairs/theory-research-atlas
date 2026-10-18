# Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-104 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104)

For finite simple undirected graphs with identical natural frequencies and unit positive edge coupling, let mu_c be the infimum of thresholds guaranteeing convergence to the all-in-phase state from almost every initial phase configuration whenever minimum degree/(n-1) exceeds the threshold. Determine whether mu_c = 3/4. This concerns nonlinear almost-everywhere global synchronization, not merely the absence of positive eigenvalues at selected equilibria.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2021 paper proves the upper bound; the August 2026 follow-up still calls sharpness conjectural. Targeted later-work searches found no resolution. This is a dated source-supported status, not an exhaustive novelty audit. No historical lower bound is asserted as current.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-104: 2020, SRC-FORMAL-105: 2021, SRC-FORMAL-106: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Establish whether a proposed finite family or density has already been classified.
- Determine nonlinear behavior separately whenever the reduced Jacobian is singular.
- Refresh lower-bound constructions before any bound-improvement claim; no historical lower bound is designated current.

**Primary branch:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Extremal and Ramsey theory](../domains/math.md#math-comb-ext).

**Sources:** [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104); [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105); [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106).

**Exact locator:** Kassabov et al., abstract and Sections I, VI; McRae (2026 v2), Section 3.4.3

**Potential difficulty:** High. The complete target is an unresolved existence problem. A bounded search does not establish the general statement.

**Possible AI role:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions. AI can suggest graph families and derive spectra while exact arithmetic checks stability. Expert review must prevent a marginal linear condition from being mistaken for a nonlinear obstruction.

**Verification burden:** High. Linear degeneracies and the all-graph quantifier are serious obstacles.

**Resource expectations:** Experiment: None for the homogeneous graph model. Testing real oscillator networks requires measured frequencies, coupling, noise and model adequacy. Data: Explicit adjacency matrices and exact phase parameters; no observed time series is required. Computation: Suggested pilot cap: 1,000 (graph,q) pairs, n≤32, one CPU-hour and 8 GiB memory, with timeouts marked unresolved. These are proposed limits, not benchmarks. Small circulant spectra support inexpensive numerical filtering, but exact sign certificates and proofs about all graph sizes may be substantially harder.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The small circulant family may only recover known examples. No model has been tested and no likelihood of improving the bound is claimed.

[Read the full card](../cards/Q-FORMAL-104.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
