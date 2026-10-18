# Reproduce Huang's hypercube degree theorem

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

More than half of a Boolean cube forces a vertex with many selected neighbors. A published short proof makes this useful for checking whether a research workflow can preserve a theorem's quantifiers and produce a reviewable proof.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-001%3A+Reproduce+Huang%27s+hypercube+degree+theorem&target=Q-FORMAL-001) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-001%3A+Reproduce+Huang%27s+hypercube+degree+theorem&target=Q-FORMAL-001)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Computational complexity](../domains/cs.md#cs-complex) |
| Related fields | [Combinatorics and discrete mathematics](../domains/math.md#math-comb), [Type theory and formal verification](../domains/logic.md#logic-type) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Reconstruct a proof that every induced subgraph on 2^(n-1)+1 vertices of the n-dimensional hypercube has maximum degree at least sqrt(n), for every integer n &gt;= 1.

**Required output:** A self-contained proof document with a dependency ledger; optionally a machine-checked formalization with the same statement.

**Scope:** Known-theorem reproduction. First reconstruct the mathematical argument for all n. A formal proof-assistant version is optional and requires a separate environment choice; small numerical checks alone do not complete this task.

### Assumptions

- n is an integer at least 1.
- The graph is the undirected n-dimensional binary hypercube with edges at Hamming distance one.
- The selected graph is induced and has exactly 2^(n-1)+1 vertices.
- Classical real linear algebra, including eigenvalue interlacing, is allowed.

### Success criteria

1. A specialist accepts the proof with all lemmas and quantifiers explicit.
2. The induced-subgraph condition and vertex threshold agree with Theorem 1.1.
3. Any formal artifact declares axioms and dependencies and is checked by an independent trusted kernel.
4. The result is labeled reproduction throughout.

### Background needed

- Graphs and hypercubes
- Real symmetric matrices
- Eigenvalues and principal-submatrix interlacing
- Inductive block-matrix construction

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Symbolic proof first. Optional small matrices grow as 2^n by 2^n; never materialize large cubes merely because no experiment is needed. Formalization cost unknown; no run or time estimate exists.

**Data:** The cited paper and mathematical definitions only; no empirical dataset.

**Experiments:** none

**Theory and model requirements:** Finite simple graphs and classical real linear algebra. Formal foundations and allowed axioms must be recorded if formalized.

**Validation modes:** Proof.

### Verification steps

1. Freeze the reference version and restate all definitions.
2. Review each lemma independently, especially matrix dimensions and signs.
3. Check the final statement against Theorem 1.1 rather than the paper's historical conjecture wording.
4. If formalized, record proof-assistant/library versions and inspect the theorem and axioms after kernel checking.

**Statement alignment:** A proof about non-induced subgraphs, another vertex threshold, or finite tested dimensions is not this task.

**Human review difficulty:** Moderate; a reviewer needs spectral graph theory or linear algebra. Automated acceptance alone does not validate the source-to-formal-statement translation.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made.

### Methods and obstacles

**Proposed methods:**

- proof reconstruction
- symbolic derivation
- formal verification

**Expected obstacles:**

- An attractive but wrong eigenvalue-index argument can look convincing.
- Checking a few values of n cannot establish a universal theorem.
- A formalization can prove a weakened statement if the translation is not audited.

### Checks still needed

- Whether an existing formalization can be reused should be searched before a later attempt.
- Choose a proof assistant only if formalization is in scope; no toolchain has been selected.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Huang's proof is explicit; the 2012 open-list entry is superseded. Reproduction is calibration, not a new solution.

**Exact problem / theorem locator:** SRC-FORMAL-002, Theorem 1.1 and Section 2

### Sources

- [Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture](../sources.md#src-formal-002). Hao Huang. 2019. [Read source](https://arxiv.org/html/1907.00847v2).
  - **Relevant sections:** Theorems 1.1, 1.4, 1.5; Section 2, Lemmas 2.1–2.3
  - **Source limitations:** The published proof was inspected, not independently re-proved or formally verified.
- [Open Problems in Analysis of Boolean Functions](../sources.md#src-formal-005). Ryan O'Donnell (compiler); Simons Symposium participants. 2012. [Read source](https://arxiv.org/html/1204.6447v1).
  - **Relevant sections:** Named entries: Fourier Entropy–Influence; Mansour; Tomaszewski; Sensitivity versus Block Sensitivity
  - **Source limitations:** Historical collection, not a live open-status register. Several entries are now resolved; only individually extracted questions are indexed.

### Known results and partial progress

- Huang's Theorem 1.1 proves this statement; Theorems 1.4–1.5 connect it to sensitivity.
- The 2012 problem-list entry is historical evidence, not an open problem to solve again.

**Research value:** A compact cross-domain calibration for proof reconstruction, citation accuracy and statement alignment. Its scientific novelty is zero unless a separately reviewed extension is proposed.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** Original statement and explicit proof inspected. The candidate is a known result, so no current-open claim is made.

**Search limits:** No formal-library census or erratum search across all indexes.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture](../sources.md#src-formal-002)
- [Open Problems in Analysis of Boolean Functions](../sources.md#src-formal-005)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Huang 2019 provides the known solution. No project attempt has been made; no specific AI reproduction is claimed.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Hao Huang
- Nisan and Szegedy (original sensitivity problem)
- Chung, Füredi, Graham and Seymour (earlier cube work)

**Suggested citation:** Hao Huang (2019), Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture, arXiv:1907.00847v2, Theorem 1.1.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

Useful first calibration because the target and reference proof are explicit and errors can be localized to linear-algebra lemmas. This predicts auditability, not research discovery or model success.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with source retrieval, symbolic reasoning and optional access to a proof assistant.

**Uncertainty:** No model has been tested. Familiarity with the published proof may contaminate any discovery-style benchmark; this is intentionally a reproduction benchmark.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The graph, threshold and desired bound are fixed. |
| Decomposability | High | Separate signed-matrix construction, spectrum, interlacing and degree bound. |
| Methods and literature | High | An accessible primary proof supplies a reference. |
| Search / symbolic fit | Medium | Symbolic block-matrix reasoning is useful; brute-force graph search is unnecessary. |
| Checkability | High | A human can compare a short derivation to the reference theorem. |
| Expertise needed | Medium | Linear algebra and graph-theoretic proof review are needed. |
| Scholarly significance | Medium | High workflow-calibration value; no new theorem is sought. |
| Verification difficulty | Medium | Submatrix dimensions and eigenvalue ordering are subtle despite a short statement. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-001` |
| Duplicate key | `reproduce-huang-s-hypercube-degree-theorem` |
| Original domain label | Computational complexity |
| Original cross-domain labels | Discrete mathematics; Formal verification |
| Primary domain ID | `CS.COMPLEX` |
| Cross-domain IDs | `MATH.COMB`, `LOGIC.TYPE` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `symbolic_derivation`, `formalization` |
| Validation tags | `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-001.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
