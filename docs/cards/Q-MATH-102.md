# Exact mixing certificates for small positive Markov chains

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Turn a small exact transition matrix into a checkable guarantee on how quickly its probability distributions approach equilibrium.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-102%3A+Exact+mixing+certificates+for+small+positive+Markov+chains&target=Q-MATH-102) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-102%3A+Exact+mixing+certificates+for+small+positive+Markov+chains&target=Q-MATH-102)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Markov chains, mixing and interacting systems](../domains/prob.md#prob-mix) |
| Related fields | [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process), [Randomized, online and distributed algorithms](../domains/cs.md#cs-random) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Given a rational row-stochastic matrix P of order 2 &lt;= n &lt;= 6 with every entry positive and every reduced denominator at most 100, compute its stationary probability row vector pi and tau = max_(i,j) (1/2) sum_k |P_ik-P_jk|. Certify d(t) = max_i ||P^t(i,.)-pi||_TV &lt;= tau^t for every integer t &gt;= 1, and return an integer T &gt;= 1 with tau^T &lt;= 1/100. Supply exact row-coupling certificates and a general argument, not only sampled trajectories.

**Required output:** An exact certificate package for stationarity, maximal one-step couplings, the contraction factor and an integer mixing bound.

**Scope:** Individual matrices satisfying the stated bounds. Strict positivity avoids reducibility, periodicity and a one-step coefficient equal to one; sparse chains require a separately specified extension.

### Assumptions

- The input is an n-by-n rational matrix, 2 &lt;= n &lt;= 6, with positive entries, row sums exactly one and reduced denominators at most 100.
- Time is discrete; row distributions evolve as mu P.
- Total variation is one half of the sum of absolute coordinate differences.
- The target bound concerns every integer t &gt;= 1; the fixed tolerance is 1/100. If tau=0, T=1 is admissible.

### Success criteria

1. Verify positivity, rational input limits and stochastic row sums exactly.
2. Return a nonnegative normalized row vector pi with pi P=pi and explain uniqueness under strict positivity.
3. Provide a rational coupling for each pair of rows with the correct marginals and mismatch probability equal to their total variation distance.
4. Prove the all-time inequality using the source's submultiplicativity or a coalescing coupling, then certify tau^T &lt;= 1/100 with rational arithmetic.

### Background needed

- Finite Markov chains and stationary distributions
- Total variation distance
- Exact linear algebra and probability couplings

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Rational linear algebra on matrices of order at most 6 and coupling tables of order at most 6 by 6. Rational bit lengths can grow when certifying large T; resource estimates should be recorded for selected inputs before execution.

**Data:** An explicit rational transition matrix; no observed trajectories or external data.

**Experiments:** No physical experiment or stochastic simulation is required.

**Theory and model requirements:** A finite homogeneous discrete-time Markov chain with a strictly positive stochastic matrix. This is a model-internal assertion, not an estimate of an unknown transition law.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Check every input constraint and the row-distribution convention.
2. Recompute pi P, normalization and nonnegativity with exact fractions.
3. Verify row-coupling marginal sums and mismatch probabilities independently.
4. Review the induction or coupling argument for all integer times and check the final rational inequality at T.

**Statement alignment:** The textbook applies broadly; the bounded task deliberately assumes strict positivity. It does not claim the displayed upper bound is the exact mixing time or infer P from data.

**Human review difficulty:** Moderate: finite arithmetic is straightforward; the passage from one-step certificates to all times needs a probability-trained reviewer.

### Formal validity and empirical support

**What the formal task can establish:** Certificates and proof must establish the bound for the exact supplied matrix.

**Empirical support and limits:** Applying the bound to measured systems would require separate evidence that their transition law is adequately represented by this fixed matrix.

### Methods and obstacles

**Proposed methods:**

- Maximal coupling construction
- Submultiplicativity of pairwise total variation
- Exact linear algebra
- Independent rational certificate checking

**Expected obstacles:**

- The coefficient can be close to one, giving a conservative bound.
- Floating-point stationarity residuals do not prove exact stationarity.
- A coupling must have the specified marginals at each step and remain together after meeting if the coalescence argument is used.

### Checks still needed

- Choose representative matrices, including identical-row and slowly contracting examples, before making performance comparisons.
- Any extension to chains with zero entries needs a new irreducibility, aperiodicity and multi-step analysis.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The cited textbook gives the coupling and submultiplicativity facts from which the stated certificate follows. Matrix-size, denominator and tolerance limits are curator-defined calibration conditions.

**Exact problem / theorem locator:** SRC-MATH-102, Proposition 4.7, Lemmas 4.11-4.12 and Corollary 5.3.

### Sources

- [Markov Chains and Mixing Times, first edition](../sources.md#src-math-102). David A. Levin; Yuval Peres; Elizabeth L. Wilmer. 2009. [Read source](https://www.cs.cmu.edu/~15859n/RelatedWork/MarkovChains-MixingTimes.pdf).
  - **Relevant sections:** Chapter 4: Proposition 4.2 (p. 48), Proposition 4.7 (pp. 50-51), Lemmas 4.11-4.12 (pp. 53-55); Chapter 5: Theorem 5.2 and Corollary 5.3 (pp. 64-65).
  - **Source limitations:** This is the first-edition text, distinct from the second-edition portal already indexed as SRC-FORMAL-014. The 2009 publication year is confirmed by the opened faculty record https://digitalcommons.oberlin.edu/faculty_schol/1345/; the author's portal also describes a 2008 first-edition release. No assertion of sharpness is made for the proposed bound.

### Known results and partial progress

- The textbook's Lemmas 4.11-4.12 bound distance to equilibrium by a submultiplicative pairwise distance; Proposition 4.7 and Corollary 5.3 give the coupling route.

**Research value:** A compact bridge between probabilistic arguments and exact certificates. It tests whether an assistant distinguishes a rigorous uniform bound from simulation-based evidence.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The contraction tools are established textbook results. This card specifies a bounded exact reproduction.

**Search limits:** No claim is made about optimal mixing-time estimation, all later refinements or actual solver performance.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Markov Chains and Mixing Times, first edition](../sources.md#src-math-102)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited text presents the underlying classical arguments. No specific matrix output is asserted here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- David A. Levin
- Yuval Peres
- Elizabeth L. Wilmer

**Suggested citation:** Levin, Peres and Wilmer (2009), Markov Chains and Mixing Times, first edition, Chapter 4 and Sections 5.1-5.2. Input limits and certificate packaging are editorial choices.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The proof decomposes into established coupling facts and exact arithmetic checks. Small input dimensions allow independent review while retaining an all-time probabilistic claim.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with finite probability, coupling arguments and exact rational computation.

**Uncertainty:** No model has been tested. A compact matrix does not ensure a sharp bound or small rational intermediates.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The admissible matrix class, norm and required inequality are specified. |
| Decomposability | High | Input checking, stationarity, couplings and the infinite-time argument are separable. |
| Methods and literature | High | The inspected textbook supplies both coupling and submultiplicativity approaches. |
| Search / symbolic fit | High | Linear systems and finite couplings admit rational certificates. |
| Checkability | High | A second exact checker can verify the finite objects; the short general argument is reviewable. |
| Expertise needed | Medium | Stationarity and coupling must be interpreted correctly; simulation intuition is insufficient. |
| Scholarly significance | Low | The bound is known and may be loose; the task mainly develops trustworthy probabilistic tools. |
| Verification difficulty | Medium | The main risk is mistaking several checked times for an all-time proof or mixing up row and column conventions. |

**Correctness:** No project answer.

No candidate answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

The mathematical result is established; the bounded reproduction protocol is not a claim of a new theorem.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The task combines finite exact calculations with a uniform probabilistic proof.

**Evidence type:** Editorial estimate not measured.

**Significance:** Low.

The main benefit is reliable preparation for more difficult mixing-time questions.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-102` |
| Duplicate key | `exact-mixing-certificates-for-small-positive-markov-chains` |
| Original domain label | Mixing times |
| Original cross-domain labels | Stochastic processes; Randomized algorithms |
| Primary domain ID | `PROB.MIX` |
| Cross-domain IDs | `PROB.PROCESS`, `CS.RANDOM` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `bounds`, `construction`, `exact_computation`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-102.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
