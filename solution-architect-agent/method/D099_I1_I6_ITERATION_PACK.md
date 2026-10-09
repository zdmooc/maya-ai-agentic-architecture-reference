# D-099 — Six-iteration bounded implementation pack (2026-10-09)

Status: **DRAFT / SYNTHETIC_STATIC_ONLY / CI_TO_BE_VERIFIED**.
No DAAROPS-related source fixtures or execution were changed; the
existing historical references remain for reproducibility and are
owned by the other live session.

| Iteration | Scope | Deliverable | Current proof boundary |
| --- | --- | --- | --- |
| I1 | AA0 | `method/validate_workflow.py`, stage/owner/approval regression | Contract only; ADR still proposed |
| I2 | AA2 | `policies/validate_profiles.py`, four-role policy negative tests | Matrix design; not live tool enforcement |
| I3 | AA3 | `evals/grounding_gate.py` fact-first exact-source gate | Lexical quotes; not semantic entailment |
| I4 | AA3 | `evals/decision_gate.py` identity/repository/options/ADR gate | Static review eligibility; no approved ADR |
| I5 | AA3 | Independent fictional `NOTIFY-01` blind packet | No LLM call or human-reviewed golden |
| I6 | AA4 | `build/plan_guard.py` branch/worktree/edit/test/rollback plan | Synthetic plan only; no build, no approval |

**Remaining acceptance requirements:** AA0 ADR human review and merge;
AA1 resource/64k/model assessment and resolved permissions; AA2
end-to-end policy gateway negative tests with independent trace and
approval; AA3 real blind two-case candidate evaluation on an adequate
model and >=85/100 per case with separate human sign-off; AA4 actual
isolated worktree build, tests and external approval; AA5 OpenHands;
AA6 LangGraph/HITL checkpoints; AA7 security/evals; AA8 authorized CRC
bounded proof; AA9 replayable demo. Maintain all gate booleans FALSE
until corresponding evidence exists.

No merge, no new repo, no D-093 work, no runtime change. Review the
PR CI at its final head, then update the cadrage checkpoint accordingly.
