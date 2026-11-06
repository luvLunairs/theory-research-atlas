# Exact capacity of the independent binary deletion channel

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-328 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328)

Determine the Shannon capacity C(d) in bits per input bit of the binary channel that independently deletes each input bit with probability d∈(0,1), preserves the order of surviving bits and does not reveal deletion locations, without feedback.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The inspected September 2026 run-length paper retains the exact-capacity question and reports additional lower bounds. These results and the previously indexed enclosure remain source-reported computations, not independently replayed project benchmarks.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Run-length paper first submitted 21 September 2026; inspected version 2, 26 September 2026, which corrects the VTR chain penalty and replaces double-precision evaluation with reported interval enclosures. Prior enclosure and replay limitations retain their 20 October 2026 scope.

**Scope limits:** Retains the exact no-feedback capacity C(d). Compared the newer run-length lower bounds with the existing enclosure; source-family optimization gives achievable rates, not a converse or exact capacity.

**Information still needed**

- Independent scrutiny of both recent preprints and complete numerical replay.
- Availability and reuse permission for all required numerical inputs.
- Check full-precision bounds at the chosen deletion probability before claiming an improvement.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [Binary Deletion Channel Capacity to Within One Hundredth of a Bit](../sources.md#src-formal-318); [Binary deletion-channel capacity: verification materials](../sources.md#src-impact-009); [Improved Lower Bounds on the Capacity of the Binary Deletion Channel via a Learning Approach to Run-Length Inputs](../sources.md#src-math-810).

**Exact locator:** SRC-FORMAL-318, Sections 1.2, 2 and 14.3; SRC-IMPACT-009 README; Khodaiemehr-Feng-Duman v2, Theorems 1-2, Lemma 8, Section VI-C and Table IV

**Potential difficulty:** High. The source leaves both source optimality and converse tightness unsettled.

**Possible AI role:** The published computation supplies concrete methods and checking obligations. Reviewing its assumptions and obtaining complete inputs should precede a new attempt. No named model evaluated.

**Verification burden:** High. High: an information theorist must review the reduction, while numerical evidence needs an independent replay.

**Resource expectations:** No estimate has been measured. Small analytic and certificate checks can be separated from large finite-window enumeration, whose state count grows exponentially. Full source replay requires specialist numerical infrastructure.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** No project research attempt or model evaluation has been performed. Published attempts do not establish a success probability for this task.

[Read the full card](../cards/Q-FORMAL-328.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Add the second numerical approach while retaining the existing half-deletion benchmark and its replay limitations.

**Search scope:** Retains the exact no-feedback capacity C(d). Compared the newer run-length lower bounds with the existing enclosure; source-family optimization gives achievable rates, not a converse or exact capacity. Checked the arXiv version history and the September 26 correction rather than carrying forward the original numerical method.

**Inspected evidence**

- [Improved Lower Bounds on the Capacity of the Binary Deletion Channel via a Learning Approach to Run-Length Inputs](../sources.md#src-math-810) — Version 2: Section I revision comparison; Theorems 1-2; Lemma 8; Section VI-C and Table IV. Reports run-length achievable rates after a chain-penalty correction and interval evaluation; the half-deletion rate remains below the previously indexed lower endpoint.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "binary deletion channel" "capacity" "2026"
- "2609.24908" correction OR capacity


</details>

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

No exact-capacity resolution or correction was located in the focused search; the author's repository exposes a replay-availability limitation.

**Search scope:** Primary passages, current metadata and linked maintained records, followed by targeted later-result searches through 2026-10-20.

**Inspected evidence**

- [Binary Deletion Channel Capacity to Within One Hundredth of a Bit](../sources.md#src-formal-318) — Sections 1.2, 2, 12-14; Table 1. Exact capacity remains unknown; Table 1 reports outward-rounded bounds at d=1/2.
- [Binary deletion-channel capacity: verification materials](../sources.md#src-impact-009) — README: portable checks, full calculation and reuse terms. Distinguishes checking stored enclosure assembly from numerical replay; lists incomplete availability of large inputs.

**Limits and remaining work**

- Search coverage is bounded. No mathematical proof, code or numerical certificate was independently verified.

<details>
<summary>Search queries</summary>

- "binary deletion channel" "capacity" "2026" "October"
- "deletion channel capacity" "Papailiopoulos" correction
- "2609.19412" correction


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
