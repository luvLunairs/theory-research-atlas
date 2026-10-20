# EFX and Pareto optimality for personalized bi-valued goods

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Can indivisible goods always be shared so that envy disappears after removing any one good from another person's bundle, while no reassignment can benefit someone without harming another?

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-204%3A+EFX+and+Pareto+optimality+for+personalized+bi-valued+goods&target=Q-MODEL-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-204%3A+EFX+and+Pareto+optimality+for+personalized+bi-valued+goods&target=Q-MODEL-204)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Mechanism design and fair allocation](../domains/econ.md#econ-mech) |
| Related fields | [Computational complexity](../domains/cs.md#cs-complex), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For arbitrary finite numbers of agents and goods with additive values v_i(g)∈{a_i,b_i}, where each agent has its own fixed positive pair a_i&gt;b_i&gt;0, determine whether a complete EFX allocation always exists that is also Pareto optimal among complete allocations. EFX requires v_i(X_i)≥v_i(X_j\{g}) for all i,j,g∈X_j; Pareto optimality excludes any allocation weakly improving every agent and strictly improving one.

**Required output:** Prove simultaneous existence for all such instances or give one instance in which every EFX allocation is Pareto dominated.

**Scope:** Exact EFX together with integral Pareto optimality. EFX alone is established. Efficient computation is a further question if simultaneous existence holds; no restriction to a selected number of agents or ratio range is imposed here.

### Assumptions

- Finitely many agents and goods; every good is assigned once and values are additive.
- Each agent uses its own two strictly positive values. Ratios a_i/b_i may differ between agents.
- Pareto comparisons are against complete integral allocations. Fractional reallocations are outside this target.

### Success criteria

1. An existence proof must satisfy both properties for the same complete allocation.
2. A counterexample must rule out every complete EFX allocation, not merely one algorithm's output.
3. State any restricted parameter class explicitly and report its result as partial progress.

### Background needed

- Additive fair division, EFX and Pareto dominance.
- Exact finite optimization and certificates of exhaustive coverage.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Unmeasured. A fixed n-agent, m-good instance has n^m complete assignments. Exact small-instance checking may be manageable; growth and general Pareto verification can be expensive.

**Data:** Published definitions and exact valuation matrices for any future finite study.

**Experiments:** None for this existence question. People's acceptance of EFX is an empirical matter outside its scope.

**Theory and model requirements:** Additive, strictly positive, personalized two-value preferences and integral complete assignment.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Check positivity, the two-value condition and complete assignment.
2. Evaluate EFX using the potentially envious agent's values for both bundles.
3. For a finite negative result, give coverage of all EFX allocations and an integral Pareto dominator for each.
4. Independently check exact data and any symmetry or pruning argument.

**Statement alignment:** Goods, personalized ratios and integral Pareto optimality are essential. Approximate EFX, chores or fractional efficiency answer different questions.

**Human review difficulty:** Moderate for a small fully enumerated instance; high for a general theorem or a large exhaustive certificate.

### Formal validity and empirical support

**What the formal task can establish:** Source inspection confirms the recorded formulation, not an independent proof of the cited theorems.

**Empirical support and limits:** A formal allocation guarantee does not establish that people endorse this fairness criterion or report additive preferences.

### Methods and obstacles

**Proposed methods:**

- Study the source's Pareto characterization and matching-based EFX construction.
- Compare any proposed result with the published failures of maximum Nash welfare and fractional-market approaches.

**Expected obstacles:**

- Fairness and efficiency can each hold for different allocations.
- Checking one EFX witness does not establish Pareto optimality.
- A fractional Pareto improvement is not necessarily an integral one.

### Checks still needed

- Refresh the literature before selecting a special case or claiming novelty.
- Clarify the inconsistent manuscript and repository dates for arXiv:2610.00122v1.
- Independently audit any source theorem used in a new proof.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Jin and Tao pose exact simultaneous existence as open; He and Tao repeat this status. The later maximum-Nash-welfare result proves a tight approximation guarantee for that rule, not a resolution of exact EFX plus integral Pareto optimality. No later matching resolution was located.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-204.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Jin and Tao, Sections 2-5; He and Tao, Section 6; Lin, Wu and Zhou, Theorem 3.5 and Example 3.6.

### Sources

- [On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities](../sources.md#src-model-204). Jiarong Jin; Biaoshuai Tao. 2025. [Read source](https://arxiv.org/html/2507.18251v2).
  - **Relevant sections:** Version 2, 17 October 2025; abstract, Section 2, Lemma 1 and Section 5.
  - **Source limitations:** The separate existence of EFX and Pareto-optimal allocations does not prove simultaneous existence. Pareto testing is hard for general fractional ratios.
- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202). Wentao He; Biaoshuai Tao. 2026. [Read source](https://arxiv.org/html/2606.08872v1).
  - **Relevant sections:** Version 1, 7 June 2026; Section 2, Theorems 1–3, start of Section 5 and Section 6.
  - **Source limitations:** Preprint. Distinguish common from personalized values, chores from goods, and fairness alone from fairness with efficiency.
- [When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods](../sources.md#src-impact-004). Zehan Lin; Xiaowei Wu; Shengwei Zhou. 2026. [Read source](https://arxiv.org/html/2610.00122v1).
  - **Relevant sections:** Version 1; Theorem 3.5, Example 3.6 and Section 6. The arXiv abstract and HTML header report 9 September 2026, while the manuscript title page says December 2025; the date discrepancy is retained.
  - **Source limitations:** Preprint; proof not independently audited. Publication chronology needs clarification. Tightness for maximum Nash welfare does not exclude another exact EFX and Pareto-optimal allocation.

### Known results and partial progress

- Jin and Tao prove polynomial-time EFX existence. They also characterize Pareto optimality and distinguish integral from fractional ratios in its decision complexity.
- Their Section 5 shows that maximum Nash welfare can fail exact EFX and that fractional Pareto optimality can be incompatible with EFX.
- Lin, Wu and Zhou report a tight 2/3-EFX guarantee for maximum Nash welfare. Tightness of that rule does not rule out another allocation satisfying exact EFX and Pareto optimality.

**Research value:** Locates the boundary between a strong fairness guarantee and efficient use of resources in a simple heterogeneous-preference model.

### Related problems

- **Related to:** [Complete EFX for four additive goods agents](../candidates.md#q-model-201). Both concern additive goods. This entry restricts each agent to two positive values and adds efficiency; the four-agent entry permits general values and requires fairness alone.

### Scope of the status check

**Finding:** Jin and Tao pose exact simultaneous existence as open; He and Tao repeat this status. The later maximum-Nash-welfare result proves a tight approximation guarantee for that rule, not a resolution of exact EFX plus integral Pareto optimality. No later matching resolution was located.

**Search limits:** Bounded title, identifier and terminology searches; unpublished results or different terminology may be missed. No full proof audit.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "personalized" "bi-valued" "EFX" "Pareto" 2026 solved
- "EFX" "personalized" "Pareto" "October"
- "2507.18251" solved

**Sources checked:**

- [On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities](../sources.md#src-model-204)
- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202)
- [When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods](../sources.md#src-impact-004)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The source records failed routes through maximum Nash welfare and fractional market equilibria. No project attempt has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Jiarong Jin
- Biaoshuai Tao

**Suggested citation:** Jin and Tao, On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities, arXiv:2507.18251v2, Section 5 (WINE 2025). For the later approximation guarantee, cite Lin, Wu and Zhou, arXiv:2610.00122v1.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

The problem is explicit and has reusable published arguments. Assessing a specific AI attempt requires a narrower, independently checked target.

**Model or capability conditions:** No model evaluated; assumes a tool-using assistant able to read the cited mathematics and preserve reproducible evidence.

**Uncertainty:** Editorial planning judgment only. No model, search strategy, runtime or success probability has been measured.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The source specifies the objects and quantifiers. |
| Decomposability | Medium | A selected lemma or finite instance can be checked separately; it need not settle the full problem. |
| Methods and literature | High | The cited papers provide concrete methods and known limitations. |
| Search / symbolic fit | Medium | Symbolic or finite computations can assist a declared task, without proving the general claim. |
| Checkability | Medium | Exact certificates help, but the claimed scope still requires proof. |
| Expertise needed | High | Specialist review is needed for a new general result. |
| Scholarly significance | High | Locates the boundary between a strong fairness guarantee and efficient use of resources in a simple heterogeneous-preference model. |
| Verification difficulty | High | Moderate for a small fully enumerated instance; high for a general theorem or a large exhaustive certificate. |

**Correctness:** No project answer.

No project proof, counterexample or research computation is supplied.

**Novelty:** Requires future literature review.

Any new claim needs a focused comparison at the time of submission.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The full target requires a general argument beyond the inspected partial results.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-20 | Expanded the existing candidate into a full card and added the maximum-Nash-welfare approximation result; retained the original question and ID. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-204` |
| Duplicate key | `efx-po-personalized-bivalued-goods` |
| Original domain label | Mechanism design and fair allocation |
| Original cross-domain labels | Computational complexity; Optimization and operations research |
| Primary domain ID | `ECON.MECH` |
| Cross-domain IDs | `CS.COMPLEX`, `MATH.OPT` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `construction`, `counterexample`, `finite_search`, `exact_computation`, `algorithm` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-204.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
