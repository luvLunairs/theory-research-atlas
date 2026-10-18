# The exact ten-point Heilbronn number in the unit square

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Arrange ten points in a unit square so that the smallest of their 120 triangles is as large as possible. A better arrangement has a short exact certificate; proving that no better arrangement exists is much harder.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-203%3A+The+exact+ten-point+Heilbronn+number+in+the+unit+square&target=Q-MATH-203) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-203%3A+The+exact+ten-point+Heilbronn+number+in+the+unit+square&target=Q-MATH-203)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Geometry](../domains/math.md#math-geom) |
| Related fields | [Optimization and operations research](../domains/math.md#math-opt), [Numerical analysis and scientific computation](../domains/math.md#math-numer) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-17 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For P=(p_1,...,p_10) in ([0,1]^2)^10, let a(P)=min_(i&lt;j&lt;k) |det(p_j-p_i,p_k-p_i)|/2 and H_10=max_P a(P). Determine H_10 by an exact or rigorously certified attaining configuration and a matching upper bound over the full square configuration space.

**Required output:** Determine H_10. Curator-proposed first milestone: search the full twenty-coordinate space for a configuration whose rigorously verified minimum area exceeds L=(5/8)z^2-(1/2)z^3, where z=3/4-(63+8*sqrt(62))^(1/3)/12-1/(12*(63+8*sqrt(62))^(1/3)) and positive real roots are used.

**Scope:** Unrestricted ten-point optimization. The proposed first milestone seeks a certified improvement over a published exact configuration; it does not assume the current configuration is optimal.

### Assumptions

- Points lie in the closed Euclidean unit square, with no lattice, symmetry or prescribed boundary positions.
- Every triple contributes its unsigned area, including zero for collinear or coincident points.
- Numerical optimization is only a search method; certified lower bounds require exact arithmetic or rigorous intervals.

### Success criteria

1. A lower-bound improvement supplies ten exact rational or algebraic points in the square and a proof that all 120 triangle areas exceed L.
2. Cap the proposed exploratory search at 100 starting configurations, 4 CPU-hours and 8 GiB RAM; stop at the first cap reached. These limits define a manageable experiment, not a predicted requirement.
3. Refine promising floating-point outputs to exact coordinates or rigorous intervals. A solver-reported objective by itself is not a certified bound.
4. An exact solution also requires a matching upper bound for all configurations, with every reduction justified. A restricted-family optimum or local optimality certificate must retain that restricted label.

### Background needed

- Determinant area formulas
- Nonconvex max-min optimization
- Rational and real-algebraic arithmetic
- Interval certification and the difference between local and global optima

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Proposed search cap: 4 CPU-hours, 8 GiB RAM and 100 starts. A candidate has twenty real coordinates and 120 triangle constraints. Exact witness checking is small compared with unrestricted global optimization; no cost or runtime has been measured.

**Data:** The exact reference points are in SRC-MATH-205, Appendix A, Table 11, n=10 column. No empirical dataset is needed.

**Experiments:** None.

**Theory and model requirements:** Ordinary Euclidean geometry and exact or outward-rounded arithmetic. Boundary patterns and determinant-sign patterns are not assumed universally.

**Validation modes:** Exact computation, Proof, Numerical evidence.

### Verification steps

1. Retrieve the reference n=10 column and verify the interpretation of its algebraic parameters.
2. Check all candidate coordinates belong to the square, using exact arithmetic or outward-rounded intervals.
3. Independently enumerate all 120 unsigned determinant areas.
4. Certify a strict comparison with L; do not compare rounded decimal displays.
5. For an upper bound, review the full domain cover, every pruning inequality and every claimed symmetry reduction.

**Statement alignment:** The full target allows arbitrary real coordinates. A rational grid, a chosen boundary pattern or a finite set of starts is only a search restriction and cannot support universal nonexistence.

**Human review difficulty:** Moderate for an exact lower-bound witness; high for a global proof. Optimization certificates require scrutiny of tolerances and omitted regions.

### Formal validity and empirical support

**What the formal task can establish:** Only a checked finite witness or a proof covering the declared space establishes the mathematical claim.

**Empirical support and limits:** No physical model, empirical data or experiment is needed.

### Methods and obstacles

**Proposed methods:**

- Max-min numerical optimization without compulsory boundary occupancy
- Rational or algebraic reconstruction
- Exact determinant enumeration
- Interval branch-and-bound for explicitly bounded regions

**Expected obstacles:**

- Rounded coordinates can destroy an apparent improvement.
- Solver feasibility tolerances can exceed the claimed improvement.
- Fixing eight boundary points without proof restricts the global problem.
- A local maximum does not provide an unrestricted upper bound.
- Literature record claims may lag newer constructions.

### Checks still needed

- Independently check the published n=10 algebraic witness before using it as a numerical baseline.
- Identify and check a rigorous unrestricted upper bound before using one in a proof; distinguish numerical solver bounds from exact optimality and account for the precision qualification in Sudermann-Merx v2, Section 4.1.
- Check newer exact constructions and unrestricted bounds before a novelty claim.
- Reconcile solver-objective and recomputed-area discrepancies rather than treating them as distinct certified records.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Both inspected preprints leave unrestricted n=10 optimality unresolved; the 2026 paper supplies an exact incumbent. A scoped search through 2026-10-14 found no authoritative matching global bound. Inspection of Sudermann-Merx v2 on 2026-10-17 confirmed that n=10 certification remains a stated open direction and clarified the numerical precision of the reported optimization certificates. Solver-tolerance discrepancies in the 2025 paper are retained as unresolved numerical evidence.

[Dated literature checks and remaining limits](../candidates/Q-MATH-203.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Monji et al. v1, Table 5 and Section 5; Sudermann-Merx v1, Section 7 and Appendix A, Table 11; v2, Sections 4.1, 5.6 and 7, and Appendix A, Table 11.

### Sources

- [Solving the Heilbronn Triangle Problem using Global Optimization Methods](../sources.md#src-math-204). Amirhossein Monji; Amirali Modir; Burak Kocuk. 2025. [Read source](https://arxiv.org/html/2512.14505v1).
  - **Relevant sections:** Section 3.2.3, Conjecture 1; Section 4.3, Table 5 and its footnote; Section 5.
  - **Source limitations:** Solver objective values and recomputed triangle areas differ in Table 5. Restricted models and floating-point tolerances must not be turned into exact unrestricted bounds.
- [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-math-205). Nathan Sudermann-Merx. 2026. [Read source](https://arxiv.org/html/2603.11107v1).
  - **Relevant sections:** Sections 2.1, 3.5, 5.5, 6.1 and 7; Appendix A, Table 11, n=10 column.
  - **Source limitations:** Preprint claims and computational certificates have not received project-level mathematical review. Only the n=10 coordinates and identified research questions are used; other appendix record claims have not been audited.
- [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-review-901). Nathan Sudermann-Merx. 2026. [Read source](https://arxiv.org/html/2603.11107v2).
  - **Relevant sections:** arXiv:2603.11107v2; Sections 4.1, 5.6 and 7; Appendix A, Table 11.
  - **Source limitations:** Selected passages inspected. Optimization runs and certificates were not independently replayed. The reported nine-point algebraic value is not adopted as a rigorously certified upper bound for the ten-point problem.

### Known results and partial progress

- Appendix A, Table 11 of the 2026 preprint reproduces Comellas-Yebra coordinates and the exact lower bound L above; global optimality is explicitly unproved.
- Sudermann-Merx gives an exact nine-point configuration with minimum triangle area -11/64+9*sqrt(65)/320 and reports numerical global optimization. Version 2, Section 4.1, qualifies the optimization certificate by solver precision. Although H_10 &lt;= H_9, the algebraic value is not adopted here as a rigorously certified upper bound for H_10: exact coordinate recovery does not by itself prove global optimality. Any upper bound used in a future argument needs its own checked justification.
- The 2025 paper's n=10 model uses unproved restrictions. Its Table 5 distinguishes solver objective 0.0465383 from recomputed minimum area 0.0465369; this card does not adopt the larger floating-point value as an exact bound.

**Research value:** A certified improved arrangement would strengthen a classical finite geometric bound. A rigorous global upper bound would settle an unresolved exact case; negative local searches alone do neither.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The scoped search through 2026-10-14 found no authoritative resolution of unrestricted n=10 optimality. The 2026-10-17 version check inspected Sudermann-Merx v2, whose Section 7 still identifies n=10 certification as an open direction; Section 4.1 limits the reported optimization certificates to numerical precision. This version check does not replace or extend the earlier search into an exhaustive status review.

**Search limits:** The 2026-10-17 check concerns the cited version and relevant passages, not an independent audit of optimization certificates or a complete survey of later and unpublished records. The strongest rigorously justified unrestricted upper bound remains to be checked.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Solving the Heilbronn Triangle Problem using Global Optimization Methods](../sources.md#src-math-204)
- [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-math-205)
- [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-review-901)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The 2002 Comellas-Yebra arrangement is reproduced with attribution in the 2026 preprint. The 2025 and 2026 papers discuss computational formulations; their reported computations are not project or model evaluations.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- F. Comellas
- J. L. A. Yebra
- Amirhossein Monji
- Amirali Modir
- Burak Kocuk
- Nathan Sudermann-Merx

**Suggested citation:** Sudermann-Merx (2026), arXiv:2603.11107v1, Appendix A, Table 11 and Sections 3.5 and 7; v2, Sections 4.1, 5.6 and 7 and Appendix A, Table 11. Monji, Modir and Kocuk (2025), arXiv:2512.14505v1, Table 5. Credit for the exact construction follows their reference to Comellas and Yebra (2002); that original paper was not directly inspected.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Priority applies to the capped construction search and exact certificate workflow. The twenty-variable formulation and 120-triangle checker make a limited experiment reviewable; the full global optimum remains difficult.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with nonconvex optimization, symbolic algebra, rational reconstruction and exact or interval checking.

**Uncertainty:** No model or optimization trial has been evaluated. The incumbent has survived substantial prior work, so the chance of improving it in the proposed cap is unknown and may be very small.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The square, objective and exact comparison value are specified. |
| Decomposability | High | Search, exact coordinate recovery and certification can be reviewed separately. |
| Methods and literature | High | Recent primary papers provide explicit formulations and algebraic configurations. |
| Search / symbolic fit | High | Numerical search and symbolic area comparisons are directly applicable. |
| Checkability | High | A proposed exact configuration has only 120 triangle inequalities. |
| Expertise needed | Medium | Lower-bound checking is accessible; rigorous global optimization requires specialist review. |
| Scholarly significance | Medium | A strict improvement strengthens a recognized finite bound. |
| Verification difficulty | Medium | A lower-bound witness is compact; global completeness and numerical tolerances are difficult. |

**Correctness:** No project answer.

No project candidate solution has been submitted or independently reviewed.

**Novelty:** Requires future literature review.

A future certified improvement must be compared with updated exact records; an alternative representation of the existing configuration is not a new bound.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

A verified improvement would resolve a finite case or tighten a recognized extremal bound.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-17 | Added Sudermann-Merx v2 and corrected the distinction between an exact nine-point construction and a numerical global optimality certificate. The algebraic nine-point value is not adopted as a certified upper bound for H_10. The ten-point target and open-status category are unchanged. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-203` |
| Duplicate key | `the-exact-ten-point-heilbronn-number-in-the-unit-square` |
| Original domain label | Discrete geometry |
| Original cross-domain labels | Global optimization; Numerical analysis |
| Primary domain ID | `MATH.GEOM` |
| Cross-domain IDs | `MATH.OPT`, `MATH.NUMER` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `bounds`, `numerical_computation`, `symbolic_derivation`, `exact_computation` |
| Validation tags | `exact_computation`, `pure_proof`, `numerical_evidence` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-203.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
