# Verification specifications

Store one `VSPEC-*.json` file per fixed verification specification. The filename must match its ID. A specification identifies the exact claim and scope, retained target and definitions, checker version, locked environment, execution protocol and trust assumptions. It links a problem's current statement digest and records a named human decision on correspondence, protocol and trust.

The scientific specification digest excludes approval metadata, revision history and artifacts used only for approval. Target, checker, environment and protocol artifacts always remain in the digest, even when also cited by the approval. A changed scientific digest requires renewed approval and verification. Keep older records and their evidence; they do not confer a badge on a changed target.

Use the [machine verification guide](../../docs/machine-verification.md) and [verification specification schema](../../schemas/verification-spec.schema.json). Put incomplete drafts in `work/`. Approval metadata records a decision; repository validation cannot authenticate the reviewer or perform that review.

There are no approved specifications in the collection yet.
