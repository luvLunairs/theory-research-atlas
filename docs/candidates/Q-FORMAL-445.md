# Tight instance-optimal identity testing

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-445 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-445%3A+Tight+instance-optimal+identity+testing&target=Q-FORMAL-445) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-445%3A+Tight+instance-optimal+identity+testing&target=Q-FORMAL-445)

For a known probability distribution q on a finite domain and epsilon in (0,1], find a succinct functional Phi(q,epsilon) that characterizes, up to universal constant factors, the least number of independent samples from an arbitrary unknown p needed to distinguish p=q from TV(p,q)>epsilon, with each error probability at most 1/3. The source asks ideally for a closed form or efficient computation from explicit q; this succinctness criterion is not fully formalized.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The COLT 2024 source poses this fixed-q, fixed-epsilon sample-complexity target. Its warning about constant changes to epsilon is essential: existing bounds can differ by arbitrarily large multiplicative factors. The scoped search did not establish a solution to Question 1; a located 2026 claim addresses only the different lower-bound repair in Question 3.

**Statement check:** Needs clarification. **Status check:** Later literature checked.

**Source date and freshness:** COLT 2024 problem note; later keyword search on 6 November 2026.

**Scope limits:** The target is sample complexity at the same epsilon, not merely the optimal separation radius up to constants or worst-case complexity over all reference distributions. Question 3 is a separate proof repair.

**Information still needed**

- Adopt a precise class of admissible succinct functionals before claiming a negative result or a complete characterization.
- A source establishing the present resolution status of Question 1 remains missing.

**Primary branch:** [Inference and decision theory](../domains/stat.md#stat-infer). **Related branches:** None recorded.

**Sources:** [Open Problem: Tight Characterization of Instance-Optimal Identity Testing](../sources.md#src-formal-442).

**Exact locator:** Canonne (2024), Section 1; Sections 2-3, epsilon-dependent gaps; Section 5, Open Question 1.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Compare the epsilon dependence of known functionals and explicit reference distributions; clarify the desired functional class before attempting a characterization.

**Verification burden:** High. Use one fixed finite-domain model, independent samples and the same epsilon in matching upper and lower bounds. Constant-factor rescaling of epsilon need not preserve a constant-factor sample bound.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The COLT 2024 source poses this fixed-q, fixed-epsilon sample-complexity target. Its warning about constant changes to epsilon is essential: existing bounds can differ by arbitrarily large multiplicative factors. The scoped search did not establish a solution to Question 1; a located 2026 claim addresses only the different lower-bound repair in Question 3.

**Search scope:** Read all five pages of the primary note, focusing on the finite-domain model, epsilon gap and separation of Questions 1-3. A later author-hosted Question 3 claim was inspected to classify its scope; it is not evidence of a Question 1 solution.

<details>
<summary>Previous indexed wording</summary>

Find a succinct functional of a known discrete distribution q and epsilon that characterizes, within constants, the samples needed to distinguish p=q from TV(p,q)>epsilon with error at most one third.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Tight Characterization of Instance-Optimal Identity Testing](../sources.md#src-formal-442) — Section 1; Sections 2-3; Section 5, Question 1. Defines the target and explicitly leaves succinctness incompletely formalized.

**Limits and remaining work**

- The targeted search is not comprehensive. No correctness or acceptance verdict was made on the separate 2026 Question 3 claim.

<details>
<summary>Search queries</summary>

- "instance-optimal identity testing" 2025 2026 Canonne solution
- "identity testing" "Open Question 2" "Canonne"


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [Open Problem: Tight Characterization of Instance-Optimal Identity Testing](../sources.md#src-formal-442) — Section 5, Open Question 1; section 1. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later results and a formal meaning of succinctness; the source itself notes this term is not fully formal.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "Tight Characterization of Instance-Optimal Identity Testing" solution


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
