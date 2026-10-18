# Exact finite satisfiability for a small monadic fragment

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-101 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-101%3A+Exact+finite+satisfiability+for+a+small+monadic+fragment&target=Q-MATH-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-101%3A+Exact+finite+satisfiability+for+a+small+monadic+fragment&target=Q-MATH-101)

For a closed, equality-free first-order formula with k <= 3 unary predicates, no functions or constants, at most 40 syntax-tree nodes and quantifier nesting at most 4, decide satisfiability over nonempty finite domains. Reproduce the predicate-type reduction to nonempty subsets of {0,1}^k, then return a satisfying model or an exhaustive rejection certificate. The size limits are curator-defined calibration conditions.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The source proves decidability for a broader unary-predicate fragment. The bounded certificate task is an editorial specialization of that known result.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MATH-101: 2021. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Select a public, versioned formula corpus or document a small new corpus before any evaluation.
- Confirm availability and compatibility of the source's formal artifact before choosing it as a dependency.

**Primary branch:** [Model theory](../domains/logic.md#logic-model). **Related branches:** [Computability and degree theory](../domains/logic.md#logic-recur), [Type theory and formal verification](../domains/logic.md#logic-type).

**Sources:** [Trakhtenbrot's Theorem in Coq: Finite Model Theory through the Constructive Lens](../sources.md#src-math-101).

**Exact locator:** SRC-MATH-101, Section 5.1, Lemmas 36 and 38 (printed p. 17); Section 2.4 and Definition 14 fix the logical setting.

**Potential difficulty:** Medium. Semantic induction and a small exact evaluator are required, with no unknown theorem targeted.

**Possible AI role:** No named model evaluated; assumes tool-using AI with first-order logic, exact enumeration and optional proof-assistant support. The type space is small, the semantic reduction is documented, and certificates can be checked independently. The useful challenge is preserving the statement through its encoding, not discovering an unknown theorem.

**Verification burden:** Medium. A faulty translation of quantifiers or accidental equality support can invalidate an otherwise exhaustive search.

**Resource expectations:** Experiment: None; the objects and semantics are mathematical. Data: Formula inputs and generated certificates only; no empirical or proprietary data. Computation: At k=3 there are 8 predicate types and 255 nonempty subsets. Evaluating a formula also branches over quantified assignments. These are combinatorial sizes, not measured time or memory; exhaustive formula generation is out of scope.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model performance has been measured. Familiar textbook content may be recalled rather than independently derived; such success would not establish research ability.

[Read the full card](../cards/Q-MATH-101.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
