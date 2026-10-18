# Reproduce front-door identification in a latent-confounded mediator graph

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-105 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-105%3A+Reproduce+front-door+identification+in+a+latent-confounded+mediator+graph&target=Q-FORMAL-105) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-105%3A+Reproduce+front-door+identification+in+a+latent-confounded+mediator+graph&target=Q-FORMAL-105)

For a finite-valued acyclic structural causal model with observed X, M, Y, latent U, and only arrows U->X, U->Y, X->M, M->Y, derive P(y | do(X=x)) = sum_m P(m | x) sum_xprime P(y | m,xprime) P(xprime). Assume independent exogenous disturbances, well-defined interventions and strictly positive relevant observed probabilities. Identify assumptions at each step and distinguish identification from estimation or empirical confirmation of the graph.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The opened 2026 paper restates Pearl's classical sufficient criterion and formula. This is a calibration on the classical graph; the criterion is not claimed necessary and the graph is not inferred from observations.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-107: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Causal inference and identifiability](../domains/stat.md#stat-causal). **Related branches:** [Probability theory](../domains/prob.md), [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Generalization of Pearl's Front-Door Criterion](../sources.md#src-formal-107).

**Exact locator:** Wu and Robeva, Figure 1(b) and Theorem 2.5

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** A tool-using mathematical assistant could compare hypotheses, locate relevant results and propose a narrower proof, construction or counterexample task; a specialist must first select and check that task.

**Verification burden:** Unknown. The statement and source need a task-specific proof or certificate plan before an attempt.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated on this target; AI usefulness and success probability remain unmeasured.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
