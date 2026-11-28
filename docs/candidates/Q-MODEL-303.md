# Smallest neutral birth–death diversity time on undirected graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-303 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-303%3A+Smallest+neutral+birth%E2%80%93death+diversity+time+on+undirected+graphs&target=Q-MODEL-303) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-303%3A+Smallest+neutral+birth%E2%80%93death+diversity+time+on+undirected+graphs&target=Q-MODEL-303)

Determine the asymptotic order of min_G E[T] over connected simple undirected N-vertex graphs, initially all types distinct, for mutation-free neutral birth–death updating. Choose a uniform reproducer and then a uniform neighboring replacement; count all updates until consensus.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** The paper bounds the minimum between order N log N and order N^2. On the loopless complete graph the expected time is exactly (N-1)^2. The star reaches order N log N under the opposite update rule.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** PNAS Nexus, August 2025; arXiv v2, September 2025; mixed-update comparison, September 2026.

**Scope limits:** Use a uniform sender and a uniform neighbour as receiver. The complete-graph example uses no self-loops; the all-graphs lower bound counts distinct replacement sites.

**Information still needed**

- Find an attaining family or a stronger universal lower bound for the sender-first rule.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Maintaining diversity in structured populations](../sources.md#src-model-301); [Maintaining diversity in structured populations](../sources.md#src-model-800).

**Exact locator:** Brewster et al., Table 1, Well-mixed populations, Discussion and Supplementary Section 9.2.

**Potential difficulty:** High. The finite Markov chain is explicit, but a statement for every population size needs structure beyond finite enumeration.

**Possible AI role:** Check any candidate fast family against the update order and benchmark it against the loopless complete graph.

**Verification burden:** High. Check the update order, null updates, initial partition and the recurrence proof; simulations do not establish an asymptotic theorem.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The later mixed-update comparison does not settle this minimum; no matching result was identified in the scoped search.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

The paper bounds the minimum between order N log N and order N^2. On the loopless complete graph the expected time is exactly (N-1)^2. The star reaches order N log N under the opposite update rule.

**Search scope:** Compared the published article and its September preprint with the later mixed-update model (Brewster et al., 2026, DOI 10.1371/journal.pcbi.1014829), which changes the update rule and initial labels.

**Inspected evidence**

- [Maintaining diversity in structured populations](../sources.md#src-model-301) — Well-mixed populations, following equation (6); Supplementary Section 9.2. Separates loopless and looped complete graphs and bounds the minimum from below.
- [Maintaining diversity in structured populations](../sources.md#src-model-800) — Table 1 and Discussion. The order-matching star example applies to receiver-first updating.

**Limits and remaining work**

- The later mixed-update comparison does not settle this minimum; no matching result was identified in the scoped search.

<details>
<summary>Search queries</summary>

- "Brewster" "absorption time" birth-death 2026 double star diversity times sharp upper bound Moran process neutral diversity time open problem


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
