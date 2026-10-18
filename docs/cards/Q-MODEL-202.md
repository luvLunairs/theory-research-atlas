# Complete EFX for more than four common bi-valued chore agents

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

When every chore is either cheap or expensive for each person, and everyone uses the same two cost levels, can five or more people always obtain exact EFX fairness? The positive four-person result gives a concrete structural starting point.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-202%3A+Complete+EFX+for+more+than+four+common+bi-valued+chore+agents&target=Q-MODEL-202) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-202%3A+Complete+EFX+for+more+than+four+common+bi-valued+chore+agents&target=Q-MODEL-202)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Mechanism design and fair allocation](../domains/econ.md#econ-mech) |
| Related fields | [Computational complexity](../domains/cs.md#cs-complex), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For every n≥5, finite chore set M and common real ratio r&gt;2, with additive costs c_i(g)∈{1,r} for every agent i and chore g, must there be a complete partition X with c_i(X_i\{g})≤c_i(X_j) for all i,j and every g∈X_i? Empty bundles impose no deletion comparison. No Pareto-optimality condition is required.

**Required output:** Find a general construction, a reusable structural lemma beyond known cases, or an exact counterexample. The bounded pilot is intended to identify such structure and record precisely which instances were examined.

**Scope:** The source question permits all n≥5, m and r&gt;2. A curator-proposed first pilot fixes n=5, m=11 and r=3, sampling at most 100 explicitly listed cost-pattern multisets. This pilot's separate novelty and openness have not been established; it is not exhaustive over the literature problem.

### Assumptions

- n≥5, finitely many chores, and a common ratio r&gt;2 with each c_i(g) equal to 1 or r.
- Costs add over bundles. Each chore is assigned once; empty bundles are permitted.
- For chores, delete from the envious agent's own bundle. Fairness alone is required; Pareto optimality is not assumed.

### Success criteria

1. For each tested pattern multiset, store the complete five-by-eleven matrix and either an exact EFX allocation or an explicit unresolved outcome.
2. A claimed counterexample must include a complete, independently verified exclusion of all 5^11 allocations; a search timeout is not nonexistence.
3. A proposed structural lemma must state its entire input class and prove every comparison for that class.
4. Do not infer universal existence from sampled success or claim novelty for a fixed small case without checking earlier theorems.

### Background needed

- Additive chore allocation, EFX deletion semantics and common versus personalized values.
- Finite constraint search and exact integer arithmetic.
- The item-type decomposition and insertion arguments in the four-agent proof.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Suggested first cap: 100 cost-pattern multisets, one CPU-hour and 8 GiB total memory, stopping unresolved instances explicitly. These are proposed limits, not timing estimates. There are 2^55 labeled five-by-eleven cost matrices and 5^11=48,828,125 allocations per fixed matrix; exhaustive global search is not described as cheap.

**Data:** A future pilot uses fully specified matrices with entries 1 or 3; no external dataset is needed.

**Experiments:** None for the formal allocation question. Actual workload, strategic reporting and perceived fairness require separate evidence.

**Theory and model requirements:** Common cost levels, positivity, additivity, indivisibility and complete allocation. The ratio and pilot dimensions are curator choices.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Compute every bundle cost independently from the saved integer matrix.
2. Check every ordered agent pair and every owned-chore deletion, including comparisons to empty bundles.
3. Use a checker written separately from the allocation-search code. For no-solution claims, require complete enumeration or a proof object with an audited translation.
4. Audit any symmetry reduction as a bijection on allocations and cost patterns; retain a record of omitted but equivalent cases.
5. Have a fair-division reviewer compare any candidate lemma with the m≤2n, r≤2 and four-agent results.

**Statement alignment:** All costs use the same {1,r}; the chore is removed from the owner's bundle. EF1, approximate EFX, partial allocations and EFX plus efficiency do not answer this target.

**Human review difficulty:** Individual positive allocations are straightforward; negative instances and structural lemmas require exhaustive coverage and expert review.

### Formal validity and empirical support

**What the formal task can establish:** An exact result concerns the stated finite cost model. The mathematical meaning of costs and deletion fairness is fixed by the assumptions.

**Empirical support and limits:** No evidence about real workloads or people's preferences is inferred. Using the model operationally would require separate empirical and institutional review.

### Methods and obstacles

**Proposed methods:**

- Cost-pattern hypergraphs, recording for each chore the set of agents for whom it is cheap.
- SAT or integer-constraint allocation search with exact checking.
- Insertion lemmas, balanced assignments and minimal-counterexample reasoning.

**Expected obstacles:**

- There are 32 possible cheap-agent subsets per chore already for five agents.
- Finding an allocation on every sampled input offers no universal guarantee.
- Changing from common to personalized ratios, or adding Pareto optimality, produces a different question.

### Checks still needed

- Check whether the proposed n=5,m=11,r=3 pilot is already covered by a known special-case theorem.
- Review the four-agent insertion lemmas before applying them to five agents.
- Refresh common bi-valued status and compare any proposed counterexample with existing public records.

<a id="evidence"></a>

## Evidence and context

**Status basis:** He and Tao explicitly leave the more-than-four-agent common bi-valued case open. Their r≤2 case works for any n; m≤2n is also known. No later general resolution was located. Particular bounded pilots may already be known.

**Exact problem / theorem locator:** He and Tao, Section 2, start of Section 5 and Section 6; Garg and Murhekar, abstract.

### Sources

- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202). Wentao He; Biaoshuai Tao. 2026. [Read source](https://arxiv.org/html/2606.08872v1).
  - **Relevant sections:** Version 1, 7 June 2026; Section 2, Theorems 1–3, start of Section 5 and Section 6.
  - **Source limitations:** Preprint. Distinguish common from personalized values, chores from goods, and fairness alone from fairness with efficiency.
- [Existence of 2-EFX Allocations of Chores](../sources.md#src-model-206). Jugal Garg; Aniket Murhekar. 2026. [Read source](https://ojs.aaai.org/index.php/AAAI/article/view/38738).
  - **Relevant sections:** AAAI 2026, 40(20), 16922–16929; abstract; published 14 March 2026.
  - **Source limitations:** The opened publisher abstract supports these scope statements; detailed proofs were not audited. A factor-two bound does not establish exact EFX.

### Known results and partial progress

- He and Tao prove common bi-valued EFX for four agents and describe an all-n construction when r≤2.
- Garg and Murhekar report the exact m≤2n boundary. Their general 2-EFX theorem does not solve exact EFX.
- He and Tao's incompatibility with Pareto optimality for some bi-valued instances is not an EFX nonexistence theorem.

**Research value:** This restricted cost model isolates a surviving exact-fairness question after general additive chores were shown to fail. A small counterexample or a structural extension would clarify the true boundary.

### Related problems

- **Related to:** [Complete EFX for three additive chore agents](../candidates.md#q-model-203). Both concern chore EFX, but this question restricts costs and allows more agents; the three-agent question permits arbitrary nonnegative costs.

### Scope of the status check

**Finding:** He and Tao explicitly leave the more-than-four-agent common bi-valued case open. Their r≤2 case works for any n; m≤2n is also known. No later general resolution was located. Particular bounded pilots may already be known.

**Search limits:** Dated primary-source checks and targeted later-work searches cannot establish that no unpublished or newly posted solution exists. Refresh the literature before claiming progress.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202)
- [Existence of 2-EFX Allocations of Chores](../sources.md#src-model-206)

</details>

<details>
<summary>Previous attempts and public records</summary>

- He and Tao's four-agent proof and Garg and Murhekar's approximation framework are external mathematical work. No project trial is recorded.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Wentao He
- Biaoshuai Tao
- Jugal Garg
- Aniket Murhekar

**Suggested citation:** He and Tao (2026), arXiv:2606.08872v1, Sections 5–6; Garg and Murhekar (2026), AAAI 40(20), 16922–16929, doi:10.1609/aaai.v40i20.38738. The five-agent pilot is curator-proposed.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

First check whether the proposed five-agent, eleven-chore, ratio-three pilot is covered by an existing special-case theorem, and select a useful unresolved class. Exact integer checks could then support AI-generated cost patterns and proposed extensions of the four-agent structure.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions.

**Uncertainty:** The n=5,m=11,r=3 pilot may have known positive structure. No AI success, runtime or cost has been measured, and the general n≥5 problem may resist finite experimentation.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Both the open target and the limited pilot specify their quantifiers. |
| Decomposability | High | Pattern generation, allocation search and proof checking are separable. |
| Methods and literature | Medium | Four-agent methods are available, but their extension is uncertain. |
| Search / symbolic fit | High | Fixed-ratio costs allow exact combinatorial constraint search. |
| Checkability | Medium | An allocation is cheap to verify; absence of any allocation is much harder. |
| Expertise needed | High | A specialist must judge structural generalization and known subclasses. |
| Scholarly significance | High | The target separates exact fairness from known general impossibility. |
| Verification difficulty | High | Universal existence and exhaustive nonexistence need more than heuristic search. |

**Correctness:** No project answer.

The literature supports the question; no project answer has been submitted for review.

**Novelty:** Requires future literature review.

The source poses common bi-valued existence for more than four agents. The selected pilot and future outputs require separate novelty review.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The complete target is an unresolved existence problem. A bounded search does not establish the general statement.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-202` |
| Duplicate key | `efx-common-bivalued-chores-n-ge5` |
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
| Method tags | `construction`, `counterexample`, `finite_search`, `proof`, `exact_computation`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-202.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
