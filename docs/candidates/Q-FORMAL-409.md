# Minimum-stabbing triangulation complexity

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-409 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-409%3A+Minimum-stabbing+triangulation+complexity&target=Q-FORMAL-409) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-409%3A+Minimum-stabbing+triangulation+complexity&target=Q-FORMAL-409)

Determine the complexity of finding a straight-line triangulation of a finite planar point set that minimizes the maximum number of edges intersected by any line. Intersections at edge endpoints count; the triangulation uses the given points without adding vertices.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-10-15.

**Status basis:** Ribeiro's 2016 dissertation, Chapter 4, Theorem 4.2, states an NP-hardness proof for general stabbing lines and the same point-set triangulation objective. This supersedes the historical TOPP question. The dissertation proof was not independently audited here; journal acceptance and later errata were not established.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP's older question is superseded by a 2016 dissertation theorem.

**Scope limits:** General-line stabbing counts edges, including endpoint contacts. Changing the input to a polygon, adding Steiner vertices or asking for a constant-factor approximation changes the problem.

**Information still needed**

- Independently audit the geometric reduction, including collinear vertices and endpoint incidences.
- A final journal version or errata have not been located.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [The Open Problems Project: Problem 20](../sources.md#src-formal-409); [Finding Geometric Structures with Minimum Stabbing Number](../sources.md#src-formal-603); [Computing Triangulations with Minimum Stabbing Number](../sources.md#src-review-803).

**Exact locator:** TOPP Problem 20, Partial and Related Results; Ribeiro (2016), Chapter 4, §§4.1 and 4.4, Theorem 4.2.

**Potential difficulty:** Unknown. The original complexity question has a reported NP-hardness proof in Ribeiro's 2016 dissertation; it is retained as a historical problem. The effort needed to audit that proof has not been assessed.

**Possible AI role:** Reconstruct the published hardness reduction and produce exact incidence checks for its gadgets. Novel approximation work would require a separately stated target.

**Verification burden:** High. Check the reduction's two directions, coordinate encoding length and worst stabbing line. Degenerate contacts must use the stated counting convention; drawings alone are insufficient.

**Resource expectations:** Proof review and exact arithmetic need no external dataset. A small gadget implementation may be feasible on a workstation, but neither its workload nor the proof-audit effort has been measured.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** No model or implementation has been tested. The dissertation proof has not been independently audited here, and subsequent publication or errata remain unverified.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Reported resolved → Reported resolved.

The hardness result counts endpoint contacts. Polygon triangulations, Steiner vertices and approximation guarantees define separate problems.

**Search scope:** Compared TOPP with the dissertation's definition and theorem; inspected a 2017 author's workshop paper for subsequent citation and variant boundaries.

<details>
<summary>Previous indexed wording</summary>

Determine the complexity of a straight-line triangulation of a planar point set minimizing the maximum number of its edges intersected by any line.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Finding Geometric Structures with Minimum Stabbing Number](../sources.md#src-formal-603) — §4.1, printed p. 55; Theorem 4.2, printed p. 70. The definition counts endpoint contacts, and the theorem treats unrestricted stabbing-line directions.
- [Computing Triangulations with Minimum Stabbing Number](../sources.md#src-review-803) — Introduction and reference 9. Cites the triangulation hardness manuscript while studying a distinct polygon variant.

**Limits and remaining work**

- The later citation is not an independent proof audit. A formally published final version and errata remain unconfirmed.

<details>
<summary>Search queries</summary>

- "On triangulations with minimum stabbing" Fekete Ribeiro Souza
- Fekete Ribeiro Souza triangulations stabbing number 2016 2018 2020
- "On Triangulations" "Stabbing" "Ribeiro"


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Reported resolved.

Ribeiro's 2016 dissertation, Chapter 4, Theorem 4.2, states an NP-hardness proof for general stabbing lines and the same point-set triangulation objective. This supersedes the historical TOPP question. The dissertation proof was not independently audited here; journal acceptance and later errata were not established.

**Search scope:** Compared TOPP's remaining triangulation question with the later dissertation's general-line theorem; distinguished polygon and axis-parallel variants.

**Inspected evidence**

- [The Open Problems Project: Problem 20](../sources.md#src-formal-409) — TOPP Problem 20: Partial and Related Results, remaining triangulation question. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Finding Geometric Structures with Minimum Stabbing Number](../sources.md#src-formal-603) — Chapter 4, Section 4.4, Theorem 4.2, printed p.70. The theorem proves NP-hardness for the same point-set triangulation objective over arbitrary stabbing lines.

**Limits and remaining work**

- The reduction has not been independently re-proved; subsequent journal publication and errata were not traced exhaustively.

<details>
<summary>Search queries</summary>

- "minimum stabbing triangulation" solved
- "On triangulations with minimum stabbing" Piva


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
