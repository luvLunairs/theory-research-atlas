# Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-104 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-104%3A+Determine+the+sharp+connectivity+threshold+for+homogeneous+Kuramoto+synchronization&target=Q-FORMAL-104)

For finite simple undirected graphs with identical natural frequencies and unit positive edge coupling, let mu_c be the infimum of thresholds guaranteeing convergence to the all-in-phase state from almost every initial phase configuration whenever minimum degree/(n-1) exceeds the threshold. Determine whether mu_c = 3/4. This concerns nonlinear almost-everywhere global synchronization, not merely the absence of positive eigenvalues at selected equilibria.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-05.

**Status basis:** The dynamical 3/4 conjecture remains source-reported open. Later papers distinguish it from a local-minimum conjecture and report new bounds; see the dated literature check. These preprint claims have not received independent review here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Primary passages from 2021, August 2026 and October 2026 were compared on 2026-11-05; see LC-Q-FORMAL-104-20261105 for scope and limits.

**Scope limits:** The original almost-everywhere dynamical target is unchanged. A result about local minima alone does not resolve it.

**Information still needed**

- Establish whether a proposed finite family or density has already been classified.
- Determine nonlinear behavior separately whenever the reduced Jacobian is singular.
- Compare proposed improvements with SRC-FORMAL-620 and subsequent work; independently review its proof and obtain the supporting scripts before claiming a reproduction.

**Primary branch:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Extremal and Ramsey theory](../domains/math.md#math-comb-ext).

**Sources:** [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104); [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105); [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106); [Graphs with connectivity 3/4 - epsilon are globally synchronizing](../sources.md#src-formal-619); [Beyond 11/16: dense Kuramoto networks that resist synchrony](../sources.md#src-formal-620).

**Exact locator:** Kassabov et al., abstract and Sections I, VI; McRae (2026 v2), Section 3.4.3; Lepsveridze and Zhang (2026), Theorem 1, footnote 1 and Remark 1; O'Keeffe (2026), Section I, footnotes 1–2 and Theorem 1

**Potential difficulty:** High. The historical dynamical sharpness question is still source-reported open. A bounded search does not establish its all-graph statement.

**Possible AI role:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions. AI can suggest graph families and derive spectra while exact arithmetic checks stability. Expert review must prevent a marginal linear condition from being mistaken for a nonlinear obstruction.

**Verification burden:** High. Linear degeneracies and the all-graph quantifier are serious obstacles.

**Resource expectations:** Experiment: None for the homogeneous graph model. Testing real oscillator networks requires measured frequencies, coupling, noise and model adequacy. Data: Explicit adjacency matrices and exact phase parameters; no observed time series is required. Computation: Suggested pilot cap: 1,000 (graph,q) pairs, n≤32, one CPU-hour and 8 GiB memory, with timeouts marked unresolved. These are proposed limits, not benchmarks. Small circulant spectra support inexpensive numerical filtering, but exact sign certificates and proofs about all graph sizes may be substantially harder. See the full card for the distinction between its pilot and the later existence construction.

**Assessment:** 2026-11-05; untested forecast. **Uncertainty:** The small circulant family may only recover known examples. The pilot has not been evaluated; external AI-assisted work does not establish its likely success.

[Read the full card](../cards/Q-FORMAL-104.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-05

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Preserve the original dynamical 3/4 question and source-reported status; do not replace it with the different local-minimum problem or silently transfer a resolution between them.

**Search scope:** Compared the historical dynamical target with two later primary preprints and targeted searches for updates or corrections; inspected theorem statements and definition caveats.

**Inspected evidence**

- [Sufficiently dense Kuramoto networks are globally synchronizing](../sources.md#src-formal-105) — Abstract and Section I. States the almost-everywhere dynamical target and the sufficient 3/4 bound.
- [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106) — Section 3.4.3. Records the historical sharpness conjecture and marginal examples.
- [Graphs with connectivity 3/4 - epsilon are globally synchronizing](../sources.md#src-formal-619) — Theorem 1, footnote 1 and Remark 1. The reported local-minimum result does not establish the dynamical extension.
- [Beyond 11/16: dense Kuramoto networks that resist synchrony](../sources.md#src-formal-620) — Section I, footnotes 1–2; Theorem 1. Reports a lower-bound improvement applicable to the retained target.

**Limits and remaining work**

- No independent proof audit or computation replay.
- The scoped search cannot exclude further results or corrections.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- Kuramoto "dynamical" "3/4" "2026"
- "2608.20010" correction OR dynamical OR synchronization
- "2610.21271" correction OR synchronization


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
