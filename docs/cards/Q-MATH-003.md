# Determine the four-color triangle Ramsey number R(3,3,3,3)

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How many vertices force a same-colored triangle when every pair is assigned one of four colors? Existing constructive and universal bounds leave a gap.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-003%3A+Determine+the+four-color+triangle+Ramsey+number+R%283%2C3%2C3%2C3%29&target=Q-MATH-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-003%3A+Determine+the+four-color+triangle+Ramsey+number+R%283%2C3%2C3%2C3%29&target=Q-MATH-003)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Determine the least positive integer N such that every map from the unordered pairs of {1,...,N} to {1,2,3,4} gives some three distinct vertices whose three pair colors are equal.

**Required output:** Find an exact integer N and establish both a triangle-free four-coloring of K_(N-1) and a proof that no such coloring of K_N exists.

**Scope:** The unrestricted finite threshold. A restricted construction class or a single improved bound is valuable partial progress but does not determine the exact number.

### Assumptions

- Finite simple complete graph K_N, without loops.
- Coloring is a total map from unordered two-element vertex subsets to {1,2,3,4}; not all colors need occur.
- A monochromatic triangle uses three distinct vertices with all three pair colors equal.
- No restrictions such as cyclicity, group constructions, or balanced color-class sizes are imposed.

### Success criteria

1. For a lower bound, serialize a complete coloring and independently test all vertex triples.
2. For an upper bound, supply a complete mathematical proof or a complete encoding with a independently checkable unsatisfiability proof and justified symmetry reductions.
3. For exact determination, the certified lower and upper bounds must coincide.
4. Document theorem assumptions, source versions, computation artifacts, reviewer scope, and unresolved gaps.
5. A certified improvement alone is labeled partial progress, not resolution.

### Background needed

- Extremal graph theory and Ramsey bounds
- Multicolor edge encodings and symmetry
- SAT/constraint programming and certificate checking for computational approaches
- Literature on critical colorings and structural upper-bound arguments

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Unassessed and potentially substantial. The naive space at N vertices is 4^(N*(N-1)/2). Structural restrictions, solver complexity, certificate storage, and checking cost require separate planning. No hardware, runtime, fee, or affordable-solution promise is made.

**Data:** Public papers and, for a future attempt, existing lower-bound colorings with checked provenance. No empirical dataset required.

**Experiments:** None; a mathematical finite-coloring problem.

**Theory and model requirements:** Ordinary finite combinatorics. Every symmetry breaking or restricted construction must have its scope proved. Approximate SDP output is not by itself an upper-bound certificate.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Specialist verifies current scope and rechecks recent literature before a future attempt.
2. Verify a lower-bound artifact on every triple with a separately authored exact checker.
3. For upper bounds, audit reduction from the mathematical statement to constraints, including both directions and all symmetry assumptions.
4. Check any solver proof with an independently maintained checker and preserve environment, hashes, and logs.
5. Human reviewers separate correctness, novelty, and significance; perform a fresh novelty/status search before announcing progress.
6. If formalized, review the correspondence between the formal finite coloring theorem and the unrestricted source question.

**Statement alignment:** Four available colors, unordered edges, and monochromatic triangles are essential. Proving an asymptotic density theorem or impossibility inside one construction family does not solve the threshold problem.

**Human review difficulty:** High for universal upper bounds; low for a supplied finite lower-bound witness after its complete encoding is established.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made.

### Methods and obstacles

**Proposed methods:**

- Construction
- Bounds improvement
- Proof
- Finite search
- SAT/constraint programming
- Exact certificate checking
- Optional symbolic inequality or semidefinite methods with exact certification

**Expected obstacles:**

- Search space grows exponentially in the number of edges.
- Failure to find a coloring is not nonexistence.
- Restricted cyclic/group constructions may have known limitations.
- The source notes a typo in a displayed historical lower-bound matrix; reconstructing from the paper without checking is unsafe.
- Ramsey multiplicity, Ramsey thresholds, and unrelated Rado-number notation can be confused in searches.
- Old source lists and unreviewed online claims can disagree.

### Checks still needed

- Inspect Chung's original lower-bound construction and obtain a corrected machine-readable witness.
- Audit the full upper-bound paper and available code before adopting its implementation.
- Perform a focused citation-forward review after April 2026 in addition to this web search.
- Select a genuinely bounded research subproblem only after expert review; do not treat the full question as the first cheap AI trial.
- Estimate computation and proof-checker storage only after selecting a method.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The April 2026 author-maintained survey explicitly calls this open and states 51 &lt;= N &lt;= 62. Targeted October 2026 searches found no source establishing an exact value; the inspected recent-sounding multiplicity paper addresses a different quantity. This is a scoped literature check, not proof that no solution exists.

**Exact problem / theorem locator:** DS1.18 section 6.1.1, printed page 56 (PDF page index 55); Fettes–Kramer–Radziszowski abstract; Kiem–Pokutta–Spiegel section 2.

### Sources

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001). Stanisław P. Radziszowski. 2026. [Read source](https://www.cs.rit.edu/~spr/ElJC/sur.pdf).
  - **Relevant sections:** Revision 18, 24 April 2026; sections 2.1 and 6.1.1, Tables Ia and Ib; selected two-color and four-color bounds.
  - **Source limitations:** Living URL may change; record revision before each reuse. Selected entries were inspected, not every cited computation. For R(4,6), read Table Ib together with Table Ia rather than treating the earlier table as current on its own.
- [An Upper Bound of 62 on the Classical Ramsey Number R(3,3,3,3)](../sources.md#src-math-013). Susan E. Fettes; Richard L. Kramer; Stanisław P. Radziszowski. 2004. [Read source](https://repository.rit.edu/article/667/).
  - **Relevant sections:** Institutional record abstract and recommended citation; Ars Combinatoria 72, 41–63; publisher abstract independently opened
  - **Source limitations:** Inspection is limited to institutional and publisher abstracts. The full computational proof and software have not been independently verified.
- [The Four-Color Ramsey Multiplicity of Triangles](../sources.md#src-math-014). Aldo Kiem; Sebastian Pokutta; Christoph Spiegel. 2023. [Read source](https://arxiv.org/pdf/2312.08049).
  - **Relevant sections:** arXiv:2312.08049v1; abstract, Theorem 1.1, section 2 definitions
  - **Source limitations:** Only relevant definitions and theorem scope inspected. This result must not be mistaken for an exact finite Ramsey threshold or for this project's AI evidence.

### Known results and partial progress

- The April 2026 dynamic survey gives 51 &lt;= R(3,3,3,3) &lt;= 62 and explicitly calls the exact value open.
- Fettes, Kramer, and Radziszowski establish the upper bound 62 (2004).
- The Kiem–Pokutta–Spiegel asymptotic multiplicity theorem concerns triangle density, not this finite threshold.

**Research value:** A concrete unresolved finite parameter connects extremal constructions, structural graph theory, and computational proof. Its apparent simplicity does not make its search space tractable.

### Related problems

- **Calibrated by:** [Reproduce the exact Ramsey number R(3,3)=6](../candidates.md#q-math-001). The two-color known-result case can test encoding and checking, without predicting performance at the open four-color scale.
- **Related to:** [Determine the two-color Ramsey number R(5,5)](../candidates.md#q-math-004). Both seek finite Ramsey thresholds, but color counts and forbidden clique sizes differ; they are not duplicate or equivalent problems.

### Scope of the status check

**Finding:** Current opened author survey explicitly reports open. Inspected primary upper-bound metadata supports 62; the relevant multiplicity paper does not settle this threshold. No exact solution was found in the scoped search.

**Search limits:** No exhaustive database/citation search and no private or unpublished results checked. The 2026 journal publication of the multiplicity paper was not independently opened; the inspected author preprint is dated 2023.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001)
- [An Upper Bound of 62 on the Classical Ramsey Number R(3,3,3,3)](../sources.md#src-math-013)
- [The Four-Color Ramsey Multiplicity of Triangles](../sources.md#src-math-014)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Published computer-assisted upper-bound work: Fettes, Kramer, Radziszowski (2004).
- The dynamic survey attributes the lower bound to Chung and warns about an error in a displayed matrix; the original construction was not independently inspected.
- No attempt or model test by this project.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Stanisław P. Radziszowski (consulted survey and statement)
- Susan E. Fettes
- Richard L. Kramer
- Stanisław P. Radziszowski (upper-bound paper)
- Fan Chung (lower bound, credited in survey; original paper not yet inspected)

**Suggested citation:** Radziszowski, Small Ramsey Numbers, Electronic Journal of Combinatorics DS1, revision 18 (24 April 2026), section 6.1.1; Fettes, Kramer, Radziszowski, Ars Combinatoria 72 (2004), 41–63, institutional record https://repository.rit.edu/article/667/. Cite original construction after direct inspection.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

Precise objects and locally verifiable constructions offer a credible role for tool-using AI in literature synthesis, encoding audit, or designing bounded subproblems. The exact unrestricted target requires substantial combinatorial expertise and may exceed available resources.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI capable of reading advanced combinatorics, writing exact graph code, and working under specialist human review.

**Uncertainty:** No named model or project attempt was evaluated. Public computer-assisted mathematics supports the method family, not a measured AI ability to improve these bounds. A solution newer than the scoped search may exist.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | A finite extremal threshold with two complementary proof obligations. |
| Decomposability | Medium | Construction, structural lemmas, and upper-bound certification separate, but difficult global dependencies remain. |
| Methods and literature | High | Relevant graph constructions, computer-assisted bounds, and exact proof-checking methods are established. |
| Search / symbolic fit | High | Colorings and constraints have explicit discrete encodings; this does not make exhaustive search feasible. |
| Checkability | Medium | A candidate construction is cheap to check; global nonexistence proofs may be large and difficult. |
| Expertise needed | High | An extremal combinatorics expert and computational-proof reviewer are needed. |
| Scholarly significance | High | The author-maintained survey highlights this open multicolor case. |
| Verification difficulty | High | Upper-bound completeness, solver proof artifacts, and symmetry reductions can dominate review. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Requires future literature review.

This is a literature-stated open target with a scoped status check. No project result exists. Any proposed new bound, construction or exact value needs comparison with current literature and the precise problem assumptions before novelty can be claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The reasons are given in the [AI trial assessment](#assessment).

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
| Stable ID | `Q-MATH-003` |
| Duplicate key | `math:ramsey:4colors:triangle:exact-threshold` |
| Original domain label | Combinatorics |
| Original cross-domain labels | Graph theory; Theoretical computer science; Optimization |
| Primary domain ID | `MATH.COMB.EXT` |
| Cross-domain IDs | `CS.ALG`, `MATH.OPT` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `construction`, `bounds`, `finite_search`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-003.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
