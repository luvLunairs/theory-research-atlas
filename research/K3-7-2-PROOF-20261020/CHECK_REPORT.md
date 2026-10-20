# Check report

Checked: `K3-7-2-PROOF-20261020`, identified by [MANIFEST.json](MANIFEST.json),
SHA-256 `1db66968f948cf57b2af0056308da2e65946b1f81925c6ee210376e141183be6`. The manifest covers 34 payload files;
the directory contains 36 files, including the manifest and this report.

Action: publish a presentation-only documentation revision.

## Retained scientific checks

The [positive replay](proof/verification.json) completed in 149.953 seconds.
It regenerated 4,753 scalar rows, 33 integer Gram columns in 16 blocks,
101 identities, 4,294 orbit bounds and 4,295 aggregate coefficients,
obtaining the manuscript's strictly negative rational bound.

The separate direct-distance checker verified the 34 codewords against
all 2,187 ambient words: no uncovered words, with nearest-distance counts
34, 467 and 1,686 at distances 0, 1 and 2. The words printed in the
manuscript matched the witness file and passed the same exhaustive check.

The [four negative controls](proof/negative-controls.json) passed in
149.891 seconds: three malformed word inputs and an altered Gram factor
were rejected. The latter test bypassed only the initial checksum, so
exact coefficient reconstruction detected the corruption.

Contributor readings checked the constraint families, normalizations,
orbit counting and structural lemmas. Corrections clarified five-point
digit order, the lifting lemma's integer hypotheses and the radial-origin
average. Source checking corrected the thesis pages to 53–59 and added
the upstream MIT notice. Coefficients and orbit bounds independently
reproduced the final rational expression; source-map and replay-source
digests matched. Python/JSON parsing, equation numbering and rejection
of optimized Python execution passed.

## Documentation revision

The manuscript, reproduction instructions, every file under `proof/`,
and the licenses are byte-identical to the previously checked version.
The shortened documentation preserves the results, credit and review
limits. Current manifest and source-digest checks passed. The separate
coverage checker again verified all 2,187 words with no holes. Repository
validation passed all 208 tests, 628 generated views and documentation
checks covering 874 text files and 20,127 links.

## Limits and outcome

The interval is **30–34**, with exact value unresolved. These are
AI-assisted contributor checks, not a proof-assistant formalization or
independent scientific acceptance. The reported human preliminary pass
has unspecified scope. Priority and significance remain unassessed;
the literature comparison used arXiv v2 because the final IEEE text was
unavailable through the inspected route. The package remains a research
draft available for independent assessment.
