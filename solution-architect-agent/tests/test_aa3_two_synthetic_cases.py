"""Two independent fictional cases exercise the same bounded static gates."""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from independent.prepare_case import assemble_case, case_path
from staged_review import review
from test_aa3_staged_review import sample


def inventory():
    facts = [
        {"id": "I-M", "kind": "mission", "value": "INVENTORY-02",
         "source_id": "I1",
         "quote": "Mission INVENTORY-02 covers inventory reservation and expiry."},
        {"id": "I-R1", "kind": "repository", "repository": "lab/inventory-api",
         "source_id": "I1",
         "quote": "Canonical repo lab/inventory-api owns stock availability API and reservation request validation."},
        {"id": "I-R2", "kind": "repository", "repository": "lab/stock-ledger",
         "source_id": "I2",
         "quote": "Canonical repo lab/stock-ledger owns reservation IDs, stock mutation journal and idempotency keys."},
    ]
    _, obj = sample()
    obj["mission"].update({"id": "INVENTORY-02", "title": "Fictional stock reservation",
                           "source": "I1"})
    for kind in ("FR", "NFR"):
        for r in obj["requirements"][kind]:
            r["source"] = "I1" if kind == "FR" else "I2"
    obj["repositories"][0].update({"name": "lab/inventory-api", "source": "I1"})
    obj["repositories"][1].update({"name": "lab/stock-ledger", "source": "I2"})
    obj["gaps"][0]["source"] = "I1"
    obj["evidence"][0]["source"] = "I2"
    return facts, obj


def test_two_fictional_cases_share_same_review_contract():
    for name, id_expected in (
        ("notification_case.json", "NOTIFY-01"),
        ("inventory_case.json", "INVENTORY-02"),
    ):
        packet, meta = assemble_case(name)
        assert packet["mission_id"] == id_expected
        assert meta["model_invoked"] is False
        assert len(packet["repository_sources"]) == 2
    facts, candidate = inventory()
    digest = hashlib.sha256(case_path("inventory_case.json").read_bytes()).hexdigest()
    result = review(facts, candidate, expected_fixture_sha256=digest,
                    fixture_name="inventory_case.json")
    assert result["status"] == "AA3_OFFLINE_PRECHECK_PASS"
    assert result["AA3_ARCHITECT_REASONING_VALIDATED"] is False


def test_unapproved_case_name_rejected():
    import pytest
    with pytest.raises(ValueError, match="UNAPPROVED_INDEPENDENT_FIXTURE"):
        case_path("../../private/file.json")


def test_mixed_case_sources_and_identity_do_not_pass():
    facts, candidate = inventory()
    sha = hashlib.sha256(case_path("notification_case.json").read_bytes()).hexdigest()
    result = review(facts, candidate, expected_fixture_sha256=sha,
                    fixture_name="notification_case.json")
    assert result["status"] == "AA3_OFFLINE_PRECHECK_FAIL"
    assert "MISSION_ID_MISMATCH" in result["violations"]
    assert "REPOSITORY_REQUIRED_MISSING:lab/notification-api" in result["violations"]
