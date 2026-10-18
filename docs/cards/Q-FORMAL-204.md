# The optimal randomized stretch for two online bins

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Items arrive one at a time and must immediately be assigned to one of two bins. They could have fit in two unit bins if their future sizes were known. How much extra load is unavoidable when the online algorithm may randomize?

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-204%3A+The+optimal+randomized+stretch+for+two+online+bins&target=Q-FORMAL-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-204%3A+The+optimal+randomized+stretch+for+two+online+bins&target=Q-FORMAL-204)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Randomized, online and distributed algorithms](../domains/cs.md#cs-random) |
| Related fields | [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Determine inf_A sup_I E[max(L1(A,I),L2(A,I))], where I ranges over finite positive real item sequences that fit offline into two unit-capacity bins, A assigns each arriving item irrevocably before seeing the next, and I is fixed independently of A's random bits. Can the reported interval [7/6,5/4] be narrowed?

**Required output:** Produce a compact exact lower-bound certificate exceeding the cited baseline, or an exact value for the explicitly limited game with a clear statement of its limited scope.

**Scope:** Curator-proposed first milestone, pending review: search a declared pool of at most 200 input sequences, each of length at most eight and with sizes in {1/8,2/8,…,1}. Seek a rational probability distribution on that pool whose expected load exceeds 7/6 for every deterministic online policy. The pool and grid are exploratory restrictions; their potential to improve the known lower bound is unverified.

### Assumptions

- Every input is a finite sequence of strictly positive real sizes with an explicit offline packing into two unit bins.
- Assignments are irrevocable and depend only on revealed items, prior assignments and private randomness.
- The adversary is oblivious: its full input is fixed independently of the algorithm's random bits.
- The objective is the expectation of the maximum final load, then the worst case over inputs; changing the order of these operations changes the problem.

### Success criteria

1. A genuine improvement must lower-bound every deterministic history-consistent policy on the selected input distribution, not merely a chosen library of heuristics.
2. Supply rational input probabilities, offline packing witnesses and an exact independently checked proof of the minimum expected cost over all policies.
3. A restricted-game optimum no larger than 7/6 is a bounded negative result only. It neither proves optimality for the full problem nor rules out stronger distributions.
4. Stop if the complete game representation exceeds 20,000 history states or the stated memory/time cap. Do not silently prune legal online actions.

### Background needed

- Competitive analysis with oblivious adversaries.
- Finite zero-sum games, rational linear programming and dual certificates.
- Online information constraints and offline feasibility of a packing.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** The input pool is capped at 200 sequences of at most eight items. Build the complete online-history representation for that pool only, stopping before 20,000 history states, 1 GiB memory or four elapsed hours. Exact arithmetic can be substantially costlier than floating-point search. These are proposed limits, not measured costs; a small grid is not a guarantee of a small policy space.

**Data:** A finite list of rational item sequences and offline packings; no empirical dataset.

**Experiments:** No physical experiment.

**Theory and model requirements:** The finite-distribution lower bound uses the minimax/Yao principle with the stated oblivious adversary. The checker must range over all deterministic online policies allowed by the shared-prefix information structure.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Check every input size, every rational distribution weight, normalization and every offline packing.
2. Verify identical observed histories impose the same policy choices; hidden future items cannot enter the policy state.
3. Recompute the minimum expected load over all deterministic policies in the finite support game using an independent exact method.
4. Check any LP dual or dynamic-programming certificate in rational arithmetic.
5. Apply the lower-bound transfer argument explicitly; compare the resulting rational value with 7/6.

**Statement alignment:** The milestone restricts the adversary's support, not the algorithm's policy class. Its lower bound transfers to the full problem; a restricted-game upper bound does not.

**Human review difficulty:** High for the reduction from a computational game to the randomized online claim; lower for arithmetic once the game is sound.

### Formal validity and empirical support

**What the formal task can establish:** A valid finite oblivious input distribution lower-bounds the full randomized optimum only when all admissible online policies are covered.

**Empirical support and limits:** Performance on sampled inputs is not a worst-case bound. No application workload or practical scheduling benefit is asserted.

### Methods and obstacles

**Proposed methods:**

- Rational distributions on finite feasible input pools.
- History-consistent game formulations and exact dynamic programming.
- Linear-programming search followed by rational reconstruction and certificate checks.

**Expected obstacles:**

- Enumerating policies directly grows exponentially.
- Restricting algorithms to a heuristic library invalidates a general lower bound.
- An adaptive adversary can prove a different and easier statement than the required oblivious-adversary result.
- A finite-grid algorithm does not automatically handle arbitrary real item sizes.

### Checks still needed

- Confirm the exact finite-game formulation against the source before implementation.
- Recheck later publications for improved numerical bounds before interpreting an improvement.
- Determine whether the proposed grid already appears in the source's computational data.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The randomized paper gives distinct lower and upper bounds. The author publication list and later computational-method paper were checked; no closing of this randomized gap was identified. The later paper primarily concerns deterministic algorithms.

**Exact problem / theorem locator:** Lhomme–Catusse–Brauner, randomized paper §§2–4.2; later convergence paper §1.

### Sources

- [Computational bounds on randomized algorithms for online bin stretching](../sources.md#src-formal-206). Antoine Lhomme; Nicolas Catusse; Nadia Brauner. 2024. [Read source](https://arxiv.org/html/2405.19071).
  - **Relevant sections:** Definitions in §2; §3 game formulation; §§4.1–4.3, Theorems 4.1 and 4.5; §5.
  - **Source limitations:** The finite discretization is a lower-bound device; a strategy only valid for grid inputs is not a continuous-input upper bound. The M2 lower bound is not a lower bound for unrestricted randomization.
- [On the convergence of computational methods for the online bin stretching problem](../sources.md#src-formal-207). Antoine Lhomme; Nicolas Catusse; Nadia Brauner. 2025. [Read source](https://arxiv.org/html/2506.17271v1).
  - **Relevant sections:** §1 and Figure 1; §§1.1–1.2; §2 convergence theorem.
  - **Source limitations:** Convergence is an established result of this paper, not an open candidate. It does not make fine discretizations computationally inexpensive or settle the small-bin optima.
- [Antoine Lhomme: publications](../sources.md#src-formal-209). Antoine Lhomme. Year not verified. [Read source](https://lhommeant.github.io/).
  - **Relevant sections:** Publication entries for randomized bin stretching and the 2025 convergence paper.
  - **Source limitations:** No page publication date was verified. Absence of a listed paper cannot establish that a question remains open.

### Known results and partial progress

- The randomized paper reports lower bound 7/6 and an algorithm with expected stretch at most 5/4 for two bins.
- Its stronger 29/24 lower bound concerns the restricted class M2 and cannot replace 7/6 for unrestricted randomization.
- Finite-grid lower bounds and all-real-input upper bounds require different arguments.

**Research value:** A small certified distribution can improve a general online lower bound while remaining inspectable. It also tests whether the current gap can be approached with compact adversarial examples.

### Related problems

- **Related to:** [Optimal two-bin stretch using an initial mixture of two deterministic policies](../candidates.md#q-formal-210). M2 restricts the algorithm's randomization and has a different lower bound.
- **Method bridge to:** [The optimal deterministic stretch for three online bins](../candidates.md#q-formal-206). Both use finite adversarial certificates, but deterministic and randomized information structures differ.

### Scope of the status check

**Finding:** The inspected randomized paper retains a two-bin gap; the later convergence paper and author list did not supply a resolution.

**Search limits:** Later deterministic results cannot by themselves certify the randomized frontier. The search did not establish exhaustive coverage of all 2026 work.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Computational bounds on randomized algorithms for online bin stretching](../sources.md#src-formal-206)
- [On the convergence of computational methods for the online bin stretching problem](../sources.md#src-formal-207)
- [Antoine Lhomme: publications](../sources.md#src-formal-209)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Lhomme, Catusse and Brauner provide computational bounds and an explicit randomized upper construction. These external results have not been reproduced here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Antoine Lhomme
- Nicolas Catusse
- Nadia Brauner

**Suggested citation:** Lhomme, Catusse and Brauner, Computational bounds on randomized algorithms for online bin stretching, arXiv:2405.19071 (2024), §§2–4.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Finite games offer exact certificates and a bounded entry point, but a game model that leaks future input information or omits policies yields invalid bounds.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI can formulate finite games and rational certificates, with an independent verifier and human review of adversary semantics.

**Uncertainty:** The small proposed support may be incapable of improving 7/6. No search, runtime, model performance or success probability has been measured.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The cost, adversary and feasible input sequences are explicit. |
| Decomposability | High | One can investigate small rational supports before seeking a general algorithm. |
| Methods and literature | High | The source gives game and linear-programming approaches. |
| Search / symbolic fit | High | Rational optimization and finite-history search are suitable. |
| Checkability | Medium | Certificates can be exact, but their game semantics require careful review. |
| Expertise needed | High | Online-algorithm and minimax expertise is needed to validate the quantifiers. |
| Scholarly significance | High | Any strict certified improvement applies to the unrestricted randomized problem. |
| Verification difficulty | High | A numerical LP optimum is insufficient; complete policy coverage and exact feasibility must be established. |

**Correctness:** No project answer.

No game was solved and no bound was computed in this project.

**Novelty:** Requires future literature review.

The literature gap is sourced; the restricted support is curator-proposed and may reproduce existing computations.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Small exact games are approachable; a stronger general bound may require larger support or new ideas.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

An exact lower-bound improvement would narrow a concrete online-optimization gap.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-204` |
| Duplicate key | `the-optimal-randomized-stretch-for-two-online-bins` |
| Original domain label | Randomized, online and distributed algorithms |
| Original cross-domain labels | Optimization and operations research |
| Primary domain ID | `CS.RANDOM` |
| Cross-domain IDs | `MATH.OPT` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `finite_search`, `bounds`, `exact_computation`, `certificate_checking`, `algorithm` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-204.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
