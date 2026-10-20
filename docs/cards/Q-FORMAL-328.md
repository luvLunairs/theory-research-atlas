# Exact capacity of the independent binary deletion channel

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

When missing bits leave no position markers, even the maximum reliable information rate is unknown. The half-deletion case provides a fixed parameter at which stronger bounds would be useful.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Classical information theory](../domains/info.md#info-shannon) |
| Related fields | None recorded |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Determine the Shannon capacity C(d) in bits per input bit of the binary channel that independently deletes each input bit with probability d∈(0,1), preserves the order of surviving bits and does not reveal deletion locations, without feedback.

**Required output:** Determine capacity, or establish a rigorously stronger achievable-rate or converse bound at an explicitly fixed deletion probability.

**Scope:** Retains the canonical question for C(d). The source's d=1/2 case is a bounded entry point; improvement there is partial progress, not the exact capacity function.

### Assumptions

- Each binary input symbol is deleted independently with fixed probability d; surviving symbols retain their order.
- Use Shannon capacity without feedback, normalized per input bit, and vanishing error as block length grows.
- Allow arbitrary input distributions when claiming an upper bound on capacity. A bound restricted to one source family is not a general converse.

### Success criteria

1. State the exact parameter, normalization, inequalities and theorem connecting the certificate to unrestricted channel capacity.
2. Compare against precise source endpoints, rather than claiming novelty from rounded displayed decimals.
3. Provide an independently reproducible proof or numerical certificate with controlled arithmetic, including every required input.

### Background needed

- Information theory and coding theorems
- Entropy rates and finite-state processes
- Rigorous numerical bounds and exact certificate arithmetic

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** No estimate has been measured. Small analytic and certificate checks can be separated from large finite-window enumeration, whose state count grows exponentially. Full source replay requires specialist numerical infrastructure.

**Data:** Exact source laws, bound parameters, certificate inputs and versions. Availability of all large baseline inputs remains unconfirmed.

**Experiments:** None for the mathematical channel model.

**Theory and model requirements:** Independent deletions, binary input, no feedback and asymptotic reliable communication; distinguish this model from insertions, substitutions and multiple-read channels.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Check input/output normalization, deletion law and capacity definition.
2. Review achievability or converse quantifiers and the finite-to-asymptotic argument.
3. Pin every input and verify arithmetic enclosures, omitted tails and all rows required by a converse.
4. Run the final certificate independently; distinguish its result from a light assembly or file-integrity check.

**Statement alignment:** A source-specific rate, numerical optimizer output or midpoint is not exact channel capacity.

**Human review difficulty:** High: an information theorist must review the reduction, while numerical evidence needs an independent replay.

### Formal validity and empirical support

**What the formal task can establish:** Any theorem is conditional on the explicitly stated deletion-channel model.

**Empirical support and limits:** Capacity for this ideal channel does not establish performance in a physical communication or storage system.

### Methods and obstacles

**Proposed methods:**

- Source-based achievable-rate analysis
- Information-theoretic converse bounds
- Finite-state and renewal-source calculations with rigorous arithmetic

**Expected obstacles:**

- Hidden alignment creates long-range dependence.
- Finite windows leave tails requiring explicit control.
- Improving evaluation of one input process does not prove its optimality.

### Checks still needed

- Independent scrutiny of the recent preprint and complete numerical replay.
- Actual availability and reuse permission for all external proof inputs.
- A fresh check of precise bounds before reporting an improvement.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The September 2026 preprint retains the exact-capacity question. A focused later-work search found no resolution. Its numerical bounds remain reported results with incomplete replay availability, not independently verified project benchmarks.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-328.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** SRC-FORMAL-318 sections 1.2, 2 and 14.3; SRC-IMPACT-009 README.

### Sources

- [Binary Deletion Channel Capacity to Within One Hundredth of a Bit](../sources.md#src-formal-318). Dimitris Papailiopoulos. 2026. [Read source](https://arxiv.org/html/2609.19412v1).
  - **Relevant sections:** Sections 1.2, 2, 12-14; Table 1.
  - **Source limitations:** Preprint. Bounds and numerical certificates were not independently replayed. The linked repository still reports incomplete availability of its large proof inputs.
- [Binary deletion-channel capacity: verification materials](../sources.md#src-impact-009). Dimitris Papailiopoulos. 2026. [Read source](https://github.com/anadim/binary-deletion-channel-capacity).
  - **Relevant sections:** README: portable checks, full calculation and reuse terms.
  - **Source limitations:** README was opened on 2026-10-20. External input availability was not independently checked; no checker was run. Reuse license remains unspecified.

### Known results and partial progress

- SRC-FORMAL-318 Table 1 reports 0.114540&lt;=C(1/2)&lt;=0.130162 bits per input bit, rounded outward. These are claimed certified enclosures, not ordinary floating-point estimates; the project has not replayed them.
- The source distinguishes an achievable lower endpoint from a midpoint estimate, and leaves source and converse optimization open.
- SRC-IMPACT-009 lists portable checks but says the full large-input collection is not yet downloadable in full. Those checks do not rerun the numerical inequalities.

**Research value:** A sharper capacity benchmark would clarify limits of communication with synchronization loss. Practical encoders and realistic DNA-storage models require additional analysis.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** No exact-capacity resolution or correction was located in the focused search; the author's repository exposes a replay-availability limitation.

**Search limits:** Search coverage is bounded. No mathematical proof, code or numerical certificate was independently verified.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "binary deletion channel" "capacity" "2026" "October"
- "deletion channel capacity" "Papailiopoulos" correction
- "2609.19412" correction

**Sources checked:**

- [Binary Deletion Channel Capacity to Within One Hundredth of a Bit](../sources.md#src-formal-318)
- [Binary deletion-channel capacity: verification materials](../sources.md#src-impact-009)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Papailiopoulos reports an AI-assisted bound construction; its paper and verification materials are linked. No project research attempt is recorded.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Dimitris Papailiopoulos

**Suggested citation:** Papailiopoulos, Binary Deletion Channel Capacity to Within One Hundredth of a Bit, arXiv:2609.19412v1 (2026), especially sections 1.2, 2 and 12-14. This is a recent reference for a classical problem, not an attribution of its origin.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

The published computation supplies concrete methods and checking obligations. Reviewing its assumptions and obtaining complete inputs should precede a new attempt.

**Model or capability conditions:** A tool-using assistant able to inspect mathematical sources and preserve exact computations; no named model or configuration evaluated.

**Uncertainty:** No project research attempt or model evaluation has been performed. Published attempts do not establish a success probability for this task.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The channel and capacity units are fixed. |
| Decomposability | High | Achievability, converse and numerical certificate obligations are distinct. |
| Methods and literature | High | The cited paper provides explicit established and recent methods. |
| Search / symbolic fit | High | Finite-state and interval calculations admit reproducible tooling. |
| Checkability | Medium | A complete bound needs both its analytic reduction and all numerical premises. |
| Expertise needed | High | Capacity and numerical-certification expertise are required. |
| Scholarly significance | High | The question is a basic limit for synchronization-error communication. |
| Verification difficulty | High | Finite calculations must support a uniform assertion over allowed inputs. |

**Correctness:** Not assessed.

No candidate solution supplied; published certificates not independently replayed.

**Novelty:** Not assessed.

No new result claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The source leaves both source optimality and converse tightness unsettled.

**Evidence type:** Source discussion; no project measurement..

**Significance:** High.

Fundamental channel-capacity benchmark; practical relevance depends on a separate code and channel model.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-20 | Expanded the existing capacity entry with a half-deletion entry point, reported bounds and replay limitations. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-328` |
| Duplicate key | `information:binary-deletion-channel:exact-capacity` |
| Original domain label | Shannon theory |
| Original cross-domain labels | None |
| Primary domain ID | `INFO.SHANNON` |
| Cross-domain IDs | None |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `bounds`, `proof`, `exact_computation`, `numerical_computation` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-328.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
