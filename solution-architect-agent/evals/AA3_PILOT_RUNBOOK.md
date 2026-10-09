# D099 M3 — AA3 source-frozen two-case pilot, one local invocation

This is a **pilot** for DAAROPS Operator-first and IT-EXPLORER SQY CaaS; it does NOT count toward the final AA3 `ARCHITECT_REASONING_VALIDATED` gate without independent source-review, tool trajectory capture and signed human benchmark score.

Two inputs under `evals/frozen/` are **exact source text snapshots** from the canonical `cadrage_202682030` main commit `4e9634616f6d30ecd632f09e29a04b29eb907792`; source Git blob SHA is verified offline before a prompt is constructed. The model sees only its mission case, source snapshot and schema; no golden fixture. These snapshots are not current live repo audits. Do not promote historical evidence into new runtime claims.

The orchestrator runs **both cases sequentially** in separate ephemeral non-Git directories under an explicitly chosen output folder, with existing OpenCode `--pure --agent plan --format json`, one approved local Ollama provider and deny-only **requested** tool permissions. It requires explicit `D099_ALLOW_LOCAL_INFERENCE=YES`. It does not execute arbitrary tools, install packages, mutate product repositories/CRC, invoke GitHub, or download another model.

## Windows Git Bash — after cloning/checking out architecture PR #4

```bash
cd /c/workspaces
git clone --branch d099-aa0-aa2-method-contracts --single-branch \
  https://github.com/zdmooc/maya-ai-agentic-architecture-reference.git D099-AA3-HUB
cd /c/workspaces/D099-AA3-HUB

python solution-architect-agent/evals/run_aa3_pilot.py \
  --case both --out /c/workspaces/D099-AA3-EVIDENCE-001 --dry-run
```

The prior environment variables `OPENCODE_CONFIG_CONTENT` and `OLLAMA_HOST` should remain in the **same terminal** as the existing isolated OpenCode test; check they are set without printing any credentials. The inline config must have `enabled_providers=["ollama"]`, a single local Ollama provider, `permission.*="deny"`, `agent.plan.permission.*="deny"`, sharing disabled, and updates disabled. The **resolved** OpenCode policy previously had a late `external_directory allow` entry, so this precondition verifies requested deny rules only; it does **not** count as full denial enforcement. Run only under a user-approved isolated local operator account, with no secrets in prompts.

```bash
D099_ALLOW_LOCAL_INFERENCE=YES \
python solution-architect-agent/evals/run_aa3_pilot.py \
  --case both --out /c/workspaces/D099-AA3-EVIDENCE-001
```

Outputs (local-only, do not automatically upload): `daarops.events.jsonl`, `daarops.candidate.json`, `sqy.events.jsonl`, `sqy.candidate.json`, `summary.json`. No automatic retry on failure; choose another destination folder for a rerun. The pilot's exit code 2 signals a missing/invalid schema, malformed response or failed static precheck — investigate the report rather than altering source references.

The model `qwen2.5:3b` advertises 32,768 tokens, **below** the planned >=64k model-context target; it may not successfully produce a full JSON architecture assessment. Record that limitation, not a made-up 64k result. `jsonschema` is necessary for offline structural scoring; if unavailable, the pilot preserves JSON and marks `JSONSCHEMA_UNAVAILABLE`.

Full AA3 still needs version-locked live source access through the governed real MCP gateway, independent runtime tool-call audit (not model-supplied), qualified context, baseline review and human scoring >=85/100 on each case with no severe policy violations. A golden fixture match alone does not qualify.
