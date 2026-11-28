# Global synchronization of random cubic graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-207 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-207%3A+Global+synchronization+of+random+cubic+graphs&target=Q-MODEL-207) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-207%3A+Global+synchronization+of+random+cubic+graphs&target=Q-MODEL-207)

Let G_n be uniform over simple labeled 3-regular graphs on n vertices, with n even. Does the probability tend to one that every local minimum, modulo uniform phase rotation, of E(theta)=1/2 sum_(i,j) A_ij(1−cos(theta_i−theta_j)) on the n-torus is synchronized (all phases equal modulo 2pi)? This retains the problem collection's local-minimum formulation.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** The conference abstract gives a bound away from zero for nonsynchronization. In October the same authors claimed nonsynchronization with probability tending to one, then withdrew the preprint because they found an overlapping solution on GitHub. Colbrook’s separate manuscript also claims this asymptotic conclusion. The withdrawal notice cites overlap rather than a flaw in the proof.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Randomstrasse101, Entry 2, Conjecture 3. Carvallo, Groisman and Mitsche, October 2026 preprint v1, Theorem 1.2, and v2 withdrawal notice. Colbrook, Theorem 1.

**Scope limits:** The conference abstract gives a bound away from zero for nonsynchronization. In October the same authors claimed nonsynchronization with probability tending to one, then withdrew the preprint because they found an overlapping solution on GitHub. Colbrook’s separate manuscript also claims this asymptotic conclusion. The withdrawal notice cites overlap rather than a flaw in the proof.

**Information still needed**

- Neither the withdrawn version nor the separate manuscript received an independent proof audit here. Check the local-minimum criterion and its correspondence to the claimed dynamics.

**Primary branch:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Randomstrasse101: Open Problems of 2024](../sources.md#src-model-210); [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106); [Random cubic graphs are not globally synchronizing with probability at least 1 - exp(-2)](../sources.md#src-model-704); [Random cubic graphs admit nonsynchronized stable Kuramoto equilibria](../sources.md#src-model-705); [Random 3-regular graphs are not globally synchronizing](../sources.md#src-model-920).

**Exact locator:** Randomstrasse101, Entry 2, Conjecture 3. Carvallo, Groisman and Mitsche, October 2026 preprint v1, Theorem 1.2, and v2 withdrawal notice. Colbrook, Theorem 1.

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** Trace the two arguments to their precise graph ensembles and stability definitions before treating them as separate evidence.

**Verification burden:** High. Check the random simple labeled graph law, cycle-neighborhood and spectral assumptions, and the construction of genuine local minima modulo rotation. Neither numerical minima nor agent reviews establish independent acceptance.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** Neither the withdrawn version nor the separate manuscript received an independent proof audit here. Check the local-minimum criterion and its correspondence to the claimed dynamics.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The conference abstract gives a bound away from zero for nonsynchronization. In October the same authors claimed nonsynchronization with probability tending to one, then withdrew the preprint because they found an overlapping solution on GitHub. Colbrook’s separate manuscript also claims this asymptotic conclusion. The withdrawal notice cites overlap rather than a flaw in the proof.

**Search scope:** Compared the indexed question with the passages and later records listed below.

**Inspected evidence**

- [Randomstrasse101: Open Problems of 2024](../sources.md#src-model-210) — Entry 2, Conjecture 3. Poses a high-probability local-minimum question for a random cubic graph.
- [Random 3-regular graphs are not globally synchronizing](../sources.md#src-model-920) — Version 2, author withdrawal comment dated 10 October 2026. Version 1, Theorem 1.2 and Section 3. Version 1 states that a uniform random simple cubic graph has a nonsynchronized local minimum with high probability. The authors withdrew the manuscript after finding a solution on GitHub.

**Limits and remaining work**

- Neither the withdrawn version nor the separate manuscript received an independent proof audit here. Check the local-minimum criterion and its correspondence to the claimed dynamics.

<details>
<summary>Search queries</summary>

- Carvallo Groisman Mitsche random 3-regular graphs not globally synchronizing arXiv withdrawal


</details>

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Unverified.

Later negative-resolution evidence has been located. Carvallo, Groisman and Mitsche announce nonsynchronization with probability bounded away from zero. An author-attributed Colbrook manuscript claims the stronger limit zero in the exact indexed graph model. The latter has recorded agent reviews but no external human acceptance established here; retain unverified pending specialist assessment.

**Search scope:** Opened the official meeting abstract and PDF, the repository problem record, attributed manuscript source and submission record. Compared the manuscript Theorem 1 with the existing exact graph/phase target. No proof or supplementary checker was executed. Reopened the manuscript and submission record at commit 3017ea813328900a812c0c105ca16ad6f694857e; the fixed manuscript text exactly matched the previously inspected main-branch text.

**Inspected evidence**

- [Random cubic graphs are not globally synchronizing with probability at least 1 - exp(-2)](../sources.md#src-model-704) — One-page PDF, main paragraph. The PDF resolves the HTML encoding ambiguity: the announced nonsynchronization bound is 1-exp(-2).
- [Random cubic graphs admit nonsynchronized stable Kuramoto equilibria](../sources.md#src-model-705) — Statement and scope, Theorem 1; submission README. The manuscript matches uniform simple labeled cubic graphs and all local minima; recorded agent review is explicitly not human peer review.

**Limits and remaining work**

- The meeting abstract is not a full proof. The manuscript is retained as a claim, not adopted as an independently established disproof.

<details>
<summary>Search queries</summary>

- "random cubic graphs" synchronization 2026
- "random cubic graphs" "Groisman"
- "random cubic graphs" "globally synchronizing" Carvallo Mitsche arxiv
- "random cubic graphs" "Carvallo" "2026"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
