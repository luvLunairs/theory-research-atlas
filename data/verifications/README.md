# Verification runs

Store one `VER-*.json` file per actual verification execution. The filename must match its ID. Each run binds a specification digest, an attempt digest and the submitted result artifacts, with a named runner, command arguments, execution time, outcome, retained certificates, logs and check evidence.

Use the [machine verification guide](../../docs/machine-verification.md) and [verification run schema](../../schemas/verification.schema.json). Record failed, inconclusive and error outcomes as well as successful runs. Incomplete drafts belong in `work/`; preparing a draft does not count as execution.

`Machine checked` is derived from an approved current specification and admissible verification evidence. It is not a stored verdict, a human review label or a claim that validation reran the checker. Conflicting reruns of the same certificate remain visible. No scientific code runs when these records are loaded or rendered.

There are no verification runs in the collection yet.
