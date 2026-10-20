# A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-511 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-511%3A+A+rank-47+decomposition+for+4x4+matrix+multiplication+in+characteristic+zero&target=Q-FORMAL-511) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-511%3A+A+rank-47+decomposition+for+4x4+matrix+multiplication+in+characteristic+zero&target=Q-FORMAL-511)

Find r<=47 and linear forms L_s,R_s on complex 4x4 matrices, with coefficient matrices P_s, such that AB=sum_{s=1}^r L_s(A)R_s(B)P_s for every pair A,B. Supply exact coefficients and verify the identity. A rational construction is a stronger coefficient restriction; a characteristic-two or border-rank construction does not meet this target.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** The maintained problem page calls the target unsolved, the institutional catalog lists rank 48, and the October 2026 campaign reports no rank-47 construction. No matching resolution was found in a focused search; this does not establish a lower bound.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Primary sources and maintained records inspected on 2026-10-20; publication and revision dates are recorded in the source entries.

**Scope limits:** The fixed-size exact tensor problem. It does not ask for the general matrix-multiplication exponent or a claim of hardware speedup.

**Information still needed**

- Independent verification of any imported baseline coefficient files.
- A fresh literature and catalog check before claiming a new record.
- Exact recovery and field validation for any future numerical candidate.

**Primary branch:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit). **Related branches:** [Algebra](../domains/math.md#math-alg).

**Sources:** [The Rank of the 4x4 Matrix-Multiplication Tensor](../sources.md#src-impact-006); [A non-commutative algorithm for multiplying 4x4 matrices using 48 non-complex multiplications](../sources.md#src-impact-007); [Cloudroom Math: new matrix multiplication algorithms found by AI agents](../sources.md#src-impact-008); [Description of fast matrix multiplication algorithm: 4 x 4 x 4](../sources.md#src-impact-010).

**Exact locator:** SRC-IMPACT-006 mathematical specification; SRC-IMPACT-007 sections 4-6; SRC-IMPACT-008 Results; SRC-IMPACT-010 Commentaries.

**Potential difficulty:** High. The target persists despite recent computational searches.

**Possible AI role:** Exact certificates make results easier to inspect than searches. Published computational attempts provide context, but do not imply that a new construction is likely. No named model evaluated.

**Verification burden:** Medium. Moderate for a compact exact construction; much higher for an impossibility claim or a complicated coefficient field.

**Resource expectations:** A fixed candidate has a finite exact checker; search cost is unconstrained and may be substantial. Coefficient growth can also make checking expensive. No project runtime or budget is measured.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** No project research attempt or model evaluation has been performed. Published attempts do not establish a success probability for this task.

[Read the full card](../cards/Q-FORMAL-511.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The maintained listing and catalog retain the 47-term gap; the October attempt explicitly reports no solution.

**Search scope:** Primary passages, current metadata and linked maintained records, followed by targeted later-result searches through 2026-10-20.

**Inspected evidence**

- [The Rank of the 4x4 Matrix-Multiplication Tensor](../sources.md#src-impact-006) — About the problem and mathematical specification. Explicit open target: an exact decomposition with at most 47 terms over the complex numbers.
- [A non-commutative algorithm for multiplying 4x4 matrices using 48 non-complex multiplications](../sources.md#src-impact-007) — Version 7, 2026-07-27; abstract, sections 4-6 and appendix A. A rational 48-term construction and its relationship to the complex construction and characteristic-two result.
- [Cloudroom Math: new matrix multiplication algorithms found by AI agents](../sources.md#src-impact-008) — README: Results, Scope and honesty; release dated 2026-10-08. The campaign reports no rank-47 construction for 4x4 matrices over Q or C.
- [Description of fast matrix multiplication algorithm: 4 x 4 x 4](../sources.md#src-impact-010) — Algorithm description and Commentaries. The institutional catalog lists a rational rank-48 scheme and downloadable encodings.

**Limits and remaining work**

- Focused search only. Neither coefficient files nor claimed obstructions were independently checked.

<details>
<summary>Search queries</summary>

- "4x4" "rank" "47" "2026" matrix multiplication
- "matrix multiplication" "rank 47" rational 2026
- "4" "matrix multiplication" "47" "October 2026"
- "2506.13242" "2026" rank 47


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
