> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Findings of the strict analytic audit

18 October 2026. This is a contributor assessment of the revised
[candidate proof](manuscript.md), not an independent scientific verdict.
No unresolved membership or eventual-periodicity gap was identified in
the stated domains during the recorded readings. That is an assessment
with the scopes below, not a guarantee of correctness or novelty.

## Corrections incorporated in this version

The inherited candidate needed three wording corrections, made normative
in [errata.md](errata.md) while leaving the sealed files unchanged:
distinguish z from the disjoint residue components containing it; include
the same-block pair s[1],u[1] in the first-seed-three distinctness summary;
and call 8k the second seed, not the least seed, in the first-seed-four
exclusion argument. None changes a membership formula or parameter domain.

A genuine hypothesis defect was found in the **new consolidation**, before
handoff. The rectangle specialization of the cylinder sum formula cannot
be used on an empty input. For m=3, block interval [0,1] and residue
interval [1,0], the actual cylinder is empty, but the unguarded formula
returns {3,5}. [Framework Lemma 2](framework.md#2-block-coordinates-and-distinct-actual-integers)
now requires nonempty inputs and returns the empty set first otherwise.
The general set identity was unaffected. Ordinary endpoint addition now
has the same nonempty guard, and the feedback lemma states its activation
threshold n>=s_i explicitly. A second same-team reading checked the repair.

The new tail summaries initially counted eighteen and twenty-two identities
as nineteen and twenty-four respectively. The final text and arithmetic
reports use the corrected counts. These were description errors, not
changes in the displayed identities. The final integration also corrected
an intermediate sentence wrongly associating S(2,4) with the relaxed band;
that case is covered by its explicit elementary proof.
Another final wording correction limits automatic cross-block distinctness
to the 22 uniform first-seed-four identities. The 38 early gap rows
still require their original explicit distinctness checks, including
three strict self-pairs; the compression does not remove those checks.

## Counterexamples to stronger formulas

Each row below is a contradiction inside a proposed *extended candidate
set*. It is not a claim that all three numbers are actual greedy entries.
In particular none is a counterexample to eventual periodicity.

| Rejected extension | Exact obstruction | Consequence |
| --- | --- | --- |
| First-seed-two three-block formula at h=3 | For a=7, m=31, the formula selects 12,38,50 and 12+38=50. For a=9, m=33, it selects 12,42,54 and 12+42=54. | Keep h>=4; the omitted g=11,12 cases have separate fixed proofs. |
| First-seed-three zero-offset formula at k=4 | m=96; proposed s[1]=106 and A[3] row 9 is 342; their sum 448 is proposed F[4] row 10. | Keep k>=5; g=24 has a different fixed proof. |
| First-seed-four zero-offset formula at k=5 | m=161; 1006=6m+40 and 1167=7m+40 are distinct proposed tail terms, and their sum 2173=13m+80 is also proposed. | Keep k>=6; g=40 has a different fixed proof. |
| General offset-one formula extended to f=3,k=3 | m=52; proposed offsets 13 and 42 sum to m+3. The distinct proposed tail terms 169 and 198 sum to proposed 367. | The f>=4 relaxation cannot be lowered unchanged; the first-seed-three family uses its own argument. |

The detailed memberships are in the [small-seed audit](small/audit.md) and
[first-seed-four audit](four/audit.md). They explain why exceptional small
families remain necessary despite the common mechanisms.

Several tempting objections or shortcuts also failed:

- The equation 24+24=48 repeats one actual term and is inadmissible.
  In contrast 24+120=144 uses different actual terms of the same residue
  modulo 96 and is a valid omission witness. The proof treats these
  differently by exact lifetimes, not by deleting all residue doubles.
- Removing only extreme doubles from an interval sum fails for a
  singleton: {2} dotplus [1,3]={3,5}, with an interior missing point.
  The exact feasible-summand criterion handles this case.
- At the upper-interior boundary a=f-1 the endpoint obstructing the core
  coincides with the one point left by the partial-core anchor. The
  feedback mechanism no longer proves extinction. The separate boundary
  lemma is required; this is a failed proof extension, not a conjecture
  counterexample.
- A finite residue envelope alone does not force stabilization. The set
  {3*2^n+1:n>=0} lies in a single sumfree residue class modulo 3 but has
  unbounded gaps. It fails greedy coverage and only refutes that shortcut.
- The midpoint supersolution is an upper bound, not an asserted exact
  transient. Its causal comparison proof is retained instead of assuming
  equality or importing the acyclic-strip argument where it does not apply.

## What the revision simplifies

| Part of the proof | Revised mathematical structure | Retained necessary work |
| --- | --- | --- |
| Strict sums and all-block identification | Six common lemmas for feasible summands, cylinders, lifetimes, anchor lifting, acyclic extinction and causal comparison | Each family's actual seed guard, collision list and coverage identities |
| Odd multiples and upper boundary | One reflection lemma handles wrapped and unwrapped sums together | Unique actual exceptions and the original complete gap coverage |
| Even multiples | Explicit endpoint cutoffs followed by one cleanup step | Causal protection and the different-block lower bound |
| S(3,6k), k>=5 | Eleven stable gaps covered by eighteen cross-block identities | Exclusion and blocks zero through three |
| S(4,8k), k>=6 | One lemma on an independent parameter box; thirteen gaps and twenty-two cross-block identities for every n>=3 | Exclusion and 38 early gap rows; 51 gap rows overall instead of 103 |
| Four elementary known boundaries | Short complete exclusion-and-coverage arguments | Attribution to the original known results; no novelty claim |

No larger greedy census was run. The optional calculations recompute
the actual printed arithmetic and targeted strict-sum boundary examples.
The infinity symbols in lifetime arithmetic denote entire rays; no
finite-prefix success is used to infer a universal statement.

## Scope, limits and next steps

The exact reading scopes and findings are recorded in the [parent audit](root-audit.md),
[large-family audit](large/audit.md), [small-seed audit](small/audit.md)
and [first-seed-four audit](four/audit.md). These are coordinated readings
by the same AI team, not independent reviews. Supporting parsers remain
fallible code. Their reports are corroboration and are not proof premises.

The manuscript gives an exhaustive parameter partition and states the
eventual-periodicity conclusion as a complete **candidate** theorem. No
step is intentionally left as a program pass flag or an unproved finite
scan. Human full-text screening and independent mathematical assessment
are still pending. Least periods, optimal transients, general seed sets,
historical novelty and significance are outside the established outcome.
The [source record](literature.md) identifies the remaining historical
full-text gaps. The next step is human examination of the complete proof
and appendices, followed by manual submission of the reviewed version.
