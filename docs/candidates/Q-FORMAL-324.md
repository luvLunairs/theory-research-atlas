# Martin's conjecture, part 1, under determinacy

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-324 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-324%3A+Martin%27s+conjecture%2C+part+1%2C+under+determinacy&target=Q-FORMAL-324) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-324%3A+Martin%27s+conjecture%2C+part+1%2C+under+determinacy&target=Q-FORMAL-324)

In ZF+AD+DC_R, is every Turing-invariant f:2^ω→2^ω either constant in Turing degree on a cone or above the identity on a cone? A cone has the form {x:x≥_T a}.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The expert-maintained problem page labels the unrestricted Turing-invariant dichotomy open. Yu's October 2026 preprint still assumes order preservation. The indexed ZF+AD+DC_R assumptions follow Lutz-Siskind; the directory's stronger DC convention does not replace them.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Lutz-Siskind v3: 5 April 2024; living directory inspected 6 November 2026; Yu v1: 10 October 2026.

**Scope limits:** Compared the unrestricted invariant target with monotone special cases and checked foundational assumptions. The Borel ZFC version is a related formulation, not an unrestricted ZFC assertion.

**Information still needed**

- Independent assessment of the October 2026 preprint.
- Any proposed extension must justify removing order preservation without silently strengthening the axioms.

**Primary branch:** [Computability and degree theory](../domains/logic.md#logic-recur). **Related branches:** [Set theory and independence](../domains/logic.md#logic-set).

**Sources:** [Part 1 of Martin's Conjecture for order-preserving and measure-preserving functions](../sources.md#src-formal-315); [Computable learning of natural hypothesis classes](../sources.md#src-formal-316); [Martin's Conjecture — Open Problems in Mathematical Logic](../sources.md#src-math-807); [Order-preserving maps of the Turing degrees: regularity and consistency strength](../sources.md#src-math-808).

**Exact locator:** Lutz-Siskind v3, Sections 1.1 and 1.4; Open Problems in Mathematical Logic, Problem 2; Yu, Theorem 1.2 and Remark 1.3

**Potential difficulty:** Frontier. The unrestricted invariant case lacks the monotonicity used by the established results.

**Possible AI role:** Audit where a known proof uses order preservation and formalize a candidate weakening of that hypothesis.

**Verification burden:** High. Keep determinacy and dependent-choice assumptions explicit; the unrestricted assertion is not a ZFC theorem.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Add a current expert entry and a recent special-case reference while preserving the exact foundation and unresolved general scope.

**Search scope:** Compared the unrestricted invariant target with monotone special cases and checked foundational assumptions. The Borel ZFC version is a related formulation, not an unrestricted ZFC assertion.

**Inspected evidence**

- [Part 1 of Martin's Conjecture for order-preserving and measure-preserving functions](../sources.md#src-formal-315) — Sections 1.1 and 1.4. States the DC_R formulation and distinguishes stronger uniformization principles.
- [Martin's Conjecture — Open Problems in Mathematical Logic](../sources.md#src-math-807) — Problem 2, statement and status. Retains the unrestricted conjecture and distinguishes the Borel variant.
- [Order-preserving maps of the Turing degrees: regularity and consistency strength](../sources.md#src-math-808) — Theorem 1.2; Remark 1.3. The later result retains the order-preserving hypothesis.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "Martin's conjecture" 2026
- "Martin's conjecture" "2026" Turing solved


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
