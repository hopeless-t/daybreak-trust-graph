import unittest

from src.trust_graph import ActionTier, Decision, Evidence, evaluate


class TrustGraphPolicyTests(unittest.TestCase):
    def test_known_verified_user_has_zero_work_for_routine_use(self):
        evidence = Evidence(identity_valid=True, known_device=True)
        self.assertEqual(evaluate(evidence, ActionTier.ROUTINE).decision, Decision.ALLOW)

    def test_new_device_requires_step_up_not_new_identity_document(self):
        evidence = Evidence(identity_valid=True, known_device=False)
        result = evaluate(evidence, ActionTier.ROUTINE)
        self.assertEqual(result.decision, Decision.STEP_UP)
        self.assertEqual(result.missing, ("prove_control_of_existing_trusted_device",))

    def test_high_risk_action_requires_independent_assurance(self):
        evidence = Evidence(
            identity_valid=True,
            known_device=True,
            hardware_backed_key=True,
            recent_user_verification=True,
        )
        result = evaluate(evidence, ActionTier.HIGH_RISK)
        self.assertEqual(result.decision, Decision.STEP_UP)
        self.assertEqual(result.missing, ("independent_factor",))

    def test_revocation_is_hard_stop(self):
        evidence = Evidence(identity_valid=True, identity_revoked=True)
        self.assertEqual(
            evaluate(evidence, ActionTier.ROUTINE).decision,
            Decision.DENY_RECOVER,
        )


if __name__ == "__main__":
    unittest.main()
