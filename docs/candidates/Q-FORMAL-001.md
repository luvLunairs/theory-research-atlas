# Reproduce Huang's hypercube degree theorem

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-001 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-001%3A+Reproduce+Huang%27s+hypercube+degree+theorem&target=Q-FORMAL-001) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-001%3A+Reproduce+Huang%27s+hypercube+degree+theorem&target=Q-FORMAL-001)

Reconstruct a proof that every induced subgraph on 2^(n-1)+1 vertices of the n-dimensional hypercube has maximum degree at least sqrt(n), for every integer n >= 1.

**Origin:** Known-result calibration. **Curator-designed scope:** No.

**Current status:** Known result in literature. **Last checked:** 2026-10-13.

**Status basis:** Huang's proof is explicit; the 2012 open-list entry is superseded. Reproduction is calibration, not a new solution.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-002: 2019, SRC-FORMAL-005: 2012. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Whether an existing formalization can be reused should be searched before a later attempt.
- Choose a proof assistant only if formalization is in scope; no toolchain has been selected.

**Primary branch:** [Computational complexity](../domains/cs.md#cs-complex). **Related branches:** [Combinatorics and discrete mathematics](../domains/math.md#math-comb), [Type theory and formal verification](../domains/logic.md#logic-type).

**Sources:** [Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture](../sources.md#src-formal-002); [Open Problems in Analysis of Boolean Functions](../sources.md#src-formal-005).

**Exact locator:** SRC-FORMAL-002, Theorem 1.1 and Section 2

**Potential difficulty:** Medium. Useful first calibration because the target and reference proof are explicit and errors can be localized to linear-algebra lemmas. This predicts auditability, not research discovery or model success.

**Possible AI role:** No named model evaluated; assumes tool-using AI with source retrieval, symbolic reasoning and optional access to a proof assistant.

**Verification burden:** Medium. Submatrix dimensions and eigenvalue ordering are subtle despite a short statement.

**Resource expectations:** Experiment: none Data: The cited paper and mathematical definitions only; no empirical dataset. Computation: Symbolic proof first. Optional small matrices grow as 2^n by 2^n; never materialize large cubes merely because no experiment is needed. Formalization cost unknown; no run or time estimate exists.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No model has been tested. Familiarity with the published proof may contaminate any discovery-style benchmark; this is intentionally a reproduction benchmark.

[Read the full card](../cards/Q-FORMAL-001.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
