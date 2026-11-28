# Existence of a p-optimal propositional proof system

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-315 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-315%3A+Existence+of+a+p-optimal+propositional+proof+system&target=Q-FORMAL-315) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-315%3A+Existence+of+a+p-optimal+propositional+proof+system&target=Q-FORMAL-315)

Does TAUT have a Cook–Reckhow proof system that polynomial-time simulates every other Cook–Reckhow proof system, with the translator allowed to depend on the simulated system?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** Egidy asks the unrelativized TAUT question. There are oracles with an infinite polynomial hierarchy where TAUT has a p-optimal proof system and others where it lacks even an optimal one. These conflicting oracle behaviors constrain relativizing approaches. They do not decide the ordinary TAUT question.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The problem statement and references listed in the 28 November 2026 literature check were inspected.

**Scope limits:** Egidy, questions Q1–Q2 and oracle O₂. Egidy and Glaßer, abstract, oracle O₁.

**Information still needed**

- A proposed unrelativized argument needs to explain which step avoids the known relativization barrier.

**Primary branch:** [Proof theory and constructive logic](../domains/logic.md#logic-proof). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](../sources.md#src-formal-309); [Optimal Proof Systems for Complex Sets are Hard to Find](../sources.md#src-math-927).

**Exact locator:** Egidy, questions Q1–Q2 and oracle O₂. Egidy and Glaßer, abstract, oracle O₁.

**Potential difficulty:** Frontier. Quantification over all polynomial-time proof systems resists ordinary finite comparisons.

**Possible AI role:** Test whether a proposed simulation is uniform and polynomial-time and whether the proof would relativize to the known counterexamples.

**Verification burden:** High. Simulation must be an effective polynomial-time translation, not just a proof-length comparison.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** A proposed unrelativized argument needs to explain which step avoids the known relativization barrier. Model performance on this task has not been measured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Egidy asks the unrelativized TAUT question. There are oracles with an infinite polynomial hierarchy where TAUT has a p-optimal proof system and others where it lacks even an optimal one. These conflicting oracle behaviors constrain relativizing approaches. They do not decide the ordinary TAUT question.

**Search scope:** Egidy, questions Q1–Q2 and oracle O₂. Egidy and Glaßer, abstract, oracle O₁.

**Inspected evidence**

- [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](../sources.md#src-formal-309) — Abstract, Q1 and O₂, and Section 1.2.2. Asks about ordinary TAUT and constructs an oracle with an infinite polynomial hierarchy and p-optimal systems for all PSPACE sets.
- [Optimal Proof Systems for Complex Sets are Hard to Find](../sources.md#src-math-927) — Abstract, first oracle. In an oracle with an infinite polynomial hierarchy, no set in PSPACE outside NP has optimal systems. This includes relativized TAUT in that setting.

**Limits and remaining work**

- A proposed unrelativized argument needs to explain which step avoids the known relativization barrier.

<details>
<summary>Search queries</summary>

- Egidy Glaßer TAUT optimal proof systems relativized infinite polynomial hierarchy


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
