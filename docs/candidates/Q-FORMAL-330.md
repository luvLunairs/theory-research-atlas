# A deterministic factor-2 approximation for tournament feedback vertex set

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-330 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-330%3A+A+deterministic+factor-2+approximation+for+tournament+feedback+vertex+set&target=Q-FORMAL-330) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-330%3A+A+deterministic+factor-2+approximation+for+tournament+feedback+vertex+set&target=Q-FORMAL-330)

Given a tournament with nonnegative rational vertex weights, find deterministically in polynomial time a feedback vertex set of weight at most twice the optimum.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The September 2026 paper gives (2+ε) for each fixed ε>0 and explicitly leaves the exact deterministic factor-2 question.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-321: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Algorithms and data structures](../domains/cs.md#cs-alg). **Related branches:** [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [A deterministic (2+ε)-approximation for directed feedback vertex sets in tournaments](../sources.md#src-formal-321).

**Exact locator:** Ghorbani–Mnich, abstract, section 1.1 and section 2.

**Potential difficulty:** High. The approximation gap is narrow, but taking a limit of approximation schemes does not preserve polynomial runtime.

**Possible AI role:** Test local-ratio or rounding lemmas against exhaustively solved small tournaments, then seek a symbolic worst-case guarantee.

**Verification burden:** High. Feasibility is easy to check; the factor-2 bound requires a valid comparison with the unknown optimum on every input.

**Resource expectations:** No physical experiment or external data is needed. Tiny tournaments admit exact optimization; exhaustive labeled searches grow as 2^{n(n−1)/2}. Use a declared size limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
