> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Eventual periodicity of strict two-seed greedy sequences

**Analytic candidate submitted for review, 18 October 2026.** This
manuscript and its explicit mathematical appendices constitute the
proposed proof. The current assistance note records the recovered model
identity, maintainer authorization and preliminary human reading.
Contributor checks are not independent scientific verification. The
conjecture, predicted periods and previously known cases are credited
to Daan van Berkel and Wieb Bosma.

## 1. Statement, conventions and proof plan

Let f<g be positive integers. Starting from f,g, scan the integers x>g
in increasing order and select x precisely when x is not a sum of two
different earlier selected integers. Write S(f,g) for the resulting set.
The two summands must be different **actual integers**. Equal residues
in different blocks are permitted; a single actual integer used twice
is not. Integers below g other than the seeds are skipped by definition.

**Theorem.** For every positive f<g there exist positive integers m,N
such that

    x in S(f,g) if and only if x+m in S(f,g),  for every x>=N. (1)

The successive gaps are consequently eventually periodic.

This is the eventual-periodicity target in Conjecture 1 of
[van Berkel and Bosma, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
No least-period, exact-preperiod, arbitrary-initial-set or novelty claim
is part of the theorem asserted here. Every recurring row used below
is nonempty. Listing its selected residues in order gives the recurring
gaps, including the wrap to the next block, proving the final assertion.

All intervals in the proof are integer intervals with inclusive endpoints.
Empty intervals and empty index ranges contribute no entries. A formula
for a nonempty interval must not be applied to an empty one. For sets
A,B, write A dotplus B={a+b:a in A,b in B,a!=b}.

The proof uses three mechanisms. Explicit candidate sets are identified
by exact exclusion and coverage. Dynamic envelopes are identified by
chronological induction and their exceptions disappear in a finite
dependency order. The odd midpoint instead has an exact endpoint
recurrence dominated by a finitely supported supersolution. These
mechanisms are unified where their hypotheses agree; the midpoint
argument is retained separately rather than assuming finite memory.

## 2. General lemmas and the mathematical audit of a table

The following six lemmas, with full proofs and boundary guards, are
collected in [framework.md](framework.md).

1. **Strict interval sums.** For I=[a,b], J=[c,d], the possible first
   summands of t are [max(a,t-d),min(b,t-c)]. The sum t is lost
   precisely when this interval is {t/2}. If both inputs contain at
   least two integers, only a shared extreme double can be lost. A
   singleton can instead remove an interior sum.
2. **Canonical block sums.** For C(A,I)={qm+r:q in A,r in I},
   the strict sum is the image of
   ((A dotplus B) x (I+J)) union ((A+B) x (I dotplus J)).
   This proves distinctness even with overlapping components. It also
   gives the exact carry formula for arithmetic progressions.
3. **Global identification.** A positive candidate T containing exactly
   f,g at or below g equals S(f,g) if its strict sumset covers exactly
   the complement of T above g. Induction on the actual integer proves
   this because every positive summand is smaller than its sum.
4. **Anchor lifting.** A fixed initial component plus a recurring
   component in block n or n-1 gives an identity for every later n.
   Different canonical blocks ensure actual distinctness; the early
   overlapping-block case must be checked separately.
5. **Acyclic extinction.** If a core deficit in block n requires two
   exceptional strips with earlier dependency indices and n=q+r+c,
   extinction bounds B_j,B_l imply no such deficit from
   B_j+B_l+c-1. Explicit anchor sums then remove the next strip.
   A single delayed-endpoint feedback can be discharged in one further
   block when its obstructing endpoint has been removed.
6. **Causal comparison.** Nondecreasing endpoint recurrences using only
   earlier indices are bounded by any supersolution satisfying the
   initial inequalities. Finite support of that supersolution proves
   extinction; bounded endpoint values alone do not.

For clarity, the exact table criterion in Lemma 3 can be written without
any reference to a program. Let L_r={q>=0:qm+r in T}. For residue r,
unite all lifetimes L_a+L_b+floor((a+b)/m) with a<b and
(a+b) mod m=r. For a=b use L_a dotplus L_a+floor(2a/m).
Call this union Q_r. With D_r={q>=0:qm+r>g}, the required identity is

    Q_r intersect D_r = D_r minus L_r,       for every r.   (2)

Finite unions of lifetime intervals and rays are closed under these
sum operations. Thus a printed interval identity establishes every
block index, including the infinite ray. The fixed-case tables below
are mathematical appendices evaluated by (2), not scanned-prefix
certificates. Their full arithmetic remains part of the proof.

## 3. Family lemmas for first seeds at least five

Fix f>=5. In each row below all additional parameters are integers.
The linked appendices give the actual residue sets, exclusions and
coverage identities. They are integral parts of the family lemmas;
software results and optimal-period portions of older files are not
imported as premises. The three explicit wording corrections in
[errata.md](errata.md) govern the incorporated small-seed appendices.

| Label | Exact domain | Sufficient characteristic period m | Mathematical appendix |
| --- | --- | --- | --- |
| L | g=2kf+a, k>=1, 2<=a<=floor(f/2) | (6k-1)f+2a-1 | [Lower offsets](../greedy-proof-audit-20261018/lower-lemma.md) |
| M | f=2h-1, h>=2, g=2kf+h, k>=1 | 2f | [Midpoint](../greedy-proof-audit-20261018/midpoint-lemma.md) |
| U | g=2kf+a, k>=1, ceil(f/2)+1<=a<=f-2 | (6k+1)f+2a-1 | [Compatibility](../greedy-upper-20261018/compatibility.md), [interval identities](../greedy-upper-20261018/upper1/proof.md), [chronological U1](../greedy-proof-audit-20261018/upper-audit.md#proposition-u1-confinement-followed-by-finite-extinction) |
| E | g=2kf, k>=3 | (6k-1)f-1 | [Even multiples](../greedy-analytic-20261018/even-multiples/proof.md) |
| B | g=(2k+1)f-1, k>=2 | 3g | [Upper boundary](../greedy-analytic-20261018/upper/boundary.md) |
| R | g=(2k+1)f+b, k>=2, b=1 or 2 | (6k+3)f+2b-1 | [Two rays](../greedy-analytic-20261018/upper/rays.md) |
| P | g=(2k+1)f+b, k>=2, 3<=b<f, (k,b)!=(2,3) | (6k+3)f+2b-1 | [Plateau identities](../greedy-upper-20261018/upper2/proof.md), [chronological U2](../greedy-proof-audit-20261018/upper-audit.md#proposition-u2-a-fixed-tail-without-exact-transient-assumptions) |
| C | g=5f+3 | 15f+5 | [Plateau corner](../greedy-analytic-20261018/plateau-corner.md) |
| A1 | g=2f+1 | 5f+1 | [First quotient](../greedy-families-20261018/j12/proof.md) |
| A2 | g=4f+1 | 11f+1 | [Second quotient](../greedy-comprehensive-20261018/a1/boundary.md) |
| A3 | g=2kf+1, k>=3 | (6k-1)f+1 | [General offset one](../greedy-comprehensive-20261018/a1/proof.md) |
| D | g=4f | 11f-1 | [Endpoint](../greedy-lower-20261018/endpoint-proof.md) |
| O | g=(2k+1)f, k>=1 | (6k+3)f-1 | [Odd multiples](../greedy-unified-20261018/odd-multiple-proof.md) |
| T | g=3f-1 | 9f-3 | [Transition](../greedy-lower-20261018/lower/proof.md) |
| F | g=2f+j, f<=j<=2f-1 | 7f+2j-1 | [First-quotient band](../greedy-lower-20261018/lower/proof.md) |

Here is how the infinite part of these arguments follows from the
general lemmas. In L, the controlling C_i deficit requires strip
indices j+l=i-1 with no carry. The anchor C_0[0]+C_i[n-1]
removes strip i. Lemma 5 gives strip bounds 2i+2, and then all
remaining A deficits end by block 4k. In U the dependency order
is reversed: j+l=k+i forces j,l>i. The only feedback uses the
top of strip i in block n-1. Since a<=f-2, removing every extra
except its lowest point removes that top. Lemma 5 gives bounds
3(k-i)-1 and a fixed tail from block 6k-3.

In E, two actual unique exceptions and a protected two-point core
provide the causal base. A triangular deletion of beta endpoints is
followed by two-point anchor sums deleting the remaining strips.
Writing K=max(2,k-2), every extra is absent from K and every core
deficit is absent from 2K. The distinct-block condition at the
two-point self-pair requires the lower bound 2 in K.
The complete cutoff reduction is in [the even-multiple consolidation](large/lemmas.md#2-even-multiples-as-a-cutoff-recurrence-plus-one-cleanup-step).

In B, R, P and C, the candidate blocks or short exceptional lifetimes
are explicit. Their respective sufficient starts are m, 3m, 2m
and 4m. Ordinary residue doubles are retained in the classification;
they are excluded only when their actual lifetimes make two different
summands impossible. The chronology in P uses the chronological rule
following Lemma 4; it does not assume that a future block already exists.
The remaining boundaries similarly have direct global identities.
The [reflection lemma](large/lemmas.md#1-one-sided-reflection-and-a-single-deleted-diagonal)
also removes duplicated wrapped-case analysis for O and B: the symmetric
auxiliary set has no unwrapped collision in O, and only one diagonal
collision in B. Its reflection accounts for every wrapped collision.

In M, the exact endpoint recurrence is first established using strict
same-block sums. Its finite supersolutions differ for h>=3 and h=2.
Lemma 6 proves endpoint extinction for both, with the explicit sufficient
bounds in the midpoint appendix. Neither supersolution is asserted
to equal the actual transient. Thus every row in the table establishes
an infinite conclusion by a written argument.

## 4. Exhaustion of the large-seed parameters

If f<g<2f, use the source's Theorem 12. If g=2f, use its
Theorem 14; the exceptional f=2 case will be treated below.
Otherwise divide uniquely

    g=2kf+a,       k>=1,       0<=a<2f.                  (3)

For a=0 use D when k=2 and E when k>=3. For a=1 use A1,
A2 or A3 according to k. For 2<=a<=floor(f/2) use L.
When f is odd, the next integer a=(f+1)/2 is M; when f is
even there is no missing integer between L and U. Use U on
ceil(f/2)+1<=a<=f-2, omitting an empty range. In particular
that range is empty at f=5.

For a=f-1 use T at k=1 and B otherwise. For a=f use O.
For a>f and k=1 use F. Finally, if a>f and k>=2, put b=a-f.
The choices b=1,2 are R. Larger b are P except (k,b)=(2,3),
which is C. This exhausts every integer allowed by (3), so the
theorem holds for f>=5.

## 5. Small first seeds

### First seed one

Every f=1 case is already covered by Theorems 9 and 10 and Remarks 12
of [van Berkel and Bosma, On t-sumfree sequences, Section 5](https://arxiv.org/html/2609.16843v1#S5).
These are attributed known results, not new contributions of this proof.
The exceptional even second seeds 2, 4 and 6 have short complete exclusion
and coverage proofs in [the elementary boundary appendix](known-small-boundaries.md),
so no inference from the source's continuation dots is required.

### First seed two

The four unbounded classes have the following direct arguments:

| Second seed | Domain | Sufficient period | Proof |
| --- | --- | --- | --- |
| 4k+1 | k>=1 | 12k+3 | [Two-class proof](../greedy-analytic-20261018/small/f2-two-classes.md) |
| 4k+2 | k>=1 | 12k+9 | [Same proof](../greedy-analytic-20261018/small/f2-two-classes.md) |
| 4k+3 | k>=3 | 12k+7 | [Three-block proof](../greedy-analytic-20261018/small/f2-three-blocks.md) |
| 4k | k>=4 | 12k-3 | [Same proof](../greedy-analytic-20261018/small/f2-three-blocks.md) |

The exact finite complement is g=3,4,7,8,11,12. The first two
are the source's Theorem 12 and Example 13. The case g=4 is also
proved explicitly in the elementary boundary appendix. The relaxed
band F at (f,j)=(2,3) covers g=7; its equality boundary is checked in
[the domain appendix](../greedy-analytic-20261018/small-domain-extensions.md).
The [explicit fixed proofs](../greedy-analytic-20261018/finite-small.md)
cover g=8,11,12 with periods 7,31,33. All-block witnesses and
strict pair exclusions establish (2). This covers every g>2.

### First seed three

Known near-diagonal and diagonal results cover g=4,5,6. Write every
larger g as 6k+a, 0<=a<6. The assignment is exhaustive:

| a | Mathematical coverage |
| --- | --- |
| 0 | k>=5: [zero-offset proof](../greedy-analytic-20261018/small/f3-zero.md); k=2,3,4: [fixed lifetime proofs](../greedy-analytic-20261018/even-multiples/small-boundaries.md) |
| 1 | k>=2: [one-offset proof](../greedy-analytic-20261018/small/f3-one.md); k=1: A1 with f=3 |
| 2 | M with h=2, all k>=1 |
| 3 | O with its proved f>=3 relaxation |
| 4,5 | k>=2: R, valid for f>=3; k=1: relaxed band F |

The three fixed cases use periods 16,122,96 and sufficient starts
80,244,480. Their [lifetime table](../greedy-analytic-20261018/even-multiples/boundary-lifetime-tables.md)
and [arithmetic table](../greedy-analytic-20261018/even-multiples/boundary-arithmetic-tables.md)
display the terms needed for (2), including every exceptional target
and every early gap repair. Their lifetimes extend to infinity, so
these are all-block proofs. The general zero-offset proof's k>=5
boundary must not be dropped: its unchanged formula is false at k=4.
That value is covered by its different fixed proof.
For the general zero-offset family, the rewritten
[stable coverage lemma](small/f3-zero-tail.md) replaces the original
coverage after block three by eleven complete gaps and eighteen
cross-block identities. Their sources lie in blocks zero or one and
n or n-1>=3, so distinctness is automatic. The original exclusion
and early blocks remain the necessary, separately checked base.

### First seed four

Known results cover g=5,6,7,8. Write every larger g as 8k+a,
0<=a<8. Then:

| a | Mathematical coverage |
| --- | --- |
| 0 | k=2: relaxed D; k=3,4,5: [fixed lifetime proofs](../greedy-analytic-20261018/upper/f4-fixed.md); k>=6: zero-offset proposition below |
| 1 | [Offset-one relaxation](../greedy-analytic-20261018/even-multiples/a1-first-seed-four.md), every k>=1 |
| 2 | L with f=4,a=2 |
| 3 | k=1: relaxed T; k>=2: B, valid at f=4 |
| 4 | Relaxed O |
| 5,6 | k=1: relaxed F; k>=2: R |
| 7 | k=1: relaxed F; k=2: C, valid at f=4; k>=3: relaxed P |

Every relaxed domain has its endpoint inequalities proved in the
[domain appendix](../greedy-analytic-20261018/small-domain-extensions.md).
The fixed g=24,32,40 proofs use periods 67,91,23 and sufficient
starts 603,637,1035. For the last case a working modulus 115
compresses its [lifetime arithmetic](../greedy-analytic-20261018/upper/f4-fixed-tables.md);
its recurring word also has period 23. Neither modulus is justified
by a numerical repetition test.

**Zero-offset proposition.** For k>=6, S(4,8k) has period
m=32k+1 from 6m. Define P_0,...,P_5,R by the
[explicit candidate table](../greedy-analytic-20261018/even-multiples/f4-zero-coverage.md#candidate-target-and-notation)
and set P_n=R for every n>=6. The candidate has exactly the
two positive seeds at or below 8k. The
[complete exclusion proof](../greedy-analytic-20261018/small/f4-zero-exclusion.md)
places it in a thirteen-component envelope. Its 91 unordered pair
types have sixteen possible hits in the recurring core; the actual
lifetimes exclude every one. Every selected transient component is
also protected by its full possible-pair list and lifetime bounds.
For coverage, retain blocks zero, one and two from the
[original printed identities](../greedy-analytic-20261018/even-multiples/f4-coverage-tables.md).
They contain 38 complete omitted intervals and the three strict self-pairs.
For every block n>=3 use the new [uniform anchor lemma](four/anchor-compression.md).
Its independent parameter domain is k>=6,2<=a<=5,2<=b<=3,2<=d<=5.
The candidate's current rows have (a,b,d)=(2,2,2),(2,3,4),(4,3,5)
in blocks 3, 4 and 5 respectively and (5,3,5) thereafter. The lemma checks
their preceding-block interfaces explicitly and covers all thirteen
gaps by 22 cross-block identities. Thus only 51 gap rows are required
instead of 103. The 22 uniform identities use factors in different
blocks; the early identities retain their explicit distinctness checks.
These early and uniform identities supply distinct
representations of every omission. Lemmas 1–4
therefore identify the candidate with S(4,8k). Its literal fixed row
from block six gives the proposition.

The condition k>=6 is substantive for that unchanged formula. At k=5,
m=161, its recurring class-zero row would contain offsets 40 and 80.
The proposed distinct terms 6m+40=1006 and 7m+40=1167 sum to
13m+80=2173, another proposed selected term. This refutes the
extension, not eventual periodicity; g=40 has the different fixed proof.

All rows of the f=4 partition are now covered. Combined with the
preceding three small-seed cases and Section 4, this proves (1) for
every positive f<g. The nonempty recurring rows give eventual gap
periodicity as explained in Section 1. QED.

## 6. Status and retained obligations

This version presents a complete analytic candidate. It retains the
family-specific mathematical appendices as integral parts of the proof;
none is replaced by a diagnostic success flag. The new general lemmas
reduce repeated arguments and expose their exact empty-input, singleton,
chronological and feedback conditions.

The final [review findings](findings.md) distinguish counterexamples to
invalid extensions from counterexamples to the theorem. No latter
counterexample has been found. The [assistance and exact-version report](../../assistance-and-checks.md)
records actual reading scopes, arithmetic checks, corrections and limits.
Full-text human screening, independent scientific assessment, historical
novelty and publication remain pending. This is a contributor draft,
not a scientific or machine-verification approval.
