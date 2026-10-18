# Complete EFX for binary submodular chore costs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-208 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-208%3A+Complete+EFX+for+binary+submodular+chore+costs&target=Q-MODEL-208) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-208%3A+Complete+EFX+for+binary+submodular+chore+costs&target=Q-MODEL-208)

For arbitrary finite N and M, let each cost c_i:2^M→R_≥0 satisfy c_i(empty)=0, monotonicity, submodularity c_i(S)+c_i(T)≥c_i(S∪T)+c_i(S∩T), and c_i(S∪{g})−c_i(S)∈{0,1} whenever g∉S. Must a complete partition X exist such that c_i(X_i\{g})≤c_i(X_j) for every i,j and g∈X_i?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The August 2026 paper explicitly leaves binary submodular chores open after counterexamples for binary XOS and supermodular costs. Targeted later searches found no resolution; general monotone counterexamples do not transfer to this narrower class.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-209: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Mechanism design and fair allocation](../domains/econ.md#econ-mech). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Non-Existence of EFX Chore Allocations for Monotone Cost Functions with Binary Marginals](../sources.md#src-model-209).

**Exact locator:** Lin et al., Section 2, Figure 1 and Section 4.

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** A tool-using mathematical assistant could compare hypotheses, locate relevant results and propose a narrower proof, construction or counterexample task; a specialist must first select and check that task.

**Verification burden:** Unknown. The statement and source need a task-specific proof or certificate plan before an attempt.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated on this target; AI usefulness and success probability remain unmeasured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
