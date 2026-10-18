# Improve the lower bound for R(4,6) with a 36-vertex graph

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Find a graph on 36 vertices in which neither four vertices are all joined nor six vertices are all mutually unjoined. Its complete correctness check involves fewer than two million small subsets.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-204%3A+Improve+the+lower+bound+for+R%284%2C6%29+with+a+36-vertex+graph&target=Q-MATH-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-204%3A+Improve+the+lower+bound+for+R%284%2C6%29+with+a+36-vertex+graph&target=Q-MATH-204)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Does there exist a finite simple undirected graph on exactly 36 vertices having neither a clique of four vertices nor an independent set of six vertices? A witness proves R(4,6) &gt;= 37; ruling out all such graphs would prove R(4,6)=36.

**Required output:** Construct a 36-vertex (4,6)-graph. Curator-proposed milestone: use Exoo's 37 listed 35-vertex graphs, add one freely adjacent vertex, and allow at most four changes to edges among the original vertices.

**Scope:** A one-vertex improvement of the constructive bound for R(4,6). The proposed first milestone uses public 35-vertex graphs as seeds; the novelty of that restricted search is not established.

### Assumptions

- The graph is simple, undirected and has exactly 36 vertices.
- A K_4 means all six edges among four vertices are present; an independent six-set means all fifteen edges among six vertices are absent.
- An optional edit neighborhood is not assumed to contain every possible solution.

### Success criteria

1. Supply a complete 36-vertex adjacency record with no K_4 and no independent six-set, checked by an independent program.
2. Identify and validate the 37 seeds; define the edit budget on unordered pairs among the original 35 vertices.
3. Cap the proposed search at 8 CPU-hours and 16 GiB RAM. These are resource limits for an experiment, not an estimate of the cost of resolving the problem.
4. Preserve checked witnesses and restricted UNSAT certificates. A timeout or a failed neighborhood search does not imply R(4,6)=36.

### Background needed

- Ramsey graph definitions
- Exact finite graph checking
- SAT or constraint optimization
- Reproducible graph files

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Proposed cap: 8 CPU-hours and 16 GiB RAM for all seeds together. The witness has 630 possible edges; independent brute-force verification examines C(36,4)=58,905 four-sets and C(36,6)=1,947,792 six-sets. Search and global nonexistence can be far more expensive.

**Data:** The 37 attributed graph files linked by SRC-MATH-203. Their source and content identifiers should accompany any extension result.

**Experiments:** None.

**Theory and model requirements:** Ordinary finite graph theory. The seed list and four-edge radius define a curator-proposed restricted experiment only.

**Validation modes:** Exact computation, Proof, Public data.

### Verification steps

1. Independently parse and validate the 36-vertex simple graph.
2. Enumerate all four-subsets and reject complete ones.
3. Enumerate all six-subsets and reject independent ones.
4. Confirm the lower-bound implication is R(4,6) &gt;= 37, not &gt;= 36.
5. For a negative neighborhood result, check the encoding, seeds, edit radius and certificate separately.

**Statement alignment:** A 36-vertex witness improves the Ramsey lower bound to 37. Only ruling out every 36-vertex graph would prove the exact value 36.

**Human review difficulty:** Low for a positive witness; high for an unrestricted impossibility proof. Restricted failures need precise scope and provenance.

### Formal validity and empirical support

**What the formal task can establish:** Only a checked finite witness or a proof covering the declared space establishes the mathematical claim.

**Empirical support and limits:** No physical model, empirical data or experiment is needed.

### Methods and obstacles

**Proposed methods:**

- One-vertex seed extension with bounded edge changes
- SAT or local search with forbidden-subgraph penalties
- Independent subset enumeration
- Checked certificates for explicitly restricted neighborhoods

**Expected obstacles:**

- The known seed collection is small and not exhaustive.
- Search may rediscover an already checked neighborhood.
- The complementary color convention can be accidentally reversed.
- A wrong proof of symmetry breaking can invalidate a negative result.

### Checks still needed

- Fetch and independently validate the individual seed files before a trial.
- Check whether four-edge extension neighborhoods have already been exhausted.
- Confirm the live survey bounds before describing a result as an improvement.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The 2026 survey gives 36 &lt;= R(4,6) &lt;= 40, with the upper bound in Table Ib rather than the older Table Ia entry. The author collection supplies 35-vertex witnesses. No authoritative later resolution was located in a scoped check on 2026-10-14.

**Exact problem / theorem locator:** DS1 revision 18, Table Ia for the lower bound and Table Ib for the improved upper bound; Exoo's R(4,6) collection.

### Sources

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001). Stanisław P. Radziszowski. 2026. [Read source](https://www.cs.rit.edu/~spr/ElJC/sur.pdf).
  - **Relevant sections:** Revision 18, 24 April 2026; sections 2.1 and 6.1.1, Tables Ia and Ib; selected two-color and four-color bounds.
  - **Source limitations:** Living URL may change; record revision before each reuse. Selected entries were inspected, not every cited computation. For R(4,6), read Table Ib together with Table Ia rather than treating the earlier table as current on its own.
- [R(4,6) Colorings](../sources.md#src-math-203). Geoffrey Exoo. 2012. [Read source](https://cs.indstate.edu/ge/RAMSEY/R46/index.html).
  - **Relevant sections:** Heading and numbered links h0001 through h0037; the author's Ramsey Numbers parent page dates the improvement to March 2012.
  - **Source limitations:** The collection itself has no displayed date; 2012 is the construction date given by the author on the parent page. Individual adjacency files have not been independently checked here, and the collection is not claimed exhaustive.
- [Ramsey Numbers](../sources.md#src-math-206). Geoffrey Exoo. Year not verified. [Read source](https://cs.indstate.edu/ge/RAMSEY/).
  - **Relevant sections:** Two Color Ramsey Colorings table, links for R(3,10), R(3,11) and R(4,6); page update note 2024-04-09.
  - **Source limitations:** The displayed page is not a current upper-bound survey. Seeds require independent validation and a stable local copy before use.

### Known results and partial progress

- The 2026 survey gives 36 &lt;= R(4,6) &lt;= 40; its stronger upper bound appears in Table Ib.
- Exoo's collection contains 37 constructions at order 35, rather than an exhaustive classification of all such graphs.
- The survey excludes an improved lower bound from circulant graphs at this order, so a cyclic-only restriction is unsuitable.

**Research value:** A valid 36-vertex graph improves a longstanding lower bound by one. A full nonexistence proof would determine the number exactly, but is far beyond the proposed local search.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The 2026 survey retains the interval 36 to 40; the author's collection provides order-35 seeds. A scoped October search found no authoritative later improvement or resolution.

**Search limits:** Individual seed files and the cited upper-bound computation have not been rerun. Unpublished searches may cover the proposed milestone.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001)
- [R(4,6) Colorings](../sources.md#src-math-203)
- [Ramsey Numbers](../sources.md#src-math-206)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Exoo publishes 37 order-35 constructions; the 2026 survey cites improved upper-bound computations. These records motivate a finite construction task without implying AI performance.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Geoffrey Exoo
- Vigleik Angeltveit
- Brendan McKay
- Stanisław P. Radziszowski

**Suggested citation:** Exoo (2012), R(4,6) Colorings, 37 constructions of K_35; Radziszowski (2026), Small Ramsey Numbers, revision 18, Tables Ia and Ib, which credits the upper-bound computations to Angeltveit and McKay.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The proposed bounded construction trial has reusable attributed seeds and a transparent independent checker. The recommendation concerns reviewability and controlled scope, not an expectation of solving the full problem.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with exact graph algorithms, SAT encodings and reproducible solver inputs.

**Uncertainty:** No model or seed neighborhood has been tested. Existing expert searches may already have covered these neighborhoods, and success within the proposed cap is unknown.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Fixed vertex count and two forbidden subsets are explicit. |
| Decomposability | High | Seed validation, extension generation and witness verification are independent components. |
| Methods and literature | High | Published constructions and a maintained survey support concrete graph-search approaches. |
| Search / symbolic fit | High | The problem has a direct Boolean encoding and exact local predicates. |
| Checkability | High | Every forbidden four-set and six-set can be checked by a separate small program. |
| Expertise needed | Medium | Implementing the checker is elementary; useful search design needs combinatorial experience. |
| Scholarly significance | Medium | A witness advances a recognized small Ramsey bound. |
| Verification difficulty | Low | A positive graph has a transparent exhaustive checker; this rating does not apply to a global impossibility claim. |

**Correctness:** No project answer.

No project candidate solution has been submitted or independently reviewed.

**Novelty:** Requires future literature review.

Future results must be checked against live sources and existing computational records.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

A verified improvement would resolve a finite case or tighten a recognized extremal bound.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MATH-204` |
| Duplicate key | `improve-the-lower-bound-for-r-4-6-with-a-36-vertex-graph` |
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
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `bounds`, `finite_search`, `certificate_checking` |
| Validation tags | `exact_computation`, `pure_proof`, `public_data` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-204.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
