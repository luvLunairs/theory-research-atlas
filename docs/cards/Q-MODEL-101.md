# Reproduce exact Moran fixation probabilities

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Calculate the chance that one mutant eventually replaces a whole idealized population. Exact finite-state calculations make the assumptions and arithmetic inspectable before more complicated evolutionary models are considered.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-101%3A+Reproduce+exact+Moran+fixation+probabilities&target=Q-MODEL-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-101%3A+Reproduce+exact+Moran+fixation+probabilities&target=Q-MODEL-101)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol) |
| Related fields | [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For a well-mixed Moran population of N=20 individuals, with no mutation and constant relative mutant fitness r in {1/2,1,2}, compute the probability that a single mutant reaches fixation before extinction. At each discrete update, choose a reproducing individual proportional to fitness and independently choose a uniformly random individual for replacement, including the reproducer. Use exact arithmetic to solve the absorbing-chain equations and reproduce u_1=(1-r^(-1))/(1-r^(-20)) for r≠1 and u_1=1/20 for r=1.

**Required output:** An exact transition specification, absorbing-probability vector for each parameter value, and a proof that its first interior entry matches the known formula.

**Scope:** Three fixed rational fitness values in a discrete-time, well-mixed Moran process. No estimation of biological fitness or extrapolation to other update rules.

### Assumptions

- The population contains exactly 20 individuals and each is mutant or wild type; mutation, migration and spatial structure are absent.
- Wild-type fitness is 1 and mutant fitness is the fixed positive number r; fitness is independent of frequency and time.
- Parent selection is proportional to fitness; replacement is independent and uniform over the original population, allowing a self-replacement event.
- State i is the number of mutants. States 0 and 20 are absorbing; the initial state is i=1.

### Success criteria

1. State all transition probabilities and show that each row sums to one with nonnegative entries.
2. Solve u_i=p_i^+u_(i+1)+p_i^0u_i+p_i^-u_(i−1), with u_0=0 and u_20=1, in exact arithmetic for each r.
3. Check every residual and boundary value exactly, and justify uniqueness by almost-sure absorption in this finite chain.
4. Compare u_1 with the cited formula; treat r=1 separately or use a justified limit.
5. Keep empirical biological applicability outside the mathematical certificate.

### Background needed

- Finite Markov chains and absorbing-state boundary equations.
- Rational arithmetic and basic linear algebra.
- The distinction between a stochastic update rule and a diffusion approximation.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Three systems with 19 unknown interior probabilities and exact rational coefficients. A local exact-arithmetic environment is a plausible resource class; runtime, memory and cost have not been measured.

**Data:** Only the stated N and r values; no sequence, clinical or experimental dataset.

**Experiments:** None for the formal calculation. Estimating fitness or checking a real population would require biological evidence and a separate task.

**Theory and model requirements:** Fixed population size, constant selection, no mutation and the specified well-mixed birth–death update.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Translate the update rule into p_i^+=r i(20−i)/(20(ri+20−i)) and p_i^-=i(20−i)/(20(ri+20−i)); derive the self-loop by subtraction.
2. Build the three exact finite systems and retain their coefficients and solution vectors.
3. Check residuals with an independently written evaluator and establish almost-sure absorption.
4. Match the source variables s=log(r), N=20 and the single-mutant initial condition.
5. Have a probability or population-genetics reviewer inspect the update rule and the scope of the conclusion.

**Statement alignment:** An exact solution certifies fixation for this transition matrix only. It does not certify Wright–Fisher dynamics, frequency-dependent selection or structured populations.

**Human review difficulty:** Low to moderate: arithmetic is finite, but a reviewer must confirm that the stochastic model matches the claimed reproduction.

### Formal validity and empirical support

**What the formal task can establish:** A finite absorbing-chain proof would establish the declared probabilities conditional on the update rule and parameters.

**Empirical support and limits:** No biological population is asserted to satisfy the assumptions; constant fitness, well-mixing and fixed population size require evidence for any application.

### Methods and obstacles

**Proposed methods:**

- Absorbing Markov-chain boundary equations
- Exact rational linear algebra
- Recurrence proof and neutral-limit checking

**Expected obstacles:**

- Confusing r with log(r), or importing a diffusion approximation as an exact finite-population result.
- Silently changing which individuals can be replaced.
- Using Monte Carlo agreement instead of an exact probability certificate.

### Checks still needed

- Select an exact-arithmetic representation and independent checker before a trial.
- Confirm that any implementation retains self-replacements; omitting them changes transition timing even when the fixation probability happens to agree.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The sources give the known formula and update rule. The population size, fitness values and exact-arithmetic deliverable are curator-selected calibration conditions.

**Exact problem / theorem locator:** McCandlish et al., equation (1) and Section 2; Adlam and Nowak, Introduction and equation (1).

### Sources

- [Formal properties of the probability of fixation: identities, inequalities and approximations](../sources.md#src-model-101). David M. McCandlish; Charles L. Epstein; Joshua B. Plotkin. 2015. [Read source](https://arxiv.org/html/1312.1673v4).
  - **Relevant sections:** Equation (1); Section 2, equation (6); Section 3, equation (14) and its neutral limit; arXiv:1312.1673v4 (2014), journal publication in Theoretical Population Biology 99 (2015), 98–113
  - **Source limitations:** The exact finite-population formula belongs to the specified Moran model. The paper separately discusses approximations for other population models; they are not interchangeable.
- [Universality of fixation probabilities in randomly structured populations](../sources.md#src-model-102). Ben Adlam; Martin A. Nowak. 2014. [Read source](https://www.nature.com/articles/srep06692).
  - **Relevant sections:** Introduction: well-mixed Moran update rule and equation (1); Scientific Reports 4, 6692 (2014)
  - **Source limitations:** The atlas calibration uses the well-mixed baseline, not the article's random-graph universality theorem. Population structure requires additional assumptions.

### Known results and partial progress

- The Moran fixation probability is a classical result; McCandlish et al. express it using s=log(r), while Adlam and Nowak use relative fitness r.
- The neutral value is the continuous limit 1/N. Formula agreement at a few parameter values is not evidence for the adequacy of a population model.

**Research value:** A compact benchmark for translating biological assumptions into an exact stochastic model. It can reveal update-rule mistakes and spurious agreement from simulation while making no novel evolutionary claim.

### Related problems

- **Related method:** [Reproduce log-concavity of Moran fixation probability](../candidates.md#q-model-104). The log-concavity calibration studies the same known single-mutant formula analytically; the present task checks its finite-chain interpretation.

### Scope of the status check

**Finding:** The exact formula and well-mixed update rule are established in the opened papers. This task makes no open-status assertion.

**Search limits:** Source verification establishes the calibration target, not an independently checked project derivation or empirical model fit.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Formal properties of the probability of fixation: identities, inequalities and approximations](../sources.md#src-model-101)
- [Universality of fixation probabilities in randomly structured populations](../sources.md#src-model-102)

</details>

<details>
<summary>Previous attempts and public records</summary>

- McCandlish, Epstein and Plotkin (2015) analyze the established fixation formula and attribute the underlying process to Moran.
- Adlam and Nowak (2014) use the well-mixed formula as a reference for structured populations.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- P. A. P. Moran (original process, credited in the inspected literature)
- David M. McCandlish
- Charles L. Epstein
- Joshua B. Plotkin
- Ben Adlam
- Martin A. Nowak

**Suggested citation:** McCandlish, D. M., Epstein, C. L. and Plotkin, J. B. (2015). Formal properties of the probability of fixation: identities, inequalities and approximations. Theoretical Population Biology 99, 98–113. https://doi.org/10.1016/j.tpb.2014.11.004. Adlam, B. and Nowak, M. A. (2014). Scientific Reports 4, 6692. https://doi.org/10.1038/srep06692.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Small exact systems, explicit update rules and a published formula provide independent checking routes. Priority concerns a future calibration, not an assessed ability to solve open evolutionary questions.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with exact rational arithmetic, elementary probability and human review of the update rule.

**Uncertainty:** No AI trial was run. A familiar formula may be reproduced from memory, so success would measure a controlled reproduction and checking task rather than novel discovery.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | All states, parameters, endpoints and update choices are fixed. |
| Decomposability | High | Transition construction, exact solution and interpretation can be reviewed separately. |
| Methods and literature | High | The sources supply the stochastic model and exact comparison formula. |
| Search / symbolic fit | High | Finite rational linear algebra supports exact residual checks. |
| Checkability | High | Every interior equation and boundary condition has a finite certificate. |
| Expertise needed | Medium | A reviewer must recognize how birth, death and population structure affect the model. |
| Scholarly significance | Medium | Useful model-translation calibration; it does not improve a biological prediction. |
| Verification difficulty | Low | Exact residual checking is small; absorption and update conventions still need explanation. |

**Correctness:** No project answer.

The cited sources support the mathematical target. No project answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

A known-result calibration with curator-selected checks; no new theorem or empirical finding is claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

Nineteen-state exact systems and explicit reference probabilities are compact; mapping the update rule remains a substantive check.

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-101` |
| Duplicate key | `moran-single-mutant-n20-exact-calibration` |
| Original domain label | Evolutionary theory |
| Original cross-domain labels | Stochastic processes |
| Primary domain ID | `BIO.EVOL` |
| Cross-domain IDs | `PROB.PROCESS` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `model_analysis`, `exact_computation`, `proof` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-101.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
