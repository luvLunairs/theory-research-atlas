# Complete EFX for four additive goods agents

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Can four people always divide indivisible goods so that removing any one item from someone else's share eliminates envy? A finite number of goods still leaves infinitely many possible valuations.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-201%3A+Complete+EFX+for+four+additive+goods+agents&target=Q-MODEL-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-201%3A+Complete+EFX+for+four+additive+goods+agents&target=Q-MODEL-201)

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

For four agents and every finite set M of indivisible goods with nonnegative additive values v_i, does there exist a complete partition X of M such that v_i(X_i)≥v_i(X_j\{g}) for all agents i,j and every g∈X_j? The deletion quantifier includes goods of zero value to i (EFX0).

**Required output:** Seek an existence argument for the full question or a rigorously certified counterexample. A first bounded milestone is an exact EFX0 cover for one stated continuous valuation region, or a concrete counterexample that survives exhaustive allocation checking.

**Scope:** The literature question allows arbitrary m. A proposed first milestone uses m=10 and one explicitly specified rational polytope of normalized valuation matrices. This restriction is curator-designed and awaits assessment; it is not a separately verified open case.

### Assumptions

- Four agents; a finite good set; nonnegative additive values, with zeros and ties allowed.
- Every good belongs to exactly one bundle. Empty bundles are allowed.
- Comparisons use the potentially envious agent's valuation of both bundles. EFX0 quantifies over every removed good, including goods that agent values at zero.

### Success criteria

1. Write the region R as explicit rational linear inequalities in the 40 values before search; explain nonemptiness and any row normalization or symmetry reduction.
2. For a positive regional result, give a finite menu of complete allocations and an exact proof that every v∈R admits at least one menu allocation satisfying all EFX0 inequalities.
3. For a negative result, give exact rational valuations and a checkable reason every one of the 4^10 complete allocations fails EFX0.
4. State uncovered regions and preserve ties and zero values. A regional certificate alone does not settle all ten-good instances or the all-m question.

### Background needed

- Additive fair division and the distinction between EFX, EFX0, EF1 and partial allocation.
- Linear real arithmetic, exact certificates and coverage proofs for a finite union of regions.
- Symmetry reductions that preserve one common labeling of goods across all agents.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** First-pilot policy: one region, at most 128 menu allocations, one CPU-hour and 8 GiB memory, then stop with an unresolved region if necessary. These are proposed resource caps, not measured requirements or a promise of completion. The complete allocation space at m=10 has 4^10=1,048,576 assignments; exhaustive region coverage may require much more.

**Data:** Only explicitly recorded valuation constraints and any future exact candidate matrix; no preference survey is required.

**Experiments:** None for the mathematical existence task. Whether people accept EFX as fair is an empirical question outside this target.

**Theory and model requirements:** Finite indivisibility, additivity, nonnegative values, complete assignment and EFX0 deletion semantics.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Implement a small independent allocation checker from the displayed EFX0 inequalities, without sharing the search encoder.
2. For each menu allocation, reconstruct its inequalities directly from bundle membership.
3. Require an exact checkable proof of unsatisfiability for region-and-failure formulas; cross-checking two solvers is corroboration, not a substitute for an audited encoding.
4. For a putative counterexample, verify exact nonnegativity and enumerate all complete allocations independently, retaining a violated comparison for each.
5. Have a fair-division researcher review regional coverage and compare the resulting lemma with existing existence theorems.

**Statement alignment:** Removing a good from the envied bundle is essential; every good is quantified, including zero values. Unallocated goods and approximate inequalities change the target.

**Human review difficulty:** High for a universal regional proof: the certificate checker, encoding and region cover all matter. A small concrete allocation is easy to check but does not prove existence for other values.

### Formal validity and empirical support

**What the formal task can establish:** The target is a theorem about idealized additive preferences. Only an aligned proof or exact counterexample supports a mathematical conclusion.

**Empirical support and limits:** No claim about measured human preferences, fairness judgments or implementation outcomes follows from the theorem.

### Methods and obstacles

**Proposed methods:**

- Exact linear-real encoding of allocation failures.
- Counterexample-guided allocation-menu generation on a declared rational polytope.
- Proof-carrying region subdivision, with independently checked branch coverage.

**Expected obstacles:**

- A finite grid of values cannot prove a statement over real valuations.
- Positive results can become vacuous if the selected region only contains a previously solved special class.
- Symmetry choices and discarded allocation clauses can silently remove hard boundary cases.

### Checks still needed

- Assess the novelty and usefulness of a proposed ten-good region before running it.
- Independently inspect the recent m≤9 certificate and any later version before relying on its detailed reductions.
- Refresh the all-m four-agent status before any claimed solution.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The August 2026 source still reports the unrestricted four-agent question as open while proving m≤9. Targeted later searches found no general resolution; the suggested m=10 pilot has not received a separate exhaustive novelty check.

**Exact problem / theorem locator:** Alkassar et al., Introduction and Theorem 1; He and Tao, Section 6.

### Sources

- [Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods](../sources.md#src-model-201). Eyad Alkassar; Mahmoud Fouz; Kurt Mehlhorn. 2026. [Read source](https://arxiv.org/html/2608.08590v1).
  - **Relevant sections:** Version 1, 9 August 2026; Introduction, Theorem 1, Definition 1, Lemmas 1–3 and Section 5.
  - **Source limitations:** Preprint. The associated computational certificate has not been independently replayed here. It does not establish the ten-good case.
- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202). Wentao He; Biaoshuai Tao. 2026. [Read source](https://arxiv.org/html/2606.08872v1).
  - **Relevant sections:** Version 1, 7 June 2026; Section 2, Theorems 1–3, start of Section 5 and Section 6.
  - **Source limitations:** Preprint. Distinguish common from personalized values, chores from goods, and fairness alone from fairness with efficiency.

### Known results and partial progress

- SRC-MODEL-201 reports the m≤9 theorem. Its continuous-domain encoding supplies a relevant method; it does not solve unrestricted m.
- SRC-MODEL-202 distinguishes additive goods, still open, from chore nonexistence and nonadditive goods counterexamples.

**Research value:** The four-agent case is a small-agent boundary of exact fair division. A new regional argument could expose reusable structure, but a collection of successful sampled allocations is not an existence theorem.

### Related problems

- **Related to:** [Exact EFX for common three-value additive goods](../candidates.md#q-model-206). Restricting the value alphabet is another route into additive-goods EFX; the unrestricted four-agent and arbitrary-agent three-value questions do not imply one another directly.

### Scope of the status check

**Finding:** The August 2026 source still reports the unrestricted four-agent question as open while proving m≤9. Targeted later searches found no general resolution; the suggested m=10 pilot has not received a separate exhaustive novelty check.

**Search limits:** Dated primary-source checks and targeted later-work searches cannot establish that no unpublished or newly posted solution exists. Refresh the literature before claiming progress.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods](../sources.md#src-model-201)
- [EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence](../sources.md#src-model-202)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Alkassar, Fouz and Mehlhorn (2026) provide a computer-assisted proof through nine goods; their package is an external public record, not a project attempt.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Eyad Alkassar
- Mahmoud Fouz
- Kurt Mehlhorn
- Wentao He
- Biaoshuai Tao

**Suggested citation:** Alkassar, Fouz and Mehlhorn (2026), arXiv:2608.08590v1; He and Tao (2026), arXiv:2606.08872v1, Section 6. These sources document the target and recent boundary results; the ten-good regional milestone is curator-proposed.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Exact linear constraints let AI propose regions and allocation menus while a separate checker tests each claim. A specialist must first judge whether the chosen region adds anything to known reductions.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI able to manipulate exact formulas, generate auditable code and explain mathematical assumptions.

**Uncertainty:** Novelty of any chosen ten-good subregion is unverified. Solver difficulty and generalization from local structure are unknown.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The allocation and inequality quantifiers are explicit. |
| Decomposability | High | Encoding, region selection, allocation generation and certificate checking can be separated. |
| Methods and literature | High | A recent bounded existence proof supplies a concrete continuous-region method. |
| Search / symbolic fit | High | Linear-real formulas support symbolic reasoning and solver-guided search. |
| Checkability | Medium | A finite certificate is possible, but covering continuous regions and validating the encoding require care. |
| Expertise needed | High | Fair-division and computer-assisted-proof expertise are needed. |
| Scholarly significance | High | The full target is a central small-agent existence case. |
| Verification difficulty | High | All valuations in the claimed region must be covered, including boundary faces. |

**Correctness:** No project answer.

The literature supports the question; no project answer has been submitted for review.

**Novelty:** Requires future literature review.

The all-m question is source-reported open. Neither the selected ten-good region nor any future certificate is claimed novel without a fresh literature comparison.

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
| Stable ID | `Q-MODEL-201` |
| Duplicate key | `efx0-four-additive-goods-complete` |
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
| Method tags | `proof`, `finite_search`, `exact_computation`, `certificate_checking`, `counterexample` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-201.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
