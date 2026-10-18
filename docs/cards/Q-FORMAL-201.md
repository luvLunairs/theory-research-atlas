# A linear bound for avoiding a specified automaton state

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A resettable finite machine can be driven away from a chosen state. The question is whether fewer than twice as many input symbols as states always suffice. A single small counterexample would be decisive; an unsuccessful sample search would not establish the bound.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-201%3A+A+linear+bound+for+avoiding+a+specified+automaton+state&target=Q-FORMAL-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-201%3A+A+linear+bound+for+avoiding+a+specified+automaton+state&target=Q-FORMAL-201)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Related fields | [Combinatorics and discrete mathematics](../domains/math.md#math-comb) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For every complete deterministic strongly connected synchronizing automaton A=(Q,Σ,δ), with n=|Q| ≥ 2, and every q∈Q, does there exist w∈Σ* of length at most 2n−2 such that q∉δ(Q,w)?

**Required output:** Seek an exact counterexample to 2n−2, or a structural lemma for a clearly specified family that improves understanding of the avoiding mechanism.

**Scope:** The literature question ranges over all n and alphabets. Curator-proposed first milestone, pending review: inspect at most 1,000 explicitly recorded binary automata with 12≤n≤14, including perturbations of extremal constructions, and compute the exact avoiding distance of every state. This sample limit and choice of sizes are not a literature-established open subcase; novelty of an individual sampled configuration is unverified.

### Assumptions

- Transitions are total and deterministic; the alphabet is finite.
- The automaton is strongly connected and synchronizing, and n≥2.
- Avoiding q means excluding q from the image of every possible starting state under the same word.

### Success criteria

1. A counterexample must include its transition table, evidence of strong connectivity and synchronization, a specified state, and a checkable certificate that no word of length ≤2n−2 avoids it.
2. A positive theorem must state the complete family assumptions and prove the bound for all its members; finite samples alone do not qualify.
3. A completed bounded exploration must identify the tested instances and exclusions. Stop at the declared sample or resource limit; report an incomplete search without an absence claim beyond the checked set.

### Background needed

- Actions of words on subsets of a finite set.
- Strong connectivity, synchronization and breadth-first search.
- Distinguishing shortest avoiding words from shortest reset words.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** For one n-state instance, exact image-subset exploration uses at most 2^n subsets; at n=14 this is 16,384 possible subsets. Checking one instance is finite, while exhaustive enumeration of all transition tables is much larger. Proposed stop limits are 1,000 instances, 512 MiB memory and four elapsed hours, whichever is reached first. These are proposed ceilings, not measured requirements or performance claims.

**Data:** Use explicit transition tables and cited constructions. No external observational dataset is required.

**Experiments:** No physical experiment is needed for the formal question.

**Theory and model requirements:** Results concern total deterministic automata satisfying the stated graph and synchronization hypotheses, with no probabilistic or physical-machine assumption.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Check transition totality, strong connectivity and a supplied reset word.
2. Recompute δ(S,a) in an independent implementation, beginning from Q.
3. Verify all reachable images through length 2n−2 before accepting a violation; also record a shortest avoiding word to demonstrate finiteness.
4. Compare any family lemma and extremal example with the cited papers before making a novelty claim.

**Statement alignment:** Retain the strong-connectivity hypothesis of the original conjecture. The bounded sampling milestone is exploratory and does not cover all binary automata of those sizes.

**Human review difficulty:** Moderate for a single transition table and independently reproduced distance; high for a universal structural theorem.

### Formal validity and empirical support

**What the formal task can establish:** An exact counterexample disproves the quantified bound; an upper-bound proof must cover every admitted machine.

**Empirical support and limits:** No claim about a physical controller follows from this automata theorem. Computational samples are finite mathematical evidence only.

### Methods and obstacles

**Proposed methods:**

- Exact image-subset breadth-first search.
- Certified distances or closed reachable layers up to the proposed bound.
- Perturbation of sourced extremal constructions, followed by structural proof.

**Expected obstacles:**

- The number of automata grows far faster than the cost of checking one automaton.
- State relabeling and redundant letters can create misleading apparent novelty.
- A short reset word is not a certificate that an avoiding word is shortest.

### Checks still needed

- Confirm that any proposed sample family lies outside published classifications and later exhaustive checks.
- The 2026 survey wording differs from the original by omitting strong connectivity; the original hypothesis governs this card.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The original formulation supplies the essential strong-connectivity condition. The 2026 survey still presents the avoiding bound as a conjecture; no general resolution was found in the scoped later-source check.

**Exact problem / theorem locator:** Kisielewicz–Kowalski–Szykuła, §3, Conjecture 5; Szykuła, §2.2, Conjecture 2.

### Sources

- [Experiments with Synchronizing Automata](../sources.md#src-formal-210). Andrzej Kisielewicz; Jakub Kowalski; Marek Szykuła. 2016. [Read source](https://arxiv.org/pdf/1607.04025).
  - **Relevant sections:** §3, 'Avoiding states', Conjecture 5 (PDF p. 9); §3.1, Table 2.
  - **Source limitations:** Historical status and extremal values are supplemented by the 2021 and 2026 sources. The original conjecture contains a tightness assertion that is not adopted as a checked result here.
- [Lower Bounds on Avoiding Thresholds](../sources.md#src-formal-202). Robert Ferens; Marek Szykuła; Vojtěch Vorel. 2021. [Read source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol202-mfcs2021/LIPIcs.MFCS.2021.46/LIPIcs.MFCS.2021.46.pdf).
  - **Relevant sections:** MFCS 2021, article 46; Theorem 1, §2, §5, Conjectures 13–15.
  - **Source limitations:** Historical experiments and conjectures require later status checks. The broader two-state avoiding question is not added because the 2026 survey's summary requires reconciliation with this paper.
- [Synchronizing Automata: Open Problems](../sources.md#src-formal-201). Marek Szykuła. 2026. [Read source](https://arxiv.org/pdf/2608.24245).
  - **Relevant sections:** EPTCS 451, pp. 33–47; §§2.2–2.6; Conjectures 2 and 6, Open Problems 4 and 13.
  - **Source limitations:** The statement of Conjecture 2 omits the strong-connectivity condition present in the original KKS formulation. The atlas retains that condition. Later September and October 2026 preprints change some examples in this survey; its Figure 3 conjecture is not treated here as unresolved.

### Known results and partial progress

- The original KKS conjecture includes strong connectivity; omitting it admits unavoidably fixed sink states.
- Ferens–Szykuła–Vorel give extremal avoiding constructions and report binary checks through 11 states.
- The 2026 survey records a quadratic general upper bound, (n−2)(n−1)+2, and retains the linear-bound conjecture.

**Research value:** Avoiding-word bounds feed into bounds for synchronization. A new extremal construction or a rigorous structural lemma would have broader value than another unqualified random sample.

### Related problems

- **Related to:** [Sharp bounds for avoiding or compressing a subset](../candidates.md#q-formal-208). The avoiding-or-compressing lemma supplies a related route to upper bounds.
- **Related to:** [A linear bound for merging a specified state with some other state](../candidates.md#q-formal-202). Specified-state merging is a different invariant; its short certificates may suggest methods but do not answer avoidance.

### Scope of the status check

**Finding:** The scoped check found the avoiding conjecture retained in the 2026 survey; the later preprints address other synchronization invariants.

**Search limits:** This establishes a dated source-reported open question, not an exhaustive proof that no resolution exists. Finite-source claims await independent review.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Experiments with Synchronizing Automata](../sources.md#src-formal-210)
- [Lower Bounds on Avoiding Thresholds](../sources.md#src-formal-202)
- [Synchronizing Automata: Open Problems](../sources.md#src-formal-201)
- [The triple rendezvous time of a synchronizing automaton can be floor(4n/3)](../sources.md#src-formal-204)
- [The compress-with-another threshold of Szykuła's Figure 3 family](../sources.md#src-formal-205)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The 2016 and 2021 papers report finite exhaustive checks and explicit constructions; their computations have not been rerun here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Andrzej Kisielewicz
- Jakub Kowalski
- Marek Szykuła

**Suggested citation:** Kisielewicz, Kowalski and Szykuła, Experiments with Synchronizing Automata (2016), §3, Conjecture 5; see also Ferens, Szykuła and Vorel (2021) and Szykuła (2026).

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Transition-table generation and exact distance checks are well specified, but useful family selection needs an automata specialist and the general conjecture is difficult.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI can write finite-state search code and work with an independent checker under human supervision.

**Uncertainty:** No AI attempt has been evaluated. Modest instance verification does not imply that a counterexample exists or is likely to be found; the proposed sizes may contain no useful new behavior.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The quantified word-length inequality and admissible machines are explicit. |
| Decomposability | High | Individual machines and structural families can be treated separately. |
| Methods and literature | High | Subset search, extremal constructions and linear-algebraic bounds are documented. |
| Search / symbolic fit | High | Small transition tables admit exact search and inspectable certificates. |
| Checkability | High | A claimed finite counterexample can be checked independently with integer operations. |
| Expertise needed | High | Novel family selection and universal upper bounds require specialist knowledge. |
| Scholarly significance | High | A valid counterexample or new general bound changes the synchronization picture. |
| Verification difficulty | Medium | Finite witnesses are direct; a family theorem requires a separate mathematical audit. |

**Correctness:** No project answer.

The question and verification plan have been curated; no answer or search result is claimed.

**Novelty:** Requires future literature review.

The main question is sourced; the small exploration is curator-proposed and its outcomes require comparison with prior computations.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

General progress is difficult even though individual small instances can be checked exactly.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

Avoiding thresholds are connected to synchronization upper bounds.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-201` |
| Duplicate key | `a-linear-bound-for-avoiding-a-specified-automaton-state` |
| Original domain label | Algorithms and data structures |
| Original cross-domain labels | Combinatorics and discrete mathematics |
| Primary domain ID | `CS.ALG` |
| Cross-domain IDs | `MATH.COMB` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `finite_search`, `counterexample`, `certificate_checking`, `proof` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-201.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
