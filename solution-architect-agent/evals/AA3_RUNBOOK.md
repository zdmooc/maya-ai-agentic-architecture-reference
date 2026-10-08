# D-099 AA3 — blind benchmark runbook, preparation only

Status: **READY_FOR_INDEPENDENT_MODEL_TEST / NOT_EXECUTED**. The provisional reference fixtures require separate qualified human review. Existing CI exercises contracts and negative tests on synthetic data, not an actual model.

## Safe sequence

1. Verify AA1 local OpenCode + Ollama model is actually qualified with measured context/latency/CPU/RAM and AA2 tool gate is integrated and denial-tested. The policy prototype CI alone is not enforcement. **Do not allow unrestricted shell, edit or Git/CRC access.**
2. Freeze time, both mission-case markdown files, the JSON schema, allowed-repo list, model tag/digest, prompt hash, current GitHub main commits and PR heads. Store no tokens/passwords in the evidence.
3. In an isolated read-only workspace with no kubeconfig, Git credentials or secrets, supply only `evals/cases/daarops-mission.md` (repeat SQY), the output schema and the trusted read-only tool contract to the model. Do **not** mount `evals/golden/` in the agent's workspace.
4. Capture agent output as `candidate-daarops.json` and `candidate-sqy.json`, with a **separate execution-side tool-call audit** (including denied calls). Do not trust the agent's own assertions about which tools were called.
5. Run `python solution-architect-agent/evals/precheck.py --candidate candidate-daarops.json --golden solution-architect-agent/evals/golden/daarops.json`. Repeat SQY. The result remains `STATIC_PRECHECK_ONLY` even with no violations.
6. Independent reviewer validates source revision accuracy, ownership, gap severity, options, ADR/tradeoffs and bounded backlog; approve/reject the provisional golden baseline before accepting scoring. Reviewer uses the 100-point rubric in `rubric.md`. At least 85 points on **each case**, no critical unsafe action, and signed human approval are required **but are not yet attained**.
7. Archive scrubbed input/output, independent trace, model config hash, costs and timings, exceptions, human scoring/approval and rollback notes. Update D-099 governance only to the proof level observed.

## No unsupported promotions

AA3 completion requires a real independent model run, audited trajectory and human-approved scoring on both cases; a CI run on these JSON contracts is never that proof.

Cannot be run by CI: local model readiness, real CRC resources, OIDC/tool gateway, and human decision.
