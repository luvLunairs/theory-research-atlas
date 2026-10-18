# NP-completeness of ordinary MCSP under deterministic many-one reductions

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-310 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-310%3A+NP-completeness+of+ordinary+MCSP+under+deterministic+many-one+reductions&target=Q-FORMAL-310) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-310%3A+NP-completeness+of+ordinary+MCSP+under+deterministic+many-one+reductions&target=Q-FORMAL-310)

Is the ordinary Minimum Circuit Size Problem NP-complete under deterministic polynomial-time many-one reductions? Input is a complete Boolean truth table and a gate bound s; ask whether a circuit of size at most s computes the table.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** 2025–2026 conditional, quasipolynomial, randomized and implicit-variant results do not prove this exact completeness statement.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-305: 2025, SRC-FORMAL-306: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions](../sources.md#src-formal-305); [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](../sources.md#src-formal-306).

**Exact locator:** Hirahara–Ilango, section I; Goldberg–Juvekar–Kabanets, abstract.

**Potential difficulty:** Frontier. Reductions must encode hardness into a fully explicit truth table and respect known meta-complexity barriers.

**Possible AI role:** Check the size blowup and both directions of a proposed reduction; independently test a tiny parameter instance.

**Verification burden:** High. The reduction must be polynomial in its original input and unconditional; a succinct or partial table changes the problem.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
