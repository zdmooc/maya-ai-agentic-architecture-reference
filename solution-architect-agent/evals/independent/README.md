# AA3 I5 — independent synthetic blind fixture, NON-QUALIFYING

`notification_case.json` is a fictional NOTIFY-01 event-delivery
scenario, independent of any active banking client or other session.
The two `lab/...` owner names are **invented synthetic fixtures**,
never claims about public GitHub repositories.

`prepare_case.py` builds a UTF-8 source digest packet *without*
loading the reviewer-only reference, no network calls, no agent
invocation, no tests against a real service. The fixture must be
pinned to a reviewed **Git commit SHA** before any comparative model
benchmark; the runtime-computed text digests by themselves are only
self-consistency checks and are not independently trusted provenance.
The model sees only the scenario and source excerpts; the downstream
fact/decision gates must check mission identity, source quotes,
canonical owner mapping and S1/S2/S3 plus PROPOSED ADR. A human must
sign and separately score a reference before evaluating a model.

Commands (offline): `python solution-architect-agent/evals/independent/prepare_case.py`
and `python -m unittest discover -s solution-architect-agent/tests -v`.
This iteration does not assert `AA3_ARCHITECT_REASONING_VALIDATED`.
