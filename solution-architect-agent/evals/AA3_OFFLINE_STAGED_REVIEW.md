# AA3 — Connected offline fact-first review (candidate and facts provided by caller)

**Scope:** fictional NOTIFY-01 only. No real client/repository connection.
`staged_review.py` calls **both** `grounding_gate.evaluate_facts` and
`decision_gate.evaluate_design` against the same pinned source packet.
It fails closed for missing repo facts, unknown repo names, invented source
IDs, wrong mission ID, invalid JSON Schema, duplicate options, premature ADR
approval and runtime evidence overclaims. Result
`AA3_OFFLINE_PRECHECK_PASS` means **only** ready for a separate human
review, never `ARCHITECT_REASONING_VALIDATED`.

The tool accepts candidate JSON and fact JSON **generated elsewhere**.
It makes **no Ollama/OpenCode call**, executes no tools or shell, and does not
modify source data. Input paths are local and capped at 256 KiB.
Before a real blinded evaluation, an independently reviewed commit/fixture
digest must be approved out of band (the `--expected-fixture-sha256` flag
is an equality check, not proof of a trusted approval).

Usage after producing `facts.json` and `candidate.json` offline:

```bash
python solution-architect-agent/evals/staged_review.py \
  --facts /tmp/facts.json --candidate /tmp/candidate.json \
  --expected-fixture-sha256 <sha256_of_approved_notification_case.json>
```

Synthetic integration tests produce their own fake facts/candidate; no
reference is leaked to any model. The two-case independent,
source-grounded model benchmark, scored architectural review, external
tool trace and permissions enforcement are still pending.
