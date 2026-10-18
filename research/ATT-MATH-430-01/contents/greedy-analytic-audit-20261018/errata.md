> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Wording corrections governing the incorporated appendices

18 October 2026. These corrections are part of the revised proof. The
sealed source files remain unchanged for version comparison. None changes
a selected set, interval identity, parameter domain or sufficient period.

1. In [f2-three-blocks.md](../greedy-analytic-20261018/small/f2-three-blocks.md),
   lines 82–83, replace the ambiguous disjointness sentence by:

   > The residue sets I, A, B, C, {s} and {v} are pairwise disjoint.
   > The distinguished residue z=min I is a member of I, not a separate
   > disjoint component; its occurrence in block one is treated separately.

   The existing decomposition of z's lifetime as {0,1} and of
   I minus {z} as {0} is unchanged. An initial z is not counted twice.

2. In [f3-zero.md](../greedy-analytic-20261018/small/f3-zero.md),
   lines 267–270, replace the summary of distinctness by:

   > Every specified summand belongs to its declared candidate block.
   > Same-residue factors use different blocks except for the pair of
   > different entries in x[1] and the pair s[1],u[1]. These latter
   > points have row indices 1 and 3k-1 in residue 4, so they are
   > different for k>=5. All other pairs have different residues or
   > explicitly different actual entries. Every summand is positive.

   This includes the exceptional pair already checked in the preceding
   coverage argument instead of accidentally omitting it from the summary.

3. In [f4-zero-exclusion.md](../greedy-analytic-20261018/small/f4-zero-exclusion.md),
   lines 190–192, replace the sentence beginning "Two nonseed terms"
   with:

   > Two terms other than the first seed 4 cannot hit these low
   > progressions, except through the double of the second seed 8k;
   > that pair repeats an actual summand and is forbidden.

   Each term other than 4 is at least 8k; only the inadmissible
   double 8k+8k can reach the indicated low endpoint. This also
   removes the ambiguity of "nonseed" in the original sentence.

These are scoped contributor corrections, not human-review or
machine-verification approvals. The concrete mathematical failures of
broader formula extensions are recorded separately in [findings.md](findings.md).
