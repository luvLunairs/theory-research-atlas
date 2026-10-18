# Chemical recurrence for weakly reversible stochastic reaction networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-308 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-308%3A+Chemical+recurrence+for+weakly+reversible+stochastic+reaction+networks&target=Q-MODEL-308) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-308%3A+Chemical+recurrence+for+weakly+reversible+stochastic+reaction+networks&target=Q-MODEL-308)

For every finite weakly reversible reaction network with stochastic mass-action propensities and positive rate constants, is each state of the associated continuous-time count process positive recurrent? Address arbitrary species number, beyond announced two-species results, with well-posedness and nonexplosion explicit. Stoichiometric conservation and communicating classes must be retained.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The general conjecture is explicit in the paper; the author's later abstract reports a two-species solution. Searches found later two-dimensional announcements, not a general-dimensional theorem.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-303: 2020, SRC-MODEL-304: 2023. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Reaction-network and kinetics theory](../domains/chem.md#chem-reaction). **Related branches:** [Systems biology and biological networks](../domains/bio.md#bio-systems), [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process).

**Sources:** [Stochastically modeled weakly reversible reaction networks with a single linkage class](../sources.md#src-model-303); [Solving the chemical recurrence conjecture in two dimensions](../sources.md#src-model-304).

**Exact locator:** 2020 introduction and section 3; Cappelletti's 2023 two-dimensional talk abstract.

**Potential difficulty:** Frontier. An infinite count space and boundary effects obstruct direct finite-state reasoning.

**Possible AI role:** An assistant could inspect reaction-graph subclasses, construct candidate Foster–Lyapunov functions and check symbolic drift inequalities.

**Verification burden:** High. A valid proof must cover boundary states, closed classes and explosion; finite truncations cannot certify recurrence.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy. Large state-space truncations may consume substantial memory and introduce uncontrolled boundary artifacts.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model was evaluated. This is a method-based forecast, not a measured success rate; a narrower task and a specialist literature check are required before a research attempt.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
