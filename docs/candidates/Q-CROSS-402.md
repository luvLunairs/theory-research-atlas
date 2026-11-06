# An algebraic test for time-controllability

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-402 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-402%3A+An+algebraic+test+for+time-controllability&target=Q-CROSS-402) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-402%3A+An+algebraic+test+for+time-controllability&target=Q-CROSS-402)

Give an algebraic test on a polynomial matrix R over C in m spatial variables and one time variable that characterizes time-controllability of B = ker R(partial_x, partial_t) within C-infinity(R^(m+1), C^w). For every w1,w2 in B, there must be a trajectory w in B and one finite tau >= 0 such that w(x,t)=w1(x,t) for t<=0 and w(x,t)=w2(x,t-tau) for t>=tau, for every spatial x.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The original target uses unrestricted smooth continuous trajectories. Bharti and Pal (2026) give discrete two-dimensional criteria, not a resolution of this signal-space formulation. The general smooth case remains unverified here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The original problem is from 2002. The dated literature check identifies the later version inspected; neither access date nor a related theorem establishes current openness.

**Scope limits:** The transition time is uniform over space. Discrete behaviors, spatially tempered functions and finite sampled trajectories are different settings.

**Information still needed**

- Check later continuous-time results for unrestricted smooth trajectories and arbitrary polynomial matrices.
- An algorithm must justify termination and any search bound in the stated signal space.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [On the Willems closure with respect to W_s](../sources.md#src-cross-604); [From 2D system to 1D system via restriction to a vertical strip: applications to time-controllability and zero-time-controllability](../sources.md#src-cross-800).

**Exact locator:** Problem 59, section 59.1, pp. 4–6; Amol J. Sasane

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could compare module-theoretic criteria and verify small symbolic examples. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check the smooth function space, both trajectory quantifiers and the uniform transition time. Symbolic examples cannot establish a universal characterization or an algorithm termination claim.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The original target uses unrestricted smooth continuous trajectories. Bharti and Pal (2026) give discrete two-dimensional criteria, not a resolution of this signal-space formulation. The general smooth case remains unverified here.

**Search scope:** Inspected the original formulation in the editor-hosted MTNS collection and the identified later paper. Targeted searches compared model assumptions and the claimed output; this is not an exhaustive status review.

<details>
<summary>Previous indexed wording</summary>

Characterize time-controllability of smooth PDE behaviors by their polynomial kernel matrix R.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 59, section 59.1, pp. 4–6; Amol J. Sasane. Checked the original assumptions and target.
- [From 2D system to 1D system via restriction to a vertical strip: applications to time-controllability and zero-time-controllability](../sources.md#src-cross-800) — 6 October 2026; Sections II, IV and V, Theorem 5, Proposition 7 and Algorithm 2. Proposition 7 and Algorithm 2 address scalar autonomous discrete behaviors; the algorithm takes a known H_max. These restrictions prevent treating it as a solution of the smooth target.

**Limits and remaining work**

- Check later continuous-time results for unrestricted smooth trajectories and arbitrary polynomial matrices.
- An algorithm must justify termination and any search bound in the stated signal space.
- No independent proof audit or comprehensive present-status assessment was performed.

<details>
<summary>Search queries</summary>

- "time-controllability" smooth algebraic test solved
- "time-controllability" "2026"
- "Sasane" "time-controllability"


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The smooth signal-space statement is identifiable. The inspected 2003 paper concerns W_s and does not establish a resolution for unrestricted smooth trajectories.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 59, section 59.1, pp. 4–6; Amol J. Sasane. Identifies the historical target.
- [On the Willems closure with respect to W_s](../sources.md#src-cross-604) — Discussion of time-controllability, p. 230; IMA Journal of Mathematical Control and Information 20, 217–232. Discusses the outstanding algebraic time-controllability question in a spatially tempered signal space.

**Limits and remaining work**

- Trace later results for C-infinity trajectories, rather than discrete or spatially tempered behaviors.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "time-controllability" smooth algebraic test solved


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
