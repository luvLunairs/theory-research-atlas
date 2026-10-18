# Irreducibility of a random zero-one polynomial

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-425 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-425%3A+Irreducibility+of+a+random+zero-one+polynomial&target=Q-MATH-425) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-425%3A+Irreducibility+of+a+random+zero-one+polynomial&target=Q-MATH-425)

Let Pn(x)=1+x^n+sum_{i=1}^{n-1} ai*x^i, with independent coefficients ai uniformly distributed on {0,1}. Does the probability that Pn is irreducible over Q tend to one as n tends to infinity?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-15.

**Status basis:** Kogler's claimed theorem matches the indexed probability model. A public Lean repository now supplies statement mappings and reported verification records. These are author-maintained claims, and independent theorem alignment, build reproduction and acceptance remain unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Green's list: December 2025. Claimed theorem: 22 September 2026. Public formalization documentation inspected on 15 October 2026.

**Scope limits:** The public artifact makes a formal reproduction task concrete. Repository verification reports are external evidence, not tests performed by this project.

**Information still needed**

- Choose a fixed repository revision and independently compare its probability model and theorem declaration with the original conjecture.
- Reproduce the stated build, dependency and axiom checks before treating the formal artifact as verified.
- Obtain a documented independent mathematical assessment; author acknowledgments do not substitute for its scope.

**Primary branch:** [Discrete probability and random structures](../domains/prob.md#prob-discrete). **Related branches:** [Number theory and arithmetic geometry](../domains/math.md#math-num).

**Sources:** [100 Open Problems, December 2025 revision](../sources.md#src-math-302); [The Odlyzko–Poonen conjecture on irreducibility of random polynomials](../sources.md#src-math-606); [Odlyzko–Poonen Lean formalization](../sources.md#src-review-704).

**Exact locator:** Problem 93 and comments.

**Potential difficulty:** Unknown. A claimed resolution is now part of the evidence. Difficulty of the original target and difficulty of checking that claim must be assessed separately; the claim has not been independently verified.

**Possible AI role:** Help compare the historical conjecture with the repository's finite uniform model, map paper theorems to Lean declarations, and organize a reproducible audit of a fixed revision.

**Verification burden:** High. Check statement equivalence, fixed dependency revisions, axiom use and the resulting proof artifacts. Successful compilation alone would not establish that the formal statement matches the historical conjecture.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** A public formalization reports successful checks but no independent human review. No formal verification or model evaluation was run in this project.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The formalization is an accessible external attempt, but its presence does not by itself justify resolved status.

**Search scope:** Compared the primary manuscript's statement and acknowledgments with its linked public formalization documentation. This was a documentation review; no proof code was executed.

**Inspected evidence**

- [The Odlyzko–Poonen conjecture on irreducibility of random polynomials](../sources.md#src-math-606) — Theorem 1.1; Lean Formalization; Acknowledgments. The manuscript claims the exact asymptotic statement and credits a proof check and formalization.
- [Odlyzko–Poonen Lean formalization](../sources.md#src-review-704) — README: mathematical statements, source correspondence and independent statement files. The repository identifies the main Lean declaration and explicitly disclaims independent human review of the formalization.

**Limits and remaining work**

- No fixed-revision build or axiom audit was reproduced.
- The complete formal statement and proof were not independently checked.

<details>
<summary>Search queries</summary>

- "Odlyzko-Poonen Conjecture" Kogler review


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Green's older open question is directly covered by Kogler's September 2026 claimed unconditional theorem. The statement and date were checked, but independent acceptance and the proof or formalization were not established. The entry remains unverified and must not be presented as currently open.

**Search scope:** The original statement and the named later primary result were inspected; the recorded queries delimit the update search.

**Inspected evidence**

- [100 Open Problems, December 2025 revision](../sources.md#src-math-302) — Problem 93 and comments. The leading and constant coefficients are both fixed at one and the interior coefficients are independent fair zero–one variables.
- [The Odlyzko–Poonen conjecture on irreducibility of random polynomials](../sources.md#src-math-606) — Theorem 1.1; arXiv version 1, 22 September 2026. The theorem asserts the precise asymptotic irreducibility statement for monic zero–one polynomials with constant term one.

**Limits and remaining work**

- The search is not exhaustive and the later proof was not independently verified.
- No inference of currently open or accepted solved status is justified while this claimed resolution remains unreviewed.

<details>
<summary>Search queries</summary>

- "random" "0,1" polynomials irreducible 2026 probability
- "The Odlyzko-Poonen Conjecture" 2026 proof


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
