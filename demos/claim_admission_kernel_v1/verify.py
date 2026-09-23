# SPDX-License-Identifier: MIT
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASELINE = ROOT / "PUBLIC_BASELINE.json"
EXPECTED_BASELINE_SHA256 = "09f8599ddb1319181424fbe9fca431297079f9259961968f00ac40bd6c45e163"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT)
    if p.returncode != 0:
        raise SystemExit(p.returncode)


def main() -> int:
    actual = sha256_file(BASELINE)
    if actual != EXPECTED_BASELINE_SHA256:
        print("BASELINE HOLD: public baseline SHA256 mismatch", file=sys.stderr)
        print(f"expected={EXPECTED_BASELINE_SHA256}", file=sys.stderr)
        print(f"actual  ={actual}", file=sys.stderr)
        return 2

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if baseline.get("status") != "RESEARCH_STAGE":
        print("BASELINE HOLD: unexpected public baseline status", file=sys.stderr)
        return 2
    if baseline.get("real_actuation") is not False or baseline.get("production_admission") is not False:
        print("BASELINE HOLD: public claim boundary changed", file=sys.stderr)
        return 2

    print(f"Public research baseline: PASS / {actual}")
    print("\n[1/2] Unit tests")
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
    print("\n[2/2] Visible replay")
    run([sys.executable, "replay.py"])
    print("\nVERIFY PASS: research-stage offline kernel only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
