# A 150-point no-three-in-line configuration on a 75 by 75 grid

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Place 150 lattice points on a 75 by 75 board so that no straight line contains three. A finite output is easy to check independently, although finding it may be hard.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-201%3A+A+150-point+no-three-in-line+configuration+on+a+75+by+75+grid&target=Q-MATH-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-201%3A+A+150-point+no-three-in-line+configuration+on+a+75+by+75+grid&target=Q-MATH-201)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Geometry](../domains/math.md#math-geom) |
| Related fields | [Extremal and Ramsey theory](../domains/math.md#math-comb-ext), [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Does there exist S contained in {0,...,74}^2 with |S|=150 such that (x_j-x_i)(y_k-y_i)-(x_k-x_i)(y_j-y_i) is nonzero for every three distinct points of S? A construction attains the row-count upper bound; an impossibility proof must cover all configurations.

**Required output:** Find a 150-point witness, or prove none exists. First milestone: encode configurations invariant under (x,y) -&gt; (74-x,74-y), provide the exact constraints, and conduct one capped search.

**Scope:** The unrestricted size-75 existence question. A separately proposed first milestone examines half-turn invariant configurations; this is a curator-designed restriction, not a reduction of the whole problem.

### Assumptions

- Coordinates are integers from 0 to 74 inclusive.
- Collinearity includes every slope, not just rows, columns and main diagonals.
- All points must be distinct; a tolerance-based drawing is insufficient.

### Success criteria

1. Supply all 150 integer pairs and pass an independently written determinant checker.
2. For the proposed milestone, require two points in every row and column, half-turn invariance, and at most two points on every grid line; declare any further restrictions.
3. Cap the proposed milestone at 8 CPU-hours and 16 GiB RAM. These are chosen limits, not measured requirements or predicted time to success.
4. A checked UNSAT certificate for the restricted encoding establishes only absence in that subclass. A timeout establishes neither existence nor nonexistence.

### Background needed

- Integer determinant geometry
- SAT or constraint programming
- Symmetry and orbit constraints

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Proposed cap: 8 CPU-hours and 16 GiB RAM. The grid has 5,625 positions. A positive witness needs C(150,3)=551,300 exact triple checks. Full impossibility may require much larger resources.

**Data:** Self-contained. Optional attributed configurations and encodings come from Flammenkamp's database.

**Experiments:** None.

**Theory and model requirements:** Euclidean collinearity of integer points. Half-turn symmetry is a voluntary search restriction, not a theorem about optimal configurations.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Check count, distinctness and coordinate bounds independently.
2. Enumerate every triple with exact integer arithmetic and reject zero determinants.
3. For a solver proof, reconstruct the constraints and use an independent certificate verifier.
4. Refresh the source before a novelty claim.

**Statement alignment:** The main statement covers all configurations; the half-turn milestone cannot establish unrestricted nonexistence.

**Human review difficulty:** Low for a positive witness; high for a global impossibility proof.

### Formal validity and empirical support

**What the formal task can establish:** Only a checked finite witness or a proof covering the declared space establishes the mathematical claim.

**Empirical support and limits:** No physical model, empirical data or experiment is needed.

### Methods and obstacles

**Proposed methods:**

- SAT or constraint programming with line-capacity constraints
- Half-turn orbit variables
- Local search guided by collinear triples
- Independent integer determinant checking

**Expected obstacles:**

- A symmetry restriction may remove every solution.
- Checking only familiar slopes changes the problem.
- Existing unpublished searches may cover the restricted case.
- A 149-point output is not automatically a new record; the database primarily records full configurations.

### Checks still needed

- Refresh the latest table.
- Determine whether the proposed symmetry case has already been exhausted.
- Audit sub-150 records before claiming a lower-count improvement.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The author-maintained frontier records all sizes 2 through 74 and size 76, but no size 75. Searches for a size-75 construction or impossibility result found no authoritative resolution by 2026-10-14. This is an open-status inference from a dated frontier gap, not an explicit theorem of open status.

**Exact problem / theorem locator:** Introduction and maintained frontier entries for n=71,73,74,76; summary-table date 2026-09-11.

### Sources

- [The No-Three-in-Line Problem](../sources.md#src-math-201). Achim Flammenkamp. Year not verified. [Read source](https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html).
  - **Relevant sections:** Introduction; Conjectures; entries for grid sizes 71, 73, 74 and 76; summary table updated 2026-09-11.
  - **Source limitations:** A maintained collection is not an exhaustive account of unpublished work. Its missing size-75 entry supports a frontier candidate, not a proof of nonexistence or a global certification of open status. The page contains superseded historical conjecture formulations.

### Known results and partial progress

- The maintained source records constructions at all sizes 2 through 74 and at 76; size 75 is absent in the inspected frontier.
- The elementary row argument gives at most 150 points. No independently audited best sub-150 value is asserted.

**Research value:** A witness closes a gap below the largest recorded solved board. An obstruction for a precisely specified symmetry class may guide searches, subject to a separate novelty check.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The maintained September frontier leaves a size-75 gap; the scoped October search found no authoritative resolution.

**Search limits:** Missing records do not certify universal open status. Unpublished constructions or restricted-case impossibility results may exist.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [The No-Three-in-Line Problem](../sources.md#src-math-201)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The maintained collection attributes recent frontier constructions to Thomas Prellberg, Mitchell Riley and Marijn Heule; it lists no size-75 solution.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Henry Ernest Dudeney
- Achim Flammenkamp

**Suggested citation:** Flammenkamp, The No-Three-in-Line Problem, maintained database, table updated 2026-09-11, accessed 2026-10-14. Historical credit to Dudeney follows the source; the 1906 original was not inspected.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Priority applies to the bounded construction experiment: its output is precise and independently checkable. It does not predict that the frontier target will be solved.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI able to implement integer constraints, reason about symmetry and produce inspectable solver inputs.

**Uncertainty:** No model or search has been evaluated. Easy checking gives no estimate of success probability, and the frontier can change quickly.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The board, point count and predicate are explicit. |
| Decomposability | High | Encoding, symmetry, search and checking separate naturally. |
| Methods and literature | High | The source documents constraint searches and reusable symmetry records. |
| Search / symbolic fit | High | The predicates are finite exact integer constraints. |
| Checkability | High | A positive witness requires a modest number of determinant checks. |
| Expertise needed | Medium | Search design needs experience; the witness checker is elementary. |
| Scholarly significance | Medium | A witness fills an actively maintained finite frontier gap. |
| Verification difficulty | Medium | Positive checking is simple; UNSAT needs an encoding proof and certificate audit. |

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
| Stable ID | `Q-MATH-201` |
| Duplicate key | `a-150-point-no-three-in-line-configuration-on-a-75-by-75-grid` |
| Original domain label | Discrete geometry |
| Original cross-domain labels | Extremal combinatorics; Algorithms |
| Primary domain ID | `MATH.GEOM` |
| Cross-domain IDs | `MATH.COMB.EXT`, `CS.ALG` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `construction`, `finite_search`, `exact_computation`, `certificate_checking` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MATH-201.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
