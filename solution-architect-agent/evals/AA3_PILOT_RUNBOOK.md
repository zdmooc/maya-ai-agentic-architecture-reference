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

## 2026-10-09 — deterministic 68-byte stderr after dedicated evaluator change

The user retested local `--smoke-only` after updating to the
dedicated `d099-evaluator` (`e8df54a`). Result:
`LOCAL_OPENCODE_SMOKE_FAILED`, `opencode_exit_code=1`,
`stdout_bytes=0`, `stderr_bytes=68`,
`stderr_sha256=d08708a6593b173f0e27d8ce95e079f88b566abc2e91b37def6c38b88c071a5e`.
This is **identical to earlier failures** with the built-in `plan`
agent. The new agent is not shown to resolve this transport issue. Because
no JSON event was produced, the report does not prove that the evaluator
agent actually executed. It also does not invalidate the separate
observed non-JSON read-only response from a previous successful model
turn. No full mission was started by the guarded command.

The **only change here** is durable capture of failed-process raw stderr
to a **new, local-only** `smoke.stderr.local.txt` (or
`daarops.stderr.local.txt`) inside the operator-selected output folder.
The JSON summary contains only the local filename, a sensitivity-review
flag, byte count, categories and hash, never raw stderr. Do **not** commit
or upload the file: raw OpenCode diagnostics may contain usernames,
machine paths or credentials. The file is written exclusively (`x`)
and only on `exit_code != 0`. Success never writes a stderr file.
Existing safety boundaries and one-shot behavior are unchanged.

One fresh Windows smoke execution to capture the missing 68 bytes:

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only origin d099-aa0-aa2-method-contracts
export OLLAMA_HOST=192.168.56.1:11434
D099_ALLOW_LOCAL_INFERENCE=YES env -u OPENCODE_CONFIG_CONTENT \
 python solution-architect-agent/evals/run_aa3_pilot.py \
 --smoke-only --out /c/workspaces/D099-AA3-SMOKE-009
```

If status is nonzero, **inspect locally**
`C:/workspaces/D099-AA3-SMOKE-009/smoke.stderr.local.txt` and
redact secrets before sharing its short diagnostic text. **Do not rerun
DAAROPS or SQY** until the error is identified. Successful smoke JSON
contract alone is not AA3 acceptance.

## 2026-10-09 — root diagnostic: EUNKNOWN unknown error, read

The operator finally inspected the **actual failed-process stderr**
`D099-AA3-SMOKE-009/smoke.stderr.local.txt`:

```text
Error: Unexpected error

EUNKNOWN: unknown error, read
```

This is a process-level I/O read error, **not** a JSON parse error,
provider authentication proof, or a definitive LLM problem.
The exact same 68-byte stderr signature was repeated across runs.
Direct Windows Python **heredoc** invocations with a short or full prompt
have sometimes succeeded, while calls from `python script.py` via Git
Bash frequently fail. The runner had omitted the `stdin` argument to
`subprocess.run`, therefore the native OpenCode/Bun process inherited a
possible MSYS pseudo-terminal standard input. An independent upstream
OpenCode issue describes similar Git Bash/tmux native read errors:
https://github.com/anomalyco/opencode/issues/10129
That public issue is contextual evidence, **not** proof of this machine's
exact root cause.

**One narrow and reversible fix**: `execute_local_turn()` now passes
`input=""` (text mode) to `subprocess.run`, so the child receives a new
empty anonymous pipe and EOF instead of inheriting Git Bash stdin.
The model prompt still travels only as a direct argument in argv; no
cmd.exe/shell interpolation; no new permissions or external network
providers. Regression unit tests check stdin isolation on all invocation
paths. This commit has not yet been proven on the operator's Windows runtime.

Run one fresh JSON smoke only:

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only origin d099-aa0-aa2-method-contracts
export OLLAMA_HOST=192.168.56.1:11434
D099_ALLOW_LOCAL_INFERENCE=YES env -u OPENCODE_CONFIG_CONTENT \
 python solution-architect-agent/evals/run_aa3_pilot.py \
 --smoke-only --out /c/workspaces/D099-AA3-SMOKE-010
```

If `LOCAL_OPENCODE_SMOKE_JSON_CONTRACT_PASS` appears, follow with a
single frozen architecture case in a new output directory, not both;
if `exit_code=1` remains, inspect the new local stderr and investigate
additional inherited OS handles only based on that evidence. Full AA3
cannot be marked validated by this smoke alone.

## 2026-10-09 — full mission run: OpenCode PASS, schema-vs-instance confusion

User confirmed frozen DAAROPS case `D099-AA3-EVIDENCE-011` ran with
`opencode_exit_code=0`, `stdout_bytes=14171`, `stderr_bytes=0`
on the HP17G3 after isolated stdin. `LOCAL_PILOT_OUTPUT_INVALID`,
`JSONDecodeError`, `NON_JSON_MODEL_TEXT` persists.

**Offline JSONL inspection (read-only)**: 14,174-byte trace,
`step_start=1`, `text=1`, `step_finish=1`. The 11,984-character
text begins by describing a *structured data schema for a public GitHub
repository / personal technical portfolio for Go/Kubebuilder* and ends in
descriptive prose, with Markdown code fences. Attempt to decode the
whole text as JSON fails at position 0. Parsing the first embedded
object finds **a JSON Schema** with keys `$schema`,
`additionalProperties`, `properties`, `required`, `type`, and
**4,472 trailing characters**, not an instance of the assessment contract.

**Grounded verdict**: transport and local model generation succeeded;
the required *instance* containing `mission`, `requirements`,
`repositories`, `gaps`, `options`, `adr` etc. was **not produced**.
Do not relax the extractor to accept the embedded schema, strip prose to
produce an illusory pass, alter the schema/golden or promote any
evidence claim. A short smoke JSON pass does not imply an AA3
architectural pass. Small local `qwen2.5:3b` can follow a small JSON
instruction, but **has not demonstrated** this long-form task.

**One measured prompt-only remediation**: keep frozen source snapshots,
Git blob hashes, model, agent, deny-only config, validator, golden
fixtures and subprocess all unchanged. `assemble()` now appends a
last-position `INSTANCE_FINAL_DIRECTIVE` *after* the full JSON Schema,
explicitly prohibiting a repeated schema, manifesto, Markdown or
narrative and requiring exactly the assessment root keys, distinct
S1/S2/S3, a PROPOSED ADR, explicit uncertainty and a single full JSON
object. This addresses the observed tendency for the last, large
SCHEMA block to be treated as the task instead of validation metadata.
It is a hypothesis to be tested, **not proof of better model reasoning**.
Regenerated prompt SHA-256 changes by design; source revision/hash
provenance must not change. Regression tests cover the final instruction
position and refusal to emit schema keys.

**Controlled next run** (only after CI success): one DAAROPS case using
a new output directory `C:/workspaces/D099-AA3-EVIDENCE-012`, no
additional OpenCode smoke required since transport was already proven.
Review `summary.json` and schema/precheck; a valid syntactic JSON
instance can still be inaccurate or incomplete. If output is again
narrative/schema/truncated, record `AA3_LOCAL_3B_LIMITATION` and
evaluate a qualified longer-context model in a **separate, approved
iteration**, rather than repeatedly tweaking extraction or declaring
AA3 success. Do not automatically run SQY. `AA3_ARCHITECT_REASONING_VALIDATED=false`.

## 2026-10-09 — DAAROPS generated JSON precheck fails repository-grounding

Operator ran `python -m pip install "jsonschema>=4.20,<5"` on the HP,
successfully installing `jsonschema 4.26.0` with its dependencies. The
user then ran `precheck.py` **offline** against the **unchanged** prior
`D099-AA3-EVIDENCE-012/daarops.candidate.json` and frozen
`evals/golden/daarops.json`. The precheck returned `STATIC_PRECHECK_ONLY`
with `case="mission-id-123"` and three violations:
`REQUIRED_REPOSITORY_NOT_MAPPED:zdmooc/argocd-expert-pack`,
`...:zdmooc/cadrage_202682030`,
`...:zdmooc/shared-platform-services-openshift`. It also reported
`required_repositories_mapped=false`, `ownership_matches=true`,
`trajectory=NO_INDEPENDENT_TRACE`, `human_architecture_review=REQUIRED`,
`AA3_ARCHITECT_REASONING_VALIDATED=false`.

**Interpretation:** generating a syntactically valid schema-conforming
object is **not** equivalent to correct mission analysis. The model
misidentified DAAROPS as `mission-id-123` and failed to map every
canonical repo expected by the provisional offline golden baseline.
The old precheck incorrectly failed to flag the mission mismatch,
and its ownership field was vacuously true when no required repos
overlapped. **Small evaluator hardening, not a model remediation:**
add `MISSION_ID_MISMATCH` against the golden case id, and change
`ownership_matches` to false when any required repo is missing.
Add regression tests for both failure modes. Do not edit the model
candidate, score reference, source manifest, evaluator tolerances
or runtime permissions. Do not change the case golden based on
later D-093 progress while grading this frozen test.

**Next run is offline only**: pull the architecture PR branch and rerun
`python solution-architect-agent/evals/precheck.py
--candidate C:/workspaces/D099-AA3-EVIDENCE-012/daarops.candidate.json
--golden solution-architect-agent/evals/golden/daarops.json`.
The expected result is still a static **FAIL**, now explicitly
including `MISSION_ID_MISMATCH` and `ownership_matches=false`.
Inspect FR/NFR, alternatives, evidence limitations and ADR before
choosing a revised evaluation model or benchmark scenario. Do NOT
rerun DAAROPS/SQY inference, alter score fixtures, merge PRs or
mutate CRC as part of this correction. AA3 OPEN.


## 2026-10-09 — result of second offline precheck and candidate review

After applying the deterministic precheck hardening (`9951e759...`), the
operator **replayed only the offline validator** on the unchanged
`D099-AA3-EVIDENCE-012/daarops.candidate.json`. The output had exactly
four violations: `MISSION_ID_MISMATCH` plus
`REQUIRED_REPOSITORY_NOT_MAPPED` for `zdmooc/cadrage_202682030`,
`zdmooc/shared-platform-services-openshift` and
`zdmooc/argocd-expert-pack`. Corrected status:
`required_repositories_mapped=false`, `ownership_matches=false`,
`trajectory=NO_INDEPENDENT_TRACE`, and
`AA3_ARCHITECT_REASONING_VALIDATED=false`.

The locally printed **actual candidate** identifies mission
`mission-id-123` / `OpenShift Platform Architecture Review`, repositories
`openplatform-controllers` and `openplatform-admin-ops`,
`FR=1`, `NFR=1`, `gaps=2`, and three documentation / benchmarks
alternatives unrelated to the operator-first mission. It proposes
`ADR-001` selecting documentation standardization (S1) with
`status=PROPOSED`, `approval_ref=null`, and
`evidence.level=DESIGNED`. A structurally valid JSON candidate is
**not a grounded DAAROPS assessment**. The repository names were not
verified by the frozen source or any external repository tool.

**Gate verdict**: `LOCAL_3B_SCHEMA_CONFORMANT_BUT_SEMANTIC_FAILURE`;
local OpenCode/Bun transport and JSON encoding are now demonstrated,
but end-to-end AA3 model reasoning is **not**. Stop repeated attempts to
make a 3B response pass by rewriting prompts/schema/golden, and do not
promote an irrelevant ADR or synthesized repositories to evidence.
Do not run SQY using the same configuration solely to accumulate
more non-qualifying traces.

**Next design decision, not yet implemented:** qualify a different local
model with adequate context and measured HP RAM/latency (target >=64k),
or define a multi-step fact-grounded analysis with a deterministic
mission/repo ownership gate before generation of S1/S2/S3 and ADR.
Whichever path is approved must be independently assessed on the
unchanged blind cases, with external tool audit, real deny enforcement,
an architecture reviewer score >=85/100 on both DAAROPS and SQY,
and no critical policy failure. AA3 OPEN; no merges or CRC changes.
