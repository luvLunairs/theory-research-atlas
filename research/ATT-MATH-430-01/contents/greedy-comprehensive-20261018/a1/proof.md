> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct proof for S(f,2kf+1), f>=5 and k>=3

18 October 2026. Proposed scientific result, pending full-text human review
and manual submission. This is an AI-assisted contributor proof, not an
independent verification or a novelty claim. All intervals are inclusive.

## Target, sources and notation

For integers f>=5 and k>=3, put g=2kf+1 and m=(6k-1)f+1. We prove the
complete membership formula below for the strict greedy sequence S(f,g),
where only sums of two distinct earlier entries are forbidden. We also
derive its least characteristic period m, least gap period k(f+2),
characteristic start (14k-3)f+1, and gap preperiod k(2f+3)+4.

The period and preperiod values are predicted in Definition 3(2) and
Definition 8(e), respectively, of Daan van Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
For the second substitution, use h=k-1 and r=f+1. The earlier local
`greedy-unified-20261018/quotient/candidate.md` proposed the membership
table and left its general-f proof open. The argument here supplies a
direct proof of that table; it does not rely on a finite-block inference.
The parent bundle retains the literature check and priority limitations.

Define three indexed tail families, with 0<=i<=k-1:

    A_i=(2i+1)f + a_i,
    B_i=(2k+2i)f + b_i,
    C_i=(4k+2i)f + c_i,

where the within-cell offsets are

| i | a_i | b_i | c_i |
| --- | --- | --- | --- |
| 0 | [-1,0] | [2,f-1] | [1,2] |
| 1 | {-1} | [1,f-1] | [0,1] |
| 2<=i<=k-1 | [-2,-1] | [1,f-2] | [0,1] |

Let R be the union of all A_i,B_i,C_i. Also put

    F_i=[(2k+2i)f+1,(2k+2i+1)f],
    beta_i=(2k+2i+1)f,       gamma_i=beta_i-1.

Define the first three m-blocks by their offsets:

* P_0 contains {f}, every F_i, C_0,C_1, and the upper endpoint of
  each C_i for 2<=i<=k-1.
* P_1 contains {f,(2k-1)f-1}, B_0, and
  [(2k+2i)f+1,(2k+2i+1)f-1] for 1<=i<=k-1, together with all C_i.
* P_2 contains A_0, the upper endpoint of A_i for 1<=i<=k-1,
  every B_i and every C_i.

The proposed sequence is the increasing enumeration of

    T=P_0 union (m+P_1) union (2m+P_2)
      union union_{n>=3}(nm+R).                              (1)

All displayed runs lie in [0,m), are disjoint and have nonempty gaps.
The first two elements of T are f,g. Compared with the periodic residue
set R, the only extra elements of T are

    g;
    beta_i                  (0<=i<=k-1);
    gamma_i, m+gamma_i       (2<=i<=k-1).                     (2)

All other differences from the periodic template are omissions.

## Tail sum exclusion

We first prove (R+R) mod m is disjoint from R, allowing equal summands.
Write s=i+h. Adding cells gives an integer of the form Lf+t. Subtracting
m changes this to (L-6k+1)f+(t-1). The following six cases exhaust all
pairs of tail families.

**A+A.** The sum is 2(i+h+1)f+(a+a'), with -4<=a+a'<=0, and is below m.
It is too small to reach C. At a matching even B-cell its offset is
nonpositive, whereas B offsets are positive. It cannot reach an odd
A-cell: a change of one f-cell requires at least f in the offset
difference, but the possible difference is in [-4,2]. Here f>=5 is used.

**A+B.** The sum is (2(k+s)+1)f+e, with -1<=e<=f-1, and is below m.
It is beyond A. The only possible B collision is in B_s, at e=-1 and
its upper offset f-1. But e=-1 requires i>=2 and h>=1, so s>=3, where
B_s has upper offset f-2. If that index is outside the B range there
is no target. Adjacent C-cells cannot be reached: the candidate offset
in the preceding even cell is at least f-1>2, and the next even cell
requires a negative C offset.

**A+C.** Before reduction the sum is (4k+2s+1)f+e, -2<=e<=2. An
unwrapped sum can only approach B at s=0, where e>=0, beyond the end
of B_(k-1). Neighboring even C-cells require an offset change of f and
cannot be reached. After a wrap the sum is 2(s-k+1)f+(e-1), with
0<=s-k+1<=k-1 and -3<=e-1<=1. This lies below B. Its offset is too
close to an even cell boundary to reach an A-cell: the next possible A
offset is at least f-2>=3 and the previous one is at most -f<=-5.

**B+B.** An unwrapped sum is (4k+2s)f+(b+b'). Its only possible C
collision has b+b'=2, requiring i,h>=1 and hence s>=2; C_s has upper
offset 1. There is no carry by 2f because b+b'<=2f-2. After a wrap the
sum is (2(s-k)+1)f+(b+b'-1). It lies below B. Its offset is between 1
and 2f-3: it misses the nonpositive A offsets in the current odd cell
and also misses those in the next odd cell, which begin at 2f-2.

**B+C.** There is exactly one wrap, giving (2s+1)f+e with
e=b+c-1 in [0,f]. A collision with A could only have e=0; that requires
i,h>=1, so s>=2 and the target A_s excludes 0. B cannot be hit because
its positive offsets end below f in the preceding even cell, while the
next even cell is not reached with a positive offset. A C collision
could only occur at e=f, at the start of the next even cell. But e=f
requires h=0 and i in {0,1}, so s+1<=2<2k, before every C-cell.

**C+C.** There is exactly one wrap, giving (2k+2s+1)f+e with
e=c+c'-1 in [-1,3]. This is beyond A, and its offset cannot reach an
adjacent C-cell when f>=5. A B collision could only have e=-1 and the
target B_s upper offset f-1. But e=-1 requires i,h>=1, hence s>=2,
where B_s has upper offset f-2. This completes tail exclusion.

## Exceptions and distinctness

Next every exceptional residue in (2), added to R, avoids R. It suffices
to check g and D_i=beta_i+epsilon, where epsilon=0 for every i and
epsilon=-1 only when i>=2. The actual block of an exception does not
matter for this modular assertion.

| Pair | Relevant offset or possible collision | Reason it is excluded |
| --- | --- | --- |
| g+A_i | Odd cell (2k+2i+1)f, offset 1+a | Only offset -1 can approach a B upper endpoint; then i>=2 and that endpoint f-1 is absent. |
| g+B_i | Even cell (4k+2i)f, offset 1+b | At i=0 this is at least 3>C_0's upper offset 2; at i>=1 it is at least 2>C_i's upper offset 1. |
| g+C_i | After wrapping: (2i+1)f+c | For i=0, c>=1>A_0's upper offset 0; for i>=1, c>=0>A_i's upper offset -1. |
| D_i+A_h | Even cell 2(k+i+h+1)f, offset epsilon+a<=0 | A is excluded by cell parity and f>=5; B has positive offsets. A possible C offset 0 forces h=0, epsilon=0 and then its index is at most 0; C_0 excludes 0. |
| D_i+B_h | Unwrapped: odd cell beyond B, offset epsilon+b in [0,f-1]. Wrapped: even cell 2(s-k+1)f, offset epsilon+b-1 in [-1,f-2]. | An A collision in the wrapped case would require epsilon=0, b=f-1 and target index at least 2. But b=f-1 implies h<=1 and the target index s-k+1<=h<=1. |
| D_i+C_h | After wrapping: even cell 2(s+1)f, offset epsilon+c-1 in [-2,1]. | Only B offset 1 could be hit. This forces epsilon=0,h=0,c=2, so the possible B index is at most 0; B_0 excludes 1. A is excluded by parity and C is beyond this range. |

In the first two rows neighboring cell types are excluded by the same
offset bounds as in the tail argument. In the fourth row there is no
wrap. In the last row there is exactly one. In the fifth row a wrapped
value lies below B. Thus the table exhausts the possible target types.

For exceptional pairs, g has only one copy, so g+g is not a distinct
pair. The sums of g with beta_i or either copy of gamma_i lie in gaps:
before a wrap they are in odd cells beyond B, with offset 1 or 0;
the largest g+beta_i equals m. A translate by m does not change this.
They cannot hit an exceptional target either: the unshifted sums exceed
every initial exception, and a shifted sum exceeds every exception in
block 1.

The remaining exceptional pairs have the following behavior. The block
numbers mentioned include any extra m-translate of a gamma.

* beta_i+beta_h equals (4k+2s+2)f. For s<=k-2, its residue is the
  lower endpoint of C_(s+1). That endpoint is omitted in block 0 if
  s>=1; at s=0 the only pair is the forbidden equal pair i=h=0.
  For s>=k-1, its residue is the upper endpoint of A_(s-k+1) in
  block 1. All such points are omitted there, except for the last A
  endpoint, whose only representation in this case is i=h=k-1 and
  is again an equal pair.
* beta_i+gamma_h has the preceding even coefficient and offset -1.
  Before a wrap it is outside R and outside the exception list. After
  a wrap it is the lower endpoint, with offset -2, of A_(s-k+1).
  It lies in block 1 or 2. Block 1 omits it, and block 2 contains only
  the upper A endpoints (apart from A_0, which also excludes offset -2).
* gamma_i+gamma_h has offset -2 before wrapping, or offset -3 in an
  odd A-cell afterwards. Both are outside R and the exception list,
  regardless of the one or two available block translates.

It remains to check that a sum of regular elements cannot hit an
exceptional target. Every initial exception belongs to one of the F_i.
Below the end of F_(k-1), the only candidates are f and these F intervals.
Sums with f lie in the intervening gaps; sums of two F terms are at least
2g=4kf+2, beyond F_(k-1). Thus every initial exception is safe.

The block-1 exceptions are particularly simple as actual integers:

    m+gamma_i=(8k+2i)f,          2<=i<=k-1.                  (3)

Two block-1 terms already exceed these targets, so only P_0+P_0 and
P_0+(m+P_1) need be considered. In P_0+P_0, two F terms are at most
(8k-2)f, below (3). An F+C sum has even f-coefficient and offset strictly
between 0 and 2f, so cannot equal (3). A C+C sum could have zero offset
only by using the lower endpoint of C_1 twice, which is not allowed;
all other initial C offsets are positive. Sums with the seed f are
smaller than (3).

For P_0+(m+P_1), subtract m. The target is gamma_i<4kf. Thus an initial
C, or two B/F-sized terms, are too large. What remains is f+P_1 or
F_j+{f,(2k-1)f-1}. The first two possibilities f+P_1 and F_j+f have
gaps at gamma_i, as is seen directly from their even-cell interval
endpoints. The last has minimum (4k-1)f, greater than every gamma_i.
This excludes (3). Together these arguments prove that T contains no
sum of two distinct members of T.

## Coverage of every omitted integer

For intervals, sums of two disjoint intervals fill the interval between
their endpoint sums. The distinct self-sums of [a,b], a<b, are exactly
[2a+1,2b-1]. We now cover every omitted integer above g. All summands
used are positive, so any representation automatically uses smaller
numbers than its target.

For n>=1, write A_i[n],B_i[n],C_i[n] for the actual portions of block n
of those runs. Thus C_i[n]=nm+C_i for every n>=1. B_i[1] has the
additional upper endpoint gamma_i for i>=2; B_i[n]=nm+B_i for n>=2.
A_0[1]={m+f}; A_0[n]=nm+A_0 for n>=2. In block 0 the B-like intervals
are F_i, while C_i[0] means the actual initial C portion. All uses of
C_0[0] and C_1[0] below are legitimate full intervals.

### Block 0

The gaps between successive F intervals, and the gap after F_(k-1),
are exactly f+F_i. The gap after C_0 is

    [4kf+3,(4k+2)f-1],

which is the distinct self-sum of F_0. After C_1 and the succeeding
singletons, the gaps are supplied by

    F_0+F_i=[(4k+2i)f+2,(4k+2i+2)f],   1<=i<=k-1.

The last interval extends through the end of the m-block. These are all
initial omissions above g.

### Early cells in blocks n>=2

The following offsets are relative to nm.

* The low gap [0,f-2] is covered by F_(k-2)+B_1[n-1], which crosses
  into block n and has offsets [-f+1,f-2].
* The gap [f+1,3f-2] after A_0 is exactly F_(k-1)+B_1[n-1].
* For 1<=i<=k-2, use the union of

      F_(i-1)+C_1[n-1] = nm+[(2i+1)f,(2i+2)f],
      F_(k-1)+B_(i+1)[n-1].

  The latter starts at offset (2i+1)f+1. When n=2 it ends at
  (2i+3)f-2, exactly before the next singleton A endpoint in P_2.
  When n>=3 it ends at (2i+3)f-3, exactly before the next full A
  pair. These two intervals overlap and cover each required gap.
* The gap after A_(k-1) and before B_0 is covered by

      F_(k-2)+C_1[n-1] = nm+[(2k-1)f,2kf],
      F_(k-1)+C_0[n-1] = nm+[(2k-1)f+1,2kf+1].

The first summand in each pair is initial and the other is in a later
block, so distinctness is automatic.

### Early cells in block 1

Here the only early selected points are m+f and m+(2k-1)f-1. The low
gap [0,f-1] is covered by F_0+F_(k-1). To cover the large gap after f,
use, for 0<=i<=k-3,

    F_(k-1)+F_(i+1)
      = m+[(2i+1)f+1,(2i+3)f-1].

The factors are distinct intervals. The final pair is a restricted
self-sum instead:

    F_(k-1) distinct-plus F_(k-1)
      = m+[(2k-3)f+2,(2k-1)f-2].

For 1<=i<=k-2, insert F_(i-1)+C_1[0], whose offsets are
[(2i+1)f,(2i+2)f]. These intervals fill every junction, including the
first point lost at the beginning of the final self-sum. All overlap
claims follow from f>=5. The two C-based intervals used after A_(k-1)
in the preceding paragraph also apply with n=1 and cover the gap up
to B_0[1]. This handles every early omission in block 1.

### Gaps after the B runs

For n>=2, F_i+A_0[n] covers

    nm+[(2k+2i+1)f,(2k+2i+2)f],       0<=i<=k-1.

For i=0,1 these cover the whole gap. For i>=2 the gap begins one
integer earlier, at nm+gamma_i. Supply that point by the lower endpoint
of C_1[0] plus the lower endpoint of C_(i-1)[n-1]: their sum is

    (n-1)m+(8k+2i)f = nm+gamma_i.

The two summands lie in different blocks, even when i=2. This also
handles the final gap before C_0[n]. In block 1, F_i+{m+f} covers the
required gap except for its
first point m+beta_i. Supply those first points as follows:

* For i=0, F_(k-1)+C_1[0] covers the whole required gap.
* For i=1, the two lower endpoints of C_0[0],C_1[0] sum to m+beta_1.
* For i>=2, the lower endpoint of C_1[0] and the upper endpoint of
  C_(i-1)[0] sum to m+beta_i. If i=2 these are the two different
  endpoints of C_1, so the pair remains distinct.

### Gaps after the C runs

For every n>=1,

    F_0+B_0[n] = nm+[4kf+3,(4k+2)f-1]

covers the gap after C_0. For 1<=i<=k-1,

    F_(i-1)+B_1[n]
      = nm+[(4k+2i)f+2,(4k+2i+2)f-1]

covers the gap after C_i. The last interval continues past the end of
the current m-block. The B_1 interval is identical in every positive
block, so no transient endpoint is being assumed here.

This list covers the entire complement in every block. It uses only
actual selected summands; its only equal-interval cases were explicitly
restricted to distinct sums. Together with sum exclusion and the two
forced seeds, induction proves that (1) is exactly the greedy sequence.

## Least periods and exact preperiod

The recurring word R has exactly one run of length f-1, namely B_1.
Every other run has length at most f-2 or length at most 2. Because
f>=5 these are shorter. A nontrivial cyclic repetition would repeat
this unique longest run, which is impossible. Thus the characteristic
period m is primitive. Counting the three families gives

    |A|=2k-1,   |B|=k(f-2)+1,   |C|=2k,
    |R|=k(f+2).

A smaller gap period would yield a smaller positive translation of
the characteristic tail, so the least gap period is p=k(f+2).

The latest missing entry of P_2 relative to R is the lower endpoint of
A_(k-1), at offset (2k-1)f-2. There are no extra entries in P_2, and
all earlier discrepancies lie in earlier blocks. Hence characteristic
periodicity starts exactly at

    N=2m+(2k-1)f-1=(14k-3)f+1.

The counts in P_0 and P_1 are k(f+1)+3 and k(f+1)+1. Before N in
block 2 there are k further terms: two in A_0 and k-2 earlier singletons.
Thus the number of sequence terms before N is

    K=k(2f+3)+4.

For x_0<x_1<... and d_i=x_(i+1)-x_i, we have x_K=N. The incoming gap
to N is 2f, since the preceding early singleton is N-2f. One period
later the incoming gap is 1, since the missing lower endpoint is now
present. Thus d_(K-1)=2f and d_(K-1+p)=1; all gaps from d_K onward
repeat. This proves the exact gap preperiod K, with the comparison in
the same phase. No earlier start with a larger eventual period is
possible, since every eventual period is a multiple of the primitive one.

## Checks, limits and provenance

The proof is universal in both f and k. It does not infer either bound
from enumerated instances. The parent bundle's separate
[certificate method (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
[rectangle-sum lemma (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) and
[retained partition result (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
check the same membership table on the whole orthant f>=5,k>=3 by exact
parameter-domain subdivisions. This is supporting contributor computation,
not a premise of the direct proof or independent scientific review.

During the contributor recheck, the first draft's B-gap row was found
to omit the point gamma_i for n>=2,i>=2. The revised row supplies it
with the lower endpoints of C_1[0] and C_(i-1)[n-1]. The blocks differ,
so this correction preserves distinctness. The earlier incomplete row
and its correction are recorded in the parent attempt and check reports.

The current AI research team supplied the formula, argument and checking.
Actual service-supplied identity, version and configuration are unknown.
The parent bundle retains the single assistance note and final-version
check report. No approval, external review, formal verification or priority
has been established. The local budget was 300 CPU seconds, with no paid
computation, installation, external communication or publication. This
direct argument required no new computational search. Earlier failed
extrapolations to f=3 or k=1 remain recorded in the immutable prior bundle;
they are outside the theorem's assumptions.
