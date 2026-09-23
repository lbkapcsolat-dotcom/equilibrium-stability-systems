# SPDX-License-Identifier: MIT
from __future__ import annotations

import copy
import sys

from kernel import demo_kernel, demo_payload

EVIDENCE = b"synthetic evidence\npressure=nominal\n"


def run_case(name, payload, evidence, expected_decision, expected_reason_prefix):
    result = demo_kernel().decide(payload, evidence)
    ok = (
        result["decision"] == expected_decision
        and result["reason"].startswith(expected_reason_prefix)
    )
    print(
        f"{name:24}  {result['decision']:4}  "
        f"{result['action']:17}  {result['reason']}"
    )
    return ok


def main() -> int:
    clean = demo_payload(EVIDENCE)
    cases = []

    cases.append(("clean", clean, EVIDENCE, "PASS", "ALL_GATES_SATISFIED"))

    extra = copy.deepcopy(clean)
    extra["auto_correct"] = True
    cases.append(("unexpected field", extra, EVIDENCE, "HOLD", "SCHEMA_UNEXPECTED_FIELD"))

    mutated_evidence = bytearray(EVIDENCE)
    mutated_evidence[0] ^= 1
    cases.append(("evidence byte flip", clean, bytes(mutated_evidence), "HOLD", "EVIDENCE_HASH_MISMATCH"))

    wrong_scope = copy.deepcopy(clean)
    wrong_scope["action"] = "UNAUTHORIZED_DEMO_ACTION"
    cases.append(("authority mismatch", wrong_scope, EVIDENCE, "HOLD", "AUTHORITY_ACTION_SCOPE_MISMATCH"))

    veto = copy.deepcopy(clean)
    veto["human_veto"] = True
    cases.append(("human veto", veto, EVIDENCE, "HOLD", "HUMAN_VETO_ASSERTED"))

    high_c = demo_payload(EVIDENCE, "synthetic.overcoupled_transition.v1")
    cases.append(("C > V", high_c, EVIDENCE, "HOLD", "CLAIM_COMPLEXITY_EXCEEDS_VERIFICATION_CAPACITY"))

    print("CASE                      DEC   ACTION             REASON")
    print("-" * 92)
    results = [run_case(*case) for case in cases]

    passed = sum(results)
    print(f"\nReplay: {passed}/{len(results)} expected outcomes matched.")
    print("Scope: offline synthetic WOULD_EXECUTE only; no real actuation exists in this repo.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
