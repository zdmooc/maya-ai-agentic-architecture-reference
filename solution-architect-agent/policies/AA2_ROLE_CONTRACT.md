# D-099 AA2 — Role design invariants (I2)

`policies/validate_profiles.py` verifies the exact four-role design
matrix, least-privilege grants, authenticated approval guards, mandatory
command denials and **DESIGNED_NOT_ENFORCED** status.

It does **not** provide authorization for actual tool execution:
the real executor/approval registry and independent audit remain owned by
`TradeOps-GenAI-Integration` PR #26. The local Ollama `d099-evaluator`
used for AA3 is a completely deny-only *offline test profile*, not one
of the deployable four functional role profiles. Do not infer working
IAM, OIDC, a trusted MCP server, cross-tenant enforcement or runtime
denial from static tests. A production integration requires signed
approval and real action/trajectory checks outside the model.
