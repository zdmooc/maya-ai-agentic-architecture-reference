# AA3 I4 — bounded design output quality gate

The deterministically pinned mission ID and repository inventory from
the *trusted host* are checked against a complete candidate
`assessment.schema.json` instance. There must be exactly three distinct
S1/S2/S3 alternatives, an **unapproved PROPOSED** ADR, and no unverified
CI/runtime/production claims. Missing facts/quotes or unknown repos
**block even syntactically valid JSON**.

A zero-violation result authorizes **only requesting a human review**.
The tool cannot approve an ADR, initiate AA4, validate the model reasoning,
or prove that a quotation logically supports a conclusion. Evaluation
should use a separate case not currently under another active session.
