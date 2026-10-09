# D-099 AA3 — 2026-10-09 first real source extraction: structured-output retry

Measured **real HP** first run at 8K, Qwen3.5 9B:
- Ollama 0.35.1, host-only `192.168.56.1:11434`
- `status=AA3_LOCAL_FACT_GATE_FAIL`, **not a source-quote failure**
- The returned four quotations were verbatim and contained
  `NOTIFY-01`, `lab/notification-api`, `lab/event-relay`
- But the model omitted `mission.value`, both `repository.repository`
  fields and emitted **two** mission facts instead of one
- Violations: `MISSION_FACT_COUNT_INVALID`,
  `MISSION_ID_MISMATCH`, `REPOSITORY_NOT_IN_TRUSTED_INVENTORY`,
  both `REQUIRED_REPOSITORY_FACT_MISSING_OR_DUPLICATE`
- 231 generated tokens, 475 prompt tokens, 181.05 sec total
  (24.79 sec loading), Ollama `ps`: 11 GB, 44%/56% CPU/GPU,
  context 8192; RAM free 14.98 GiB.
- The preexisting `__pycache__` directory is untracked noise, not
  a Git conflict; a new scoped `.gitignore` prevents recurrence.

**Code adjustment:** The next one-turn local probe still uses
`num_ctx=8192` and `num_predict=384`, `think=false` and zero
agent tools, but supplies an Ollama `format` **JSON Schema** with
maximum 1+N fact slots (empty response permitted when ungrounded) and six REQUIRED fields per fact
(`id,kind,source_id,quote,value,repository`). Empty `value` for
repository facts and empty `repository` for mission fact are explicit.
The prompt separately demands *exactly one* mission and one fact per
trusted repo. Schema itself does **not** pin real repo names or accept
a source quote as fact automatically; deterministic `evaluate_facts`
still checks quotes, owners and mission identity.

No silent repair of the first output, no second automatic inference,
no AA3 closure, and no runtime/CRC tool. CI adds a regression that
replays the *malformed actual output* and expects a FAIL; passing synthetic
checks never counts as a live model benchmark result.

**Operator rerun** in `/c/workspaces/D099-AA3-HUB`:

```bash
git status --short
git pull --ff-only
D099_ALLOW_LOCAL_INFERENCE=YES python solution-architect-agent/evals/local_aa3_fact_probe.py --case notification_case.json
ollama ps
```

*Do not upgrade to 16K/64K on the strength of JSON formatting.* A
successful retry is only `AA3_LOCAL_FACT_GATE_PASS`, not proof of
architectural requirements, solution comparison or review acceptance.
