# The sharp triple rendezvous bound for binary synchronizing automata

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-203 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-203%3A+The+sharp+triple+rendezvous+bound+for+binary+synchronizing+automata&target=Q-FORMAL-203) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-203%3A+The+sharp+triple+rendezvous+bound+for+binary+synchronizing+automata&target=Q-FORMAL-203)

For each n≥6, is the maximum, over synchronizing complete n-state automata with two letters, of T3(A)=min{|w| : there exists S⊆Q, |S|=3, |δ(S,w)|=1} equal to floor(4n/3)?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** A September 2026 preprint explicitly poses this conjecture after constructing matching examples. Its reported finite enumerations do not settle all n; no later general proof or counterexample was located in the scoped check.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-203: 2022, SRC-FORMAL-204: 2026, SRC-FORMAL-201: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Independently audit the recent construction and finite-coverage claims before treating them as settled infrastructure.
- Compare proposed n=13 cycle types with supplement §S1 and the restricted-class theorems.
- Check for subsequent corrections or extensions before any claim of novelty.

**Primary branch:** [Algorithms and data structures](../domains/cs.md#cs-alg). **Related branches:** [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Synchronizing Times for k-Sets in Automata](../sources.md#src-formal-203); [The triple rendezvous time of a synchronizing automaton can be floor(4n/3)](../sources.md#src-formal-204); [Synchronizing Automata: Open Problems](../sources.md#src-formal-201).

**Exact locator:** Zhang, §7, Conjecture 7.1; supplement Question S9.1 and §S1 finite ranges.

**Potential difficulty:** High. The general bound is difficult; the limited checker is small and well specified.

**Possible AI role:** No named model evaluated; assumes a tool-using AI capable of integer graph algorithms, with a separate checker and human review of theorem scope. A small certificate graph makes candidate verification attractive, but the recent preprint and its finite-coverage table need review before choosing an untested class. The bounded search is an untested proposal, not a prediction of solving the full conjecture.

**Verification burden:** Medium. Checking a finite instance is light; certification of exhaustive generation and family proofs is harder.

**Resource expectations:** Experiment: No physical experiment. Data: Two explicit transition maps per instance; published cycle-type coverage must be consulted to avoid duplicating a known case. Computation: For n=13, the graph of nonempty subsets of size at most three has 13+78+286=377 vertices. This bounds the checker graph, not the number of machines to search. Proposed ceilings are 1,000 instances, 512 MiB memory and four elapsed hours. Stop before exceeding any ceiling; no run or timing has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The sharp conjecture and finite classifications come from a recent preprint and have not been independently reproduced. Existing constructions may already explain all behavior in the proposed sample.

[Read the full card](../cards/Q-FORMAL-203.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
