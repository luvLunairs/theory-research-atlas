> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Scoped mathematical audit of the small-seed analytic branches

18 October 2026. Local scientific review draft. Actual service-supplied model
identity, version and configuration are unknown. This is substantive same-team
AI work, requiring full-text human review and manual submission. It is not an
independent review, a machine-verification approval, or a novelty assessment.

## Scope and outcome

The target was to find logical gaps in the complete assigned small-seed
arguments, especially at their parameter endpoints and when AP factors
overlap. All eight assigned prose/table files below were read in full.
The universal arguments were rederived by residue and endpoint algebra.
The fixed arithmetic tables were additionally checked directly from their
printed Markdown by a new exact interval/ray calculation. No existing file
was changed, and no new greedy sequence or parameter census was generated.

**No unresolved substantive mathematical gap was found in the stated domains.**
Two wording qualifications are recorded below; neither changes a candidate
or a witness. Two excluded-parameter formula extensions have explicit
counterexamples. A shorter stable-tail coverage proof is supplied for the
first-seed-three zero-offset family.

This conclusion covers membership identification and eventual periodicity.
It does not establish least periods, exact preperiods, historical priority,
fresh literature completeness, or the correctness of unassigned branches.

## Exact examined versions

Paths in this table are relative to `work/greedy-analytic-20261018/`.
Line numbers are one-based. The full ranges include attribution/status prose.

| File and complete read span | SHA-256 |
| --- | --- |
| `small/f2-two-classes.md`, 1–198 | `58952EBFE91BBEAE69171C3CB1C3FB0CA427F0CFFD630546DA0699EB045D9D01` |
| `small/f2-three-blocks.md`, 1–256 | `BFD5C4A873A76ED9F9B87C8414F3388F360D5D5C14179D4F049724D2BD2A4AEC` |
| `finite-small.md`, 1–201 | `1B44F75E8D6E3F188562EB9AA3E096A19B58FA5714C0E775B3BE7123AD81E1EA` |
| `small/f3-one.md`, 1–213 | `6F4777F5BD7F0E50E7C3DC802814251B1F3B4A5D231D9A1CFC4E6B26D6E746CA` |
| `small/f3-zero.md`, 1–293 | `4C9F03D478E233F60C1BCC4343EA8DA511F14C8A748E90D35E83874BFE23B243` |
| `even-multiples/small-boundaries.md`, 1–224 | `0256808BC32E1B087EBBE5BE7F07A48423F13C591A01B8000B8D79AD012D702E` |
| `even-multiples/boundary-lifetime-tables.md`, 1–54 | `FD63BC4147C25F74652D1EEB0F3FB55F6B8D576C1AB3586FDDF68BF811CFEA3E` |
| `even-multiples/boundary-arithmetic-tables.md`, 1–378 | `FB98BC5A1FB8ED51ADFCEB495B58B17439AC11F00B8B23E152ACC4D258180A39` |

The checks are against these printed definitions, not the earlier generators'
private data structures or pass flags. The older formulas and source credit
remain those linked in the examined files. Their attribution to van Berkel
and Bosma and the parent's source review are retained; this scoped audit
does not repeat or strengthen the parent's literature claim.

## Universal first-seed-two families

### Two classes, odd parameter w>=5

In `f2-two-classes.md`, lines 31–55 specify a positive candidate containing
exactly the two seeds below the second seed. The two possibilities
`e=w+1` and `e=w-1` produce precisely the claimed second-seed classes.
At w=5 the interval X without its last point is a singleton, not empty.

Lines 57–91 correctly reduce exclusion to the three ordinary core pair
types, the two mixed types involving u=2w, and protection of u itself.
Ordinary core sums are deliberately allowed to repeat a residue: this is
safe for exclusion and protects different actual block translates too.
The exceptional u occurs only once, so its self-pair is unavailable. Two
distinct initial odd summands begin at w and w+4, above the forbidden
endpoint double w+w. There is no missing selected-target case.

Lines 93–113 cover the four initial congruence classes. The possible
shortest join in class zero is controlled by `2e+4<=2w+6`, with step four.
Both relevant self-pair intervals have at least two input terms at w=5.
Lines 115–181 handle the first positive block separately where necessary.
In particular `u+(X without u)` is strict even at w=5, and the truncated
initial O self-sum is repaired by `2+O[1]`. Every other cross pair is either
in different blocks or in disjoint even/odd supports. The four offset
classes partition the entire block, including offset zero when present.

### Two further classes, h>=4 and a in {7,9}

In `f2-three-blocks.md`, lines 17–47 give the correct parameter conversion,
block bounds, positivity and seeds. Lines 49–70 contain all ten core pair
types. Recomputing both endpoints and subtracting m gives the stated
exclusions; the tightest displayed bound is
`m-max(A+A)=4h-a-4>=3`, attained at h=4,a=9.

Lines 72–140 correctly isolate v, the interval I, and the second occurrence
of z=min I. All nine mixed intervals were recalculated. The two relevant
strict exceptional sums hit only the missing A entries in blocks one and
two. At h=4, I has two terms, so its strict sum remains a genuine singleton.
The candidate `m+z` equals twice min C for every parameter in the family;
that tempting obstruction is forbidden, whereas the least distinct C pair
is `m+z+4`. The separate cross-block lower bounds exclude all other ways of
representing that target. This is a real use of strict distinctness.

Lines 142–160 cover every initial omission. Lines 162–237 cover all four
classes in every positive block. The low odd-class self-sums and the high
C self-sum need the stated n=1 repairs; later pairs have different actual
blocks. In the other odd class the shortest n=1 join has difference zero
or four, precisely one AP step. No overlap diagonal is silently restored.

## First-seed-three parameter families

### Offset one, k>=2

In `f3-one.md`, lines 9–44 define the candidate and sufficient start.
All fifteen ordinary core rows at lines 48–74 and twenty mixed rows at
lines 76–90 were recalculated, including their carries modulo `24k+3`.
The residue shift by three is essential and is used consistently.

Lines 92–124 correctly account for all exceptional-exceptional collisions
and protect the exceptional targets. At k=2, u=30 belongs to A, and the
strict Z self-sum intersects A in {36}; the corrected maximum at lines
95–107 handles that boundary. It does not incorrectly suppress the
selected u=30. The block-one extra is 30k, and the same-block/cross-block
case split excludes every possible representation.

All initial coverage rows at lines 126–145 and all positive-block identities
at lines 147–195 were recalculated. In the row `E[1]+B[n-2]`, n=3 puts
both factors in block one, but their residue classes are different, so
they are still distinct. In the class-two row, two copies of B have
different actual blocks, and their endpoint doubles must remain. At k=2,
D is a singleton; every claimed source interval and endpoint join remains
valid. The written omissions are exactly the block complements.

### Zero offset, k>=5

In `f3-zero.md`, lines 9–39 provide the correct six-residue row convention.
Lines 41–93 were checked by recomputing all 55 unordered pairs of the ten
envelope components, including both possible block carries. The ten listed
core collisions are complete. In each, the contributing portions are
outside the periodic core. The lifetime checks at lines 95–120 exclude
every selected core target.

For lines 122–167, the full strict carried sum of the seven initial
components was recomputed. Its six row unions agree exactly with lines
136–141. The block-zero/block-one and block-one/block-one alternatives
were checked separately, including the target `2m+2`. In particular the
uncarried class-two sums end at most at row `4k-2` or begin at least at
`5k-1`, so they cannot represent its required row `4k`.

Lines 169–270 contain an exhaustive coverage partition, first outside H
and then inside H. All displayed interval endpoints, isolated witnesses,
source lifetimes and joins were checked. The least parameter k=5 is
needed when the block-one F endpoint `4k-3` is used: it coincides with
the start `3k+2` of the high selected component. The initial Z and G
progressions overlap, so their restricted cross sum ends at row `2k-2`,
not `2k-1`. The retained `3[0]+B[1]` repair supplies that last omission.
The block-one x pair uses its two different rows k,k+1; the separate
s[1],u[1] pair consists of two different actual integers.

The new [stable-tail note](f3-zero-tail.md) replaces only the n>=4 coverage
with eleven literal gap rows and eighteen cross-block identities. All
factors have automatically different block indices. In residue two, the
three intervals

    [k-1,2k-2], [2k-1,3k-1], [3k,4k-1]

tile the high gap exactly. In residue four, two full interval sums replace
the earlier isolated low-row repairs. Exclusion and blocks zero through
three remain separate, explicitly retained obligations. This simplification
does not change the candidate or claim a smaller onset.

## Fixed boundaries and exhaustive printed arithmetic

`finite-small.md` lines 19–53 give a complete direct proof for S(2,8).
The initial omissions and all five eventual residue witnesses were checked;
at n=3 the factor 9 is an explicit initial term, so no premature tail
assumption is used. Lines 55–186 give the other two fixed candidates.
Every triangular sum row, mixed row, initial witness and positive-block
witness was checked from the displayed P,R sets. This included all 46
eventual residue witnesses and their separate block-one repairs.

For `small-boundaries.md`, lines 10–48 correctly define the three infinite
sets from their lifetime tables and give sufficient starts 5m,2m,5m.
Lines 50–77 distinguish unequal residues, different components of a single
residue lifetime, and strict self-pairs of one component. Different
components are disjoint; their ordinary cross sum is therefore legitimate.
A singleton's strict self-sum is empty, while a ray's strict sum starts
at `2a+1+c`, not `2a+c`.

The entire containment argument at lines 79–149 and coverage argument at
151–192 were checked against both printed appendices. The separate parser
[printed_audit.py](printed_audit.py) reads those final Markdown tables,
recomputes all full interval/ray sums without an upper block cutoff, and
compares every printed Q lifetime and every claimed contributor list.
It also checks each matrix cell, all ray witnesses, all early repairs,
the exact first required block `max(0,floor((g-r)/m)+1)`, seeds, and
global disjointness/complementarity. It imports none of the old generators.

| Second seed g, first seed 3 | Matrix cells | Nonempty unordered residue-pair lifetimes | Exceptional pairs hitting R | Pairs hitting exceptional targets | Ray witnesses | Early repairs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 12 | 6 | 26 | 2 | 4 | 9 | 1 |
| 18 | 238 | 554 | 7 | 30 | 89 | 1 |
| 24 | 272 | 553 | 18 | 54 | 63 | 9 |

The same parser checks the printed fixed S(2,11),S(2,12) arithmetic:
18 triangular rows, four mixed rows, 23 initial witnesses and 46 all-block
witnesses, each with its separate block-one representation. These counts
describe the actual final calculation, not an independent validation.

## Findings, corrections and attempted refutations

1. **The unchanged f2 three-block formula cannot be extended to h=3.**
   For either a=7 or 9, it would select v=12, the block-one member
   `m+min J=m+a`, and the extra `m+z=m+a+12`. The first two are
   different and sum to the third. This explains the retained failures
   `12+38=50` and `12+42=54` uniformly. It is a counterexample to that
   extended membership formula, not to eventual periodicity.
2. **The unchanged f3 zero-offset formula cannot be extended to k=4.**
   It would select `s[1]=96+10=106` and A[3] row 9, the integer
   `3*96+54=342`. Their sum 448 is the proposed F[4] row 10,
   `4*96+64`. This is the envelope x+s collision excluded by k>=5.
   The lower bound is therefore structural for this formula. No claim
   that these are the actual earlier greedy terms is needed for the
   internal-consistency obstruction.
3. **Allowing equal actual summands creates false objections.** The
   parser deliberately repeated that invalid variant and retained its
   selected-target collisions in [printed-results.json](printed-results.json).
   Examples include 12+12=24 for S(3,12), 18+18=36 for S(3,18), and
   24+24=48 for S(3,24). These are forbidden diagonals, not counterexamples.
   The valid distinct occurrences 24 and 120 instead represent 144,
   the block-one omission at residue 48 in the last case.
4. **Two harmless wording qualifications should accompany a polished
   presentation.** In `f2-three-blocks.md` lines 82–83, “the singletons
   used here” should mean s and v, since z is explicitly a member of I;
   the proof already treats the two occurrences of z correctly. In
   `f3-zero.md` lines 267–270, the summary of same-residue exceptions
   should explicitly include the s[1],u[1] pair as well as the two-point
   x[1] pair. The next sentence already says s[1] and u[1] are different.
   Neither wording issue invalidates a calculation, and no sealed file
   was edited.

The new stable-tail note initially miscounted its eighteen factor identities
as nineteen. Rereading and counting the displayed rows corrected that
description; no mathematical formula changed.

## Actual checks and trust boundary

The supporting artifacts are bound as follows:

| Artifact | SHA-256 |
| --- | --- |
| `f3-zero-tail.md` | `7F202D6B53E8264F4C1E8F5C3220B64D6805CD3E05206EC1769E7B3CE662E8A0` |
| `printed_audit.py` | `8DFCB098562C01AD86E404F27DEBCA8AA00B2B7C587B488B65E2FF6F58D6E84F` |
| `printed-results.json` | `A84303A29ABD7D0A7203534D75CD552100C9DD9578E7D01B2C7D3AE513D1C1F3` |

The parent contributor also read the complete new tail note and rederived
all eighteen identities, eleven complement gaps, joins and source lifetimes;
no gap was reported. This is a further same-team reading, not independent
review or approval.

The final printed-table checker passed and reported **0.015625 process CPU
seconds**. The earlier narrower pass also reported 0.015625 seconds; the
two measured checker runs total 0.03125 seconds. The checker used Python
3.12.14. No memory measurement was taken.

The report binds its exact inputs and checker by SHA-256. The checker uses
integer finite endpoints and an infinity sentinel for entire rays; it does
not truncate to a finite block prefix. Its parser, arithmetic code and this
same-team mathematical reading remain a trust boundary. The written proofs
do not acquire independent or formal approval from this audit. A repository
rendering run was not used as scientific evidence.

Checked: the eight exact source versions above; the new stable-tail proof;
the printed-table checker and its retained final report.
Results: full assigned prose/table coverage, no unresolved substantive gap,
two wording qualifications, two sharp-domain formula obstructions, and the
explicit stable-tail simplification. Limits: no fresh source/priority audit,
least-period review, independent scientific review, formal verification or
human screening. Outcome: contributor audit; full-text
human review and manual submission remain required. Original prose/data use
CC BY 4.0 and code uses MIT under the repository terms.
