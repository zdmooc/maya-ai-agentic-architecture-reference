# AA3 I3 — Fact-first source gate

Input `packet` is assembled by an external trusted host from a frozen,
locally accessible source set. It declares the mission identity, exact
UTF-8 source text and SHA-256, and the allowlisted repository-to-source
mapping. The model can propose only discrete facts with exact short
quotes. `grounding_gate.evaluate_facts()` rejects unknown repository
claims, quotes that cannot be located in the pinned source, a wrong
mission ID, duplicate IDs and source hash discrepancies.

This first gate is **lexical**, not semantic entailment. An attacker
controlling both the text and its hash can forge a self-consistent
packet; therefore an independently approved source manifest and human
source relevance review remain mandatory. Successful lexical checks
must NOT issue approval, authorize execution, infer live repository
inspection or mark AA3 passed. In later orchestration, pass the accepted
fact bundle to a separate option/ADR stage rather than repeatedly
placing a full JSON Schema as the model's last prompt.
