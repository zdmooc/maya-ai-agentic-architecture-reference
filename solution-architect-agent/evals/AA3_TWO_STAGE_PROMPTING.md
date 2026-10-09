# D099 AA3 — two-stage prompting contract

`evals/prompt_stages.py` provides two PURE prompt builders for a
fictional fixture, using no LLM/HTTP/OpenCode invocation.

**Stage A** supplies a host-pinned mission and exact source text to ask
for small, exact-verbatim facts. Its output must be decoded and checked
by `evaluate_facts`.

**Stage B** only runs when `evaluate_facts` returns
`lexical_grounding_pass=true`. It receives compact facts and the
canonical repository map, not the entire source packet or a giant JSON
Schema dump. It generates a D099-AA0-v1 *proposed* design object which
must be passed through `evaluate_design` and then separately scored by
an independent architect. A model's JSON output never proves source
authentication, entailment, a valid policy, or approval.

**Safety boundary:** These are prompt construction helpers, not
integrated OpenCode agents. No provider is configured, no credentials,
no mutation, no source read beyond an already supplied immutable
packet, no automatic retries or build authorization.

**Benchmark prerequisite:** choose and measure an adequate context
model on the HP (or an explicitly approved remote test profile), pin
its digest, use a separate non-operational sandbox, and obtain approved
blinded references before either stage's outputs can count toward AA3.
