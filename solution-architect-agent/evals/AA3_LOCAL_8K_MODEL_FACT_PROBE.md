# D099 AA3 — First genuinely local fact extraction, 8K only

**Prerequisites observed on HP17G3 on 2026-10-09**:
- Qwen3.5 9B Q4_K_M downloaded (`ollama list` ID 56671c2ab938)
- Ollama API reachable on `192.168.56.1:11434`, **not** on `127.0.0.1:11434`
- simple JSON contract: **PASS** at `num_ctx=8192`, total 51.69 s including
  39.73 s model load; `ollama ps` observed 11 GB, 44%/56% CPU/GPU,
  context 8192; RAM available after model load **14.91 GiB**
- These facts prove only basic local API transport/response, not
  source-grounded architectural reasoning or usable 65 536-token context.

**Run from Git Bash, on the local branch after a reviewed fast-forward:**

```bash
cd /c/workspaces/D099-AA3-HUB
git status --short
git pull --ff-only
D099_ALLOW_LOCAL_INFERENCE=YES python solution-architect-agent/evals/local_aa3_fact_probe.py --case notification_case.json
ollama ps
```

The tool runs ONE offline fictional `NOTIFY-01` source quote
extraction at 8192 context and at most 384 output tokens, `think=false`,
against only an explicit loopback or known host-only endpoint
(192.168.56.1 is the default). It deliberately exposes NO tools and
does not call OpenCode, GitHub, CRC, ArgoCD or a shell; it makes only
one permitted local Ollama API POST. CI tests never run an LLM.

`AA3_LOCAL_FACT_GATE_PASS` means the model retrieved the
mission identifier and both fictional canonical owner repositories
with exact source quotations. It does NOT mean human semantic review,
architectural reasoning validation, independent source attestation,
tools policy evidence, or completed D-099.

Do not escalate to 32768/65536 context automatically on a machine
sharing 14.91 GiB free memory with CRC. Stop the Ollama model explicitly
to reclaim memory if required.
