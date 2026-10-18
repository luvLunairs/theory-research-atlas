# A triangle-free 40-vertex graph with independence number at most nine

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

One 40-vertex graph could decide which of two remaining values is R(3,10). Checking such a graph is easier than proving that every graph fails.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-202%3A+A+triangle-free+40-vertex+graph+with+independence+number+at+most+nine&target=Q-MATH-202) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-202%3A+A+triangle-free+40-vertex+graph+with+independence+number+at+most+nine&target=Q-MATH-202)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Does a finite simple undirected graph G on exactly 40 vertices exist with no triangle and no independent set of ten vertices? A positive witness proves R(3,10)=41; a complete impossibility proof proves R(3,10)=40, using the established interval 40 &lt;= R(3,10) &lt;= 41.

**Required output:** Construct a triangle-free 40-vertex graph with independence number at most nine. Proposed milestone: select at most 20 attributed 39-vertex source graphs, add one vertex with free adjacency, and permit at most four edge toggles among the original vertices.

**Scope:** The remaining existence question for R(3,10). The proposed first milestone is a curator-selected neighborhood search, without a claim that those neighborhoods are themselves unsolved.

### Assumptions

- The graph is simple, undirected and has exactly 40 vertices.
- An independent set contains no graph edge; it is a clique in the complement.
- No degree pattern, automorphism or source seed is assumed in the unrestricted statement.

### Success criteria

1. Supply a complete graph serialization passing independent triangle and independent-ten-set checks.
2. Identify the seeds before searching; count edge changes on unordered pairs among the original 39 vertices only.
3. Cap the proposed trial at 8 CPU-hours and 16 GiB RAM. Retain witnesses, checked certificates and unresolved cases; these caps are planning choices, not measured performance.
4. UNSAT within selected seed neighborhoods is only a restricted result. Universal nonexistence requires an exhaustive decomposition covering all 40-vertex graphs.

### Background needed

- Ramsey graphs
- Exact clique and independent-set algorithms
- SAT certificates
- Reproducible seed selection

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Proposed cap: 8 CPU-hours and 16 GiB RAM, at most 20 seeds. There are 780 possible edges. Triangle checking is small; excluding independent ten-sets needs exact branch-and-bound or a checked SAT certificate. No runtime guarantee is made.

**Data:** Attributed 39-vertex graph files from the author collection or paper records; validate and identify every selected seed.

**Experiments:** None.

**Theory and model requirements:** Finite graph theory and the cited 40-to-41 interval. Every seed or edit restriction belongs only to the proposed trial.

**Validation modes:** Exact computation, Proof, Public data.

### Verification steps

1. Parse the witness independently and check order, symmetry and zero diagonal.
2. Enumerate triangles independently.
3. Use exact complement clique search or a separately checked UNSAT certificate to exclude a ten-clique.
4. Check the graph directly, not just the searcher's clauses.
5. Report restricted negative results with their seed list and edit radius.

**Statement alignment:** A 40-vertex witness plus the established upper bound gives 41. A failed restricted search gives no exact Ramsey value.

**Human review difficulty:** Moderate for a graph with independent code and certificates; very high for universal nonexistence.

### Formal validity and empirical support

**What the formal task can establish:** Only a checked finite witness or a proof covering the declared space establishes the mathematical claim.

**Empirical support and limits:** No physical model, empirical data or experiment is needed.

### Methods and obstacles

**Proposed methods:**

- Seed extension with a declared edge-edit budget
- SAT with forbidden-subset constraints
- Lazy forbidden-subset cuts
- Exact clique search in the complement

**Expected obstacles:**

- Selected seeds cover only a small part of the known population.
- An independent-set routine that stops early cannot certify the bound.
- Unsound symmetry breaking can remove valid graphs.
- Unverified historical web claims are not evidence of an exact value.

### Checks still needed

- Identify and validate seed files before a trial.
- Check whether selected neighborhoods have already been exhausted.
- Refresh the survey and primary result before an exact-value claim.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The 2024 theorem and the survey dated 2026-04-24 leave exactly two values. A scoped search for a later resolution found none in authoritative sources as of 2026-10-14.

**Exact problem / theorem locator:** DS1 revision 18, Table Ia and Section 2.1(d); Angeltveit, Theorem 1.1 and Section 7.

### Sources

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001). Stanisław P. Radziszowski. 2026. [Read source](https://www.cs.rit.edu/~spr/ElJC/sur.pdf).
  - **Relevant sections:** Revision 18, 24 April 2026; sections 2.1 and 6.1.1, Tables Ia and Ib; selected two-color and four-color bounds.
  - **Source limitations:** Living URL may change; record revision before each reuse. Selected entries were inspected, not every cited computation. For R(4,6), read Table Ib together with Table Ia rather than treating the earlier table as current on its own.
- [R(3,10) &lt;= 41](../sources.md#src-math-202). Vigleik Angeltveit. 2024. [Read source](https://arxiv.org/html/2401.00392v2).
  - **Relevant sections:** Abstract; Theorem 1.1; Section 7, partial census of (3,10)-graphs on 39 vertices; arXiv v2.
  - **Source limitations:** The proof uses substantial computational work. Reading the paper does not reproduce its enumeration or certify every auxiliary file; current status is cross-checked against the 2026 dynamic survey.
- [Ramsey Numbers](../sources.md#src-math-206). Geoffrey Exoo. Year not verified. [Read source](https://cs.indstate.edu/ge/RAMSEY/).
  - **Relevant sections:** Two Color Ramsey Colorings table, links for R(3,10), R(3,11) and R(4,6); page update note 2024-04-09.
  - **Source limitations:** The displayed page is not a current upper-bound survey. Seeds require independent validation and a stable local copy before use.

### Known results and partial progress

- Angeltveit's theorem, retained by the 2026 survey, leaves R(3,10) in {40,41}.
- The survey describes a very large partial collection at order 39; a small selected seed set is not exhaustive.
- Survey Section 2.1(i) excludes a lower-bound improvement from a circulant graph at this order.

**Research value:** A positive witness determines an exact Ramsey number. A failed neighborhood search has narrower value and needs a novelty check before being called progress.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The primary result and April 2026 survey leave two values; the scoped October resolution check found no authoritative update.

**Search limits:** Unpublished searches and every subsequent preprint have not been audited. Seed-neighborhood novelty is unverified.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001)
- [R(3,10) &lt;= 41](../sources.md#src-math-202)
- [Ramsey Numbers](../sources.md#src-math-206)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Angeltveit's Section 7 contains a partial order-39 census; Exoo's portal links a lower-bound graph. Neither is evidence about an AI system's measured ability.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Vigleik Angeltveit
- Geoffrey Exoo
- Stanisław P. Radziszowski

**Suggested citation:** Angeltveit (2024), R(3,10) &lt;= 41, arXiv:2401.00392v2, Theorem 1.1 and Section 7; Radziszowski (2026), Small Ramsey Numbers, revision 18, Section 2.1; Exoo, Ramsey Numbers.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

There is a decisive compact witness, but existing extensive searches make an arbitrary small neighborhood uncertain. Validate the checker and justify seed selection first.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with graph algorithms, exact SAT formulations and certificate handling.

**Uncertainty:** No model or proposed neighborhood has been tested. Published computations support the relevance of search, not the likelihood of success under this cap.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Fixed order and two forbidden substructures specify the task. |
| Decomposability | High | Seed validation, encoding, search and certification separate. |
| Methods and literature | High | The primary paper and survey describe gluing, enumeration and constructions. |
| Search / symbolic fit | High | Adjacency variables admit exact finite constraints. |
| Checkability | Medium | The graph is small, but ruling out independent ten-sets requires exact computation. |
| Expertise needed | High | Useful restrictions require Ramsey and exhaustive-search expertise. |
| Scholarly significance | High | A witness settles the remaining two-valued exact-number question. |
| Verification difficulty | Medium | Positive verification is bounded; global nonexistence is much harder. |

**Correctness:** No project answer.

No project candidate solution has been submitted or independently reviewed.

**Novelty:** Requires future literature review.

Future results must be checked against live sources and existing computational records.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

A positive witness resolves R(3,10), using the established upper bound.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-202` |
| Duplicate key | `a-triangle-free-40-vertex-graph-with-independence-number-at-most-nine` |
| Original domain label | Ramsey theory |
| Original cross-domain labels | Algorithms |
| Primary domain ID | `MATH.COMB.EXT` |
| Cross-domain IDs | `CS.ALG` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `bounds`, `finite_search`, `certificate_checking` |
| Validation tags | `exact_computation`, `pure_proof`, `public_data` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-202.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
