# Checks for the English proof submission

Checked: `K3-7-2-PROOF-20261020`, bound by `MANIFEST.json`, SHA-256
`508605a30e21193404aa2a0e7ca3258cddd59f2cb05323c11b9c32bf742bb005`.
The manifest covers 34 payload files totaling 1,163,868 bytes,
excluding itself and this report. The complete directory has 36 files.
The final manuscript SHA-256 is
`9553f74dccf42c5e5ee64eaaea7957db8e02fad8133f16b98844bc224cbf0d9c`.

Action: publish this checked 36-file research contribution for Q-CODE-202
on `codex/k3-7-2-proof-submission` and open a draft pull request to
`luvLunairs/theory-research-atlas`, targeting `main`. The maintainer
explicitly authorized submission on 20 October 2026; the
[assistance note](ASSISTANCE.md#maintainer-recognition-review-report-and-authorization)
records that instruction, configuration recognition, and reported
preliminary human-review pass. No merge or scientific acceptance is
part of the action.

## Scientific checks

- The byte-preserved primary checker completed a fresh replay in the
  new package directory in 149.953 seconds. It regenerated all 4,753
  nonzero scalar rows, 33 nonzero integer Gram columns in 16 blocks,
  101 identities, 4,294 orbit bounds, and 4,295 aggregate coefficients.
  The exact negative rational estimate matched the manuscript.
- The separate direct-distance checker again checked the known
  34-word set against all 2,187 words: zero uncovered words and
  nearest-distance histogram 34, 467, 1686 for distances 0, 1, 2.
- Fresh negative controls passed in 149.891 seconds. Three malformed
  word witnesses were rejected. A changed Gram-factor entry was
  rejected by exact coefficient reconstruction after the initial
  certificate checksum alone was bypassed in memory. The original
  certificate remained unchanged.
- Separate contributor readings checked every used scalar/Gram
  family, normalization, stabilizer formula, radial counting with
  repeated rows, Fourier normalization, and the structural lemmas.
  They found no error in the lower-bound argument and identified
  presentation corrections: explicit five-point digit order,
  integer parameters for the lifting lemma, and a clearer origin
  average in the radial formula. These corrections were applied.
- Source checking corrected the thesis page range to 53–59 and
  identified the upstream MIT notice for the retained legacy formula.
  The notice was added. The finite construction retains its
  Östergård–Hämäläinen credit.

The executable checker, main certificate, bounds, and actual 34
codewords are unchanged from the earlier checked draft. The new
mathematical prose is an expanded explanation of those objects.

## Final prose and package checks

The corrected five-point encoding, integer hypotheses of Lemma 12,
and radial-origin explanation were reread after amendment. A second
contributor review checked the corrected mathematical wording against
the explicit constraint specification. The bibliography and MIT notice
were reread after correction. Subsequent changes to the manuscript
only replaced a directory link with the checker file link and made
one TeX spacing command explicit to remove trailing whitespace.

The words printed in Section 8 were extracted from the final Markdown,
compared in order with `proof/known34.txt`, and separately checked
against all 2,187 words. The results match the printed table.
Equation tags 1–29 are complete and unique, and the display-math and
code fences are balanced.

All 16 source-map entries match the distributed file digests.
All mathematical inputs and checker Python files were compared
byte-for-byte with the earlier checked package. All 11 source hashes
in the fresh positive report match the actual checker sources.
The exact final rational expression was separately recalculated from
the aggregate coefficients and orbit bounds using `Fraction`.
All Python files parsed, all JSON files loaded, and optimized Python
execution was checked to be rejected.

The four agents' application-recorded model/effort metadata was
refreshed read-only. Every inspected context has `gpt-6-astra` and
`ultra`, with provider `openai`. Public files contain no detected
host-specific absolute paths or private-key markers. The upstream
license is byte-identical to its retained original. The source map
omits two historical certificates not needed by this package;
their originals remain in the earlier version.

`verify_manifest.py` passed on the delivered inventory and hashes.
The local `.gitattributes` disables text normalization for this
directory, preserving exact input and report bytes across Git checkouts.

## Checks of the preceding proof revision

`python scripts/check.py --render` passed data integrity, 208 regression
tests, rendering of 609 views, and the generated-view comparison.
Its documentation step identified three directory links rejected by
the repository's file-link checker. They were replaced with file links
or plain directory references.

The affected documentation check was rerun and passed: 880 text files
and 19,177 local/repository Markdown links. The final manifest and
package checks were also rerun after these edits. Existing tracked
files and earlier drafts in the isolated checkout were unchanged.
The original working checkout's unrelated user edits were preserved.

## Final submission recheck

The remote default branch was inspected on 20 October 2026 and identified
as `main` at `45c0a5184062519b89be6367220855ba7e0bca8f`. No open pull
request or existing Q-CODE-202 discussion was found. A separate local
checkout was prepared from that base, carrying only this 36-file package.
The earlier 42-file exploratory contribution is not in the proposed
branch history or diff.

Only the README, assistance note, model action metadata, manifest, and
this report differ from the preceding proof revision. Every mathematical
input, checker, retained computational report, license, reproduction
instruction, and the manuscript remains byte-identical to the checked
version at local commit `1f10bf359d838e62ec2c6c3daa428a4bc06bc5bb`.
The previous exact scientific replays therefore apply to the same bytes.

The final package check confirmed the 36-file inventory, the limited
administrative differences, all 16 source-map digests, all 11 replay-source
digests, the unchanged scientific bytes, and the unchanged license.
The words printed in the final manuscript were again extracted and
checked by the separate coordinate-comparison implementation against
all 2,187 words: 34 centers, zero uncovered words, and nearest-distance
counts 34, 467, and 1686. The strict rational bound was independently
recomputed from the retained coefficients. Python and JSON parsing,
optimized-mode rejection, equation numbering, and the public-text
path/key-marker scan passed.

In the focused checkout, `python scripts/check.py --render` passed:
data integrity, 208 tests, 609 rendered views, generated-view consistency,
and documentation checks of 844 text files and 19,181 links. A separate
contributor read checked the attribution and the translations of the
maintainer's statements; its one wording correction was applied.
The final documentation and manifest checks were repeated after the
administrative amendments. Git whitespace checking allows the retained
CRLF endings. It reports a pre-existing final blank line in each of
`LICENSES/CC-BY-4.0.txt`, `manuscript.md`, and
`proof/lib/audit_fivepoint.py`; these byte-preserved files were not
rewritten solely to remove that formatting.

## Limits

The resulting interval is 30–34, with exact value unresolved. The
finite certificate computation is part of the proof. This is neither
a proof-assistant formalization nor the project's approved “Machine
checked” status. The recorded checks are AI-assisted contributor
checks. The maintainer has separately reported a preliminary human-review
pass; the readers, exact coverage and detailed findings were not supplied.
Neither independent external review nor full-text scientific screening
is inferred. Priority and significance are not certified. The final IEEE
article remains unavailable through the inspected public route; the
cited full-text comparison is arXiv v2.

Outcome: ready for the authorized draft submission and independent
scientific assessment, subject to the execution approval gate.
Preparing this report does not establish that publication has occurred.
