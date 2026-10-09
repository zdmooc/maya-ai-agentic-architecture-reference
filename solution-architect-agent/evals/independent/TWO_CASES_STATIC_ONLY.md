# D099 AA3 — two independent *synthetic* packets

`NOTIFY-01` and `INVENTORY-02` are intentionally fictional,
non-client, no-runtime scenarios. Both are available in the static
`independent/prepare_case.py` allowlist. The offline review CLI accepts
`--fixture-name` for exactly these two files, plus a SHA-256 expected
from an independent fixture approval.

Tests ensure both cases pass when provided with separate *synthetic*
matching facts/candidate structures, while cross-pairing evidence from
one with the other fails mission identity and repository mapping.

This is a **harness test, not two LLM benchmark successes**. No model
has read these prompts as part of this change. No independently
reviewed reference answers are published, no tool-side OpenCode
trajectory captured, no architect has scored the two designs.
Existing historical mission fixtures are untouched.
