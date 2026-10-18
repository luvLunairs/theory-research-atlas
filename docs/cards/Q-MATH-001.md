# Reproduce the exact Ramsey number R(3,3)=6

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A tiny, established graph-coloring theorem makes a transparent starting benchmark for testing future search-to-certificate workflows.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-001%3A+Reproduce+the+exact+Ramsey+number+R%283%2C3%29%3D6&target=Q-MATH-001) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-001%3A+Reproduce+the+exact+Ramsey+number+R%283%2C3%29%3D6&target=Q-MATH-001)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Show that every red/blue coloring of the unordered edges of K6 contains a monochromatic triangle, and exhibit a red/blue coloring of K5 without one. Produce an independently checkable finite certificate alongside a human-readable proof.

**Required output:** Produce both the lower-bound witness and universal upper-bound argument, plus a reproducible exact certificate format.

**Scope:** Known-result reproduction at five and six vertices only. Any success is a calibration result, not new mathematics or evidence of competence on open Ramsey cases.

### Assumptions

- Finite simple undirected complete graphs; no loops or multiple edges.
- Exactly one of two available colors is assigned to each unordered pair; either color may be unused.
- A triangle consists of three distinct vertices; all three edges must share the same color.

### Success criteria

1. Supply an edge list or adjacency encoding for a valid five-vertex witness.
2. Give a logically complete proof for all six-vertex colorings.
3. If enumeration is used, account for all 2^15 colorings with an explicit encoding/completeness argument and independently checked triangle witnesses.
4. Record future tools, versions, logs, and human interventions; do not infer a general AI success rate from this one result.

### Background needed

- Complete graphs and edge colorings
- Pigeonhole principle
- Finite enumeration and independent verification

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Estimated ordinary laptop CPU and modest memory for a future run. The full six-vertex space has 32,768 colorings; this is a combinatorial size, not a measured runtime or budget.

**Data:** No external data required; source metadata and generated certificates only.

**Experiments:** None; a mathematical statement.

**Theory and model requirements:** Ordinary finite combinatorics; a future formal proof must state any axioms and encoding lemmas.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Human reviewer matches graph/color definitions to the literature statement.
2. Check every triangle of the five-vertex witness using an independent implementation.
3. Review the upper-bound proof directly; if computational, verify the enumeration map and all emitted certificates.
4. If formalized, compare the formal theorem and assumptions to this exact statement.

**Statement alignment:** Both R(3,3)&gt;5 and R(3,3)&lt;=6 are required. A single good coloring or tests on sampled colorings cannot establish equality.

**Human review difficulty:** Low for mathematical reasoning; moderate only if the implementation hides enumeration or certificate assumptions.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made.

### Methods and obstacles

**Proposed methods:**

- Proof
- Construction
- Finite search
- Exact computation
- Optional proof-assistant formalization

**Expected obstacles:**

- Off-by-one confusion between the Ramsey threshold and witness size.
- A passing checker cannot establish universal coverage unless the enumeration is proved complete.
- Memorized proof reproduction is not evidence of novel reasoning.

### Checks still needed

- Choose future certificate serialization and checker language.
- Decide whether formal proof is desired in addition to a short human proof.
- No runtime, cost, success-rate, or model comparison data exist yet.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Established theorem cited by the current dynamic survey and the inspected research paper. This is a proposed reproduction, not a new open problem.

**Exact problem / theorem locator:** DS1.18 section 2.1(a,d); Kiem–Pokutta–Spiegel section 1 identifies R(3,3)=6.

### Sources

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001). Stanisław P. Radziszowski. 2026. [Read source](https://www.cs.rit.edu/~spr/ElJC/sur.pdf).
  - **Relevant sections:** Revision 18, 24 April 2026; sections 2.1 and 6.1.1, Tables Ia and Ib; selected two-color and four-color bounds.
  - **Source limitations:** Living URL may change; record revision before each reuse. Selected entries were inspected, not every cited computation. For R(4,6), read Table Ib together with Table Ia rather than treating the earlier table as current on its own.
- [The Four-Color Ramsey Multiplicity of Triangles](../sources.md#src-math-014). Aldo Kiem; Sebastian Pokutta; Christoph Spiegel. 2023. [Read source](https://arxiv.org/pdf/2312.08049).
  - **Relevant sections:** arXiv:2312.08049v1; abstract, Theorem 1.1, section 2 definitions
  - **Source limitations:** Only relevant definitions and theorem scope inspected. This result must not be mistaken for an exact finite Ramsey threshold or for this project's AI evidence.

### Known results and partial progress

- R(3,3)=6 is an established result, cited in SRC-MATH-014 section 1; SRC-MATH-001 section 2.1 discusses its history and critical graphs.

**Research value:** Low novelty, high workflow value: it tests statement translation, lower versus upper bounds, exact enumeration, and auditable evidence on a case humans can inspect.

### Related problems

- **Calibrates:** [Determine the four-color triangle Ramsey number R(3,3,3,3)](../candidates.md#q-math-003). Shares edge-coloring/certificate concepts, but the four-color research problem has vastly larger search and proof costs.

### Scope of the status check

**Finding:** The exact value is an established result in the inspected sources; the project task is calibration.

**Search limits:** No search for all historical proofs or full formal-library inventory was performed.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001)
- [The Four-Color Ramsey Multiplicity of Triangles](../sources.md#src-math-014)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The current Ramsey survey records established treatments; this project has performed no reproduction.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Stanisław P. Radziszowski (survey)
- Aldo Kiem
- Sebastian Pokutta
- Christoph Spiegel (research exposition used for the known value)

**Suggested citation:** Cite Radziszowski, Small Ramsey Numbers, DS1, revision 18 (2026), section 2.1; and Kiem, Pokutta, Spiegel, arXiv:2312.08049v1 (2023), section 1. These are consulted sources, not a claim about sole historical priority.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

A clear, finite target and short independent checks make this useful for calibrating a workflow before harder research. This is not a prediction of novel discovery.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with basic graph theory and exact programming capability.

**Uncertainty:** No model was run. A successful reproduction would measure this task only and may reflect training familiarity.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Both inequalities and the finite object class are explicit. |
| Decomposability | High | Construction, proof, enumeration, and checker are separate deliverables. |
| Methods and literature | High | Elementary proof and finite-search methods are well documented. |
| Search / symbolic fit | High | A compact exact encoding is available. |
| Checkability | High | A person can inspect the proof and five-vertex witness; enumeration is small. |
| Expertise needed | Low | Basic discrete mathematics suffices, with some programming review for certificates. |
| Scholarly significance | Low | The theorem is elementary and already known; the value is calibration. |
| Verification difficulty | Low | Remaining risks are encoding and enumeration-completeness errors. |

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
| Stable ID | `Q-MATH-001` |
| Duplicate key | `math:ramsey:2colors:triangle:exact6` |
| Original domain label | Combinatorics |
| Original cross-domain labels | Graph theory; Theoretical computer science |
| Primary domain ID | `MATH.COMB.EXT` |
| Cross-domain IDs | `CS.ALG` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `construction`, `finite_search`, `exact_computation`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-001.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
