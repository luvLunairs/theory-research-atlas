# Three-dimensional Navier–Stokes global regularity without forcing

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-LAND-305 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-LAND-305%3A+Three-dimensional+Navier%E2%80%93Stokes+global+regularity+without+forcing&target=Q-LAND-305) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-LAND-305%3A+Three-dimensional+Navier%E2%80%93Stokes+global+regularity+without+forcing&target=Q-LAND-305)

For fixed viscosity nu>0 and every divergence-free Schwartz initial velocity u0 on R^3, do there exist u,p in C-infinity(R^3 x [0,infinity)) solving the unforced incompressible Navier-Stokes initial-value equations with sup_{t>=0} integral_{R^3} |u(x,t)|^2 dx finite? Schwartz means that every spatial derivative decays faster than every inverse power of distance. This is the whole-space positive alternative in the official formulation.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** Fefferman’s alternative A sets the force to zero. OpenAI’s September construction uses an external force. In November Alpöge and Buckmaster claimed an unforced whole-space counterexample with compactly supported data. Their release omits the certificate and its computation. The unforced claim awaits independent assessment.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Fefferman’s official statement, the September Clay notice and author announcement, the October correspondence critique and the November unforced release were inspected on 26 November 2026.

**Scope limits:** Fefferman’s alternative A sets the force to zero. OpenAI’s September construction uses an external force. In November Alpöge and Buckmaster claimed an unforced whole-space counterexample with compactly supported data. Their release omits the certificate and its computation. The unforced claim awaits independent assessment.

**Information still needed**

- The November certificate and its interval-arithmetic computation were absent from the inspected release. The proof and Lean package were not independently checked.
- Clay’s September announcement predates the unforced claim. Neither a prize decision nor independent acceptance was established in this check.

**Primary branch:** [Differential equations and variational analysis](../domains/math.md#math-anal-pde). **Related branches:** [Fluid and plasma theory](../domains/phys.md#phys-fluid).

**Sources:** [Existence and Smoothness of the Navier-Stokes Equation](../sources.md#src-land-306); [Navier-Stokes Announcement](../sources.md#src-math-015); [The Millennium Prize Problems](../sources.md#src-land-301); [On the Navier–Stokes Millennium Prize Problem](../sources.md#src-land-904); [Finite-time blow-up for the Navier–Stokes equations](../sources.md#src-land-905); [Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs](../sources.md#src-land-906).

**Exact locator:** Fefferman, alternative A, conditions (1)–(4), (6) and (7). For the unforced claim see Alpöge and Buckmaster, Theorem 1.1 and the release notes.

**Potential difficulty:** Frontier. The full statement is a longstanding foundational research target. A bounded example or computational check would address only part of it.

**Possible AI role:** A tool-using assistant could compare the paper and formal theorem against alternative A, then inventory the certificate assumptions for independent verification.

**Verification burden:** High. Check the unforced whole-space hypotheses, loss of regularity and the bridge to the bounded-energy statement. The claimed computational part also requires the exact certificate, arithmetic checks and an independent replay.

**Resource expectations:** No physical experiment or empirical dataset is required. Proof development has no reliable time or computing estimate; finite calculations need a separately chosen size and budget. Experimental support for fluid modelling is separate from mathematical regularity.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** No named model or research run has been evaluated. A role in supporting lemmas is plausible; ability to settle the full target is unknown. Specialist review remains necessary.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Fefferman’s alternative A sets the force to zero. OpenAI’s September construction uses an external force. In November Alpöge and Buckmaster claimed an unforced whole-space counterexample with compactly supported data. Their release omits the certificate and its computation. The unforced claim awaits independent assessment.

**Search scope:** Compared the official alternatives, the September announcement, a critique of its formal correspondence, and the November authors’ release and statement guide.

**Inspected evidence**

- [Existence and Smoothness of the Navier-Stokes Equation](../sources.md#src-land-306) — Alternatives A–D, pp. 1–2. A asks for regularity on three-dimensional Euclidean space without a force. C and D allow a force.
- [On the Navier–Stokes Millennium Prize Problem](../sources.md#src-land-904) — 8 September announcement, paragraphs describing the smooth external force and Fefferman alternatives. OpenAI reports finite-time blow-up from rest under a smooth applied force, targeting alternatives C and D.
- [Navier-Stokes Announcement](../sources.md#src-math-015) — 11 September 2026, final two paragraphs. Clay acknowledged an apparent settlement and described its evaluation process before the November release.
- [Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs](../sources.md#src-land-906) — Abstract, discussion of the OpenAI natural-language argument and its formalization. The authors dispute the correspondence between the September written argument and its formalization.
- [Finite-time blow-up for the Navier–Stokes equations](../sources.md#src-land-905) — 20 November release, repository README on the certificate and lean/README.md under Theorem 1.1. The authors claim unforced blow-up for smooth compactly supported data on three-dimensional Euclidean space and for smooth periodic data. The release lists the missing certificate and computation.

**Limits and remaining work**

- The November certificate and its interval-arithmetic computation were absent from the inspected release. The proof and Lean package were not independently checked.
- Clay’s September announcement predates the unforced claim. Neither a prize decision nor independent acceptance was established in this check.

<details>
<summary>Search queries</summary>

- three dimensional Navier Stokes September 2026 Fefferman alternatives forced blowup
- November 2026 unforced Navier Stokes blowup Alpöge Buckmaster certificate


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The exact whole-space statement matches Fefferman's alternative (A). Clay's 2026 announcement records an apparent settlement and continuing assessment. No accepted proof or verified alignment of that claim with alternative (A) has been established here, so this record remains outside the open selection.

**Search scope:** The original statement and the named later primary results were inspected; searches were limited to the recorded queries.

**Inspected evidence**

- [Existence and Smoothness of the Navier-Stokes Equation](../sources.md#src-land-306) — Alternative (A), equations (1)–(4), (6)–(7). The candidate matches the unforced whole-space positive alternative, including bounded energy.
- [Navier-Stokes Announcement](../sources.md#src-math-015) — 11 September 2026 announcement, final three paragraphs. Clay reports an apparent settlement and an evaluation process, without identifying which formal alternative has been accepted.

**Limits and remaining work**

- The candidate proof and its precise alternative have not been audited.
- No final acceptance or prize determination is inferred from the announcement.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
