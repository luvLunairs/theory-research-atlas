# Covering a prime cyclic group by translates of a random set

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-308 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-308%3A+Covering+a+prime+cyclic+group+by+translates+of+a+random+set&target=Q-MATH-308) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-308%3A+Covering+a+prime+cyclic+group+by+translates+of+a+random+set&target=Q-MATH-308)

For prime p, choose A uniformly among floor(sqrt(p))-element subsets of Z/pZ. Does the probability that at most ceil(100sqrt(p)) translates of A cover Z/pZ tend to 1 as p→∞?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The December 2025 author revision presents this target as open. The scoped search did not establish a later resolution; coverage after that revision is incomplete.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MATH-302: 2025. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [100 Open Problems, December 2025 revision](../sources.md#src-math-302).

**Exact locator:** Green Problem 39, p. 20; rounding makes the source's asymptotic sqrt(p) notation explicit.

**Potential difficulty:** High. A constant-factor covering bound near the cardinality lower bound needs control of highly dependent random overlaps.

**Possible AI role:** A tool-using AI could compare greedy and optimized coverings on finite instances and formulate a probabilistic bound explaining their overlaps.

**Verification burden:** High. A proposed cover is easy to check; asymptotic high probability requires a proof with correct quantifiers over p and A.

**Resource expectations:** Local sampling and exact set-cover experiments are possible; optimization can become expensive, and no simulation proves the limiting assertion.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Rounding conventions are explicit. A finite sample cannot establish convergence of the success probability.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
