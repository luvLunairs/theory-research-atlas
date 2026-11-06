# Chemical recurrence for weakly reversible stochastic reaction networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-308 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-308%3A+Chemical+recurrence+for+weakly+reversible+stochastic+reaction+networks&target=Q-MODEL-308) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-308%3A+Chemical+recurrence+for+weakly+reversible+stochastic+reaction+networks&target=Q-MODEL-308)

For every finite weakly reversible reaction network with stochastic mass-action propensities and positive rate constants, is each state of the associated continuous-time count process positive recurrent? Address arbitrary species number, beyond announced two-species results, with well-posedness and nonexplosion explicit. Stoichiometric conservation and communicating classes must be retained.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The institutional project report explicitly leaves arbitrary dimension open and announces a two-species proof by Agazzi, Anderson, Cappelletti, Laurence and Mattingly. Its publication list still marks that manuscript as in preparation.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 literature check identifies the versions and passages inspected; original publication dates and earlier checks remain relevant.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Locate the full two-dimensional manuscript and check its exact assumptions before using the announced result as a theorem.
- For a new target, specify species number, communicating classes, well-posedness and nonexplosion; finite truncations cannot establish recurrence.

**Primary branch:** [Reaction-network and kinetics theory](../domains/chem.md#chem-reaction). **Related branches:** [Systems biology and biological networks](../domains/bio.md#bio-systems), [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process).

**Sources:** [Stochastically modeled weakly reversible reaction networks with a single linkage class](../sources.md#src-model-303); [Solving the chemical recurrence conjecture in two dimensions](../sources.md#src-model-304); [Results and publications — ConStRAINeD](../sources.md#src-phys-802).

**Exact locator:** Original conjecture and 2023 talk; ConStRAINeD Objective 1 and publication-list item 16.

**Potential difficulty:** Frontier. An infinite count space and boundary effects obstruct direct finite-state reasoning.

**Possible AI role:** An assistant could inspect reaction-graph subclasses, construct candidate Foster–Lyapunov functions and check symbolic drift inequalities.

**Verification burden:** High. A valid proof must cover boundary states, closed classes and explosion; finite truncations cannot certify recurrence.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy. Large state-space truncations may consume substantial memory and introduce uncontrolled boundary artifacts.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The two-species claim is an announcement with a manuscript still listed as in preparation. The arbitrary-dimensional target remains source-reported open; proof availability and later progress require rechecking.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Retain source-reported openness of the full target and make the missing proof source explicit.

**Search scope:** Targeted searches and inspection of the cited passages on 2026-11-06; neither an exhaustive literature search nor an independent scientific review.

**Inspected evidence**

- [Results and publications — ConStRAINeD](../sources.md#src-phys-802) — Objective 1; In preparation, item 16. Separates the announced two-species result from the unresolved arbitrary-dimensional conjecture and identifies the five authors.

**Limits and remaining work**

- The project page is undated and mutable.
- No full manuscript, recurrence argument or explosion analysis was independently checked.

<details>
<summary>Search queries</summary>

- "chemical recurrence conjecture" 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
