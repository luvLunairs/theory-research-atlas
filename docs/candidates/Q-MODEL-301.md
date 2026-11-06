# Exact birth–death diversity time on star graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-301 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-301%3A+Exact+birth%E2%80%93death+diversity+time+on+star+graphs&target=Q-MODEL-301) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-301%3A+Exact+birth%E2%80%93death+diversity+time+on+star+graphs&target=Q-MODEL-301)

For the mutation-free neutral birth–death process on a star with n leaves, initially all n+1 vertices have distinct types, prove or refute E[T]=n^3−n^2+n H_n, where H_n=sum_{k=1}^n 1/k. Each step chooses a reproducer uniformly and then a neighboring replacement uniformly; count every update.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The published 2025 article and its September author revision both retain the exact formula as a conjecture. Cubic-order growth is proved there; the indexed question concerns the exact expectation, with n leaves and every update counted. Targeted searches did not establish a later resolution.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Journal publication 8 August 2025; author revision 16 September 2025. Neither date is a 2026 resolution.

**Scope limits:** A mutation-free, neutral birth-death model on an unweighted star with N=n+1 vertices. The cubic order is known; the exact formula remains the source-reported target.

**Information still needed**

- A later proof or counterexample to equation (9) was not established in the scoped search.
- An exact recurrence proof must include null updates and the all-distinct initial state.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Maintaining diversity in structured populations](../sources.md#src-model-301); [Maintaining diversity in structured populations](../sources.md#src-model-800).

**Exact locator:** Published article: Stars, equation (9), Discussion and Methods; arXiv v2 supplementary section 5.1.

**Potential difficulty:** High. The finite Markov chain is explicit, but a statement for every population size needs structure beyond finite enumeration.

**Possible AI role:** A tool-using assistant could derive exact recurrences, search for potential functions and generate independently checkable symbolic identities.

**Verification burden:** High. Check an exact hitting-time argument for all n>=1, including null updates, all-distinct initial labels and N=n+1. A cubic asymptotic or simulation is not the requested formula.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** The source and time convention are confirmed. No named model was tested, and the limited search cannot establish present openness conclusively.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

The published 2025 article and its September author revision both retain the exact formula as a conjecture. Cubic-order growth is proved there; the indexed question concerns the exact expectation, with n leaves and every update counted. Targeted searches did not establish a later resolution.

**Search scope:** Read the journal article at equation (9), its Discussion and model/update definitions; compared the previously indexed author revision. Searched for the title, star formula and later proof claims.

**Inspected evidence**

- [Maintaining diversity in structured populations](../sources.md#src-model-800) — Stars, equation (9); Discussion; Methods. Retains the exact formula as a conjecture while distinguishing proved cubic growth and birth-death from death-birth updating.
- [Maintaining diversity in structured populations](../sources.md#src-model-301) — Equation (9) and supplementary section 5.1. The later author revision uses the same indexed star target.

**Limits and remaining work**

- No independent proof audit or exhaustive citation search was performed.

<details>
<summary>Search queries</summary>

- "Maintaining diversity in structured populations" "star" proof conjecture


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
