# Constant-depth IPS lower bounds for unsatisfiable CNF families

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-314 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-314%3A+Constant-depth+IPS+lower+bounds+for+unsatisfiable+CNF+families&target=Q-FORMAL-314) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-314%3A+Constant-depth+IPS+lower+bounds+for+unsatisfiable+CNF+families&target=Q-FORMAL-314)

Exhibit an explicit unsatisfiable CNF family whose standard clause-polynomial and Boolean-axiom encoding requires superpolynomial-size constant-depth Ideal Proof System certificates over Q. An IPS certificate C(x,y) satisfies C(x,0)=0 and C(x,F(x))=1.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The source explicitly distinguishes this unresolved propositional task from lower bounds for purely algebraic instances.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-308: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Proof theory and constructive logic](../domains/logic.md#logic-proof). **Related branches:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit).

**Sources:** [AC⁰[p]-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](../sources.md#src-formal-308).

**Exact locator:** Lu et al., section 1.2 and Theorem 16.

**Potential difficulty:** Frontier. Known arithmetic circuit lower bounds do not supply the needed CNF certificate lower bound.

**Possible AI role:** Audit the Boolean-to-algebraic encoding and search for unintended short certificates in a bounded template.

**Verification burden:** High. Verify unsatisfiability and both certificate identities; prove the claimed bound for every fixed certificate depth.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
