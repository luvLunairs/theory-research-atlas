# Global synchronization of random cubic graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-207 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-207%3A+Global+synchronization+of+random+cubic+graphs&target=Q-MODEL-207) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-207%3A+Global+synchronization+of+random+cubic+graphs&target=Q-MODEL-207)

Let G_n be uniform over simple labeled 3-regular graphs on n vertices, with n even. Does the probability tend to one that every local minimum, modulo uniform phase rotation, of E(theta)=1/2 sum_(i,j) A_ij(1−cos(theta_i−theta_j)) on the n-torus is synchronized (all phases equal modulo 2pi)? This retains the problem collection's local-minimum formulation.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Later negative-resolution evidence has been located. Carvallo, Groisman and Mitsche announce nonsynchronization with probability bounded away from zero. An author-attributed Colbrook manuscript claims the stronger limit zero in the exact indexed graph model. The latter has recorded agent reviews but no external human acceptance established here; retain unverified pending specialist assessment.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** 2025 conjecture; 2026 conference abstract; Colbrook manuscript dated 11 September 2026.

**Scope limits:** Keep the original probability limit and local-minimum statement. A finite nonsynchronized cubic graph alone would not refute an asymptotic high-probability assertion; the new sources make asymptotic claims.

**Information still needed**

- Locate the complete Carvallo-Groisman-Mitsche proof and confirm its graph distribution and stability definition.
- Obtain independent specialist evaluation or scholarly acceptance of the exact-model Colbrook claim.

**Primary branch:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Randomstrasse101: Open Problems of 2024](../sources.md#src-model-210); [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106); [Random cubic graphs are not globally synchronizing with probability at least 1 - exp(-2)](../sources.md#src-model-704); [Random cubic graphs admit nonsynchronized stable Kuramoto equilibria](../sources.md#src-model-705).

**Exact locator:** Randomstrasse101, Entry 2, Definition 2.1 and Conjecture 3; Carvallo et al., 2026 conference abstract; Colbrook, Statement and scope, Theorem 1.

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** Compare the announced and manuscript targets with the original conjecture and assist a specialist review of the claimed asymptotic obstruction before proposing a fresh attack.

**Verification burden:** High. Check the random simple labeled graph law, cycle-neighborhood and spectral assumptions, and the construction of genuine local minima modulo rotation. Neither numerical minima nor agent reviews establish independent acceptance.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** The exact-model negative manuscript is a public claim whose external acceptance remains unverified. Its incomplete Lean work is not machine certification.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

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
