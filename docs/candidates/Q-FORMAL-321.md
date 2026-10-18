# Polynomial-time learning parity with constant random classification noise

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-321 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-321%3A+Polynomial-time+learning+parity+with+constant+random+classification+noise&target=Q-FORMAL-321) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-321%3A+Polynomial-time+learning+parity+with+constant+random+classification+noise&target=Q-FORMAL-321)

For each fixed noise rate 0<η<1/2, can an unknown parity on n bits be recovered with high probability in polynomial time from polynomially many pairs (x,〈s,x〉 mod 2 XOR e), where x is uniform and e is independent Bernoulli(η)?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The sources treat polynomial-time LPN as unresolved and its hardness as an assumption; recent worst-case reductions remain conditional.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-307: 2025, SRC-FORMAL-312: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Computational learning theory](../domains/cs.md#cs-learn). **Related branches:** [Cryptographic foundations](../domains/cs.md#cs-crypto).

**Sources:** [The Probably Approximately Correct Learning Model in Computational Learning Theory](../sources.md#src-formal-307); [Towards Worst-case Hardness for Low-Noise LPN](../sources.md#src-formal-312).

**Exact locator:** Servedio, section 3.3; Aggarwal et al., abstract and September 2026 revision.

**Potential difficulty:** Frontier. Noise breaks exact linear-algebra recovery, and unconditional hardness is also unavailable.

**Possible AI role:** Verify distribution transformations and test proposed decoding improvements under a predeclared bounded instance size.

**Verification burden:** High. A success probability and uniform polynomial runtime require proof; restricted statistical-query lower bounds do not rule out all algorithms.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
