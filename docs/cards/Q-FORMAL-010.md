# Deterministic polynomial-time identity testing for general arithmetic circuits

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A compact algebraic expression may expand into too many terms to list. Can one always decide, efficiently and without randomness, whether all terms cancel?

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-010%3A+Deterministic+polynomial-time+identity+testing+for+general+arithmetic+circuits&target=Q-FORMAL-010) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-010%3A+Deterministic+polynomial-time+identity+testing+for+general+arithmetic+circuits&target=Q-FORMAL-010)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg), [Algebra](../domains/math.md#math-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Not yet assessed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Does a uniform deterministic Turing machine decide whether a division-free arithmetic circuit over Q computes the zero polynomial in time poly(s,n,d,L), where s counts gates and wires, n counts commuting variables, L is the total binary encoding length of the rational constants, and d bounds the circuit formal degree? Require d to be bounded by a fixed polynomial in the full input encoding length. The target is polynomial bit complexity; a count of unit-cost rational operations is insufficient.

**Required output:** An unconditional deterministic identity test with polynomial bit complexity for the stated inputs, or a clearly identified partial result for a literature-supported restricted circuit class.

**Scope:** Commutative arithmetic circuits over Q of polynomially bounded formal degree, in the binary Turing model. No depth, read-count or multilinearity restriction is imposed. The unbounded-formal-degree problem and black-box interfaces are separate variants.

### Assumptions

- The input explicitly encodes a finite directed acyclic circuit with addition and multiplication gates, commuting variables, and rational constants written as signed binary numerators and positive binary denominators. Division gates are excluded.
- Let s be the number of gates plus wires, n the number of variables, and L the sum of the binary lengths of all rational-constant encodings. The complete input length N also includes graph connectivity, gate labels and variable indices.
- Assign formal degree 1 to every leaf, including constant leaves; take the maximum at addition gates and the sum at multiplication gates. The promised bound d is at most a fixed polynomial in N. This is a syntactic bound, not merely the degree of the final polynomial after cancellation.
- Running time means deterministic Turing-machine bit operations, including exact-number handling and construction of any evaluation points. Huge integers are not unit-cost objects.
- White-box access exposes the encoded circuit. A black-box extension must separately specify its evaluation interface, size and degree bounds, query encodings and all bit costs.
- The target is uniform and unconditional, with no randomness, nonuniform advice or unproved hardness assumption.

### Success criteria

1. Give a complete algorithm and prove correctness for every permitted input, including zero and constant circuits.
2. Prove uniform construction and a polynomial bit-time bound, including every subroutine and exact-number operation; do not hide an identity-testing oracle or exponential-length evaluation point.
3. If a restriction is imposed, identify it in the theorem and compare it against current results for exactly that class.

### Background needed

- Arithmetic circuits, formal degree, rational encodings and Turing-machine bit complexity
- Derandomization, hitting sets and algebraic complexity
- The structural hypotheses of the chosen restricted circuit model

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Symbolic examples and implementations can support preparation, but no resource estimate is established for discovering or validating a general algorithm. Explicit expansion and exhaustive enumeration can be exponential.

**Data:** Primary literature and exact circuit descriptions. No empirical dataset is required.

**Experiments:** None.

**Theory and model requirements:** Binary-encoded rationals, commuting variables and the stated polynomial formal-degree promise. Any additional assumption, oracle or nonuniform advice must be disclosed.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Match the field, rational encoding, formal-degree convention, circuit representation, access model and uniform bit-time requirement against the exact theorem.
2. Audit every reduction and subroutine for correctness and bit complexity; include query lengths, intermediate-number sizes and preservation of the promised formal degree.
3. Use independently constructed exact instances to detect defects, while retaining the universal proof obligation.
4. For a hitting set, prove both deterministic construction and that every nonzero member of the class is hit; a list that works on a benchmark is insufficient.

**Statement alignment:** Known restricted-model algorithms, randomized tests, finite benchmark agreement, unit-cost huge-integer evaluations and noncommutative matrix substitutions do not by themselves meet this bit-complexity target.

**Human review difficulty:** Specialist review is required for the structural argument and the uniform complexity bound.

### Formal validity and empirical support

**What the formal task can establish:** A theorem must hold for all circuits satisfying the exact input promises in the declared computational model.

**Empirical support and limits:** Implementation experiments concern performance and defect detection; they do not establish general derandomization.

### Methods and obstacles

**Proposed methods:**

- Published hitting-set and generator constructions
- Source-based structural analysis of restricted circuits
- Exact symbolic examples and algorithm verification

**Expected obstacles:**

- Cancellations can conceal a nonzero polynomial from an inadequate evaluation set.
- A reduction can increase size, degree, depth or read count beyond the permitted class.
- A short arithmetic algorithm can have unaccounted bit complexity or require a hidden randomized subroutine.

### Checks still needed

- Any selected restricted class needs a focused current-status check before an attempt.
- The separate read-five, non-multilinear, unrestricted-depth white-box specialization was not located as an explicitly stated open question in the inspected sources. Its precise current status remains pending.
- The source proofs and their algorithmic complexity have not received independent project review.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The 2026 bounded-read paper identifies general deterministic PIT as open. The cited complexity references specify the formal-degree and bit-encoding conventions used here. Later restricted-model improvements were inspected; no resolution of this polynomial-formal-degree, commutative bit-complexity target was located in the scoped search.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-010.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** SRC-FORMAL-007 introduction and section 5; SRC-IMPACT-011 introduction, theorems 1.1-1.2 and definitions 2.1-2.2; SRC-IMPACT-012 corollary 2.7; SRC-IMPACT-013 introduction and theorem 1. SRC-IMPACT-014 definitions 2.2.1 and 2.2.6, theorem 2.2.8 and section 2.6; SRC-IMPACT-015 section 1.1.

### Sources

- [Progress on Polynomial Identity Testing — II](../sources.md#src-formal-007). Nitin Saxena. 2014. [Read source](https://arxiv.org/html/1401.0976v1).
  - **Relevant sections:** Introduction; Section 5, Open ends
  - **Source limitations:** Old survey: restricted-model status is particularly time-sensitive; no present-day completeness claim.
- [Polynomial Identity Testing for Read-4 Arithmetic Formulas](../sources.md#src-impact-011). Nimrod Kaplan; Amir Shpilka. 2026. [Read source](https://eccc.weizmann.ac.il/report/2026/076/download/).
  - **Relevant sections:** Full version, introduction, theorems 1.1-1.2 and definitions 2.1-2.2; conference version: CCC 2026, article 25, DOI 10.4230/LIPIcs.CCC.2026.25.
  - **Source limitations:** Source claims were inspected, not independently proved. The paper does not state a separate read-five conjecture.
- [A Note on Deterministic PIT for Sigma^\[3\] Pi Sigma Pi^\[delta\] Circuits](../sources.md#src-impact-012). Zeyu Guo. 2026. [Read source](https://eccc.weizmann.ac.il/report/2026/168/download).
  - **Relevant sections:** Manuscript dated 5 September 2026; ECCC release 6 September 2026; introduction and corollary 2.7.
  - **Source limitations:** The algebraic-model result has at most three top summands and constant bottom degree. It is not a general-circuit solution; no proof audit was performed.
- [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](../sources.md#src-impact-013). Marek Černý; Tim Seppelt. 2026. [Read source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.25).
  - **Relevant sections:** STACS 2026, article 25, published 25 February 2026; linked full HTML, introduction and theorem 1.
  - **Source limitations:** Used for significance and scope, not as a complete current survey or a proof audited by this project.
- [Independence in Algebraic Complexity Theory](../sources.md#src-impact-014). Johannes Mittmann. 2013. [Read source](https://d-nb.info/1045872121/34).
  - **Relevant sections:** Chapter 2: definitions 2.2.1 and 2.2.6, theorem 2.2.8, conjecture 2.6.1 and theorem 2.6.3; computational model in appendix A.2.
  - **Source limitations:** Foundational computational conventions; not evidence of present-day completeness or an independent audit of the thesis proofs.
- [Near-Optimal Bootstrapping of Hitting Sets for Algebraic Models](../sources.md#src-impact-015). Mrinal Kumar; Ramprasad Saptharishi; Anamay Tengse. 2023. [Read source](https://theoryofcomputing.org/articles/v019a012/v019a012.pdf).
  - **Relevant sections:** Theory of Computing 19(12), 1-30; published 31 December 2023; section 1.1 and footnotes 2-3.
  - **Source limitations:** Used for problem formulation; bootstrapping proofs were not independently checked and the paper is not a 2026 status survey.

### Known results and partial progress

- Random evaluation supplies a one-sided-error identity test; derandomization and explicit hitting sets remain central goals (SRC-FORMAL-007).
- Kaplan and Shpilka give polynomial-time white-box and quasipolynomial-time black-box PIT for non-multilinear read-four formulas, in characteristic zero or at least five. A read counts a variable occurrence at a leaf, not its final degree. No constant-depth assumption is imposed (SRC-IMPACT-011).
- Guo's September 2026 note removes squarefreeness for depth-four circuits with at most three product summands and constant bottom degree, in the stated algebraic model over arbitrary fields (SRC-IMPACT-012).
- Černý and Seppelt give logspace interreductions between PIT, multiplicity tree automata equivalence and a specified bounded-treewidth graph problem (SRC-IMPACT-013).
- A large-integer Kronecker substitution reduces rational PIT to exact circuit evaluation; its compact arithmetic description does not make its binary evaluation inexpensive (SRC-IMPACT-014, theorem 2.6.3).

**Research value:** PIT is a central derandomization problem linked to circuit lower bounds. Its reductions also connect algebraic identity testing with automata equivalence and graph algorithms; a restricted result needs its own significance assessment.

### Related problems

- **Related to:** [Unconditional polynomial-time derandomization: BPP versus P](../candidates.md#q-formal-301). Both concern removing randomness. The general BPP question is broader; this entry fixes an algebraic decision problem.
- **Related to:** [Valiant's VP versus VNP over the rational numbers](../candidates.md#q-formal-306). PIT and arithmetic circuit lower bounds are linked by hardness-versus-randomness results; no unconditional equivalence between these two entries is asserted.

### Scope of the status check

**Finding:** Source-reported open status retained for general commutative PIT. Recent restricted results were recorded without extending their scope.

**Search limits:** Targeted web and primary-source checks are not an exhaustive literature review. No independent proof verification or complete read-five status review was performed.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "read-5" "identity testing" 2026
- "read-five" "polynomial"
- "Polynomial Identity Testing for Read-4"
- "polynomial identity testing" "2026" deterministic general solution
- "polynomial identity testing" "October" "2026"

**Sources checked:**

- [Progress on Polynomial Identity Testing — II](../sources.md#src-formal-007)
- [Polynomial Identity Testing for Read-4 Arithmetic Formulas](../sources.md#src-impact-011)
- [A Note on Deterministic PIT for Sigma^\[3\] Pi Sigma Pi^\[delta\] Circuits](../sources.md#src-impact-012)
- [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](../sources.md#src-impact-013)
- [Independence in Algebraic Complexity Theory](../sources.md#src-impact-014)
- [Near-Optimal Bootstrapping of Hitting Sets for Algebraic Models](../sources.md#src-impact-015)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited papers provide public algorithms and reductions. No project solving attempt or implementation run is recorded for this entry.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Nitin Saxena (survey)
- Nimrod Kaplan
- Amir Shpilka
- Zeyu Guo
- Marek Černý
- Tim Seppelt
- Johannes Mittmann (complexity-model reference)
- Mrinal Kumar
- Ramprasad Saptharishi
- Anamay Tengse

**Suggested citation:** For the general problem, cite Saxena, Progress on Polynomial Identity Testing - II (2014), and the earlier work it surveys. For the bounded-read frontier, cite Kaplan and Shpilka, CCC 2026, article 25, DOI 10.4230/LIPIcs.CCC.2026.25. Other results should be credited to their individual sources; these authors are not collectively the originators of PIT. For computational conventions, cite Mittmann, Independence in Algebraic Complexity Theory (2013), chapter 2, and Kumar, Saptharishi and Tengse, Near-Optimal Bootstrapping of Hitting Sets for Algebraic Models, Theory of Computing 19(12) (2023), section 1.1.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Not yet assessed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

The card records the literature and verification conditions. No task-specific model evaluation or evidence of tractability is available.

**Model or capability conditions:** Not assessed for any named model or configuration.

**Uncertainty:** No research model has been benchmarked on this entry; success probability and cost are unknown.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | Unknown | The broad target is specified, but an attempted restricted theorem needs its own exact input class. |
| Decomposability | Unknown | No decomposition for a new algorithm has been assessed. |
| Methods and literature | Unknown | Published structural methods are available; their suitability for a new target has not been evaluated. |
| Search / symbolic fit | Unknown | Small exact examples can check conjectured steps; no search method has been selected. |
| Checkability | Unknown | A future algorithm needs a universal proof and cost analysis, beyond examples. |
| Expertise needed | Unknown | The amount of expert assistance has not been measured; algebraic-complexity review is required. |
| Scholarly significance | Unknown | The general question has established significance; a prospective partial contribution has not been assessed. |
| Verification difficulty | Unknown | No candidate algorithm or proof is available to scope the review. |

**Correctness:** Not assessed.

No new algorithm or proof is submitted.

**Novelty:** Not assessed.

No new result is claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Unknown.

The sources identify a major open problem; no narrower target has received a task-specific difficulty assessment.

**Evidence type:** Source descriptions and absence of a selected algorithm; no project measurement..

**Significance:** High.

The sources link general PIT to circuit lower bounds and specific automata and graph problems.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-20 | Specified polynomial bit complexity, rational input encoding and formal degree; recorded restricted-model results with their exact scope. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-010` |
| Duplicate key | `deterministic-polynomial-time-identity-testing-for-general-arithmetic-circuits` |
| Original domain label | Algebraic complexity |
| Original cross-domain labels | Algorithms; Symbolic computation |
| Primary domain ID | `CS.COMPLEX.CIRCUIT` |
| Cross-domain IDs | `CS.ALG`, `MATH.ALG` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `unassessed` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `algorithm`, `construction`, `symbolic_derivation` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-010.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
