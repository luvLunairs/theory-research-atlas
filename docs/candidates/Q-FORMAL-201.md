# A linear bound for avoiding a specified automaton state

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-201 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-201%3A+A+linear+bound+for+avoiding+a+specified+automaton+state&target=Q-FORMAL-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-201%3A+A+linear+bound+for+avoiding+a+specified+automaton+state&target=Q-FORMAL-201)

For every complete deterministic strongly connected synchronizing automaton A=(Q,Σ,δ), with n=|Q| ≥ 2, and every q∈Q, does there exist w∈Σ* of length at most 2n−2 such that q∉δ(Q,w)?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The original formulation supplies the essential strong-connectivity condition. The 2026 survey still presents the avoiding bound as a conjecture; no general resolution was found in the scoped later-source check.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-210: 2016, SRC-FORMAL-202: 2021, SRC-FORMAL-201: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Confirm that any proposed sample family lies outside published classifications and later exhaustive checks.
- The 2026 survey wording differs from the original by omitting strong connectivity; the original hypothesis governs this card.

**Primary branch:** [Algorithms and data structures](../domains/cs.md#cs-alg). **Related branches:** [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Experiments with Synchronizing Automata](../sources.md#src-formal-210); [Lower Bounds on Avoiding Thresholds](../sources.md#src-formal-202); [Synchronizing Automata: Open Problems](../sources.md#src-formal-201).

**Exact locator:** Kisielewicz–Kowalski–Szykuła, §3, Conjecture 5; Szykuła, §2.2, Conjecture 2.

**Potential difficulty:** High. General progress is difficult even though individual small instances can be checked exactly.

**Possible AI role:** No named model evaluated; assumes a tool-using AI can write finite-state search code and work with an independent checker under human supervision. Transition-table generation and exact distance checks are well specified, but useful family selection needs an automata specialist and the general conjecture is difficult.

**Verification burden:** Medium. Finite witnesses are direct; a family theorem requires a separate mathematical audit.

**Resource expectations:** Experiment: No physical experiment is needed for the formal question. Data: Use explicit transition tables and cited constructions. No external observational dataset is required. Computation: For one n-state instance, exact image-subset exploration uses at most 2^n subsets; at n=14 this is 16,384 possible subsets. Checking one instance is finite, while exhaustive enumeration of all transition tables is much larger. Proposed stop limits are 1,000 instances, 512 MiB memory and four elapsed hours, whichever is reached first. These are proposed ceilings, not measured requirements or performance claims.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No AI attempt has been evaluated. Modest instance verification does not imply that a counterexample exists or is likely to be found; the proposed sizes may contain no useful new behavior.

[Read the full card](../cards/Q-FORMAL-201.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
