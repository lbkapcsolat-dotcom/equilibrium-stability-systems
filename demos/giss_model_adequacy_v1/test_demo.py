import unittest

from demo import run_demo


class ModelAdequacyDemoTests(unittest.TestCase):
    def test_model_is_numerically_stable(self):
        result = run_demo()
        self.assertTrue(result.numerically_stable)

    def test_structural_stress_breaks_decision_adequacy(self):
        result = run_demo()
        self.assertFalse(result.decision_adequate)
        self.assertGreater(
            result.stress_false_negative_rate,
            result.max_false_negative_rate,
        )

    def test_fail_closed_state_is_emitted(self):
        result = run_demo()
        self.assertEqual(
            result.safeguard_state,
            "HOLD__STRUCTURAL_MODEL_INADEQUACY",
        )

    def test_demo_does_not_claim_modele_validation(self):
        result = run_demo()
        self.assertIn("NO_MODELE_VALIDATION", result.claim_ceiling)
        self.assertIn("NO_NASA_GISS_ENDORSEMENT_OR_AFFILIATION", result.claim_ceiling)


if __name__ == "__main__":
    unittest.main()
