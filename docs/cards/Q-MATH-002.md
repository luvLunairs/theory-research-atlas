# Audit exact union-closed-family certificates on at most four elements

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Build a small, complete catalog of set families that are closed under union, with a simple witness showing that some element occurs in at least half their sets.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-002%3A+Audit+exact+union-closed-family+certificates+on+at+most+four+elements&target=Q-MATH-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-002%3A+Audit+exact+union-closed-family+certificates+on+at+most+four+elements&target=Q-MATH-002)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Curator-proposed task](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Curator-proposed, pending peer assessment: enumerate every family F subseteq P({1,2,3,4}) with F nonempty, union(F) nonempty, and A union B in F for all A,B in F; for each eligible F record an element x in union(F) such that 2*|{A in F:x in A}| &gt;= |F|. Deliver a completeness argument and an independently implemented verifier. Unused ground elements are allowed; repeated sets are not.

**Required output:** A complete, reproducible certificate catalog and independent checker for the specified finite class, including an exact census keyed by family size and active-universe size.

**Scope:** Curator-proposed benchmark and certificate design, pending peer assessment. Only the at-most-four-element case is covered; its mathematical conclusion is already known.

### Assumptions

- Universe U={1,2,3,4}; all smaller-universe families are included by allowing unused elements.
- F is a family of distinct subsets, not a multiset.
- F is nonempty and union(F) is nonempty, excluding both the empty family and {empty set}.
- For every A,B in F, A union B belongs to F; F may or may not contain the empty set.

### Success criteria

1. Specify a bijection between 16-bit masks and all families of subsets of U.
2. For each eligible union-closed family, supply a witness element meeting the integer inequality in the statement.
3. Document excluded degenerate families and include cases with and without the empty set.
4. Provide a completeness argument independent of the result of the main generator.
5. An independent checker and a human reviewer must agree on definitions, counts, and witnesses; no numbers should be entered as measured before execution.

### Background needed

- Power sets and finite set families
- Closure under union
- Binary encodings and integer counting
- Basic reproducibility and independent-checker design

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Estimated ordinary CPU and small memory. There are exactly 2^16=65,536 input family masks before filtering; this size justifies a conservative laptop-scale planning assumption but is not a timing measurement.

**Data:** No empirical or private data. Generated finite families and witnesses become the future artifact.

**Experiments:** None; purely finite mathematics.

**Theory and model requirements:** Finite set theory and exact integer arithmetic. Isomorphism reductions, if added, require an explicit proof and must not replace the baseline completeness check.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Human reviews the domain exclusions and map from masks to families.
2. Independently reconstruct closure and witness frequency from serialized subsets, avoiding generator helpers.
3. Compare full enumeration and any symmetry-reduced implementation on the bounded universe.
4. Check census reconciliation: every input mask is classified once, with exclusion reasons.
5. Match the verified finite statement to the source's broader known-result context; record it as reproduction.

**Statement alignment:** Closure is under pairwise union; unused elements are allowed; the witness must lie in union(F); frequency is at least one half, not a strict inequality.

**Human review difficulty:** Low to moderate; independent software and exhaustive-coverage reasoning need careful review.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made.

### Methods and obstacles

**Proposed methods:**

- Finite search
- Construction
- Exact computation
- Classification
- Proof of enumeration completeness

**Expected obstacles:**

- Mistaking the number of sets for the number of ground elements.
- Empty-family and empty-set edge cases.
- Two checkers sharing the same flawed helper or representation assumption.
- Using a small-universe result to imply progress on the general conjecture.

### Checks still needed

- Review existing public enumeration resources before attributing infrastructure novelty.
- Choose certificate schema and independent verifier implementations.
- Counts by family size and active-universe size remain unmeasured.
- The general union-closed conjecture's present status is outside this card's verification scope.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The four-element mathematical property is a special case of the source's reported twelve-element theorem. The certificate/benchmark packaging is a curator proposal; no claim of mathematical novelty or project execution.

**Exact problem / theorem locator:** Introduction for definitions; section 5 Theorem 17 for the already-known finite-case context.

### Sources

- [The journey of the union-closed sets conjecture](../sources.md#src-math-002). Henning Bruhn; Oliver Schaudt. 2013. [Read source](https://arxiv.org/pdf/1309.3297).
  - **Relevant sections:** arXiv:1309.3297v2; introduction, section 5 Theorem 17, and reference [68]
  - **Source limitations:** Historical snapshot; its general open-status and quantitative bounds are not current certification. The underlying twelve-element proof was not independently audited.

### Known results and partial progress

- The finite conclusion is covered by the survey's Theorem 17 for at most twelve elements. No improvement of that theorem is proposed.
- The survey records several equivalent and restricted formulations; this task deliberately fixes the basic set-family formulation.

**Research value:** The catalog can expose empty-set, quantifier, and encoding mistakes before future work on harder set-system problems. It is research infrastructure with low mathematical novelty.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The specified mathematical assertion is a known special case, so it is not labeled open. The proposed certificate artifact remains unbuilt.

**Search limits:** No exhaustive check of existing four-element catalogs; no claim about present general-conjecture status.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [The journey of the union-closed sets conjecture](../sources.md#src-math-002)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The source survey documents stronger finite cases. No project attempt, certificate census, or AI outcome exists.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Peter Frankl (general conjecture, as attributed in the literature)
- Henning Bruhn
- Oliver Schaudt (consulted survey)
- M. Živković
- B. Vučković (finite theorem credited by the survey)

**Suggested citation:** Bruhn and Schaudt, The journey of the union-closed sets conjecture, arXiv:1309.3297v2 (2013), introduction and Theorem 17. Cite the underlying finite-case paper separately only after inspecting it. The bounded artifact task is curator-proposed.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

The task has fully bounded enumeration, a local exact witness, and cheap independent verification. Its purpose is to test careful formalization and tooling, not to suggest the general conjecture is easy.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with exact bitset programming and basic combinatorics.

**Uncertainty:** No implementation was run. Independent novelty of this packaging is not asserted; existing enumerations may already provide equivalent data.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | All degeneracies, allowed elements, and witness conditions are specified. |
| Decomposability | High | Generator, closure filter, witness finder, census, and checker separate cleanly. |
| Methods and literature | High | Basic bitset operations suffice; a published survey provides context. |
| Search / symbolic fit | High | Every object fits in a small exact bit representation. |
| Checkability | High | Witnesses are integer counts; completeness follows from a fixed finite encoding. |
| Expertise needed | Low | Basic combinatorics and careful programming are sufficient for this bounded task. |
| Scholarly significance | Low | No mathematical novelty; moderate infrastructure value. |
| Verification difficulty | Low | Most difficulty is proving coverage and avoiding correlated implementation errors. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Low.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-002` |
| Duplicate key | `math:union-closed:ground-set<=4:certificate-benchmark` |
| Original domain label | Combinatorics |
| Original cross-domain labels | Order theory; Theoretical computer science |
| Primary domain ID | `MATH.COMB.EXT` |
| Cross-domain IDs | `CS.ALG` |
| Origin code | `curator_proposed` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `finite_search`, `construction`, `exact_computation`, `classification`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-002.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
