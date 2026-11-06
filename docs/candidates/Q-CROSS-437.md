# Identifying contagion mechanisms from observations

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-437 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-437%3A+Identifying+contagion+mechanisms+from+observations&target=Q-CROSS-437) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-437%3A+Identifying+contagion+mechanisms+from+observations&target=Q-CROSS-437)

Research direction: identify the observation and model assumptions under which simple contagion can be distinguished from group-dependent complex contagion. Specify contact information, exposure heterogeneity and observed infection history. The roadmap reports positive single-cascade methods as well as unresolved empirical inference problems; it does not claim that every case is open.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The roadmap retains the empirical inference challenge but describes successful discrimination in specified single-cascade settings. The 2024 primary study compares infection patterns across selected models and contact networks. These results do not supply universal identifiability with unknown or heterogeneous exposures.

**Statement check:** Needs clarification. **Status check:** Source report only.

**Source date and freshness:** Primary contagion-pattern study, 10 June 2024; roadmap, 1 April 2026. The primary study is prior work, not a post-roadmap update.

**Scope limits:** A direction with known positive and confounded cases. Superlinear apparent infection rates alone need not identify complex contagion when group transmission varies.

**Information still needed**

- Choose a concrete observation model and candidate contagion classes beyond the cited positive settings.
- Determine which contact weights, infection events and repeated cascades are actually observed.

**Primary branch:** [Network inference and multiscale structure](../domains/net.md#net-infer). **Related branches:** None recorded.

**Sources:** [Hypergraphs and simplicial complexes in focus: a roadmap for future research in higher-order interactions](../sources.md#src-cross-403); [Infection patterns in simple and complex contagion processes on networks](../sources.md#src-model-804).

**Exact locator:** Abiad et al. (2026), Sections 6.1 and 6.3, pp. 25 and 27; Contreras, Cencetti and Barrat (2024), Results and Discussion.

**Potential difficulty:** High. The target involves model choice, competing mechanisms or extrapolation; a narrow instance may be manageable, but the full research direction has no established cost bound.

**Possible AI role:** AI could derive identifiability limits and compare estimators on synthetic contagion data. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Specify observable information and nuisance heterogeneity, compare with cited successful settings, and distinguish simulated pattern separation from identifiable real-world transmission mechanisms.

**Resource expectations:** Formal comparisons and synthetic simulations can begin without new experiments. The primary article links SocioPatterns contact data and analysis code; access, licensing and reproducibility were not audited. Empirical identification may require additional contact or exposure observations.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

The roadmap retains the empirical inference challenge but describes successful discrimination in specified single-cascade settings. The 2024 primary study compares infection patterns across selected models and contact networks. These results do not supply universal identifiability with unknown or heterogeneous exposures.

**Search scope:** Compared the open-direction passage with the positive single-cascade passage and inspected the cited 2024 primary infection-pattern study. This corrects the boundary; post-roadmap work was not systematically searched.

<details>
<summary>Previous indexed wording</summary>

Determine when observations distinguish simple contagion from group-dependent complex contagion.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Hypergraphs and simplicial complexes in focus: a roadmap for future research in higher-order interactions](../sources.md#src-cross-403) — Sections 6.1 and 6.3, pp. 25 and 27. Retains empirical difficulties while recognizing single-cascade discrimination and heterogeneous-weight confounding.
- [Infection patterns in simple and complex contagion processes on networks](../sources.md#src-model-804) — Results and Discussion. Finds model-dependent infection patterns on specified empirical network substrates; does not claim universal identification.

**Limits and remaining work**

- An observation model is still needed before a precise research task can be assessed. Code and datasets were not rerun.

<details>
<summary>Search queries</summary>

- "Hypergraphs and simplicial complexes in focus" pdf
- "Nonlinear bias toward complex contagion in uncertain transmission settings"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
