# Finiteness of planar six-body central configurations for fixed positive masses

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-326 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-326%3A+Finiteness+of+planar+six-body+central+configurations+for+fixed+positive+masses&target=Q-MODEL-326) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-326%3A+Finiteness+of+planar+six-body+central+configurations+for+fixed+positive+masses&target=Q-MODEL-326)

For every fixed ordered positive mass vector (m1,...,m6), are there finitely many collision-free planar Newtonian central configurations modulo translation, rotation and positive scaling? In center-of-mass coordinates they satisfy sum_i m_i q_i=0 and sum_{j≠i} m_j(q_i−q_j)/|q_i−q_j|^3=lambda q_i with lambda>0.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** Two 2026 preprints report progress for six bodies. Tomar claims finiteness outside a proper algebraic subset of positive masses. Chen and Tong leave finiteness on exceptional loci to a sequel. Neither inspected six-body source covers every positive mass vector.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-26 literature check identifies the publications, versions and limits covered.

**Scope limits:** The target quantifies over every ordered positive mass vector, including exceptional ones. A sufficient genericity condition need not describe which excluded vectors actually have finitely many configurations.

**Information still needed**

- Check exceptional mass vectors directly and look for a completed sequel addressing them.
- The reported Lean formalization has not received a project check against the indexed statement.

**Primary branch:** [Celestial dynamics](../domains/astro.md#astro-dyn). **Related branches:** [Classical mechanics and continuum theory](../domains/phys.md#phys-classical), [Dynamical systems and ergodic theory](../domains/math.md#math-dyn).

**Sources:** [Toward Finiteness of Central Configurations for the Planar Six-Body Problem by Symbolic Computations. (II) Determine Mass Relations](../sources.md#src-model-318); [Smale's sixth problem for five bodies in the plane, with a proof formalized in Lean](../sources.md#src-model-319); [Finiteness of planar central configurations of six bodies for all positive masses: Part I, exceptional-mass first limits](../sources.md#src-phys-900); [Smale's sixth problem for six bodies in the plane: finiteness of central configurations for generic masses, with a proof formalized in Lean](../sources.md#src-phys-901).

**Exact locator:** Chang and Chen (2025), abstract. Chen and Tong, Part I (2026), abstract. Tomar, six-body preprint abstract and five-body preprint v2.

**Potential difficulty:** Frontier. All positive mass vectors include exceptional algebraic loci; generic-mass elimination is insufficient.

**Possible AI role:** An assistant could audit exact elimination certificates and help isolate a specific remaining diagram once its full definition is reviewed.

**Verification burden:** High. Check real positivity, collision exclusion and quotient symmetries; finite complex counts for generic masses do not prove the target.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy. Symbolic elimination may require substantial memory; no bounded diagram or hardware budget is yet selected.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model was evaluated. This is a method-based forecast, not a measured success rate; a narrower task and a specialist literature check are required before a research attempt. The detailed Part II diagrams need full-text inspection before promotion to a complete card.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Record the generic six-body results and retain source-reported openness for the all-masses problem.

**Search scope:** The target quantifies over every ordered positive mass vector, including exceptional ones. A sufficient genericity condition need not describe which excluded vectors actually have finitely many configurations.

**Inspected evidence**

- [Toward Finiteness of Central Configurations for the Planar Six-Body Problem by Symbolic Computations. (II) Determine Mass Relations](../sources.md#src-model-318) — Publisher abstract. Uses symbolic elimination to obtain necessary mass relations for a number of six-body diagrams.
- [Finiteness of planar central configurations of six bodies for all positive masses: Part I, exceptional-mass first limits](../sources.md#src-phys-900) — Abstract, closing sentences. The authors give a reduction and defer finiteness for exceptional positive mass vectors.
- [Smale's sixth problem for six bodies in the plane: finiteness of central configurations for generic masses, with a proof formalized in Lean](../sources.md#src-phys-901) — Author's preprint abstract. Asserts generic finiteness. The exceptional set includes mass vectors with three equal components or one component equal to the sum of two others.
- [Smale's sixth problem for five bodies in the plane, with a proof formalized in Lean](../sources.md#src-model-319) — v2 abstract and submission history. The separate all-positive-mass claim has five bodies. Version 2 changed the preprint title.

**Limits and remaining work**

- No proof, certificates or Lean build were checked independently. The exceptional sets in the two papers were not identified with one another.

<details>
<summary>Search queries</summary>

- Six-body planar central configurations fixed masses generic masses Hampton Moeckel finiteness 2025 Chang Chen Smale all six bodies central configurations six exceptional cases 2026
- six body central configurations Chen Tong Part II exceptional positive mass loci six fixed positive masses finiteness November 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
