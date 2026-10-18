> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# The endpoint g=4f: a fifth run forced by distinctness

18 October 2026. Local candidate proof, pending human screening and manual
submission. Original AI-assisted argument; no independent verification or
novelty approval. All intervals below contain integers and include endpoints.

## Statement and formula

Fix any integer f>=5. Start with f,4f and repeatedly append the least larger
integer that is not a sum of two distinct earlier entries. Put m=11f-1.
Define actual selected intervals A_k,B_k,C_k,D_k,E_k by adding km to each
entry in row k of the following table, and let T be their union over k>=0.

| k | A offsets | B offsets | C offsets | D offsets | E offsets |
| --- | --- | --- | --- | --- | --- |
| 0 | {f} | [4f,5f-1] | [6f,7f-1] | {8f} | [10f-2,10f-1] |
| 1 | {f} | [4f+1,5f-2] | [6f,7f-2] | {8f} | [10f-2,10f-1] |
| k>=2 | [f-1,f] | [4f+1,5f-2] | [6f,7f-2] | {8f} | [10f-2,10f-1] |

**Proposed theorem.** T is exactly the strict greedy sequence S(f,4f).
Its least eventual characteristic period is m=11f-1, its least gap period
is 2f+2, its characteristic periodicity starts at 12f-1, and its least gap
preperiod has length 2f+4.

The gap-period value is a specialization of van Berkel and Bosma's
Definition 3(2), k=2 and local offset 0, in
[arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
That is a conjectural prediction, not the proof supplied here. The present
formula and argument were derived during this continuation. Related interval
methods and the scope of the literature search are credited in
[the source note](literature/source-check.md).

## Sum exclusion

Write A=[f-1,f], B=[4f+1,5f-2], C=[6f,7f-2], D={8f},
E=[10f-2,10f-1], and R=A union B union C union D union E.
The only selected integers with residues outside R modulo m are
u=4f, v=5f-1 and w=7f-1, each occurring once. Within R the early missing
entries are f-1 in blocks 0 and 1. The complement of R is:

```
G0=[0,f-2], G1=[f+1,4f], G2=[5f-1,6f-1],
G3=[7f-1,8f-1], G4=[8f+1,10f-3], G5=[10f,m-1].
```

All ordinary sums of residue classes are bounded by the following table.
Every interval, after reduction modulo m, lies in the indicated complement.
Permitting a diagonal in these bounds only enlarges a safe set.

| Classes | Raw sum | Containing gaps modulo m |
| --- | --- | --- |
| A+A | [2f-2,2f] | G1 |
| A+B | [5f,6f-2] | G2 |
| A+C | [7f-1,8f-2] | G3 |
| A+D | [9f-1,9f] | G4 |
| A+E | m+[-2,0] | G5 union G0 |
| B+B | [8f+2,10f-4] | G4 |
| B+C | [10f+1,12f-4] | G5 union G0 |
| B+D | m+[f+2,2f-1] | G1 |
| B+E | m+[3f,4f-2] | G1 |
| C+C | m+[f+1,3f-3] | G1 |
| C+D | m+[3f+1,4f-1] | G1 |
| C+E | m+[5f-1,6f-2] | G2 |
| D+D | m+{5f+1} | G2 |
| D+E | m+[7f-1,7f] | G3 |
| E+E | m+[9f-3,9f-1] | G4 |

The exceptional integers paired with a regular residue are also safe:

| Exceptional integer | +A | +B | +C | +D | +E |
| --- | --- | --- | --- | --- | --- |
| u | [5f-1,5f] | [8f+1,9f-2] | [10f,m-1] | m+{f+1} | m+[3f-1,3f] |
| v | [6f-2,6f-1] | [9f,10f-3] | m+[0,f-2] | m+{2f} | m+[4f-2,4f-1] |
| w | [8f-2,8f-1] | m+[1,f-2] | m+[2f,3f-2] | m+{4f} | m+[6f-2,6f-1] |

Direct endpoint comparison with G0,...,G5 proves all containments for f>=5.
For example, the smallest delicate E+E endpoint satisfies 9f-3>=8f+1
already for f>=4. Thus sums with a nonexceptional summand cannot hit a
selected integer with residue in R.

The three exceptional pairs are u+v=9f-1 in G4 of block 0,
u+w=m in G0 of block 1, and v+w=m+f-1, the missing A endpoint of block 1.
They hit no selected integer. Finally none of u,v,w can be a distinct sum:
u and v precede the least possible distinct sum f+u=5f. For w=7f-1,
the sums f+B_0 stop at 6f-1, distinct B_0 self-sums start at 8f+1,
and sums involving C_0 start at f+6f=7f. Later blocks and D_0,E_0 are
too large. This exhausts possibilities and proves T has no forbidden sum.

## Coverage of every omitted integer above 4f

Sums of disjoint integer intervals fill the interval between the endpoint
sums. Distinct self-sums of [a,b], a<b, fill [2a+1,2b-1]. These identities
follow by choosing the lower endpoint for targets at most a+b and the
upper endpoint for larger targets. All uses below are distinct actual
entries, not merely distinct residue names.

In block 0, the gaps above the second seed are covered by:

| Gap | Representing sums |
| --- | --- |
| [5f,6f-1] | f+B_0, exactly |
| [7f,8f-1] | f+C_0, exactly |
| [8f+1,10f-3] | distinct B_0+B_0, exactly |
| [10f,m-1] | B_0+C_0=[10f,12f-2] |

For block k>=1, the following table covers all gaps, with offsets relative
to km. The only special low gap is [0,f-1] in block 1; later it is G0.

| Gap offsets | Representing sums and endpoint check |
| --- | --- |
| [0,f-1], k=1 | B_0+C_0=m+[-f+1,f-1] |
| G0, k>=2 | B_0+C_(k-1)=km+[-f+1,f-2] |
| G1 | C_0+C_(k-1), B_0+E_(k-1), w+D_(k-1); special self-sum handling below |
| G2 | C_0+E_(k-1)=km+[5f-1,6f-1], exactly |
| G3 | D_0+E_(k-1)=km+[7f-1,7f], together with f+C_k=km+[7f,8f-2] and w+A_k |
| G4 | B_0+B_k=km+[8f+1,10f-3], exactly |
| G5 | B_0+C_k=km+[10f,12f-3], containing the whole high gap |

In the G1 row for k>=2, the first interval is
km+[f+1,3f-2], the second km+[3f-1,4f-1], and the third is the
endpoint km+4f. For k=1, use distinct C_0+C_0, which gives
m+[f+2,3f-2], and add u+D_0=m+f+1 for the missing first endpoint.
All intervals meet or are adjacent. In the G3 row, w+A_k supplies
offset 8f-1 for k=1 and [8f-2,8f-1] for k>=2, completing the gap.

For G5 the raw interval [10f,12f-3] begins at the first gap endpoint
and extends beyond m-1, so only its portion in block k is used. The low
gap rows similarly use the carried portion. Each paired set is disjoint
as a set of actual integers, except the explicitly restricted self-sums.
The listed gaps are exactly the complements of the defining block table.

Thus every omitted integer above 4f is a sum of two distinct positive
members of T. Both summands are smaller than their sum. Together with
sum exclusion and the forced seeds, induction identifies T with the entire
greedy sequence.

## Minimality and transient

The circular m-word has exactly five nonempty runs of ones, with lengths
2,f-2,f-1,1,2, separated by nonempty zero runs. A nontrivial repetition
factor would divide 5 and hence be 5, requiring equal run lengths; the
lengths 1 and 2 rule this out. The least characteristic period is m.
There are 2f+2 ones in that primitive word. A shorter gap period would
sum to another characteristic period; the least characteristic period
divides that sum, which would require at least 2f+2 entries. Hence the
least gap period is 2f+2 as well.

The last discrepancy from the periodic extension is the absent m+f-1
in block 1. Its later translates by m are all selected. Periodicity starts
exactly at m+f=12f-1, and no earlier start with another eventual period is
possible because every eventual period is a multiple of primitive m.
Before this point, block 0 contains 1+f+f+1+2=2f+4 selected entries.
The incoming gap has length 2f, compared with the periodic incoming gap
1 to this second member of A. All later gaps repeat, so the least gap
preperiod is 2f+4.

## Why the extra run is necessary

At g=4f, the earlier four-run broadband pattern would omit 8f. Yet all
greedy entries below 8f are {f}, [4f,5f-1] and [6f,7f-1]. Their allowed
distinct sums leave 8f uncovered:
f+C_0 ends at 8f-1 and distinct B_0+B_0 starts at 8f+1. The remaining
formal representation 4f+4f is disallowed. Thus 8f must be selected.
This forces the fifth run. It is a counterexample to continuing that
four-run formula, not to eventual periodicity.

The separate affine audit in band_check.py checks the same full membership
formula for every f>=5. It is a contributor self-check, not independent
verification. No mathematical gap was identified during this proof's
construction; human review, independent assessment and novelty checking
remain pending. Actual service model identity/version/configuration are
unknown and disclosed in the shared assistance note. Original prose/data
use CC BY 4.0 and code MIT under the repository terms.
