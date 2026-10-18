# Exact birth–death diversity time on star graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-301 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-301%3A+Exact+birth%E2%80%93death+diversity+time+on+star+graphs&target=Q-MODEL-301) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-301%3A+Exact+birth%E2%80%93death+diversity+time+on+star+graphs&target=Q-MODEL-301)

For the mutation-free neutral birth–death process on a star with n leaves, initially all n+1 vertices have distinct types, prove or refute E[T]=n^3−n^2+n H_n, where H_n=sum_{k=1}^n 1/k. Each step chooses a reproducer uniformly and then a neighboring replacement uniformly; count every update.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2025 paper explicitly leaves this target open. Searches for the title and subsequent conjecture resolutions found no settling source; this negative search is limited.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-301: 2025. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Maintaining diversity in structured populations](../sources.md#src-model-301).

**Exact locator:** Equation (9); supplementary section 5.1.

**Potential difficulty:** High. The finite Markov chain is explicit, but a statement for every population size needs structure beyond finite enumeration.

**Possible AI role:** A tool-using assistant could derive exact recurrences, search for potential functions and generate independently checkable symbolic identities.

**Verification burden:** High. Check the update order, null updates, initial partition and the recurrence proof; simulations do not establish an asymptotic theorem.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model was evaluated. This is a method-based forecast, not a measured success rate; a narrower task and a specialist literature check are required before a research attempt.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
