# Pseudomodes for discontinuous complex potentials

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-408 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-408%3A+Pseudomodes+for+discontinuous+complex+potentials&target=Q-MODEL-408) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-408%3A+Pseudomodes+for+discontinuous+complex+potentials&target=Q-MODEL-408)

Extend semiclassical Schrödinger pseudomode constructions to discontinuous complex potentials beyond the Heaviside-type example discussed in §10.1.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-10-15.

**Status basis:** Krejčiřík and Siegl explicitly identify their 2019 paper as answering AIM Problem 10.1. Their method constructs large-energy pseudomodes for specified rough potentials using energy-dependent mollification. The answer does not cover arbitrary measurable potentials or every semiclassical scaling.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Sources: SRC-MODEL-401: 2015; SRC-MODEL-609: 2019. The 2026-10-14 check covers the scope recorded in the linked literature check.

**Scope limits:** The historical request for a technique has a published answer. Check the operator domain, spectral-parameter limit and potential class; a different limit requires a separate argument.

**Information still needed**

- Choose a potential covered by Assumption II and record every growth, regularity and mollification condition before reproducing the estimate.

**Primary branch:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral). **Related branches:** [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401); [Pseudomodes for Schrödinger operators with complex potentials](../sources.md#src-model-609).

**Exact locator:** AIM §10.1, David Krejčiřík; Krejčiřík–Siegl, Introduction, Assumption II, Theorem 4.9 and §4.4.

**Potential difficulty:** Unknown. The original question is resolved. Reproducing a particular asymptotic estimate remains a specialist task with unmeasured effort.

**Possible AI role:** Help check the hypothesis list and residual estimates for a chosen example in the published paper, with an analyst reviewing uniformity and remainder bounds.

**Verification burden:** High. Verify domain membership, nonzero normalization and a rigorously vanishing relative residual in the stated limit. Numerical residuals alone do not establish an asymptotic bound.

**Resource expectations:** No experiment or observational dataset is intrinsic. Symbolic differentiation and numerical checks can support analytic review; large spectral simulations are not required to inspect the proof.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** No named model has been evaluated. This forecasts conditional assistance with literature and proof review, not measured capability or a probability that the claim is correct.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Reported resolved → Reported resolved.

The published mollification construction answers AIM Problem 10.1 for the specified rough-potential classes and large-energy limit.

**Search scope:** Compared AIM §10.1 with the paper's explicit resolution statement, theorem assumptions and examples.

**Inspected evidence**

- [Pseudomodes for Schrödinger operators with complex potentials](../sources.md#src-model-609) — Introduction, p. 3; Theorem 4.9; §4.4. The authors connect their rough-potential construction to the workshop question.

**Limits and remaining work**

- No independent proof reconstruction or extension beyond the cited hypotheses was performed.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Reported resolved.

The original request for an extension to discontinuous potentials has a published answer. Its theorem hypotheses must be retained; no unrestricted measurable-potential extension is asserted.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401) — §10.1, David Krejčiřík. Original question or research direction located.
- [Pseudomodes for Schrödinger operators with complex potentials](../sources.md#src-model-609) — Introduction p. 3, 'Rough potentials'; Theorem 4.9. The published work explicitly states that its mollification construction solves AIM Problem 10.1 for the specified classes of discontinuous potentials.

**Limits and remaining work**

- Retain the mollification, growth and regularity hypotheses of Theorem 4.9; this is not a theorem for arbitrary measurable potentials.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- non self adjoint AIM 2015 open problems status Almog Boulton


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
