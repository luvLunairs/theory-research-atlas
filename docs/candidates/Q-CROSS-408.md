# A Lyapunov characterization of measurement-to-error stability

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-408 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-408%3A+A+Lyapunov+characterization+of+measurement-to-error+stability&target=Q-CROSS-408) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-408%3A+A+Lyapunov+characterization+of+measurement-to-error+stability&target=Q-CROSS-408)

For a forward-complete system x-dot=f(x,u) on R^n with locally Lipschitz maps f,h,g and outputs y=h(x), w=g(x), and measurable essentially bounded inputs u, find a Lyapunov characterization, smooth if possible, of input-measurement-to-error stability: |y(t)| <= max{beta(|x(0)|,t), gamma_1(||w||_[0,t]), gamma_2(||u||_[0,t])} for every solution and t>=0, for some beta of class KL and gamma_1,gamma_2 of class K. The time-interval norms are essential suprema; y is the error and w the measurement.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The original target concerns the full IMES property with both input and measurement gains. The 2002 partial MES/SIT characterization and the previously recorded switched-system results do not establish this general target. Present resolution remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 update clarifies the original 2002 definition and its partial results; the earlier later-literature check remains available.

**Scope limits:** The error output, measurement output, input class and comparison-function inequality are explicit. Smoothness is a requested strengthening, not a prerequisite silently imposed on the target.

**Information still needed**

- Identify any later characterization for the exact general IMES property.
- Compare input classes, boundedness conditions and Lyapunov regularity before transferring MES or SIT results.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [Uniform stability properties of switched systems with switchings governed by digraphs](../sources.md#src-cross-605); [Measurement to Error Stability: a Notion of Partial Detectability for Nonlinear Systems](../sources.md#src-cross-700).

**Exact locator:** MTNS Problem 86, Sections 86.1-86.3, printed pp.95-97; Ingalls, Sontag and Wang (2002), abstract, Theorem 1 and Section 7.

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could compare converse-stability constructions and search counterexamples to candidate smoothness assumptions. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check necessity and sufficiency for the stated input, error and measurement channels; preserve forward completeness and distinguish nonsmooth partial characterizations from a smooth general result.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** The current resolution status remains unverified; historical partial results do not by themselves settle the full IMES target.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Expanded the historical statement without changing the research target or claiming present openness.

**Search scope:** Reopened the original problem and the cited 2002 partial characterization to specify the model and avoid conflating IMES with MES or SIT.

<details>
<summary>Previous indexed wording</summary>

Characterize input-measurement-to-error stability by a suitable, preferably smooth, Lyapunov function.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 86, Sections 86.1-86.3, printed pp.95-97; inspected author-hosted copy at https://perso.uclouvain.be/vincent.blondel/op/opmtns.pdf. Defines IMES with separate input and measurement gains and asks for a Lyapunov characterization, smooth if possible.
- [Measurement to Error Stability: a Notion of Partial Detectability for Nonlinear Systems](../sources.md#src-cross-700) — Abstract, Theorem 1 and Section 7. Provides partial nonsmooth results for MES/SIT with additional hypotheses, not the full input-dependent target.

**Limits and remaining work**

- No comprehensive later-literature search or independent proof audit.
- The distinction between the original IMES target and qualified MES/SIT results requires preservation in any future review.

<details>
<summary>Search queries</summary>

- "measurement-to-error stability" "Lyapunov" characterization


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The 2005 switched-system paper uses uniform and strengthened measurement-to-error properties. Their role in its stability proofs does not supply the requested unrestricted smooth converse theorem.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 86, section 86.1, pp. 95–97; Brian P. Ingalls and Eduardo D. Sontag. Identifies the historical target.
- [Uniform stability properties of switched systems with switchings governed by digraphs](../sources.md#src-cross-605) — Section 5; Nonlinear Analysis 63, 472–490; DOI 10.1016/j.na.2005.04.043. Defines uniform measurement-to-error properties and a stronger variant in switched-system stability arguments.

**Limits and remaining work**

- Compare converse Lyapunov results using the exact input, measurement and error norms from the original definition.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "input-measurement-to-error" Lyapunov characterization


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
