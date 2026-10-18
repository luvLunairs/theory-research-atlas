> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Direct boundary proofs for S(2,8), S(2,11), and S(2,12)

18 October 2026. Local scientific draft for full-text human review and
manual submission. These are explicit infinite-set arguments, not claims
that a long computed prefix proves periodicity. The formulas originate
in the retained [small-seed tables (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
They replace the three corresponding fixed program certificates.
The fourth previously exceptional seed, g=7, is covered by the relaxed
band proof in [small-domain-extensions.md](small-domain-extensions.md).
Known g=3,4 retain their attribution to van Berkel and Bosma.

All sums are of distinct actual entries. We use the positive-set
identification lemma: a positive set containing exactly the two seeds
at or below the second seed is the greedy set if no selected entry is
a distinct selected sum and every omitted larger integer is such a sum.
Each summand is smaller than its positive sum, so this is induction on
the integer being decided.

## A two-residue tail for S(2,8)

Put

    T={2,8,9,12,13} union union_(n>=2)(7n+{2,5}).

Its recurring residue set is R={2,5}; the two exceptional integers
are 8 and 13. Ordinary R+R has residues {0,3,4} modulo 7.
The mixed residues 8+R are {3,6}, and 13+R are {1,4}.
The distinct exceptional pair is 8+13=21, also absent. Exceptional
doubles are unavailable. The target 8 precedes the first distinct sum;
for 13, the only smaller entries are 2,8,9,12, whose seed sums are
10,11,14 and whose nonseed distinct sums start at 17. Thus no selected
target, regular or exceptional, is a distinct selected sum.

Above 8 in block one the omitted integers are 10=2+8 and 11=2+9.
In block two the omitted integers have the following representations:

    14=2+12, 15=2+13, 17=8+9, 18=2+16, 20=8+12.

For every n>=3, the five omitted residue classes are covered by

| Offset r | Representation of 7n+r |
| --- | --- |
| 0 | 2 + (7(n-1)+5) |
| 1 | 13 + (7(n-2)+2) |
| 3 | 8 + (7(n-1)+2) |
| 4 | 2 + (7n+2) |
| 6 | 8 + (7(n-1)+5) |

Every factor is in T. In the second row at n=3 the second factor
is 9, which is explicitly initial; at larger n it is in the recurring
tail. Distinctness follows directly from the displayed values or
different residues. These five offsets are exactly the complement
of R modulo 7. Hence T=S(2,8), with a periodic tail from 14.

## Two finite transient sets with one recurring row

For each of the following rows define
T=P union union_(n>=1)(nm+R):

| g | m | P | R | X=P minus R |
| --- | --- | --- | --- | --- |
| 11 | 31 | {2,11,12,15,16,19,20,24,25,29} | {2,7,11,15,16,20,24,25,29} | {12,19} |
| 12 | 33 | {2,12,13,16,17,20,21,24,27,31} | {2,9,13,16,17,20,24,27,31} | {12,21} |

Both are positive sets with exactly 2,g at or below g. The two
exceptional entries in each X occur only initially and add to m.
In particular their distinct cross sum is absent, and their doubles
are not allowed. The following complete triangular addition tables
give `(r+{s in R:s>=r}) mod m`. Each displayed entry is outside R,
so even ordinary sums of recurring residues are safe.

| r, m=31 | Resulting residues | r, m=33 | Resulting residues |
| --- | --- | --- | --- |
| 2 | 0,4,9,13,17,18,22,26,27 | 2 | 0,4,11,15,18,19,22,26,29 |
| 7 | 0,1,5,14,18,22,23,27 | 9 | 0,3,7,18,22,25,26,29 |
| 11 | 0,4,5,9,22,26,27 | 13 | 0,4,7,11,26,29,30 |
| 15 | 0,4,8,9,13,30 | 16 | 0,3,7,10,14,32 |
| 16 | 1,5,9,10,14 | 17 | 1,4,8,11,15 |
| 20 | 9,13,14,18 | 20 | 7,11,14,18 |
| 24 | 17,18,22 | 24 | 15,18,22 |
| 25 | 19,23 | 27 | 21,25 |
| 29 | 27 | 31 | 29 |

The mixed sums with the exceptional integers also avoid R:

| m | Exceptional integer x | (x+R) mod m |
| --- | --- | --- |
| 31 | 12 | 1,5,6,10,14,19,23,27,28 |
| 31 | 19 | 3,4,8,12,13,17,21,26,30 |
| 33 | 12 | 3,6,10,14,21,25,28,29,32 |
| 33 | 21 | 1,4,5,8,12,15,19,23,30 |

It remains to check the initial exceptional targets. For g=11,
12 is smaller than the first distinct sum 2+11=13. A sum of
two nonseed entries is at least 11+12=23>19, and 19-2=17
is not in P. For g=12, 12 is a seed; the first two nonseed
entries sum to 12+13=25>21, and 21-2=19 is not in P.
All later-block entries are larger than these targets. This proves
global sum exclusion, including the exceptional targets themselves.

For initial coverage, all omitted integers between g and m are
listed here, with distinct summands in P:

| g=11 | g=12 |
| --- | --- |
| 13=2+11 | 14=2+12 |
| 14=2+12 | 15=2+13 |
| 17=2+15 | 18=2+16 |
| 18=2+16 | 19=2+17 |
| 21=2+19 | 22=2+20 |
| 22=2+20 | 23=2+21 |
| 23=11+12 | 25=12+13 |
| 26=2+24 | 26=2+24 |
| 27=2+25 | 28=12+16 |
| 28=12+16 | 29=2+27 |
| 30=11+19 | 30=13+17 |
| — | 32=12+20 |

For positive blocks the next tables list every residue outside R.
The column `(a,b,c)` means the following identity, valid for all n>=2:

    nm+r = a + ((n-c)m+b),    a in P, b in R, c in {0,1}.

Its factors are in different actual blocks because n-c>=1, hence
are distinct even when a=b. The final column separately handles
block one; each listed pair consists of two distinct members of P
or one member of P and one member of m+R. All assertions can
be read directly from the displayed sets and identities.

| r, m=31 | (a,b,c), all n>=2 | Representation of 31+r |
| --- | --- | --- |
| 0 | (2,29,1) | 2+29 |
| 1 | (12,20,1) | 12+20 |
| 3 | (19,15,1) | 15+19 |
| 4 | (2,2,0) | 11+24 |
| 5 | (11,25,1) | 11+25 |
| 6 | (12,25,1) | 12+25 |
| 8 | (15,24,1) | 15+24 |
| 9 | (2,7,0) | 11+29 |
| 10 | (12,29,1) | 12+29 |
| 12 | (19,24,1) | 19+24 |
| 13 | (2,11,0) | 15+29 |
| 14 | (12,2,0) | 16+29 |
| 17 | (2,15,0) | 19+29 |
| 18 | (2,16,0) | 20+29 |
| 19 | (12,7,0) | 12+38 |
| 21 | (19,2,0) | 19+33 |
| 22 | (2,20,0) | 24+29 |
| 23 | (12,11,0) | 25+29 |
| 26 | (2,24,0) | 2+55 |
| 27 | (2,25,0) | 2+56 |
| 28 | (12,16,0) | 12+47 |
| 30 | (15,15,0) | 15+46 |

| r, m=33 | (a,b,c), all n>=2 | Representation of 33+r |
| --- | --- | --- |
| 0 | (2,31,1) | 2+31 |
| 1 | (17,17,1) | 13+21 |
| 3 | (12,24,1) | 12+24 |
| 4 | (2,2,0) | 13+24 |
| 5 | (21,17,1) | 17+21 |
| 6 | (12,27,1) | 12+27 |
| 7 | (13,27,1) | 13+27 |
| 8 | (17,24,1) | 17+24 |
| 10 | (12,31,1) | 12+31 |
| 11 | (2,9,0) | 13+31 |
| 12 | (21,24,1) | 21+24 |
| 14 | (12,2,0) | 16+31 |
| 15 | (2,13,0) | 17+31 |
| 18 | (2,16,0) | 20+31 |
| 19 | (2,17,0) | 21+31 |
| 21 | (12,9,0) | 12+42 |
| 22 | (2,20,0) | 24+31 |
| 23 | (21,2,0) | 21+35 |
| 25 | (12,13,0) | 27+31 |
| 26 | (2,24,0) | 2+57 |
| 28 | (12,16,0) | 12+49 |
| 29 | (2,27,0) | 2+60 |
| 30 | (13,17,0) | 13+50 |
| 32 | (12,20,0) | 12+53 |

The tables exhaust the complements of R in [0,m). They provide
all omitted integers in every positive block, not just a bounded
prefix. With initial coverage, global exclusion, and the seed check,
the positive-set induction proves both complete formulas. Their tails
are therefore periodic with the displayed m. QED.

## Checks and limits

The addition rows and witness proposals were constructed with the small
standard-library helper [finite_small.py (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material), whose exact
inputs and actual output are retained in [finite-small.json (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
The written proof states every required arithmetic row and every
all-block representation; it does not use the helper's pass status,
a continuation certificate, or any enlarged parameter experiment as
a mathematical premise. The contributor reread every row, checked its
membership, carry and distinctness, and checked that the listed gaps
exhaust the complements. This is self-checking, not independent review.
No least-period or exact-preperiod claim is needed here. Credit,
unknown model configuration and submission screening are in the shared
assistance note. Original prose/data use CC BY 4.0 and code MIT.
