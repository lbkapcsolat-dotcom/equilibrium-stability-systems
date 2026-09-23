# SPDX-License-Identifier: MIT
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Any, Mapping

KERNEL_VERSION = "C_LE_V_CLAIM_ADMISSION_KERNEL_V1"
SCHEMA_VERSION = "claim_transition_v1"

REQUIRED_SCHEMA: dict[str, type] = {
    "action": str,
    "target": str,
    "claim_id": str,
    "evidence_sha256": str,
    "authority_id": str,
    "human_veto": bool,
    "nonce": str,
    "proposed_state": str,
}


@dataclass(frozen=True)
class ClaimProfile:
    complexity: float
    verification_capacity: float

    def __post_init__(self) -> None:
        for name, value in (
            ("complexity", self.complexity),
            ("verification_capacity", self.verification_capacity),
        ):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be numeric")
            if not 0.0 <= float(value) <= 1.0:
                raise ValueError(f"{name} must be within [0,1]")


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ClaimAdmissionKernel:
    """Research-stage, offline, fail-closed claim-admission kernel.

    PASS means only WOULD_EXECUTE in the synthetic replay surface. This class
    has no external I/O and contains no production actuation path.
    """

    def __init__(
        self,
        claim_profiles: Mapping[str, ClaimProfile],
        authority_records: Mapping[str, Mapping[str, Any]],
    ) -> None:
        self._claim_profiles = dict(claim_profiles)
        self._authority_records: dict[str, tuple[bytes, str]] = {}
        for authority_id, record in authority_records.items():
            record_bytes = canonical_json_bytes(record)
            self._authority_records[authority_id] = (
                record_bytes,
                sha256_hex(record_bytes),
            )

    def decide(self, payload: Mapping[str, Any], evidence_bytes: bytes) -> dict[str, Any]:
        gate_results: dict[str, str] = {}

        schema_ok, reason = self._validate_schema(payload)
        gate_results["schema"] = reason
        if not schema_ok:
            return self._receipt("HOLD", reason, payload, None, None, None, None, gate_results)

        if payload["human_veto"] is True:
            gate_results["veto"] = "HUMAN_VETO_ASSERTED"
            return self._receipt(
                "HOLD", "HUMAN_VETO_ASSERTED", payload, None, None, None, None, gate_results
            )
        gate_results["veto"] = "NO_VETO"

        evidence_actual = sha256_hex(evidence_bytes)
        if evidence_actual != payload["evidence_sha256"]:
            gate_results["evidence"] = "EVIDENCE_HASH_MISMATCH"
            return self._receipt(
                "HOLD",
                "EVIDENCE_HASH_MISMATCH",
                payload,
                evidence_actual,
                None,
                None,
                None,
                gate_results,
            )
        gate_results["evidence"] = "EVIDENCE_HASH_OK"

        authority_ok, authority_reason, authority_sha = self._verify_authority(payload)
        gate_results["authority"] = authority_reason
        if not authority_ok:
            return self._receipt(
                "HOLD",
                authority_reason,
                payload,
                evidence_actual,
                authority_sha,
                None,
                None,
                gate_results,
            )

        profile = self._claim_profiles.get(payload["claim_id"])
        if profile is None:
            gate_results["claim"] = "CLAIM_PROFILE_UNKNOWN"
            return self._receipt(
                "HOLD",
                "CLAIM_PROFILE_UNKNOWN",
                payload,
                evidence_actual,
                authority_sha,
                None,
                None,
                gate_results,
            )

        c_score = float(profile.complexity)
        v_score = float(profile.verification_capacity)
        gate_results["claim"] = "CLAIM_PROFILE_OK"
        gate_results["c_le_v"] = str(c_score <= v_score)

        if c_score > v_score:
            return self._receipt(
                "HOLD",
                "CLAIM_COMPLEXITY_EXCEEDS_VERIFICATION_CAPACITY",
                payload,
                evidence_actual,
                authority_sha,
                c_score,
                v_score,
                gate_results,
            )

        return self._receipt(
            "PASS",
            "ALL_GATES_SATISFIED",
            payload,
            evidence_actual,
            authority_sha,
            c_score,
            v_score,
            gate_results,
        )

    @staticmethod
    def _validate_schema(payload: Mapping[str, Any]) -> tuple[bool, str]:
        keys = set(payload)
        expected = set(REQUIRED_SCHEMA)

        unexpected = sorted(keys - expected)
        if unexpected:
            return False, f"SCHEMA_UNEXPECTED_FIELD:{','.join(unexpected)}"

        missing = sorted(expected - keys)
        if missing:
            return False, f"SCHEMA_MISSING_FIELD:{','.join(missing)}"

        for key, expected_type in REQUIRED_SCHEMA.items():
            if type(payload[key]) is not expected_type:
                return False, f"SCHEMA_TYPE_ERROR:{key}"

        if re.fullmatch(r"[0-9a-f]{64}", payload["evidence_sha256"]) is None:
            return False, "SCHEMA_EVIDENCE_SHA256_INVALID"

        if not payload["nonce"]:
            return False, "SCHEMA_EMPTY_NONCE"

        return True, "SCHEMA_OK"

    def _verify_authority(self, payload: Mapping[str, Any]) -> tuple[bool, str, str | None]:
        trusted = self._authority_records.get(payload["authority_id"])
        if trusted is None:
            return False, "AUTHORITY_UNKNOWN", None

        record_bytes, expected_sha = trusted
        if sha256_hex(record_bytes) != expected_sha:
            return False, "AUTHORITY_RECORD_INTEGRITY_FAILURE", expected_sha

        try:
            record = json.loads(record_bytes.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return False, "AUTHORITY_RECORD_DECODE_FAILURE", expected_sha

        if record.get("enabled") is not True:
            return False, "AUTHORITY_DISABLED", expected_sha
        if payload["action"] not in set(record.get("allowed_actions", [])):
            return False, "AUTHORITY_ACTION_SCOPE_MISMATCH", expected_sha
        if payload["target"] not in set(record.get("allowed_targets", [])):
            return False, "AUTHORITY_TARGET_SCOPE_MISMATCH", expected_sha
        if payload["claim_id"] not in set(record.get("allowed_claims", [])):
            return False, "AUTHORITY_CLAIM_SCOPE_MISMATCH", expected_sha

        prefix = record.get("required_nonce_prefix", "")
        if prefix and not payload["nonce"].startswith(prefix):
            return False, "AUTHORITY_NONCE_SCOPE_MISMATCH", expected_sha

        return True, "AUTHORITY_OK", expected_sha

    @staticmethod
    def _receipt(
        decision: str,
        reason: str,
        payload: Mapping[str, Any],
        evidence_sha: str | None,
        authority_sha: str | None,
        c_score: float | None,
        v_score: float | None,
        gate_results: Mapping[str, str],
    ) -> dict[str, Any]:
        body = {
            "kernel_version": KERNEL_VERSION,
            "schema_version": SCHEMA_VERSION,
            "decision": decision,
            "reason": reason,
            "action": "WOULD_EXECUTE" if decision == "PASS" else "WOULD_NOT_EXECUTE",
            "claim_id": payload.get("claim_id"),
            "payload_sha256": sha256_hex(canonical_json_bytes(payload)),
            "evidence_actual_sha256": evidence_sha,
            "authority_record_sha256": authority_sha,
            "c_score": c_score,
            "v_score": v_score,
            "gate_results": dict(gate_results),
        }
        return {
            **body,
            "receipt_sha256": sha256_hex(canonical_json_bytes(body)),
        }


def demo_kernel() -> ClaimAdmissionKernel:
    profiles = {
        "synthetic.safe_transition.v1": ClaimProfile(0.35, 0.80),
        "synthetic.overcoupled_transition.v1": ClaimProfile(0.85, 0.60),
    }
    authorities = {
        "DEMO_AUTHORITY": {
            "enabled": True,
            "allowed_actions": ["ADVANCE_DEMO_STATE"],
            "allowed_targets": ["SYNTHETIC_TARGET_A"],
            "allowed_claims": list(profiles),
            "required_nonce_prefix": "demo-",
        }
    }
    return ClaimAdmissionKernel(profiles, authorities)


def demo_payload(evidence: bytes, claim_id: str = "synthetic.safe_transition.v1") -> dict[str, Any]:
    return {
        "action": "ADVANCE_DEMO_STATE",
        "target": "SYNTHETIC_TARGET_A",
        "claim_id": claim_id,
        "evidence_sha256": sha256_hex(evidence),
        "authority_id": "DEMO_AUTHORITY",
        "human_veto": False,
        "nonce": "demo-0001",
        "proposed_state": "DEMO_STATE_2",
    }
