# Complete EFX for four additive goods agents

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-201 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-201%3A+Complete+EFX+for+four+additive+goods+agents&target=Q-MODEL-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-201%3A+Complete+EFX+for+four+additive+goods+agents&target=Q-MODEL-201)

For four agents and every finite set M of indivisible goods with nonnegative additive values v_i, does there exist a complete partition X of M such that v_i(X_i)≥v_i(X_j\{g}) for all agents i,j and every g∈X_j? The deletion quantifier includes goods of zero value to i (EFX0).

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The August 2026 source still reports the unrestricted four-agent question as open while proving m≤9. Targeted later searches found no general resolution; the suggested m=10 pilot has not received a separate exhaustive novelty check.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-201: 2026, SRC-MODEL-202: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Assess the novelty and usefulness of a proposed ten-good region before running it.
- Independently inspect the recent m≤9 certificate and any later version before relying on its detailed reductions.
- Refresh the all-m four-agent status before any claimed solution.

**Primary branch:** [Mechanism design and fair allocation](../domains/econ.md#econ-mech). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods](../sources.md#src-model-201); [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202).

**Exact locator:** Alkassar et al., Introduction and Theorem 1; He and Tao, Section 6.

**Potential difficulty:** High. The complete target is an unresolved existence problem. A bounded search does not establish the general statement.

**Possible AI role:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions. Exact linear constraints let AI propose regions and allocation menus while a separate checker tests each claim. A specialist must first judge whether the chosen region adds anything to known reductions.

**Verification burden:** High. All valuations in the claimed region must be covered, including boundary faces.

**Resource expectations:** Experiment: None for the mathematical existence task. Whether people accept EFX as fair is an empirical question outside this target. Data: Only explicitly recorded valuation constraints and any future exact candidate matrix; no preference survey is required. Computation: First-pilot policy: one region, at most 128 menu allocations, one CPU-hour and 8 GiB memory, then stop with an unresolved region if necessary. These are proposed resource caps, not measured requirements or a promise of completion. The complete allocation space at m=10 has 4^10=1,048,576 assignments; exhaustive region coverage may require much more.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Novelty of any chosen ten-good subregion is unverified. Solver difficulty and generalization from local structure are unknown.

[Read the full card](../cards/Q-MODEL-201.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
