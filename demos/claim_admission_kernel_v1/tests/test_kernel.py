# SPDX-License-Identifier: MIT
from __future__ import annotations

import copy
import unittest

from kernel import demo_kernel, demo_payload


class KernelTests(unittest.TestCase):
    def setUp(self):
        self.evidence = b"synthetic evidence\npressure=nominal\n"
        self.payload = demo_payload(self.evidence)

    def decide(self, payload=None, evidence=None):
        return demo_kernel().decide(
            self.payload if payload is None else payload,
            self.evidence if evidence is None else evidence,
        )

    def test_clean_payload_passes_as_would_execute(self):
        r = self.decide()
        self.assertEqual(r["decision"], "PASS")
        self.assertEqual(r["action"], "WOULD_EXECUTE")

    def test_unexpected_field_holds(self):
        p = copy.deepcopy(self.payload)
        p["auto_correct"] = True
        self.assertTrue(self.decide(p)["reason"].startswith("SCHEMA_UNEXPECTED_FIELD"))

    def test_evidence_byte_flip_holds(self):
        mutated = bytearray(self.evidence)
        mutated[-1] ^= 1
        self.assertEqual(self.decide(evidence=bytes(mutated))["reason"], "EVIDENCE_HASH_MISMATCH")

    def test_authority_scope_mismatch_holds(self):
        p = copy.deepcopy(self.payload)
        p["action"] = "UNAUTHORIZED_DEMO_ACTION"
        self.assertEqual(self.decide(p)["reason"], "AUTHORITY_ACTION_SCOPE_MISMATCH")

    def test_human_veto_holds(self):
        p = copy.deepcopy(self.payload)
        p["human_veto"] = True
        self.assertEqual(self.decide(p)["reason"], "HUMAN_VETO_ASSERTED")

    def test_c_greater_than_v_holds(self):
        p = demo_payload(self.evidence, "synthetic.overcoupled_transition.v1")
        self.assertEqual(
            self.decide(p)["reason"],
            "CLAIM_COMPLEXITY_EXCEEDS_VERIFICATION_CAPACITY",
        )

    def test_receipt_is_deterministic(self):
        a = self.decide()["receipt_sha256"]
        b = self.decide()["receipt_sha256"]
        self.assertEqual(a, b)

    def test_payload_change_changes_receipt(self):
        a = self.decide()["receipt_sha256"]
        p = copy.deepcopy(self.payload)
        p["nonce"] = "demo-0002"
        b = self.decide(p)["receipt_sha256"]
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
