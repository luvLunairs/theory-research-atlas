# The exact ten-point Heilbronn number in the unit square

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-203 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-203%3A+The+exact+ten-point+Heilbronn+number+in+the+unit+square&target=Q-MATH-203) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-203%3A+The+exact+ten-point+Heilbronn+number+in+the+unit+square&target=Q-MATH-203)

For P=(p_1,...,p_10) in ([0,1]^2)^10, let a(P)=min_(i<j<k) |det(p_j-p_i,p_k-p_i)|/2 and H_10=max_P a(P). Determine H_10 by an exact or rigorously certified attaining configuration and a matching upper bound over the full square configuration space.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-17.

**Status basis:** Both inspected preprints leave unrestricted n=10 optimality unresolved; the 2026 paper supplies an exact incumbent. A scoped search through 2026-10-14 found no authoritative matching global bound. Inspection of Sudermann-Merx v2 on 2026-10-17 confirmed that n=10 certification remains a stated open direction and clarified the numerical precision of the reported optimization certificates. Solver-tolerance discrepancies in the 2025 paper are retained as unresolved numerical evidence.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-MATH-204: 2025; SRC-MATH-205 and SRC-REVIEW-901: 2026. The scoped status search ended on 2026-10-14; the 2026-10-17 check inspected version 2 and its numerical-certification limits, without repeating a comprehensive literature search.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Independently check the published n=10 algebraic witness before using it as a numerical baseline.
- Identify and check a rigorous unrestricted upper bound before using one in a proof; distinguish numerical solver bounds from exact optimality and account for the precision qualification in Sudermann-Merx v2, Section 4.1.
- Check newer exact constructions and unrestricted bounds before a novelty claim.
- Reconcile solver-objective and recomputed-area discrepancies rather than treating them as distinct certified records.

**Primary branch:** [Geometry](../domains/math.md#math-geom). **Related branches:** [Optimization and operations research](../domains/math.md#math-opt), [Numerical analysis and scientific computation](../domains/math.md#math-numer).

**Sources:** [Solving the Heilbronn Triangle Problem using Global Optimization Methods](../sources.md#src-math-204); [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-math-205); [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-review-901).

**Exact locator:** Monji et al. v1, Table 5 and Section 5; Sudermann-Merx v1, Section 7 and Appendix A, Table 11; v2, Sections 4.1, 5.6 and 7, and Appendix A, Table 11.

**Potential difficulty:** High. The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Possible AI role:** No named model evaluated; assumes tool-using AI with nonconvex optimization, symbolic algebra, rational reconstruction and exact or interval checking. Priority applies to the capped construction search and exact certificate workflow. The twenty-variable formulation and 120-triangle checker make a limited experiment reviewable; the full global optimum remains difficult.

**Verification burden:** Medium. A lower-bound witness is compact; global completeness and numerical tolerances are difficult.

**Resource expectations:** Experiment: None. Data: The exact reference points are in SRC-MATH-205, Appendix A, Table 11, n=10 column. No empirical dataset is needed. Computation: Proposed search cap: 4 CPU-hours, 8 GiB RAM and 100 starts. A candidate has twenty real coordinates and 120 triangle constraints. Exact witness checking is small compared with unrestricted global optimization; no cost or runtime has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model or optimization trial has been evaluated. The incumbent has survived substantial prior work, so the chance of improving it in the proposed cap is unknown and may be very small.

[Read the full card](../cards/Q-MATH-203.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-17

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Open after scoped check → Open after scoped check.

The indexed ten-point target is unchanged. The problem card now qualifies the numerical optimality evidence and requires separate justification for any rigorous upper bound.

**Search scope:** Compared the ten-point statement and related nine-point evidence with Sudermann-Merx version 2. This supplements the scoped search through 2026-10-14; no comprehensive status search was repeated.

**Inspected evidence**

- [From Computational Certification to Exact Coordinates: Heilbronn's Triangle Problem on the Unit Square Using Mixed-Integer Optimization](../sources.md#src-review-901) — Sections 4.1, 5.6 and 7; Appendix A, Table 11. Version 2 distinguishes numerical global optimization certificates, subject to solver precision, from exact coordinate recovery. It still leaves unrestricted ten-point optimality unresolved. The algebraic nine-point construction is not adopted as a rigorously certified upper bound for the ten-point problem.

**Limits and remaining work**

- No optimization run or certificate was independently replayed.
- Selected passages were inspected; this check does not establish an exhaustive current literature status or reject the possibility of a rigorous upper bound from another source.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
