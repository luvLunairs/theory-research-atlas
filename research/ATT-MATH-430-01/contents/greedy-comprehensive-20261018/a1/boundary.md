> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Completing the quotient boundary k=2 and linking k=1

18 October 2026. Scientific draft, pending full-text human review and manual
submission. The frozen `proof.md` and all earlier bundles are unchanged.
This is a contributor argument with AI assistance, not independent review
or a novelty claim. Every interval is inclusive.

## The k=2 theorem

For every integer f>=5, let g=4f+1 and m=11f+1. Set

    A_0=[f-1,f],           A_1={3f-1},
    B_0=[4f+2,5f-1],      B_1=[6f+1,7f-1],
    C_0=[8f+1,8f+2],      C_1=[10f,10f+1],
    F_0=[4f+1,5f],        F_1=[6f+1,7f].

Let R be the union of A_0,A_1,B_0,B_1,C_0,C_1, and put

    P_0={f} union F_0 union F_1 union C_0 union C_1,
    P_1=R minus {f-1}.

Then the strict greedy sequence S(f,4f+1) is the increasing enumeration of

    P_0 union (m+P_1) union union_{n>=2}(nm+R).              (1)

Its least characteristic period is m, its least gap period is 2(f+2),
characteristic periodicity starts at N=12f+1, and the exact gap preperiod
is K=2f+5.

### Exclusion of distinct sums

The six tail-pair calculations in [the frozen proof](proof.md) remain
valid at k=2. In those calculations the families with index at least 2
are empty. The only explicit strict k-dependent comparison is
s+1<=2<2k in the B+C case, which remains true. The remaining exclusions
use f>=5, cell parity, the listed offset bounds, and implications such
as "a collision requires index at least 2", which here simply means
that the target family does not exist. Thus (R+R) mod m avoids R, even
when equal residues are allowed.

There are only three exceptional elements relative to R: g=4f+1,
beta_0=5f, beta_1=7f, all in block 0. The g+R and beta_i+R calculations
in that proof also apply unchanged; there are no gamma exceptions.
Their distinct exceptional pairs are

    g+beta_0=9f+1,   g+beta_1=m,
    beta_0+beta_1=12f=m+(f-1).

The first two are gaps modulo m; the last is precisely the omitted
entry of P_1. A doubled beta_0 would hit C_1's lower endpoint and a
doubled beta_1 would hit m+A_1, but each beta occurs only once, so
neither is a permitted distinct pair. Finally all initial exceptions
lie in F_0 or F_1. Sums with f fall in the intervening gaps, and the
smallest sum of two F terms is at least 2g=8f+2>7f. Thus the exceptional
targets themselves are safe, and (1) is sum-free for distinct summands.

### Covering the gaps

In block 0 above g, f+F_0 and f+F_1 cover the gaps after the F runs.
The distinct self-sum of F_0 is [8f+3,10f-1], exactly the gap between
C_0 and C_1. The sum F_0+F_1=[10f+2,12f] covers the final high gap.

Write X[n]=nm+X for a run present in a positive block. Every B and C
run is present in every positive block; A_0 is full only from block 2.
The following table covers all seven gaps of a full R-block n>=2;
listed ranges are offsets relative to nm.

| Gap | Available sums and their offset range |
| --- | --- |
| [0,f-2] | F_0+B_1[n-1]: [-f+1,f-2] |
| [f+1,3f-2] | F_1+B_1[n-1]: [f+1,3f-2] |
| [3f,4f+1] | F_0+C_1[n-1]: [3f,4f], and F_1+C_0[n-1]: [3f+1,4f+1] |
| [5f,6f] | F_0+A_0[n]: [5f,6f] |
| [7f,8f] | F_1+A_0[n]: [7f,8f] |
| [8f+3,10f-1] | F_0+B_0[n]: [8f+3,10f-1] |
| [10f+2,11f] | F_0+B_1[n]: [10f+2,12f-1] |

Every pair has one initial and one later summand, so distinctness is
automatic. The parts extending beyond the stated block are harmless.

In block 1 the low gap is [0,f-1], covered by F_0+F_1 with offsets
[-f+1,f-1]. The next gap [f+1,3f-2] needs a separate boundary argument:

    F_0+C_0                 = m+[f+1,2f+1],
    F_1 distinct-plus F_1   = m+[f+2,3f-2].

These overlap and cover the whole gap. The first pair consists of
disjoint intervals; the second explicitly excludes equal summands.
The third gap uses the two C sums in the table, with their initial
copies. For the fourth gap, F_1+C_1=m+[5f,6f] supplies everything.
For the fifth gap, F_1+{m+f} covers m+[7f+1,8f]; its missing first
point is the sum of the lower endpoints of C_0 and C_1:

    (8f+1)+10f=m+7f.

The last two rows of the table apply unchanged. This accounts for every
omitted integer above g. All summands are positive and therefore smaller
than the represented target. Exclusion and coverage establish (1) by
induction on the greedy candidate.

An initially suggested repair using F_0+F_1 for the first missing point
of the F_1 self-sum was incorrect: its offset range ends at f-1, not
f+1. The repair above uses F_0+C_0 instead. No negative-index F family
is introduced, and this failed intermediate suggestion is retained here.

### Least periods and the exact transient

B_1 is the unique longest run of R, of length f-1. Its other run lengths
are 2,1,f-2,2,2, all smaller for f>=5. Hence the circular characteristic
word is primitive, with least period m. Its number of selected residues
is 2(f+2), giving the least gap period by the same translation argument
as in the frozen proof.

The last deviation from the recurring template is the missing point
m+f-1=12f. Therefore characteristic periodicity begins exactly at
N=12f+1. Every selected point before N is in P_0, whose size is 2f+5.
With x_K=N and d_i=x_(i+1)-x_i, the preceding term is 10f+1, giving
d_(K-1)=2f. One full gap period later, the corresponding incoming gap
is 1, because the lower endpoint of A_0 is present. All later gaps
repeat. Thus the exact gap preperiod is K=2f+5; a larger eventual gap
period cannot start earlier because it is a multiple of the primitive
one and has the same mismatching tail phase.

## The existing k=1 case

The immutable [earlier j=1 proof](../../greedy-families-20261018/j12/proof.md)
already proves S(f,2f+1) for f>=3. Its least periods have an exception
at f=4. Restricting to f>=5 avoids that exception and gives

    m=5f+1,  p=f+2,  N=3f+1,  K=f+1.

Here N is the characteristic start but is not selected: the first
selected value after it is 4f+1. Exactly f+1 selected terms precede
that value. Its incoming gap is f+1, from 3f; the corresponding gap
one characteristic period later is f+2, from 8f to 9f+2. This direct
same-phase mismatch confirms the exact gap preperiod convention.
The earlier membership proof and its f=4 exception are not altered.

Combining that result, (1), and the frozen k>=3 proof gives a theorem
for **every f>=5 and every k>=1** with g=2kf+1:

| Quotient | Least characteristic period | Least gap period | Characteristic start | Gap preperiod |
| --- | --- | --- | --- | --- |
| k=1 | 5f+1 | f+2 | 3f+1 | f+1 |
| k=2 | 11f+1 | 2(f+2) | 12f+1 | 2f+5 |
| k>=3 | (6k-1)f+1 | k(f+2) | (14k-3)f+1 | k(2f+3)+4 |

In particular, the two least period formulas are uniform across all k;
the transient has these three regimes. No general-a assertion follows.

## Checks and limits

`boundary_diagnostics.py` compares the explicit formula and a distinct-pair
greedy computation for exactly f=5,6,11, always k=2, through eight m-blocks.
It checks the last characteristic mismatch, the count before N, and the
last successive-gap mismatch, including 2f versus 1. The retained JSON
binds this text and the code by SHA-256. These three cases are diagnostic
checks, not the proof of an infinite family.

The source, prior formula, provenance and literature limitations are those
identified in the frozen proof and the parent bundle. Boundary preperiod
counts above are derived directly; no agreement with every small-parameter
correction in the source is assumed. The shared assistance note and final
check report apply. Service-supplied identity and configuration are unknown;
human screening and manual submission remain required. No independent
scientific verification or priority claim is made.
