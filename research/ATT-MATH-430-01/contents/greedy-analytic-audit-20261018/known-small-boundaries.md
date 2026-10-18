> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Explicit proofs for the four elementary cited boundaries

18 October 2026. These are attributed known cases, included to replace
an informal "easy to prove" citation by a complete argument. They are
not new research targets or new periodicity claims. Van Berkel and Bosma
state S(1,2), S(2,4) in [Example 13 of the period paper](https://arxiv.org/html/2609.18522v1)
and S(1,2), S(1,4), S(1,6) in [Remarks 12 of the companion paper](https://arxiv.org/html/2609.16843v1).
The exclusion and coverage proofs below are contributor-written. The
shared assistance note and manual-submission requirement apply.

## A single argument for S(1,2) and S(2,4)

Let a be 1 or 2 and put T={2a} union {a+3q:q>=0}. Its entries
at or below 2a are exactly the two seeds. Two recurring entries have
residue 2a modulo 3, and a recurring entry plus the exception 2a
has residue zero. Neither can hit the recurring class a. The only
way two recurring entries could hit the actual exception 2a is a+a,
which repeats one term. The exception also cannot pair with itself.
Thus T has no strict sum in T.

Every omitted x>2a of residue 2a is x=2a+3q, q>=1, represented
by a+(a+3q). Every omitted multiple 3q>2a is represented by
2a+(3q-2a). Its second summand is positive, congruent to a modulo 3,
and at least a. The summands cannot be equal because 3 does not divide
4a. These cover the two complement classes. The global criterion
therefore identifies T with S(a,2a), of eventual period 3.

## S(1,4)

Put m=12 and T={8} union {12q+r:q>=0,r in {1,4,6,11}}.
The seed guard is immediate. The ten unordered ordinary sums of
recurring residues, reduced modulo 12, are

    2,5,7,0,8,10,3,0,5,10.

None is recurring. The only recurring-pair hit at the actual extra
8 would be 4+4, which is inadmissible. Adding 8 to a recurring
residue gives 9,0,2,7 modulo 12, also outside the recurring set;
these positive sums cannot equal 8. The self-pair 8+8 is forbidden.
This proves exclusion. All omissions above the second seed are
covered in the following table:

| Target | Range | Distinct selected factors |
| --- | --- | --- |
| 12q | q>=1 | 8 + (12(q-1)+4) |
| 12q+2 | q>=1 | 8 + (12(q-1)+6) |
| 12q+3 | q>=1 | 4 + (12(q-1)+11) |
| 12q+5 | q>=0 | 1 + (12q+4) |
| 12q+7 | q>=0 | 1 + (12q+6) |
| 12q+8 | q>=1 | 4 + (12q+4) |
| 12q+9 | q>=0 | 8 + (12q+1) |
| 12q+10 | q>=0 | 4 + (12q+6) |

Different residues ensure distinctness except in the residue-eight
row, where different blocks do so. The missing q=0 residue-eight
case is the selected exception. The global criterion proves the formula.

## S(1,6)

Put m=9 and T={12} union {9q+r:q>=0,r in {1,6,8}}.
Its entries at or below 6 are exactly 1 and 6. The six ordinary recurring
pair residues are 2,7,0,3,5,7, all outside {1,6,8}. The only
way to hit the actual extra 12 is 6+6, inadmissible. Adding 12 to
the three recurring classes gives 4,0,2 modulo 9 and cannot hit 12.
The extra's self-pair is also inadmissible. Thus exclusion holds.

| Target | Range | Distinct selected factors |
| --- | --- | --- |
| 9q | q>=1 | 1 + (9(q-1)+8) |
| 9q+2 | q>=1 | 1 + (9q+1) |
| 9q+3 | q>=2 | 6 + (9(q-1)+6) |
| 9q+4 | q>=1 | 12 + (9(q-1)+1) |
| 9q+5 | q>=1 | 6 + (9(q-1)+8) |
| 9q+7 | q>=0 | 1 + (9q+6) |

These are precisely the omitted classes above 6; the exception 12 is
the omitted q=1 instance of the residue-three row. Equal-residue
factors occur only in the second and third rows, whose q bounds give
different blocks. All other factors have different residues. Positivity
and the global criterion finish the proof. QED.

No computational continuation is used. These four explicit base proofs
remove reliance on informal continuation dots while preserving attribution.
