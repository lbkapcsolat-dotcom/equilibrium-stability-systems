import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class ArmTargetEvidenceDemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "demo.py")],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        cls.result = json.loads(proc.stdout)

    def test_repeated_aarch64_builds_are_byte_equal(self):
        self.assertTrue(self.result["repeated_build_equal"])

    def test_declared_target_matches_aarch64_elf_machine(self):
        self.assertTrue(self.result["declared_target_matches"])
        self.assertEqual(self.result["arm_elf_machine"], 183)

    def test_wrong_architecture_negative_control_is_rejected(self):
        self.assertTrue(self.result["negative_control_rejected"])
        self.assertEqual(self.result["negative_control_elf_machine"], 62)

    def test_claim_ceiling_blocks_runtime_or_hardware_overclaim(self):
        ceiling = self.result["claim_ceiling"]
        self.assertIn("NO_RUNTIME_CORRECTNESS", ceiling)
        self.assertIn("NO_HARDWARE_VALIDATION", ceiling)
        self.assertIn("NO_ARM_ENDORSEMENT", ceiling)


if __name__ == "__main__":
    unittest.main()
