# Enumerate equilibria of a supplied rational bimatrix game

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Find every pair of mixed strategies that are best responses to one another in a small, fully specified mathematical game. The task tests complete case coverage and detection of inputs outside the algorithm scope; it makes no dynamical-stability claim.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-003%3A+Enumerate+equilibria+of+a+supplied+rational+bimatrix+game&target=Q-MODEL-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-003%3A+Enumerate+equilibria+of+a+supplied+rational+bimatrix+game&target=Q-MODEL-003)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Game and equilibrium theory](../domains/econ.md#econ-game) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Given rational m by n payoff matrices with m,n &lt;= 3 and a certified nondegeneracy assumption, reproduce support enumeration and output every Nash equilibrium with exact best-response certificates. Degenerate inputs must be flagged for a separate full-set treatment.

**Required output:** All equilibria with exact support and best-response certificates plus an explanation of completeness under nondegeneracy.

**Scope:** Nondegenerate rational bimatrix games only. Initial example: the source's equation (3), A=[[3,3],[2,5],[0,6]], B=[[3,2],[2,4],[3,0]]. Use degenerate examples only to check that the method identifies inputs outside its assumptions, not to claim the same enumeration algorithm is complete there.

### Assumptions

- Two players, simultaneous finite normal-form game and expected-utility maximization.
- Independent mixed strategies and rational payoff matrices of dimensions at most 3 by 3.
- Nondegeneracy: for either player, every mixed strategy with support size k gives the opponent at most k pure best responses. Certify this over all mixed strategies, not merely equilibria or sampled points.
- The task concerns equilibria of the stated game, not predictions about actual people.

### Success criteria

1. Document rational input and prove or independently certify the required nondegeneracy condition.
2. Enumerate support pairs and retain exact feasibility decisions.
3. Check nonnegativity, unit sums, on-support equality and off-support payoff inequalities.
4. Compare with the known source example while retaining the independent completeness argument.
5. Route degenerate cases to a separate set-valued method; do not silently omit continua or unequal-support cases.

### Background needed

- Expected payoffs and mixed strategies.
- Rational linear systems and inequalities.
- Combinatorics of supports and the precise definition of nondegeneracy.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** At most 3 by 3 matrices with a declared bit-length bound to be set in the trial. Small support enumeration is a plausible local workload; no time, cost or success measurements exist.

**Data:** Only declared payoff matrices; no personal, market or experimental data are needed.

**Experiments:** None for equilibrium computation. Behavioral interpretation requires a separate empirical study.

**Theory and model requirements:** Finite complete-information normal-form game; risk-neutral expected utility as represented by supplied payoffs; nondegeneracy for the selected algorithm.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Freeze payoff orientation and all rational entries.
2. Certify nondegeneracy with a complete method appropriate to the small game.
3. Check every support case and every reported rational certificate using independently written checks.
4. Compare the example with the source while auditing omitted cases.
5. Have a reviewer inspect completeness and economic scope separately.

**Statement alignment:** An exact best-response certificate validates the listed pair. Completeness needs the enumeration theorem and its nondegeneracy hypothesis; checking pairs alone is insufficient.

**Human review difficulty:** Moderate: arithmetic can be automated, but a game theorist should confirm hypothesis certification and all-equilibria completeness.

### Formal validity and empirical support

**What the formal task can establish:** An equilibrium is a mathematical best-response statement under the declared payoff and behavior model.

**Empirical support and limits:** No evidence is provided that real agents know the game, maximize expected utility or select these equilibria. The card offers no policy or behavioral forecast.

### Methods and obstacles

**Proposed methods:**

- finite search
- exact computation
- algorithm reproduction
- classification

**Expected obstacles:**

- Solving indifference equations but forgetting profitable off-support deviations.
- Equating supports without establishing nondegeneracy.
- Returning one equilibrium when all were requested.
- Floating-point tolerances hide zero probabilities or ties.
- Mistaking a model equilibrium for a descriptive or normative recommendation.

### Checks still needed

- Set an input numerator/denominator bit-length bound before benchmarking resource use.
- Select and review the independent nondegeneracy check.
- A future extension to degenerate games must represent equilibrium continua and cite the relevant full-set method.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The opened author survey gives support enumeration and explains its nondegeneracy requirement. The &lt;=3 restriction is a curator-selected calibration scope.

**Exact problem / theorem locator:** von Stengel Section 2, Definition 2, Propositions 1 and 3, Algorithm 4; Section 7

### Sources

- [Finding Nash Equilibria of Two-Player Games](../sources.md#src-model-007). Bernhard von Stengel. 2021. [Read source](https://arxiv.org/html/2102.04580).
  - **Relevant sections:** Section 2, Proposition 1 and Algorithm 4; Sections 7-9
  - **Source limitations:** Algorithms for general games can be expensive; Algorithm 4 requires nondegeneracy.

### Known results and partial progress

- Von Stengel Proposition 1 characterizes best responses by support and maximum payoff.
- Algorithm 4 enumerates all equilibria for a nondegenerate game; later sections describe degeneracy and full equilibrium sets.

**Research value:** A compact calibration for exhaustive reasoning, exact certificates and assumption handling. Larger market or mechanism models would need different inputs and substantive economic justification.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** Full Section 2 and later section descriptions were inspected. Established algorithm and worked example make this a known-result calibration.

**Search limits:** No solver, example reproduction or AI performance evaluation was executed.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Finding Nash Equilibria of Two-Player Games](../sources.md#src-model-007)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Von Stengel (2021) Section 2 contains an explicit worked 3 by 2 example. This literature reproduction is not a project experiment.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Bernhard von Stengel (inspected algorithm exposition)
- John Nash (equilibrium concept)

**Suggested citation:** von Stengel, B. (2021). Finding Nash Equilibria of Two-Player Games. arXiv:2102.04580, Section 2, Proposition 1, Algorithm 4 and equation (3).

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

A finite support search and exact certificates permit independent checking. The source's fully specified example makes the trial transferable without inventing new economic claims.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with literature retrieval, exact algebra or rational linear algebra, code generation, and access to a human domain reviewer.

**Uncertainty:** No named model or solver was run. Reproducing familiar examples may reflect memorization. General bimatrix complexity cannot be inferred from the small trial.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Inputs, outputs and equilibrium inequalities are explicit. |
| Decomposability | High | Check hypotheses, enumerate supports, solve, validate and prove completeness separately. |
| Methods and literature | High | An opened author survey supplies definitions, algorithm and example. |
| Search / symbolic fit | High | Finite enumeration and rational linear algebra are directly applicable. |
| Checkability | High | Every candidate can be verified using payoff inequalities. |
| Expertise needed | Medium | Game-theory review is needed for nondegeneracy and completeness, not just algebra. |
| Scholarly significance | Medium | Valuable correctness calibration; no novel equilibrium result or behavioral prediction. |
| Verification difficulty | Medium | Checking one equilibrium is simple; certifying the whole list and rejecting degenerate inputs is harder. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-003` |
| Duplicate key | `bimatrix-nondegenerate-support-enumeration` |
| Original domain label | Noncooperative game theory |
| Original cross-domain labels | Algorithms; Polyhedral geometry |
| Primary domain ID | `ECON.GAME` |
| Cross-domain IDs | `CS.ALG`, `MATH.OPT` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `algorithm`, `proof`, `exact_computation`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-003.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
