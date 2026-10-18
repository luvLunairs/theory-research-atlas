> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Adversarial reading of the large-seed analytic arguments

18 October 2026. Scoped same-team AI scientific assessment. Local draft
for full-text human review and manual submission. The contributor also
participated in earlier research in this project; this is not independent
verification, formal approval, or a novelty verdict. Service-supplied
identity, version and configuration are unknown and belong in the shared
parent assistance note. All earlier snapshots were left unchanged.

## Material and exact scope

The following files were read in full, including their mathematical
tables, boundary clauses and stated limits. Line numbers are one-based
in these exact files. The twelve files contain 3,099 lines in total.

| File relative to work/ | Lines read | SHA-256 |
| --- | --- | --- |
| greedy-analytic-20261018/even-multiples/proof.md | 1-415 | 7B873D57515C6973A13C4CFBFB26588C63DFEB88BA792344818319A734257603 |
| greedy-analytic-20261018/upper/boundary.md | 1-262 | 4CAD3877EC2D42C63F0302D5A320816AC86A25EF450E982DA5A22172BA73CC99 |
| greedy-analytic-20261018/upper/rays.md | 1-352 | 852BFEE1C131977539214BE8C9F7794EC4485E16070DA1124220065A73B48407 |
| greedy-analytic-20261018/plateau-corner.md | 1-202 | E708F0AD9B5ABEDBFC97AF5E99925C677E1CEED65E2E09B02E4753AB837B31F1 |
| greedy-families-20261018/j12/proof.md | 1-210 | 1FB4A11D23F6B3C54B7B7212482534D3537193F95F605EDA9FA945DD0F0840BB |
| greedy-comprehensive-20261018/a1/boundary.md | 1-166 | DC4FFF7236EFD13CFB1EC1FBFC647157188C7B1E8F150BC3DCF02E8D1F693902 |
| greedy-comprehensive-20261018/a1/proof.md | 1-370 | 665A56F1E317C03F5A353E16A4F21BBCC6A4B3C750790E99F6B4A9CFC869E50B |
| greedy-lower-20261018/endpoint-proof.md | 1-173 | F0F6595541BED37F958D3042A0F1A43B29B2567F695E18F7B00FE1AEE48D66C3 |
| greedy-unified-20261018/odd-multiple-proof.md | 1-206 | F5C508D9D7562015BB998F3F6FFFBB97EBDDCD086E570421D49F30065B1B6627 |
| greedy-lower-20261018/lower/proof.md | 1-317 | 37869C5D0F046630877277526F7B6ABDDE369A672811EEC017702CB2DBD82487 |
| greedy-analytic-20261018/small-domain-extensions.md | 1-183 | 608905FABEA235A8559649952184D6EFB655D8639178A449702F70CD95AD6183 |
| greedy-analytic-20261018/even-multiples/a1-first-seed-four.md | 1-243 | 72782A2D09740CDC32A98B6691F0FB899C239CB95B50B9F4240C89FC0C256123 |

The target of this review is the global membership/eventual-periodicity
argument, including all infinite parameter quantifiers, positivity,
seed initialization, actual distinctness, carries and small-domain
extensions. Period and transient paragraphs were also read and checked
against the displayed formulas; the final general theorem needs only
sufficient characteristic periods. Source novelty and a formal proof
of the whole manuscript are outside this assessment. No assigned file
or mathematical section in the table was left unread.

## Findings and attempted refutations

**Assigned family arguments: accepted within this stated contributor
scope; no unresolved membership or eventual-periodicity gap identified.**
This scoped finding does not confer a repository review approval or
independent scientific acceptance. The following are the concrete checks
behind it, rather than an inference from previous diagnostic passes.

1. **Even multiples, lines 62-220, 222-388.** Recomputed all regular,
   extra/regular and extra/extra categories, including the possible zero
   reduced value at f=5. A candidate cannot assume a whole protected
   block before excluding repeated g or beta_0: the proof instead uses
   earlier positive factors and establishes their uniqueness at the
   actual scan time. At k=3 the initial F_1/B_1 overlap loses only a
   negative endpoint; the later self-overlap loses a lower point repaired
   by F+C_1. The shortest B run has two entries at f=5, so no hidden
   singleton deletion occurs. The beta induction and final carry-one
   obstruction give the stated K and 2K bounds. The cleanup at i=2
   crucially requires different blocks. The reduction in [lemmas.md](lemmas.md)
   records the exact dependency recurrence and retains this guard.

2. **Upper boundary, lines 53-161, 163-229.** Checked every negative,
   even and carried odd cell in the auxiliary symmetric set. At f=4,
   the delicate comparison is 2<f-1, still strict. The only unwrapped
   hit is g+g=w and its reflected hit is w+w=m+g; neither survives
   in the recurring set after deleting w. The initial exceptional
   targets are separately safe by size, not merely by residues.
   At k=2,n=1 the F_1 self-sum really loses the upper low-gap endpoint
   f-1, which is supplied by the distinct u+w pair. The after-A_*
   self-sum has precisely the stated trimmed range. The other witnesses
   use disjoint initial pieces or different actual blocks.

3. **Upper rays, lines 53-172, 174-315.** Recomputed the envelope
   collision classes, including f=3,b=2 where coordinates need not be
   canonical within an f-cell. The bounds compare actual coefficient
   differences, so crossing c=f does not create an omitted case. Only
   u+u can hit the protected core; its unique initial occurrence is
   established causally. Low-gap witnesses use F_k+B_i, and the two
   endpoint losses of the initial F_k self-sum are repaired or are the
   permitted A_(k-1) when b=1. At block three, the only surviving
   obstruction would use X_2[1] twice, but that set has at most one
   actual entry. Treating equal residues in different blocks as equal
   integers would be invalid; the argument does not do so.

4. **Plateau corner, lines 39-135, 137-192.** Recomputed the 28 regular
   sum rows, seven v rows, seven indexed x_j rows, and the exceptional
   lifetime sum {0,1}+{0,1}+1={1,2,3}. At f=4, D is a singleton and
   the pre-carry B+D interval is empty; the table keeps the carried
   part and never uses an ordinary D self-pair to assert distinctness.
   The three x_j+D witness intervals have one element each at f=4
   and are adjacent. Initial strict B+B still bridges the G5 gap:
   its upper endpoint 12f+1 meets the next range starting 11f+5
   when f=4. Selected x_0[1],x_2[1] are protected by the two missing
   diagonal E self-sums; delayed U cannot supply an earlier obstruction.

5. **First quotient j=1,2, lines 75-151.** The two D endpoints each
   have one actual occurrence, which justifies trimming both extreme
   doubles even though interior residues recur. All four later gaps
   use a fixed initial D and a guaranteed later component; block one
   uses an actual strict D self-sum. The domain f>=j+2 includes f=3,j=1
   and f=4,j=2. The primitive-period exception at f=4,j=1 is preserved.
   Lines 189-191 compress the exact-gap-preperiod justification: it can
   be made explicit by comparing the incoming gap to the first C entry,
   f+1 initially versus f+2 in the tail. This supplies the same-phase
   mismatch for the stated preperiod; it is not an unresolved gap in
   the membership or eventual-periodicity assertion.

6. **Offset one, general quotient, lines 67-189, 191-308.** Checked the
   six tail-pair categories, six mixed categories, all beta/gamma pair
   lifetimes, and the selected block-one gamma targets. An initial
   C+C zero-offset representation of such a target would repeat the
   sole lower C_1 endpoint. No later missing A endpoint is silently
   used for coverage. The repaired gamma_i gap in lines 273-279 uses
   lower C_1[0] plus lower C_(i-1)[n-1], with different blocks even
   at i=2. The block-one repair instead uses two different endpoints
   of C_1. The quotient-two proof's lines 81-99 use F_0+C_0, not the
   failed F_0+F_1 repair, for the first missing self-sum endpoint.

7. **Endpoint g=4f, lines 33-135.** Checked all 15 regular and 15
   mixed residue bounds, the three exceptional pairs, and every gap
   witness. In particular the missing first point of the initial C_0
   self-sum is u+D_0. The f=4 relaxation is sound: carried E+E starts
   exactly at 8f+1, an omitted point. At f=3 it instead hits the
   selected D residue, so that extension is rightly rejected.

8. **Odd multiples, lines 66-172.** Read the full cell/reflection
   exclusion, both exceptional rows and every indexed gap witness.
   Checked k=1 separately: A_* is the first run, the two missing B
   endpoints belong to the same gap, e lies in D, and the two repairs
   overlap. In the f>=3 membership extension, any negative bound f-4
   means no carry, not a selected negative coordinate. Its refusal to
   import the primitive-period argument is necessary at f=3,k=1.
   The reflection lemma in [lemmas.md](lemmas.md) removes the separate
   v+R case analysis because v=m-u.

9. **Band/transition, lines 39-272, and relaxations.** Checked all 18
   band residue rows, all 22 transition rows, exceptional target safety
   and every complete-gap interval. At (f,j)=(2,3), a later crossing
   interval begins exactly at the new block boundary. The new domain
   appendix explicitly corrects the old strict wording to 'at or below'
   (lines 142-145), so this equality is not a remaining defect. Tail
   B,C singletons are only paired with disjoint actual sets. At the
   transition f=4, A+A fills G1 exactly; all other containments still
   hold. The failure at the next band endpoint j=2f is preserved.

10. **Offset-one f=4 and remaining relaxations.** Checked the new A+A
    alignment at offset -4 and the A+C equality at offset -2 by their
    actual indices, rather than reusing a false strict distance bound.
    The explicit g=17 formulas and all seven gap rows are consistent.
    The high-plateau f=4,b=3,k>=3 relaxation uses the two surviving
    endpoints of B_k with a length-four anchor; it never requires two
    points from the singleton B_2. The excluded k=2 corner has its own
    argument. Full U2 chronology is the parent's separate audit scope.

## New framework reading and correction request

The new parent framework was additionally read at initial SHA-256
`F0B0CA784AE52249EB957E43C9F616D792ACD97F7371985CB9A32676579F1E13`,
lines 1-289. Its generalized cylinder identity (3), exact lifetime
identity (6)/(7), positivity induction, anchor lifting and acyclic
feedback proof were checked directly.

A real hypothesis omission was found in its rectangle specialization
(4), lines 86-95. For an empty residue interval I=[1,0] and A=[0,1],
the cylinder is empty but the second displayed row is {1} times {2,0},
which has nonempty image. Discarding empty output rows does not repair
this. The parent was asked to require nonempty input intervals or make
the entire result empty before forming the rows. The same explicit
nonempty guard was requested for ordinary endpoint addition at line149.
The generalized set identity (3) itself has no such defect.

The first feedback hypothesis should also state n>=s_i explicitly.
With that reading, no circularity or off-by-one error was found: the
partial core removes its obstructing endpoint from block F_i; only
then does the core become full from F_i+1. Lower cutoffs are
F_i=2i+1,B_i=2i+2; upper reverse-order cutoffs are
F_i=3(k-i)-2,B_i=3(k-i)-1 with the separate top base 1,2.
The patched parent framework was rechecked at SHA-256
`194B05937267A6A90C6B680FC1B17CDD7BE3C129D8C2E4BF2FAE74BBA877A4B4`.
It explicitly makes (4) inapplicable to an empty input, restricts
ordinary endpoint addition to nonempty intervals, and states n>=s_i.
These changes repair the reported defect and remove the threshold
ambiguity. No unresolved issue was found in the framework's mathematical
statements within this reading.

## Source recheck and bounded search

Reopened the [primary arXiv record](https://arxiv.org/abs/2609.18522)
and [v1 full text](https://arxiv.org/html/2609.18522v1), specifically
Definition 3(2),(4),(5), the small-parameter corrections and Conjecture 5.
The visible submission history listed v1, dated 16 September 2026.
The displayed period functions are conjectural predictions, not proofs
of the audited extensions. Source coordinates use d=g-f; the local
offsets in g=2kf+a must be converted before comparing formulas.

The two targeted queries were `"2609.18522" periodicity proof` and
`"van Berkel" "Bosma" "2-sumfree" periodicity proof`. The returned
primary results were the two already inspected arXiv papers; no later
primary proof was identified in this bounded result set. Aggregator and
social-index hits were not treated as mathematical evidence. This is
not a comprehensive novelty search. Previously recorded inaccessible
historical full texts remain uninspected; no absence-of-prior-proof claim
is made. The parent owns the broader current-source check.

## Checks, limits and handoff

No old diagnostic, checker or derivation writer was executed. No new
greedy enumeration, installation, paid run, network publication or
external contact occurred. The mathematical checks here are contributor
reading and explicit algebra, not independent runs. Process CPU time
and peak memory were not separately measured for read-only file access.

Checked: the twelve frozen hashes above and the additionally identified
framework version. Action: local audit and optional proof consolidation,
with no submission. Results: no unresolved gap found in the assigned
family membership/periodicity arguments; one concrete framework
empty-input defect reported for correction, with exact counterexample.
Limits: parent-owned families, historical novelty and independent human
review are outside this assessment. Outcome: the assigned-family audit
is complete within scope, the framework correction was rechecked, and
the new consolidation was reread with an explicit l>=2 guard on its
beta recurrence. Human screening and manual submission remain pending.
