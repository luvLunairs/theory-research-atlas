# Binary length-12 covering codes of radius three

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Choose as few length-12 words over a 2-symbol alphabet as possible so that every possible word lies within 3 symbol changes of one chosen word. Any smaller verified cover improves a concrete finite bound.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CODE-201%3A+Binary+length-12+covering+codes+of+radius+three&target=Q-CODE-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CODE-201%3A+Binary+length-12+covering+codes+of+radius+three&target=Q-CODE-201)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Coding theory](../domains/info.md#info-codes) |
| Related fields | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Determine K_2(12,3), the smallest size of a set C in {0,...,1}^12 such that every word has Hamming distance at most 3 from some member of C. No linearity or symmetry restriction is imposed. The inspected sources report 19 &lt;= K_2(12,3) &lt;= 28; a certified improvement of either bound is a meaningful partial result.

**Required output:** Find and independently verify a cover of size at most 27, or obtain a rigorously certified improvement of the lower bound 19. Matching bounds would determine K_2(12,3); a one-sided improvement alone would not.

**Scope:** The exact finite parameter K_2(12,3). A proposed first milestone is a code with at most 27 words. This choice of milestone and the resource ceiling below are curator proposals, pending review; they are not a separate conjecture attributed to the source.

### Assumptions

- The alphabet is {0,...,1}, with ordinary Hamming distance: the number of unequal coordinates.
- The code is an arbitrary set, with no repeated words. Linear, additive and orbit-union constructions are optional search restrictions, not assumptions of the problem.
- Covering radius means at most the stated radius; the task is not a packing or minimum-distance problem.

### Success criteria

1. For a constructive improvement, provide a machine-readable list of at most 27 distinct words and a separate exhaustive coverage checker.
2. For a lower-bound improvement, supply a mathematical proof or independently checkable exact certificate valid for all unrestricted codes.
3. Record the achieved bound and its assumptions. A failed search, an infeasible restricted ansatz or a timeout is not a lower bound.
4. Recheck later literature before calling any improvement new.

### Background needed

- Hamming distance and covering codes
- Finite set covering and bitsets
- Exact integer arithmetic
- Certificate checking and basic computational reproducibility

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** A direct witness check for 27 codewords uses at most 1,327,104 coordinate comparisons. This is an operation bound, not a measured runtime. A direct binary set-cover formulation has 4,096 variables and 4,096 covering constraints. Proposed initial ceiling: 4 CPU-hours and 8 GiB RAM, stopping sooner on a verified improvement. This is a curator-chosen exploration cap, not an estimate of the resources needed to solve the problem; no run or cost measurement has been made.

**Data:** Generate the 4,096 words directly. Existing code constructions can be starting points if their provenance and version are recorded; no external empirical dataset is needed.

**Experiments:** No physical experiment.

**Theory and model requirements:** Finite combinatorics with exact Hamming distance. No model of physical noise or untested empirical assumption is required.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Refresh the parameter-specific literature and record the exact source versions.
2. Validate the alphabet, word lengths, distinctness and claimed code size.
3. Independently enumerate every one of the 4,096 words and check distance to the submitted code. Record any uncovered word as a counterexample to the claimed cover.
4. Use a separately written checker and save the submitted witness with a content hash.
5. For nonexistence claims, audit encoding completeness, all symmetry reductions and the complete proof certificate; a solver status alone is insufficient.
6. Obtain human review of correctness and a separate comparison with the literature for novelty.

**Statement alignment:** The checker must test covering, not packing, in the full unrestricted Hamming space. Properties of one additive or symmetric code family do not settle the unrestricted minimum.

**Human review difficulty:** Low to moderate for an explicit upper-bound witness. High for unrestricted lower bounds or exact optimality.

### Formal validity and empirical support

**What the formal task can establish:** A finite witness proves its stated covering bound only after exact checking; optimality needs a separate unrestricted lower bound.

**Empirical support and limits:** No empirical claim is involved. Heuristic success rates and AI performance are unknown.

### Methods and obstacles

**Proposed methods:**

- Represent each possible center by its exact Hamming-ball bitset.
- Use local replacement, tabu search or exact set-cover encodings with a declared cardinality target.
- Explore coordinate and symbol symmetries, documenting which restrictions may exclude valid codes.
- For lower bounds, investigate exact combinatorial arguments or rigorously certified optimization duals.

**Expected obstacles:**

- The feasible space of code subsets is enormous despite the small space of words.
- Greedy or local search can stall at the known bound.
- An orbit restriction can hide asymmetric improvements.
- Numerical SDP output alone is insufficient as a new exact lower-bound certificate.

### Checks still needed

- Confirm that no later construction or lower-bound improvement changes this exact parameter cell.
- Audit the source lower-bound certificate if it is needed in a future proof of optimality.
- Retrieve and independently validate any published starting construction before relying on it.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The most recent located primary bounds leave the interval [19,28] nontrivial. A targeted search for these parameters and subsequent improvements did not locate an exact value. This is a source-based gap, not an exhaustive certification of open status.

**Exact problem / theorem locator:** Table 1, row n=12, R=3

### Sources

- [Semidefinite lower bounds for covering codes](../sources.md#src-code-201). Dion Gijswijt; Sven Polak. 2026. [Read source](https://arxiv.org/html/2504.01932v2).
  - **Relevant sections:** arXiv:2504.01932v2; definition (1), Section 5, Tables 1–3 and numerical-method notes.
  - **Source limitations:** Selected definitions, table rows and computational notes inspected. Lower-bound certificates have not been independently audited. The quaternary upper bounds are superseded by SRC-CODE-202.

### Known results and partial progress

- The cited table or proposition reports 19 &lt;= K_2(12,3) &lt;= 28. These are literature claims, not bounds established by this project.
- The lower endpoint comes from the semidefinite bounds in SRC-CODE-201; the table also records an existing construction for the upper endpoint.

**Research value:** A small covering-code gap offers a concrete research output with an independently inspectable witness. The main value is an improved bound or construction principle, not the mere completion of a search.

### Related problems

- **Related method:** [Ternary length-seven covering codes of radius two](../candidates.md#q-code-202). Shares the covering-set formulation and exact witness checker; the parameter instances remain distinct mathematical questions.

### Scope of the status check

**Finding:** The inspected primary records leave a nontrivial interval. Parameter-specific searches for later exact values and improved bounds found no reliable resolution.

**Search limits:** The search is scoped and cannot establish absence of all later work. Recent preprint claims and numerical certificates have not been independently verified.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Semidefinite lower bounds for covering codes](../sources.md#src-code-201)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The inspected papers report computational bounds or constructions. Their reported runs are external research records and have not been repeated or used as AI benchmark results here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Dion Gijswijt
- Sven Polak

**Suggested citation:** Gijswijt and Polak, Semidefinite lower bounds for covering codes, arXiv:2504.01932v2 (2026), Table 1, row n=12, R=3. Credit earlier construction authors through the cited table references when reusing their codes.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

An explicit finite witness is cheap to inspect and the target is precise, making bounded construction search a reasonable first trial. The search itself may still be difficult.

**Model or capability conditions:** No named model evaluated; assumes a tool-using model able to implement finite search and integer checkers, with human review of problem encoding and novelty.

**Uncertainty:** No model has been evaluated on this task. A small universe and an inexpensive witness checker do not imply that a better cover is easy to find or exists at the selected target size.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | A finite Hamming space, radius and cardinality determine the question exactly. |
| Decomposability | High | Constructive upper-bound work can be separated from lower bounds and exact optimality. |
| Methods and literature | High | Set covering, local search, symmetry and exact optimization provide concrete tools; selecting an effective strategy remains research. |
| Search / symbolic fit | High | A code is a finite list and each Hamming ball has an exact bitset representation. |
| Checkability | High | A proposed upper-bound witness can be checked over all 4,096 words using integer operations. |
| Expertise needed | Medium | A construction checker is elementary; avoiding invalid symmetry restrictions and certifying lower bounds requires coding or optimization expertise. |
| Scholarly significance | Medium | An improved table entry is a modest, specific contribution; transferable constructions would have wider value. |
| Verification difficulty | Low | Low for an explicit covering witness; substantially higher for a nonexistence or optimality proof. |

**Correctness:** No project answer.

No new code or proof has been produced by this project.

**Novelty:** Requires future literature review.

A candidate improvement must be checked against current parameter tables and later papers.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Discovery and optimality remain difficult; witness verification is much easier than finding a better code.

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

A precise incremental bound improvement, with greater significance if a reusable method emerges.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-CODE-201` |
| Duplicate key | `covering-code-K-2-12-3` |
| Original domain label | Coding theory |
| Original cross-domain labels | Extremal and Ramsey theory |
| Primary domain ID | `INFO.CODES` |
| Cross-domain IDs | `MATH.COMB.EXT` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `finite_search`, `bounds`, `certificate_checking` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-CODE-201.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
