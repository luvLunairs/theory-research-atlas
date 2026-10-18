# Research artifacts

Retain the evidence for contributed attempts and reviews here. Use a directory named for the record, such as `research/ATT-<identifier>/`, and give each retained proof, program, certificate or dataset a clear version. Drafts belong in `work/` until they are ready for inclusion.

For each contribution, include the exact claim, instructions for reproducing the result, required tools and versions, expected output and known limitations. Preserve author credit, source citations and applicable licenses. Keep large external datasets at an authorized, versioned location when a repository copy is unsuitable; record access requirements and the evidence necessary to reproduce the work.

Reference each file from its [attempt or review record](../docs/maintaining.md) and include its version and SHA-256 digest in `artifact_manifest`. Local references are relative to the repository root. Preserve earlier evidence when a claim changes so that readers can identify what each review examined. External references need an exact version; unavailable checksums remain explicitly unknown.

Git newline conversion is disabled for this directory to preserve recorded file bytes across platforms. Compute the checksum from the retained file, and change its manifest only when intentionally recording a new version.

The [progress page](../docs/progress.md) links recorded work and its review status. A proposed method and a verified result have different evidential status; label each contribution according to the work and checks actually completed.
