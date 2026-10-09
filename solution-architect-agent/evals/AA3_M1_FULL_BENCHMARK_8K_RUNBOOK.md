# AA3 M1 — Full assessment benchmark (prepared, not executed)

Owner `maya-ai-agentic-architecture-reference` PR #4, not a new repository.

This is the **full contract** complement to the recent 8K synthetic
NOTIFY/INVENTORY lexical and five-field design-slice probes.
The canonical real-world benchmark source packets already exist:
`evals/cases/daarops-mission.md`,
`evals/cases/sqy-mission.md`, `evals/frozen/manifest.json`,
and the SHA-pinned alignment text snapshots.

The new local `local_aa3_full_benchmark.py` uses Qwen3.5 9B
(`qwen3.5:9b-q4_K_M`) on the already observed Ollama
`http://192.168.56.1:11434`. It requests exactly one
`D099-AA0-v1` JSON assessment of FR, NFR, gap, canonical owners,
three S1/S2/S3 alternatives, PROPOSED ADR, evidence limitations and
next actions; full output schema is transmitted via Ollama's
structured `format` field, not appended as another answer template.
No tool access. Frozen original sources and git-blob hashes are
checked offline before any API request, **no goldens are supplied
to the LLM**. Provisional goldens and existing `precheck.py` are
used on the **host AFTER** inference, not model-visible. The tool
does not inspect current live repos, and no status >DESIGNED is
accepted. This is a different, stricter benchmark than synthetic
one-off design slices.

**Operator preparation, safe read-only, in Git Bash**:

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only
python solution-architect-agent/evals/local_aa3_full_benchmark.py --case daarops --dry-run
```

**One optional local run**, only with explicit operator consent and a
fresh evidence dir outside the Git checkout:

```bash
D099_ALLOW_LOCAL_INFERENCE=YES python \
 solution-architect-agent/evals/local_aa3_full_benchmark.py \
 --case daarops --out /c/workspaces/D099-AA3-FULL-DAAROPS-001
```

Collect `summary.json` and inspect local `candidate.local.json`.
Do not post candidate output publicly without review. Do NOT run SQY
automatically if DAAROPS has failed. The backend enforces 8192
context, a 2100-token output cap, no retry, no redirects,
no tool access, and unload-on-finish to conserve host memory.

Passing `AA3_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW` means only
schema, known owner names, historical source citations and static
policy checks passed. Any claim of actual current repo reading,
live OpenCode tool denial, independent reviewer >=85/100,
or completed D099 is still unsupported. Model quality, capacity,
and performance on this *longer* prompt are not yet measured.
The local Windows interpreter already used `jsonschema` 4.26
in an earlier DAAROPS precheck, but fail closed if unavailable.

**Milestone estimate**: M1 full benchmark machinery/CI prepared,
M2 qualified independent mission evaluation and scoring pending,
M3 tool/host telemetry + reviewer signoff pending.
No AA gate closed by code- or synthetic-CI-only evidence.
