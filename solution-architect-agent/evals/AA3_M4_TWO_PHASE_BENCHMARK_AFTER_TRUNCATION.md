# D099 AA3 — M4 Two-stage full schema benchmark, not a successful model run

The operator's single full DAAROPS Qwen3.5 9B request at 8K consumed
`2100/2100` generated tokens and 1231.01 seconds and returned
`GENERATION_TRUNCATED`, `MODEL_JSON_NOT_VALID` (2026-10-09).
The previous runner discarded incomplete text and retained only the
summary. This is not a successful full architecture benchmark or a
model-semantic failure; a complete candidate never existed.

**Corrective protocol, version `D099-AA3-LOCAL-TWO-PHASE-v1`:**
- `stage1`: one bounded local model request for mission, FR/NFR,
  canonical repositories and gaps. Max 1,750 output tokens;
  a compact temporary JSON Schema is generated from the **unchanged**
  `method/assessment.schema.json`, with text lengths and list caps.
  The immutable frozen DAAROPS/SQY sources are the same and golden
  reference content is not shown to the model.
- `stage2`: run **separately only if stage1 passed**, reading locally
  saved stage1 output with SHA-256/pinned source/owner/schema checks.
  One model request for S1/S2/S3, ADR PROPOSED, evidence, limits and
  actions (1,550 tokens max). Assemble two actually generated pieces;
  check the exact original 11-field schema and baseline `precheck.py`.
  **No filling from golden, no source rewrites, no reviewer scores**.

All requests use Qwen3.5 9B, `num_ctx=8192`, `think=false`, no
tools, no model access to golden, no network other than the allowlisted
local Ollama API, and `keep_alive=0`. Phase1 alone may still take
significant time or fail; do **not** auto-run phase2 after failure.

Incomplete raw model text on future failures is retained solely under
the operator-provided unique evidence directory as
`stage1.truncated.local.txt` or `stage2.truncated.local.txt`.
Do NOT upload this private raw artifact without inspecting and
redacting it. Partial content is never promoted to an assessment.
`stage1.summary.json` and `stage2.summary.json` include request
metadata and observed token counts when available.

**Recommended operator sequence in Git Bash**:

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only
python solution-architect-agent/evals/local_aa3_staged_benchmark.py \
 --case daarops --phase stage1 --dry-run
```

Then only after checking available RAM, workload and operator consent:

```bash
OUT="/c/workspaces/D099-AA3-STAGE1-$(date +%Y%m%d-%H%M%S)-$$"
D099_ALLOW_LOCAL_INFERENCE=YES python \
 solution-architect-agent/evals/local_aa3_staged_benchmark.py \
 --case daarops --phase stage1 --out "$OUT"
echo "STAGE1_DIR=$OUT"
```

**Only on `AA3_STAGE1_STATIC_READY_FOR_REVIEW`:**

```bash
D099_ALLOW_LOCAL_INFERENCE=YES python \
 solution-architect-agent/evals/local_aa3_staged_benchmark.py \
 --case daarops --phase stage2 \
 --stage1-dir "$OUT" \
 --out "${OUT}-stage2"
```

A passing final phase is still only `AA3_STAGE2_FULL_ASSESSMENT_STATIC_READY_FOR_REVIEW`;
the source packet is historical, tool execution was absent, actual
OpenCode permission DENY is not proven, 64K context is not qualified,
and independent human >=85/100 ratings on both DAAROPS/SQY remain
pending. No CRC runtime proof or merged PR; `AA3_ARCHITECT_REASONING_VALIDATED=false`,
`D099_CLOSED=false`.
