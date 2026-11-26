# Largest neutral birth–death diversity time on undirected graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-302 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-302%3A+Largest+neutral+birth%E2%80%93death+diversity+time+on+undirected+graphs&target=Q-MODEL-302) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-302%3A+Largest+neutral+birth%E2%80%93death+diversity+time+on+undirected+graphs&target=Q-MODEL-302)

Determine the asymptotic order of max_G E[T] for connected simple undirected N-vertex graphs under neutral birth–death updating, starting from N distinct types without mutation. A step chooses a uniform reproducer then a uniform neighbor to replace; T counts all steps until consensus.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** Brewster et al. give order N^4 on double stars and an O(N^6 log N) upper bound over all undirected graphs for birth–death updating. Their finite enumeration does not determine the asymptotic maximum.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** PNAS Nexus, August 2025; arXiv v2, September 2025; mixed-update comparison, September 2026.

**Scope limits:** Count every replacement event, including one that copies a neighbour's existing label. All N vertices start differently labelled.

**Information still needed**

- Determine whether a matching upper bound or a slower family has been proved for this exact updating rule.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Maintaining diversity in structured populations](../sources.md#src-model-301); [Maintaining diversity in structured populations](../sources.md#src-model-800).

**Exact locator:** Brewster et al., Table 1, Discussion and Supplementary Sections 7 and 9.1.

**Potential difficulty:** High. The finite Markov chain is explicit, but a statement for every population size needs structure beyond finite enumeration.

**Possible AI role:** Compare upper bounds under this particular copying direction with the double-star lower bound.

**Verification burden:** High. Check the update order, null updates, initial partition and the recurrence proof; simulations do not establish an asymptotic theorem.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The exact maximum and a maximizing graph family were not independently established; the literature search was scoped.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Brewster et al. give order N^4 on double stars and an O(N^6 log N) upper bound over all undirected graphs for birth–death updating. Their finite enumeration does not determine the asymptotic maximum.

**Search scope:** Compared the published article and its September preprint with the later mixed-update model (Brewster et al., 2026, DOI 10.1371/journal.pcbi.1014829), which changes the update rule and initial labels.

**Inspected evidence**

- [Maintaining diversity in structured populations](../sources.md#src-model-301) — Supplementary Sections 7 and 9.1. Proves the double-star order and the general upper bound in single-event time.
- [Maintaining diversity in structured populations](../sources.md#src-model-800) — Table 1 and Discussion. Identifies the gap in the maximum for birth–death updating.

**Limits and remaining work**

- The exact maximum and a maximizing graph family were not independently established; the literature search was scoped.

<details>
<summary>Search queries</summary>

- "Brewster" "absorption time" birth-death 2026 double star diversity times sharp upper bound Moran process neutral diversity time open problem


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
