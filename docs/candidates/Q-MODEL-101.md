# Reproduce exact Moran fixation probabilities

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-101 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-101%3A+Reproduce+exact+Moran+fixation+probabilities&target=Q-MODEL-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-101%3A+Reproduce+exact+Moran+fixation+probabilities&target=Q-MODEL-101)

For a well-mixed Moran population of N=20 individuals, with no mutation and constant relative mutant fitness r in {1/2,1,2}, compute the probability that a single mutant reaches fixation before extinction. At each discrete update, choose a reproducing individual proportional to fitness and independently choose a uniformly random individual for replacement, including the reproducer. Use exact arithmetic to solve the absorbing-chain equations and reproduce u_1=(1-r^(-1))/(1-r^(-20)) for r≠1 and u_1=1/20 for r=1.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The sources give the known formula and update rule. The population size, fitness values and exact-arithmetic deliverable are curator-selected calibration conditions.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-101: 2015, SRC-MODEL-102: 2014. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Select an exact-arithmetic representation and independent checker before a trial.
- Confirm that any implementation retains self-replacements; omitting them changes transition timing even when the fixation probability happens to agree.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process).

**Sources:** [Formal properties of the probability of fixation: identities, inequalities and approximations](../sources.md#src-model-101); [Universality of fixation probabilities in randomly structured populations](../sources.md#src-model-102).

**Exact locator:** McCandlish et al., equation (1) and Section 2; Adlam and Nowak, Introduction and equation (1).

**Potential difficulty:** Medium. Nineteen-state exact systems and explicit reference probabilities are compact; mapping the update rule remains a substantive check.

**Possible AI role:** No named model evaluated; assumes tool-using AI with exact rational arithmetic, elementary probability and human review of the update rule. Small exact systems, explicit update rules and a published formula provide independent checking routes. Priority concerns a future calibration, not an assessed ability to solve open evolutionary questions.

**Verification burden:** Low. Exact residual checking is small; absorption and update conventions still need explanation.

**Resource expectations:** Experiment: None for the formal calculation. Estimating fitness or checking a real population would require biological evidence and a separate task. Data: Only the stated N and r values; no sequence, clinical or experimental dataset. Computation: Three systems with 19 unknown interior probabilities and exact rational coefficients. A local exact-arithmetic environment is a plausible resource class; runtime, memory and cost have not been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No AI trial was run. A familiar formula may be reproduced from memory, so success would measure a controlled reproduction and checking task rather than novel discovery.

[Read the full card](../cards/Q-MODEL-101.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
