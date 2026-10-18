# Exact finite satisfiability for a small monadic fragment

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Decide whether a small formula about unary properties can hold in a finite structure, and make every positive or negative answer independently checkable.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-101%3A+Exact+finite+satisfiability+for+a+small+monadic+fragment&target=Q-MATH-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-101%3A+Exact+finite+satisfiability+for+a+small+monadic+fragment&target=Q-MATH-101)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Model theory](../domains/logic.md#logic-model) |
| Related fields | [Computability and degree theory](../domains/logic.md#logic-recur), [Type theory and formal verification](../domains/logic.md#logic-type) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For a closed, equality-free first-order formula with k &lt;= 3 unary predicates, no functions or constants, at most 40 syntax-tree nodes and quantifier nesting at most 4, decide satisfiability over nonempty finite domains. Reproduce the predicate-type reduction to nonempty subsets of {0,1}^k, then return a satisfying model or an exhaustive rejection certificate. The size limits are curator-defined calibration conditions.

**Required output:** Produce a syntax checker, a predicate-type completeness argument, an exact finite-model evaluator, and independently checkable output certificates.

**Scope:** A reproducible calibration for each input in the stated fragment, with a proof of the decision procedure. This does not address general finite satisfiability, nor monadic logic with equality.

### Assumptions

- Classical first-order semantics with a nonempty finite domain.
- Only atoms P_i(x), Boolean connectives and first-order quantifiers are admitted; equality, constants, function symbols and predicates of other arities are excluded.
- The input is a closed formula; k &lt;= 3 counts distinct predicate symbols. Syntax-tree size counts every atom, connective and quantifier once.
- The 40-node and nesting-depth-4 limits are curator-defined bounds for individual inputs; exhaustive enumeration of all formulas is not required.

### Success criteria

1. Reject inputs outside the stated grammar and limits.
2. Justify by structural induction that collapsing elements with the same predicate truth vector preserves the truth of every allowed formula.
3. For satisfiable input, provide a nonempty type-domain and its predicate interpretation; for unsatisfiable input, account for every nonempty subset of the type space.
4. Use an independent checker or separately reviewed implementation to evaluate the output certificate; state any proof-assistant axioms if formalization is used.

### Background needed

- First-order syntax, binding and environments
- Induction on formulas
- Finite truth tables and exact enumeration

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** At k=3 there are 8 predicate types and 255 nonempty subsets. Evaluating a formula also branches over quantified assignments. These are combinatorial sizes, not measured time or memory; exhaustive formula generation is out of scope.

**Data:** Formula inputs and generated certificates only; no empirical or proprietary data.

**Experiments:** None; the objects and semantics are mathematical.

**Theory and model requirements:** Classical nonempty-domain semantics for an equality-free relational fragment. Any formal proof must connect its binder representation and evaluation function to these semantics.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Review the formal grammar and its nonempty-domain convention against the cited source.
2. Check preservation of satisfaction under the type projection, including both quantifiers.
3. Re-evaluate each reported witness or rejection certificate from the original formula.
4. If a proof assistant is used, inspect the exact theorem statement and trusted dependencies.

**Statement alignment:** The source uses a more general constructive setting; this task restricts it to a fixed classical equality-free fragment. No claim is made for equality, constants or arbitrary first-order signatures.

**Human review difficulty:** Moderate: the model enumeration is small, but the semantic proof and binder encoding need an experienced reader.

### Formal validity and empirical support

**What the formal task can establish:** A successful answer must prove the type reduction and validate each certificate under the stated grammar.

**Empirical support and limits:** No claim about an empirical system is involved.

### Methods and obstacles

**Proposed methods:**

- Structural induction on formulas
- Canonical predicate-type domains
- Exact evaluation and exhaustive certificates
- Optional proof-assistant formalization

**Expected obstacles:**

- Including equality breaks the proposed one-representative-per-type argument.
- Variable capture or an incorrect empty-domain convention can silently change satisfiability.
- Exhaustive rejection is only meaningful after the small-model reduction is proved.

### Checks still needed

- Select a public, versioned formula corpus or document a small new corpus before any evaluation.
- Confirm availability and compatibility of the source's formal artifact before choosing it as a dependency.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The source proves decidability for a broader unary-predicate fragment. The bounded certificate task is an editorial specialization of that known result.

**Exact problem / theorem locator:** SRC-MATH-101, Section 5.1, Lemmas 36 and 38 (printed p. 17); Section 2.4 and Definition 14 fix the logical setting.

### Sources

- [Trakhtenbrot's Theorem in Coq: Finite Model Theory through the Constructive Lens](../sources.md#src-math-101). Dominik Kirst; Dominique Larchey-Wendling. 2021. [Read source](https://arxiv.org/pdf/2104.14445v1).
  - **Relevant sections:** Pinned arXiv version 1; Section 2.4 and Definition 14 for syntax and finite satisfiability; Section 5.1, Lemmas 36 and 38, printed p. 17.
  - **Source limitations:** The cited locator belongs to the 2021 preprint, not a later journal layout. The calibration omits equality, constants and functions; its formula-size limits are editorial choices.

### Known results and partial progress

- Kirst and Larchey-Wendling, Lemma 38, reduce the relevant finite satisfiability problem to Boolean predicate types; Lemma 36 supplies decidability on a fixed finite domain.

**Research value:** A controlled way to assess whether an assistant preserves quantifier scope and model assumptions while producing evidence for both satisfiable and unsatisfiable cases. Its research value is preparatory.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The finite-fragment result is explicitly proved in the inspected source. The card is a calibration task.

**Search limits:** The check concerns the cited statement and local scope, not all implementations or later formal-library developments.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Trakhtenbrot's Theorem in Coq: Finite Model Theory through the Constructive Lens](../sources.md#src-math-101)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited paper reports a Coq development of finite-model-theoretic results. Its artifact has not been rerun for this task.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Dominik Kirst
- Dominique Larchey-Wendling

**Suggested citation:** Kirst and Larchey-Wendling (2021), Trakhtenbrot's Theorem in Coq: Finite Model Theory through the Constructive Lens, arXiv:2104.14445v1, Lemmas 36 and 38. The bounded task protocol is an editorial specialization.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The type space is small, the semantic reduction is documented, and certificates can be checked independently. The useful challenge is preserving the statement through its encoding, not discovering an unknown theorem.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with first-order logic, exact enumeration and optional proof-assistant support.

**Uncertainty:** No model performance has been measured. Familiar textbook content may be recalled rather than independently derived; such success would not establish research ability.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The grammar, size limits and output obligations are explicit. |
| Decomposability | High | Parsing, semantic reduction, evaluator and certificate checker can be reviewed separately. |
| Methods and literature | High | The inspected paper provides the finite-type decision argument. |
| Search / symbolic fit | High | The remaining model space is finite and exactly representable. |
| Checkability | High | Positive models and complete finite rejections can be checked without trusting the proposing model. |
| Expertise needed | Medium | Binding and semantic invariance require logical care despite the small domains. |
| Scholarly significance | Low | This reproduces a known fragment result; value lies in reliable preparation. |
| Verification difficulty | Medium | A faulty translation of quantifiers or accidental equality support can invalidate an otherwise exhaustive search. |

**Correctness:** No project answer.

No candidate answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

The mathematical result is established; the bounded reproduction protocol is not a claim of a new theorem.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

Semantic induction and a small exact evaluator are required, with no unknown theorem targeted.

**Evidence type:** Editorial estimate not measured.

**Significance:** Low.

Useful as a test of dependable logical translation and certificates.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-101` |
| Duplicate key | `exact-finite-satisfiability-for-a-small-monadic-fragment` |
| Original domain label | Finite model theory |
| Original cross-domain labels | Computability; Proof assistants |
| Primary domain ID | `LOGIC.MODEL` |
| Cross-domain IDs | `LOGIC.RECUR`, `LOGIC.TYPE` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `model_construction`, `finite_search`, `exact_computation`, `certificate_checking`, `formalization` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-101.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
