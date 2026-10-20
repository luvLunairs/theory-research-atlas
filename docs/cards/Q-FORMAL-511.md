# A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Can two 4x4 matrices be multiplied using 47 bilinear products instead of the 48 in current characteristic-zero constructions?

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-511%3A+A+rank-47+decomposition+for+4x4+matrix+multiplication+in+characteristic+zero&target=Q-FORMAL-511) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-511%3A+A+rank-47+decomposition+for+4x4+matrix+multiplication+in+characteristic+zero&target=Q-FORMAL-511)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit) |
| Related fields | [Algebra](../domains/math.md#math-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Find r&lt;=47 and linear forms L_s,R_s on complex 4x4 matrices, with coefficient matrices P_s, such that AB=sum_{s=1}^r L_s(A)R_s(B)P_s for every pair A,B. Supply exact coefficients and verify the identity. A rational construction is a stronger coefficient restriction; a characteristic-two or border-rank construction does not meet this target.

**Required output:** An explicit exact decomposition with r&lt;=47, with a fully specified coefficient representation.

**Scope:** The fixed-size exact tensor problem. It does not ask for the general matrix-multiplication exponent or a claim of hardware speedup.

### Assumptions

- Use the exact bilinear tensor of ordinary 4x4 matrix multiplication over C; identify a more restrictive coefficient field such as Q explicitly.
- Count products of an A-linear form and a B-linear form. Additions and multiplication by fixed coefficients are not part of this rank count.
- The identity must hold for all inputs. Small numerical residuals and limiting border-rank decompositions are insufficient.

### Success criteria

1. Provide all linear-form and output coefficients, ordering conventions and coefficient-field relations.
2. Verify every tensor coefficient exactly in an independent checker.
3. State whether the construction is rational or genuinely complex and assess practical implementation claims separately.

### Background needed

- Bilinear algorithms and tensor rank
- Exact rational or algebraic-number arithmetic
- Polynomial identity checking

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** A fixed candidate has a finite exact checker; search cost is unconstrained and may be substantial. Coefficient growth can also make checking expensive. No project runtime or budget is measured.

**Data:** Exact baseline and proposed coefficient arrays with source attribution. Floating-point arrays require exact recovery before certification.

**Experiments:** None for the algebraic identity.

**Theory and model requirements:** Characteristic zero and exact arithmetic; specify the coefficient field and any quotient-polynomial relations.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Fix matrix-entry ordering and independently generate the target bilinear tensor.
2. Check the number of terms and exact coefficient representation.
3. Verify all coefficient equations over the declared field without floating-point tolerance.
4. Inspect source lineage and compare with published schemes; benchmark additions, memory and stability only if practical performance is claimed.

**Statement alignment:** A characteristic-two identity, border-rank limit or faster implementation with 48 products does not establish this target.

**Human review difficulty:** Moderate for a compact exact construction; much higher for an impossibility claim or a complicated coefficient field.

### Formal validity and empirical support

**What the formal task can establish:** An exact tensor identity establishes the declared bilinear algorithm over its coefficient field.

**Empirical support and limits:** Rank alone establishes neither numerical stability nor wall-clock improvement on hardware.

### Methods and obstacles

**Proposed methods:**

- Published tensor-decomposition representations
- Exact coefficient checking
- Source-based algebraic or computational searches

**Expected obstacles:**

- A nonconvex search may converge only approximately.
- Field-specific cancellations may not survive lifting to characteristic zero.
- Search failure within a chosen ansatz is not a global rank lower bound.

### Checks still needed

- Independent verification of any imported baseline coefficient files.
- A fresh literature and catalog check before claiming a new record.
- Exact recovery and field validation for any future numerical candidate.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The maintained problem page calls the target unsolved, the institutional catalog lists rank 48, and the October 2026 campaign reports no rank-47 construction. No matching resolution was found in a focused search; this does not establish a lower bound.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-511.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** SRC-IMPACT-006 mathematical specification; SRC-IMPACT-007 sections 4-6; SRC-IMPACT-008 Results; SRC-IMPACT-010 Commentaries.

### Sources

- [The Rank of the 4x4 Matrix-Multiplication Tensor](../sources.md#src-impact-006). Epoch AI. 2026. [Read source](https://epoch.ai/frontiermath/open-problems/matrix-multiplication).
  - **Relevant sections:** About the problem and mathematical specification.
  - **Source limitations:** A maintained problem listing, not an exhaustive status review. Its field and exactness requirements are essential.
- [A non-commutative algorithm for multiplying 4x4 matrices using 48 non-complex multiplications](../sources.md#src-impact-007). Jean-Guillaume Dumas; Clément Pernet; Alexandre Sedoglavic. 2025. [Read source](https://arxiv.org/html/2506.13242v7).
  - **Relevant sections:** Version 7, 2026-07-27; abstract, sections 4-6 and appendix A.
  - **Source limitations:** Original submission 2025-06-16. The explicit identity and programs were inspected as literature, not independently executed.
- [Cloudroom Math: new matrix multiplication algorithms found by AI agents](../sources.md#src-impact-008). Cloudroom Math Campaign. 2026. [Read source](https://github.com/matyasstoch/cloudroom-math).
  - **Relevant sections:** README: Results, Scope and honesty; release dated 2026-10-08.
  - **Source limitations:** Public, unreviewed attempt report. Negative search is not an impossibility proof; its other algorithms were not checked.
- [Description of fast matrix multiplication algorithm: 4 x 4 x 4](../sources.md#src-impact-010). Alexandre Sedoglavic. Year not verified. [Read source](https://fmm.univ-lille.fr/4x4x4.html).
  - **Relevant sections:** Algorithm description and Commentaries.
  - **Source limitations:** Undated maintained page, inspected on 2026-10-20. Encodings and performance claims were not independently reproduced.

### Known results and partial progress

- SRC-IMPACT-007 gives a rational 48-term construction, following the complex construction; its abstract distinguishes the 47-term characteristic-two result.
- SRC-IMPACT-006 still lists the complex rank-47 target as unsolved. SRC-IMPACT-010 supplies the rank-48 baseline encodings.
- SRC-IMPACT-008 reports an unsuccessful October 2026 search. Failure of that search does not exclude other decompositions.

**Research value:** A smaller exact decomposition would improve a recognized small-size algebraic-complexity record. Its mathematical insight and practical speed need separate assessment.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The maintained listing and catalog retain the 47-term gap; the October attempt explicitly reports no solution.

**Search limits:** Focused search only. Neither coefficient files nor claimed obstructions were independently checked.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "4x4" "rank" "47" "2026" matrix multiplication
- "matrix multiplication" "rank 47" rational 2026
- "4" "matrix multiplication" "47" "October 2026"
- "2506.13242" "2026" rank 47

**Sources checked:**

- [The Rank of the 4x4 Matrix-Multiplication Tensor](../sources.md#src-impact-006)
- [A non-commutative algorithm for multiplying 4x4 matrices using 48 non-complex multiplications](../sources.md#src-impact-007)
- [Cloudroom Math: new matrix multiplication algorithms found by AI agents](../sources.md#src-impact-008)
- [Description of fast matrix multiplication algorithm: 4 x 4 x 4](../sources.md#src-impact-010)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The referenced public campaign supplies negative search results. Existing rank-48 constructions are baseline results, not project discoveries.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Epoch AI
- Jean-Guillaume Dumas
- Clément Pernet
- Alexandre Sedoglavic

**Suggested citation:** Epoch AI, The Rank of the 4x4 Matrix-Multiplication Tensor (2026); Dumas, Pernet and Sedoglavic, arXiv:2506.13242v7 (2025; revised 2026-07-27). Cite the original schemes and later attempt records when using their data.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

Exact certificates make results easier to inspect than searches. Published computational attempts provide context, but do not imply that a new construction is likely.

**Model or capability conditions:** A tool-using assistant able to inspect mathematical sources and preserve exact computations; no named model or configuration evaluated.

**Uncertainty:** No project research attempt or model evaluation has been performed. Published attempts do not establish a success probability for this task.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The source specifies an explicit identity and term count. |
| Decomposability | High | Coefficient generation and independent identity checking can be separated. |
| Methods and literature | High | Explicit baseline schemes and exact checking formats are available. |
| Search / symbolic fit | High | Tensor identities support symbolic and computational work. |
| Checkability | High | A finite exact coefficient certificate can establish a construction. |
| Expertise needed | High | Tensor symmetries, coefficient fields and numerical recovery require expertise. |
| Scholarly significance | Medium | A recognized record; explanatory value and speed depend on the construction. |
| Verification difficulty | Medium | Checking is localized but requires sound field arithmetic and statement alignment. |

**Correctness:** Not assessed.

No new decomposition supplied.

**Novelty:** Not assessed.

No new result claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The target persists despite recent computational searches.

**Evidence type:** Maintained problem listing and public negative attempt; no project measurement..

**Significance:** Medium.

A concrete algebraic-complexity record; insight and practical benefit must be demonstrated.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-20 | Recorded the exact characteristic-zero target, baseline sources and recent negative attempt. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-511` |
| Duplicate key | `algebraic-complexity:4x4-matrix-multiplication:exact-rank-le47:characteristic-zero` |
| Original domain label | Circuit and algebraic complexity |
| Original cross-domain labels | Algebra |
| Primary domain ID | `CS.COMPLEX.CIRCUIT` |
| Cross-domain IDs | `MATH.ALG` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `exact_computation`, `symbolic_derivation`, `finite_search` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-511.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
