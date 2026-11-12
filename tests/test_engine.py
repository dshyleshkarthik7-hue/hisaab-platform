import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
import engine

BASE = {
    "years": 5, "savings": 1_000_000, "income": 100_000, "sip": 20_000,
    "expense": 40_000, "ret": 8, "vol": 10, "income_growth": 5,
    "medical_shock": 100_000, "shocks": False, "seed": 42, "trials": 300,
    "goals": [{"name": "Education", "at": 4, "cost": 500_000, "kind": "general", "flex": False}],
}

class EngineTests(unittest.TestCase):
    def test_reproducible_seed(self):
        self.assertEqual(engine.simulate(BASE), engine.simulate(BASE))

    def test_different_seed_changes_distribution(self):
        a = engine.simulate(BASE)
        b = engine.simulate({**BASE, "seed": 43})
        self.assertNotEqual(a["fan"], b["fan"])

    def test_goal_success_probability_is_bounded(self):
        result = engine.simulate(BASE)
        self.assertTrue(0 <= result["score"] <= 1)
        self.assertTrue(0 <= result["goals"][0]["odds"] <= 1)

    def test_validation_rejects_invalid_goal_year(self):
        bad = copy.deepcopy(BASE); bad["goals"][0]["at"] = 8
        with self.assertRaises(engine.InputError): engine.validate(bad)

    def test_three_way_comparison_shape(self):
        base = engine.simulate(BASE, trials=300)
        payload = engine.nudge(BASE, base)
        self.assertIn("scenarios", payload)
        self.assertEqual(len(payload["scenarios"]), 3)

if __name__ == "__main__":
    unittest.main()
