# Deterministic polynomial-time identity testing for general arithmetic circuits

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-010 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-010%3A+Deterministic+polynomial-time+identity+testing+for+general+arithmetic+circuits&target=Q-FORMAL-010) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-010%3A+Deterministic+polynomial-time+identity+testing+for+general+arithmetic+circuits&target=Q-FORMAL-010)

Does a uniform deterministic Turing machine decide whether a division-free arithmetic circuit over Q computes the zero polynomial in time poly(s,n,d,L), where s counts gates and wires, n counts commuting variables, L is the total binary encoding length of the rational constants, and d bounds the circuit formal degree? Require d to be bounded by a fixed polynomial in the full input encoding length. The target is polynomial bit complexity; a count of unit-cost rational operations is insufficient.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** The 2026 bounded-read paper identifies general deterministic PIT as open. The cited complexity references specify the formal-degree and bit-encoding conventions used here. Later restricted-model improvements were inspected; no resolution of this polynomial-formal-degree, commutative bit-complexity target was located in the scoped search.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Survey from 2014; 2026 conference papers and the September 2026 depth-four note inspected on 20 October 2026. Computational conventions checked against the 2013 thesis and the 2023 Theory of Computing paper.

**Scope limits:** The canonical entry now specifies binary-encoded rational circuits of polynomial formal degree and polynomial bit complexity. Restricted results retain their own models; read-five status is not asserted.

**Information still needed**

- A focused current-status check for any chosen restricted class, including the suggested read-five specialization.
- Independent review of source proofs and any later proposed algorithm.

**Primary branch:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg), [Algebra](../domains/math.md#math-alg).

**Sources:** [Progress on Polynomial Identity Testing — II](../sources.md#src-formal-007); [Polynomial Identity Testing for Read-4 Arithmetic Formulas](../sources.md#src-impact-011); [A Note on Deterministic PIT for Sigma^[3] Pi Sigma Pi^[delta] Circuits](../sources.md#src-impact-012); [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](../sources.md#src-impact-013); [Independence in Algebraic Complexity Theory](../sources.md#src-impact-014); [Near-Optimal Bootstrapping of Hitting Sets for Algebraic Models](../sources.md#src-impact-015).

**Exact locator:** SRC-FORMAL-007 introduction and section 5; SRC-IMPACT-011 introduction, theorems 1.1-1.2 and definitions 2.1-2.2; SRC-IMPACT-012 corollary 2.7; SRC-IMPACT-013 introduction and theorem 1. SRC-IMPACT-014 definitions 2.2.1 and 2.2.6, theorem 2.2.8 and section 2.6; SRC-IMPACT-015 section 1.1.

**Potential difficulty:** Unknown. The general problem is a major open derandomization question. No narrower target has received a task-specific difficulty assessment.

**Possible AI role:** No model-specific assessment has been made. Assistance can be disclosed for literature inspection, exact examples and review of a selected algorithm.

**Verification burden:** High. A universal correctness proof and uniform bit-complexity bound need specialist review, including rational encodings and formal-degree promises; examples alone are insufficient.

**Resource expectations:** No project runtime or cost estimate is available. Symbolic expansion and exhaustive circuit enumeration may be exponential.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** No research model or prospective restricted theorem has been evaluated.

[Read the full card](../cards/Q-FORMAL-010.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

Retain the canonical ID and source-reported open status, with a precise polynomial bit-time target and formal-degree promise. Unit-cost large-rational operations are not an equivalent formulation. No standalone source-stated read-five question was established.

**Search scope:** General commutative deterministic PIT, 2026 bounded-read results and later restricted-model developments; source statements and hypotheses checked.

<details>
<summary>Previous indexed wording</summary>

For arithmetic circuits over a specified characteristic-zero field with a polynomial degree bound, obtain deterministic polynomial-time identity testing in a stated arithmetic or bit-cost model; separate white-box access from black-box access.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Progress on Polynomial Identity Testing — II](../sources.md#src-formal-007) — Introduction and section 5. General PIT and hitting-set derandomization supply the established parent question.
- [Polynomial Identity Testing for Read-4 Arithmetic Formulas](../sources.md#src-impact-011) — Introduction; theorems 1.1-1.2; definitions 2.1-2.2. The read-four case has algorithms; its assumptions must not be silently dropped.
- [A Note on Deterministic PIT for Sigma^[3] Pi Sigma Pi^[delta] Circuits](../sources.md#src-impact-012) — Corollary 2.7. The September note concerns a restricted depth-four class, not unrestricted circuits.
- [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](../sources.md#src-impact-013) — Introduction and theorem 1. A current application establishes precise reductions involving PIT.
- [Independence in Algebraic Complexity Theory](../sources.md#src-impact-014) — Definitions 2.2.1 and 2.2.6; theorem 2.2.8; theorem 2.6.3, printed pages 12-18 and 32-33. Formal degree and rational encoding control the computational model; a huge-integer evaluation reduction does not supply polynomial bit complexity.
- [Near-Optimal Bootstrapping of Hitting Sets for Algebraic Models](../sources.md#src-impact-015) — Section 1.1, printed page 3 and footnotes 2-3. The standard degree-bounded PIT setup uses formal degree and accounts for the binary output length of explicit hitting sets.

**Limits and remaining work**

- No proof audit or independent algorithm run.
- The search was scoped and may miss subsequent results.
- A narrower research target needs its own status check.

<details>
<summary>Search queries</summary>

- "read-5" "identity testing" 2026
- "read-five" "polynomial"
- "Polynomial Identity Testing for Read-4"
- "polynomial identity testing" "2026" deterministic general solution
- "polynomial identity testing" "October" "2026"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
