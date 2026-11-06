# Equal masses forced by a Newtonian choreography

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-450 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-450%3A+Equal+masses+forced+by+a+Newtonian+choreography&target=Q-MODEL-450) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-450%3A+Equal+masses+forced+by+a+Newtonian+choreography&target=Q-MODEL-450)

Does a Newtonian choreography, with bodies following the same curve at equal time shifts, force equal masses?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Tibboel's theorem gives equal masses for specified configuration-span ranks. For even n and rank n−3 it only equates masses within the two parity classes. These conditional results do not establish the unrestricted original claim.

**Statement check:** Needs clarification. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 literature check identifies the versions and passages inspected; original publication dates and earlier checks remain relevant.

**Scope limits:** A question within Newtonian point-mass dynamics. Mathematical orbit existence or stability is separate from applicability to finite-size astronomical bodies, dissipative effects and observations.

**Information still needed**

- For a concrete target, fix n, collision exclusion, the configuration-span rank and equal time spacing.
- Theorem 1.2 covers rank n−1, rank n−2, and odd n with rank n−3; distinguish these from the unresolved target.
- Check later literature and possible degenerate cases before asserting novelty.

**Primary branch:** [Celestial dynamics](../domains/astro.md#astro-dyn). **Related branches:** [Integrable and Hamiltonian systems](../domains/mphy.md#mphy-classical).

**Sources:** [Variational Methods in Celestial Mechanics](../sources.md#src-model-404); [Equal masses results for choreographies n-body problems](../sources.md#src-model-615).

**Exact locator:** Chenciner, AIM Problem 11; Tibboel (2020), Introduction, Remark 1.1 and Theorem 1.2.

**Potential difficulty:** High. Global variational and dynamical claims for Newtonian many-body systems involve collision singularities, symmetry and noncompact limits.

**Possible AI role:** A tool-using AI could analyze the linear constraints on masses induced by a candidate trajectory. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Review collision exclusion, symmetries and variational or dynamical hypotheses. Numerically observed orbits need rigorous error bounds before supporting an existence or stability theorem.

**Resource expectations:** Symbolic reductions and orbit exploration may use a workstation. Rigorous existence or global classifications require proof and possibly validated numerics; simulated trajectories alone are insufficient.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The rank in the cited theorem is that of the configuration for almost every time, not simply the ambient dimension. The original general statement remains unverified.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

Retain the general problem while exposing the precise partial theorem that an attempt must avoid reproducing.

**Search scope:** Targeted searches and inspection of the cited passages on 2026-11-06; neither an exhaustive literature search nor an independent scientific review.

**Inspected evidence**

- [Equal masses results for choreographies n-body problems](../sources.md#src-model-615) — Remark 1.1 and Theorem 1.2, printed pp. 3–4. Defines the rank almost everywhere in time and states the full-equality and parity-class conclusions separately.

**Limits and remaining work**

- The original AIM PDF returned 404 during this check.
- The full proof and all later results were not reviewed.

<details>
<summary>Search queries</summary>

- "choreographies" "equal masses" 2025 2026
- "Equal masses results for choreographies" 2026 correction


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

Later partial results exist; they do not establish the full unrestricted choreography claim. Preserve the original target and determine which mass, dimension and degeneracy classes remain before attempting it.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Variational Methods in Celestial Mechanics](../sources.md#src-model-404) — Problem 11, Alain Chenciner. Original question or research direction located.
- [Equal masses results for choreographies n-body problems](../sources.md#src-model-615) — Abstract. Equal-mass conclusions hold under specified dimension and symmetry hypotheses.

**Limits and remaining work**

- Identify which dimensions and degeneracies are outside the later equal-mass theorems; preserve the unrestricted original target.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- Chenciner choreography equal masses conjecture Tibboel 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
