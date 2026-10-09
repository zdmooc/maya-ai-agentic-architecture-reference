# D099 M3 — AA3 source-frozen two-case pilot, one local invocation

This is a **pilot** for DAAROPS Operator-first and IT-EXPLORER SQY CaaS; it does NOT count toward the final AA3 `ARCHITECT_REASONING_VALIDATED` gate without independent source-review, tool trajectory capture and signed human benchmark score.

Two inputs under `evals/frozen/` are **exact source text snapshots** from the canonical `cadrage_202682030` main commit `4e9634616f6d30ecd632f09e29a04b29eb907792`; source Git blob SHA is verified offline before a prompt is constructed. The model sees only its mission case, source snapshot and schema; no golden fixture. These snapshots are not current live repo audits. Do not promote historical evidence into new runtime claims.

Windows Python must invoke a **native PE** rather than the npm Git Bash shim. The runner now resolves `opencode.exe` from the npm package or its installed Windows optional dependency, verifies a real `MZ` executable over 1 MB to avoid npm's placeholder, and never passes mission Markdown to `cmd.exe` or `shell=True`. A missing native binary produces a diagnostic in `--dry-run` and a structured `LOCAL_PILOT_WINDOWS_LAUNCH_BLOCKED` status rather than a traceback. **No install/reinstall is performed.** If native binary detection fails, inspect `npm root -g` and platform package before taking action. The earlier `SOURCES_PINNED_NO_MODEL` preflight did not check the executable; it confirmed only input integrity.

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

If `OPENCODE_CONFIG_CONTENT` is already set, the runner validates its restrictions before use. If absent, the runner **creates its own restrictive, local-only inline OpenCode config** from the explicitly allowlisted `OLLAMA_HOST` value (`192.168.56.1:11434` on the tested HP). It never uses the globally installed providers as an unrestricted fallback. Do not paste secrets into the shell. The inline config must have `enabled_providers=["ollama"]`, a single local Ollama provider, `permission.*="deny"`, `agent.d099-evaluator.permission.*="deny"`, sharing disabled, and updates disabled. The **resolved** OpenCode policy previously had a late `external_directory allow` entry, so this precondition verifies requested deny rules only; it does **not** count as full denial enforcement. Run only under a user-approved isolated local operator account, with no secrets in prompts.

```bash
D099_ALLOW_LOCAL_INFERENCE=YES \
python solution-architect-agent/evals/run_aa3_pilot.py \
  --case both --out /c/workspaces/D099-AA3-EVIDENCE-001
```

Outputs (local-only, do not automatically upload): `daarops.events.jsonl`, `daarops.candidate.json`, `sqy.events.jsonl`, `sqy.candidate.json`, `summary.json`. No automatic retry on failure; choose another destination folder for a rerun. The pilot's exit code 2 signals a missing/invalid schema, malformed response or failed static precheck — investigate the report rather than altering source references.

The model `qwen2.5:3b` advertises 32,768 tokens, **below** the planned >=64k model-context target; it may not successfully produce a full JSON architecture assessment. Record that limitation, not a made-up 64k result. `jsonschema` is necessary for offline structural scoring; if unavailable, the pilot preserves JSON and marks `JSONSCHEMA_UNAVAILABLE`.

Full AA3 still needs version-locked live source access through the governed real MCP gateway, independent runtime tool-call audit (not model-supplied), qualified context, baseline review and human scoring >=85/100 on each case with no severe policy violations. A golden fixture match alone does not qualify.

## October 9, 2026 — AA3 Windows native launcher resolved; OpenCode exits 1 with zero stdout

The operator ran both cases from the native PE launcher (preflight reported
`NATIVE_BINARY_RESOLVED_NO_MODEL`), but both returned `opencode_exit_code=1`
and `*.events.jsonl` files had exactly zero bytes. **No JSON events are
available and the previous script discarded captured stderr.** This is
not an observed LLM benchmark failure, but an OpenCode invocation diagnostic
gap. Do not repeat DAAROPS/SQY until a short transport smoke succeeds.

The runner now provides `--smoke-only`: one short text turn with the exact
approved local Ollama configuration, native Windows PE, `--pure`,
`--format json`, and `--agent plan`. It does not construct either mission
prompt or load the provisional answers. Both smoke and benchmark now use a
single process builder, without optional `--title`, to avoid CLI compatibility
ambiguity. Diagnostic reports contain **only fixed error categories, stdout/
stderr byte counts and SHA-256 of stderr; raw stderr, argv, prompts, local
paths and tokens are not logged in summary.json**. The local
`smoke.events.jsonl` file may still contain model text; inspect before
sharing. No automatic retry.

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only origin d099-aa0-aa2-method-contracts
export OLLAMA_HOST=192.168.56.1:11434
D099_ALLOW_LOCAL_INFERENCE=YES env -u OPENCODE_CONFIG_CONTENT \
  python solution-architect-agent/evals/run_aa3_pilot.py \
  --smoke-only --out /c/workspaces/D099-AA3-SMOKE-003
cat /c/workspaces/D099-AA3-SMOKE-003/summary.json
```

If `LOCAL_OPENCODE_SMOKE_TRANSPORT_PASS` is observed, **only then** perform
two-case pilot with a brand-new output path; the target model remains below 64k.
If failure persists, the classified `stderr_categories` identifies the next
single corrective action. Avoid leaking raw diagnostic logs into GitHub.

## October 9 — reproducible OpenCode Windows invocation is the priority

A manual isolated invocation on the user's HP17G3 **succeeded**:
`OPENCODE_EXIT_CODE=0`, `STDOUT_BYTES=937`, `STDERR_BYTES=0`.
It used the same resolver and child environment as the pilot, but a scratch
directory created **directly under `C:/workspaces`** and the text
`Reply exactly D099_LOCAL_SMOKE_OK. Do not use tools.`. That is a
**transport/process success**, not proof of a complete correct model answer
or the formal AA3 benchmark.

The pilot has been aligned to those two known successful conditions. New
tests assert that its execution scratch folder is directly below the output
folder's parent (not nested within the evidence output), and the run
**stops after the first nonzero OpenCode exit** instead of wasting another
full-case attempt. This is a consistency change, **not a demonstrated root
cause** of the earlier 68-byte, unclassified stderr. Existing scope, source
hash checks and deny-only policy requests remain intact.

Recheck only one case initially (not both), with a new output folder:

```bash
cd /c/workspaces/D099-AA3-HUB
git pull --ff-only origin d099-aa0-aa2-method-contracts
export OLLAMA_HOST=192.168.56.1:11434
D099_ALLOW_LOCAL_INFERENCE=YES env -u OPENCODE_CONFIG_CONTENT \
 python solution-architect-agent/evals/run_aa3_pilot.py \
 --case daarops --out /c/workspaces/D099-AA3-EVIDENCE-004
```

If its returned `opencode_exit_code=0`, inspect the structured result;
if it exits 1 again, the new `diagnostic.stderr_categories` and
`stderr_bytes` are enough to decide the next troubleshooting step.
Full AA3 remains open until actual multi-case results, trustworthy
authorization, 64k target and independent review.

## 2026-10-09 — output contract failure, not JSONL corruption (read-only boilerplate)

The operator's offline inspection of `D099-AA3-EVIDENCE-006/daarops.events.jsonl`
reported a valid **1150-byte OpenCode JSONL** stream: exactly one
`step_start`, one `text`, and one `step_finish`. The reconstructed
model text was only **229 characters**, beginning with
`You are in READ-ONLY mode. I will not make any changes to the system.`
The previous `JSONDecodeError` is correctly reporting non-JSON model text.
No architectural candidate was produced. Do **not** amend the extractor
to accept this as valid architectural output.

The built-in `plan` agent is an interactive planning profile with its
own system instructions. Its use for a strict JSON evaluator is a hypothesis
for the observed read-only boilerplate, not conclusively proven. OpenCode
allows defining custom primary agents in JSON configuration with a
system prompt and tool permissions:
https://dev.opencode.ai/docs/agents/

**Constrained corrective change:** the local pilot now requests a single
dedicated `d099-evaluator` primary agent, with a fixed JSON-only system
prompt and `permission.*=deny`. Runtime configuration validation rejects
`plan`, additional agents, any prompt substitution, changed model or
tool grants. Provider remains only local Ollama `qwen2.5:3b`.
Actual resolved permissions remain `NOT_VERIFIED_BY_THIS_CHECK`;
this is not the formal AA3 acceptance gate.

**Before re-running a full mission, test only the JSON response contract:**

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only origin d099-aa0-aa2-method-contracts
export OLLAMA_HOST=192.168.56.1:11434
D099_ALLOW_LOCAL_INFERENCE=YES env -u OPENCODE_CONFIG_CONTENT \
 python solution-architect-agent/evals/run_aa3_pilot.py \
 --smoke-only --out /c/workspaces/D099-AA3-SMOKE-007
```

A meaningful smoke pass is now
`LOCAL_OPENCODE_SMOKE_JSON_CONTRACT_PASS`, which requires
`{"probe":"D099_LOCAL_SMOKE_OK"}` as **actual JSON** in an OpenCode
text event, not just a clean process exit. If it fails, report
`summary.json` instead of launching expensive frozen full-case
prompts. If it passes, a **single** DAAROPS case can be tested with
a new folder; status `AA3_ARCHITECT_REASONING_VALIDATED=false` always
requires independent validation. Older sections of this runbook are
historical and describe the prior `plan` implementation.
