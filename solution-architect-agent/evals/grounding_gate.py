"""D099 AA3 I3: lexical fact grounding against trusted, locally pinned sources.

Only verifies that exact quotes appear in source bytes. It does not infer that
claims logically follow, grant tool access, or authenticate source provenance.
"""
from __future__ import annotations
import hashlib
from typing import Any


def source_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def evaluate_facts(packet: dict[str, Any], facts: list[dict[str, Any]]) -> dict[str, Any]:
    """Fail closed before design; the packet must be supplied by trusted host."""
    faults: list[str] = []
    mission = packet.get("mission_id")
    sources = packet.get("sources")
    owners = packet.get("repository_sources")
    if not isinstance(mission, str) or not mission.strip():
        faults.append("MISSION_NOT_PINNED")
    if not isinstance(sources, list) or not sources:
        faults.append("SOURCES_ABSENT")
        sources = []
    if not isinstance(owners, dict) or not owners:
        faults.append("OWNERS_NOT_PINNED")
        owners = {}
    index: dict[str, str] = {}
    for source in sources:
        if not isinstance(source, dict):
            faults.append("SOURCE_INVALID")
            continue
        sid, text, digest = (source.get("id"), source.get("text"),
                             source.get("sha256"))
        if not isinstance(sid, str) or not sid or sid in index:
            faults.append("DUPLICATE_OR_INVALID_SOURCE_ID")
            continue
        if not isinstance(text, str) or not isinstance(digest, str) or (
            source_digest(text) != digest
        ):
            faults.append("SOURCE_DIGEST_MISMATCH:" + sid)
            continue
        index[sid] = text
    for repo, sid in owners.items():
        if not isinstance(repo, str) or not repo or not isinstance(sid, str) or sid not in index:
            faults.append("OWNER_SOURCE_UNVERIFIED")
    if not isinstance(facts, list) or not facts:
        faults.append("FACTS_ABSENT")
        facts = []
    fact_ids: set[str] = set()
    mission_count = 0
    repo_count = 0
    for fact in facts:
        if not isinstance(fact, dict):
            faults.append("FACT_INVALID")
            continue
        fid, kind = fact.get("id"), fact.get("kind")
        sid, quote = fact.get("source_id"), fact.get("quote")
        if not isinstance(fid, str) or not fid or fid in fact_ids:
            faults.append("FACT_ID_INVALID_OR_DUPLICATE")
        else:
            fact_ids.add(fid)
        if kind not in {"mission", "repository", "requirement", "gap"}:
            faults.append("FACT_KIND_UNKNOWN")
        if (not isinstance(sid, str) or sid not in index
                or not isinstance(quote, str) or not quote.strip()
                or quote not in index.get(sid, "")):
            faults.append("QUOTE_NOT_IN_PINNED_SOURCE")
        if kind == "mission":
            mission_count += 1
            if fact.get("value") != mission:
                faults.append("MISSION_ID_MISMATCH")
        if kind == "repository":
            repo_count += 1
            name = fact.get("repository")
            if (not isinstance(name, str) or name not in owners
                    or owners.get(name) != sid):
                faults.append("REPOSITORY_NOT_IN_TRUSTED_INVENTORY")
    if mission_count != 1:
        faults.append("MISSION_FACT_COUNT_INVALID")
    if repo_count < 1:
        faults.append("REPOSITORY_FACT_MISSING")
    violations = sorted(set(faults))
    return {
        "status": "AA3_LEXICAL_SOURCE_GATE_ONLY",
        "violations": violations,
        "lexical_grounding_pass": not violations,
        "source_authentication": "EXTERNAL_PINNING_REQUIRED",
        "logical_entailment_review": "HUMAN_REQUIRED",
        "may_generate_approved_adr": False,
        "AA3_ARCHITECT_REASONING_VALIDATED": False,
    }
