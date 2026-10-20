# EFX and Pareto optimality for personalized bi-valued goods

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-204 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-204%3A+EFX+and+Pareto+optimality+for+personalized+bi-valued+goods&target=Q-MODEL-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-204%3A+EFX+and+Pareto+optimality+for+personalized+bi-valued+goods&target=Q-MODEL-204)

For arbitrary finite numbers of agents and goods with additive values v_i(g)∈{a_i,b_i}, where each agent has its own fixed positive pair a_i>b_i>0, determine whether a complete EFX allocation always exists that is also Pareto optimal among complete allocations. EFX requires v_i(X_i)≥v_i(X_j\{g}) for all i,j,g∈X_j; Pareto optimality excludes any allocation weakly improving every agent and strictly improving one.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** Jin and Tao pose exact simultaneous existence as open; He and Tao repeat this status. The later maximum-Nash-welfare result proves a tight approximation guarantee for that rule, not a resolution of exact EFX plus integral Pareto optimality. No later matching resolution was located.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Versions and date limitations are recorded in the source catalog. Relevant passages were opened on 2026-10-20.

**Scope limits:** Exact EFX together with integral Pareto optimality. EFX alone is established. Efficient computation is a further question if simultaneous existence holds; no restriction to a selected number of agents or ratio range is imposed here.

**Information still needed**

- Refresh the literature before selecting a special case or claiming novelty.
- Clarify the inconsistent manuscript and repository dates for arXiv:2610.00122v1.
- Independently audit any source theorem used in a new proof.

**Primary branch:** [Mechanism design and fair allocation](../domains/econ.md#econ-mech). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities](../sources.md#src-model-204); [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202); [When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods](../sources.md#src-impact-004).

**Exact locator:** Jin and Tao, Sections 2-5; He and Tao, Section 6; Lin, Wu and Zhou, Theorem 3.5 and Example 3.6.

**Potential difficulty:** High. The full target requires a general argument beyond the inspected partial results.

**Possible AI role:** No model evaluated; assumes a tool-using assistant able to read the cited mathematics and preserve reproducible evidence.

**Verification burden:** High. Moderate for a small fully enumerated instance; high for a general theorem or a large exhaustive certificate.

**Resource expectations:** Experiment: None for this existence question. People's acceptance of EFX is an empirical matter outside its scope. Data: Published definitions and exact valuation matrices for any future finite study. Computation: Unmeasured. A fixed n-agent, m-good instance has n^m complete assignments. Exact small-instance checking may be manageable; growth and general Pareto verification can be expensive.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** Editorial planning judgment only. No model, search strategy, runtime or success probability has been measured.

[Read the full card](../cards/Q-MODEL-204.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Jin and Tao pose exact simultaneous existence as open; He and Tao repeat this status. The later maximum-Nash-welfare result proves a tight approximation guarantee for that rule, not a resolution of exact EFX plus integral Pareto optimality. No later matching resolution was located.

**Search scope:** Opened the listed source passages and searched exact identifiers and later-result terminology. This is a bounded source check.

**Inspected evidence**

- [On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities](../sources.md#src-model-204) — Sections 2-5. Poses exact EFX plus integral Pareto optimality and distinguishes known EFX and fractional impossibility results.
- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202) — Section 6. Repeats unresolved compatibility for personalized bi-valued goods.
- [When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods](../sources.md#src-impact-004) — Theorem 3.5, Example 3.6 and Section 6. A tight 2/3-EFX guarantee for maximum Nash welfare does not settle exact simultaneous existence.

**Limits and remaining work**

- Bounded title, identifier and terminology searches; unpublished results or different terminology may be missed. No full proof audit.
- The arXiv:2610.00122v1 chronology is inconsistent between repository metadata and manuscript date.

<details>
<summary>Search queries</summary>

- "personalized" "bi-valued" "EFX" "Pareto" 2026 solved
- "EFX" "personalized" "Pareto" "October"
- "2507.18251" solved


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
