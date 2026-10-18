# The sharp triple rendezvous bound for binary synchronizing automata

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How long must a resettable two-letter machine wait before some three starting states can be brought together? A recent construction reaches floor(4n/3); the matching upper bound is still conjectural.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-203%3A+The+sharp+triple+rendezvous+bound+for+binary+synchronizing+automata&target=Q-FORMAL-203) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-203%3A+The+sharp+triple+rendezvous+bound+for+binary+synchronizing+automata&target=Q-FORMAL-203)

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

For each n≥6, is the maximum, over synchronizing complete n-state automata with two letters, of T3(A)=min{|w| : there exists S⊆Q, |S|=3, |δ(S,w)|=1} equal to floor(4n/3)?

**Required output:** Find an instance with T3≥18 at n=13, or prove a matching bound for an explicitly defined additional class.

**Scope:** The full target is the binary conjecture for every n≥6. Curator-proposed first milestone, pending review: study at most 1,000 n=13 automata with one permutation letter and one rank-12 letter, chosen outside or explicitly compared with the 18 permutation cycle types already checked in the cited supplement. This is a bounded exploratory sample, not a claim that every untested cycle type is a separately established open problem.

### Assumptions

- The automaton is complete, deterministic, synchronizing and has exactly two input letters.
- T3 minimizes over both the word and the choice of three distinct starting states.
- The conjecture starts at n=6; the reported n=5 exception is excluded.

### Success criteria

1. A counterexample must give two transition maps, a synchronization witness and exact distance evidence for every triple.
2. A new subclass upper bound must state all hypotheses and supply an all-instance proof; observed maxima are insufficient.
3. Publishable partial evidence would include an exact, independently checkable census of a declared finite class with sound isomorphism reductions. A sample is labelled as a sample.
4. Stop at 1,000 checked instances or the resource ceiling, and preserve the enumeration boundary and unresolved cases.

### Background needed

- Pair and triple subset automata.
- Breadth-first search and distance potentials.
- Permutation cycle types, transformation rank and synchronization tests.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** For n=13, the graph of nonempty subsets of size at most three has 13+78+286=377 vertices. This bounds the checker graph, not the number of machines to search. Proposed ceilings are 1,000 instances, 512 MiB memory and four elapsed hours. Stop before exceeding any ceiling; no run or timing has been measured.

**Data:** Two explicit transition maps per instance; published cycle-type coverage must be consulted to avoid duplicating a known case.

**Experiments:** No physical experiment.

**Theory and model requirements:** The first milestone additionally restricts the letter ranks; conclusions from that class do not establish the full binary conjecture.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Verify each letter map and its rank; verify a reset word or synchronization independently.
2. Construct every nonempty subset of size at most three and all letter edges.
3. Compute distances to singleton sets; take the minimum over all triples and attach a word attaining it.
4. Independently verify lower-distance inequalities or repeat exact graph search; audit claimed exhaustive generation separately.
5. Check the supplement's complete hypotheses before claiming a new class or cycle-type result.

**Statement alignment:** The target minimizes over all triples, not a prescribed triple. The n=13 rank restriction and sample cap belong only to the curator-proposed initial milestone.

**Human review difficulty:** Low to moderate for one finite certificate; high for exhaustive classification or a universal theorem.

### Formal validity and empirical support

**What the formal task can establish:** Exact subset distances establish a finite T3 value. Extending finite evidence to every n needs a mathematical proof.

**Empirical support and limits:** No physical-world claim is made; reported external computations remain unreplicated evidence.

### Methods and obstacles

**Proposed methods:**

- Reverse breadth-first distances from singleton subsets.
- Shortest merging words and integer lower-bound potentials.
- Cycle-type restricted search and structural case analysis.

**Expected obstacles:**

- Exhausting all transition maps remains costly despite the small checker.
- A long word for one chosen triple does not lower-bound the easiest triple.
- Some apparently new restricted classes are already covered by supplement theorems.

### Checks still needed

- Independently audit the recent construction and finite-coverage claims before treating them as settled infrastructure.
- Compare proposed n=13 cycle types with supplement §S1 and the restricted-class theorems.
- Check for subsequent corrections or extensions before any claim of novelty.

<a id="evidence"></a>

## Evidence and context

**Status basis:** A September 2026 preprint explicitly poses this conjecture after constructing matching examples. Its reported finite enumerations do not settle all n; no later general proof or counterexample was located in the scoped check.

**Exact problem / theorem locator:** Zhang, §7, Conjecture 7.1; supplement Question S9.1 and §S1 finite ranges.

### Sources

- [Synchronizing Times for k-Sets in Automata](../sources.md#src-formal-203). Natalie Behague; Robert Johnson. 2022. [Read source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i3p41/pdf/).
  - **Relevant sections:** Electronic Journal of Combinatorics 29(3), P3.41; Table 1, Theorems 11–12, Conjecture 20.
  - **Source limitations:** Its lower bounds precede the September 2026 construction. A chosen triple and the easiest triple are different invariants.
- [The triple rendezvous time of a synchronizing automaton can be floor(4n/3)](../sources.md#src-formal-204). Enkai Zhang. 2026. [Read source](https://arxiv.org/html/2609.19173v1).
  - **Relevant sections:** Theorem A; §2, Lemma 2.2; §7, Conjecture 7.1 and computation table; supplement §S1 and Question S9.1.
  - **Source limitations:** Recent preprint; proofs and computations were inspected but not independently reproduced. Neither the construction nor the finite tables prove a universal upper bound.
- [Synchronizing Automata: Open Problems](../sources.md#src-formal-201). Marek Szykuła. 2026. [Read source](https://arxiv.org/pdf/2608.24245).
  - **Relevant sections:** EPTCS 451, pp. 33–47; §§2.2–2.6; Conjectures 2 and 6, Open Problems 4 and 13.
  - **Source limitations:** The statement of Conjecture 2 omits the strong-connectivity condition present in the original KKS formulation. The atlas retains that condition. Later September and October 2026 preprints change some examples in this survey; its Figure 3 conjecture is not treated here as unresolved.

### Known results and partial progress

- Zhang's September 2026 preprint claims constructions with T3=floor(4n/3) for every n≥9.
- It reports all binary cases through n=10, the permutation/rank-(n−1) class through n=12, and only 18 cycle types at n=13.
- Earlier work asks for a linear bound in general; the new construction does not supply a universal upper bound.

**Research value:** The first collision among three states is a basic component of synchronization bounds. A certified violation of the proposed sharp bound, or a genuinely new structural case, would clarify the extremal mechanism.

### Related problems

- **Related to:** [A linear bound for merging a specified state with some other state](../candidates.md#q-formal-202). Merging a specified state with some partner differs from minimizing over all triples; the source explains why the minima can diverge.

### Scope of the status check

**Finding:** The September paper explicitly leaves the sharp binary bound open; the October paper proves a different specified-state family result.

**Search limits:** Very recent sources carry correction risk. No later general resolution was located, but the check is not exhaustive.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Synchronizing Times for k-Sets in Automata](../sources.md#src-formal-203)
- [Synchronizing Automata: Open Problems](../sources.md#src-formal-201)
- [The triple rendezvous time of a synchronizing automaton can be floor(4n/3)](../sources.md#src-formal-204)
- [The compress-with-another threshold of Szykuła's Figure 3 family](../sources.md#src-formal-205)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The September preprint reports finite enumerations and links an accompanying code archive; no archive has been executed in this project.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Enkai Zhang
- Natalie Behague
- Robert Johnson

**Suggested citation:** Zhang, The triple rendezvous time of a synchronizing automaton can be floor(4n/3), arXiv:2609.19173v1 (2026), Conjecture 7.1; Behague and Johnson, Electronic Journal of Combinatorics 29(3), P3.41 (2022).

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

A small certificate graph makes candidate verification attractive, but the recent preprint and its finite-coverage table need review before choosing an untested class. The bounded search is an untested proposal, not a prediction of solving the full conjecture.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI capable of integer graph algorithms, with a separate checker and human review of theorem scope.

**Uncertainty:** The sharp conjecture and finite classifications come from a recent preprint and have not been independently reproduced. Existing constructions may already explain all behavior in the proposed sample.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The minimum over triples and words gives a precise integer target. |
| Decomposability | High | Instances, cycle types and structural subclasses can be separated. |
| Methods and literature | High | The cited papers supply subset graphs, potentials and explicit constructions. |
| Search / symbolic fit | High | Integer distance calculations and symbolic family descriptions fit available tools. |
| Checkability | High | At n=13 the complete relevant subset graph has only 377 vertices. |
| Expertise needed | Medium | The finite checker is straightforward, while identifying new structural classes requires automata expertise. |
| Scholarly significance | High | A sharp-bound counterexample or proof changes a specific current conjecture. |
| Verification difficulty | Medium | Checking a finite instance is light; certification of exhaustive generation and family proofs is harder. |

**Correctness:** No project answer.

No candidate machine or theorem has been produced or tested.

**Novelty:** Requires future literature review.

Published finite ranges are recorded; any additional class or example requires comparison with the supplement and later work.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The general bound is difficult; the limited checker is small and well specified.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The target is a sharp extremal question with an explicit recent lower construction.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-203` |
| Duplicate key | `the-sharp-triple-rendezvous-bound-for-binary-synchronizing-automata` |
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
| Method tags | `finite_search`, `construction`, `counterexample`, `certificate_checking`, `proof` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-203.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
