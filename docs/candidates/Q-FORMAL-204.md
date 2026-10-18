# The optimal randomized stretch for two online bins

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-204 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-204%3A+The+optimal+randomized+stretch+for+two+online+bins&target=Q-FORMAL-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-204%3A+The+optimal+randomized+stretch+for+two+online+bins&target=Q-FORMAL-204)

Determine inf_A sup_I E[max(L1(A,I),L2(A,I))], where I ranges over finite positive real item sequences that fit offline into two unit-capacity bins, A assigns each arriving item irrevocably before seeing the next, and I is fixed independently of A's random bits. Can the reported interval [7/6,5/4] be narrowed?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The randomized paper gives distinct lower and upper bounds. The author publication list and later computational-method paper were checked; no closing of this randomized gap was identified. The later paper primarily concerns deterministic algorithms.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-206: 2024, SRC-FORMAL-207: 2025, SRC-FORMAL-209: date unverified. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Confirm the exact finite-game formulation against the source before implementation.
- Recheck later publications for improved numerical bounds before interpreting an improvement.
- Determine whether the proposed grid already appears in the source's computational data.

**Primary branch:** [Randomized, online and distributed algorithms](../domains/cs.md#cs-random). **Related branches:** [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Computational bounds on randomized algorithms for online bin stretching](../sources.md#src-formal-206); [On the convergence of computational methods for the online bin stretching problem](../sources.md#src-formal-207); [Antoine Lhomme: publications](../sources.md#src-formal-209).

**Exact locator:** Lhomme–Catusse–Brauner, randomized paper §§2–4.2; later convergence paper §1.

**Potential difficulty:** High. Small exact games are approachable; a stronger general bound may require larger support or new ideas.

**Possible AI role:** No named model evaluated; assumes a tool-using AI can formulate finite games and rational certificates, with an independent verifier and human review of adversary semantics. Finite games offer exact certificates and a bounded entry point, but a game model that leaks future input information or omits policies yields invalid bounds.

**Verification burden:** High. A numerical LP optimum is insufficient; complete policy coverage and exact feasibility must be established.

**Resource expectations:** Experiment: No physical experiment. Data: A finite list of rational item sequences and offline packings; no empirical dataset. Computation: The input pool is capped at 200 sequences of at most eight items. Build the complete online-history representation for that pool only, stopping before 20,000 history states, 1 GiB memory or four elapsed hours. Exact arithmetic can be substantially costlier than floating-point search. These are proposed limits, not measured costs; a small grid is not a guarantee of a small policy space.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The small proposed support may be incapable of improving 7/6. No search, runtime, model performance or success probability has been measured.

[Read the full card](../cards/Q-FORMAL-204.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
