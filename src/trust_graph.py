"""Tiny reference policy for the Daybreak Trust Graph proposal.

This is an executable design sketch, not production authentication code.
"""

from dataclasses import dataclass
from enum import Enum, auto


class Decision(Enum):
    ALLOW = auto()
    STEP_UP = auto()
    DENY_RECOVER = auto()


class ActionTier(Enum):
    ROUTINE = 0
    SENSITIVE = 1
    HIGH_RISK = 2
    RECOVERY = 3


@dataclass(frozen=True)
class Evidence:
    identity_valid: bool
    identity_revoked: bool = False
    known_device: bool = False
    hardware_backed_key: bool = False
    recent_user_verification: bool = False
    independent_factor: bool = False
    compromise_signal: bool = False


@dataclass(frozen=True)
class Result:
    decision: Decision
    missing: tuple[str, ...] = ()
    reason: str = ""


def evaluate(evidence: Evidence, action: ActionTier) -> Result:
    """Return the minimum additional proof required by a simple deterministic policy."""

    if evidence.identity_revoked or evidence.compromise_signal:
        return Result(
            Decision.DENY_RECOVER,
            reason="revoked identity evidence or active compromise signal",
        )

    if not evidence.identity_valid:
        return Result(
            Decision.STEP_UP,
            ("fresh_identity_attestation",),
            "no currently valid identity attestation",
        )

    required: list[str] = []

    if action is ActionTier.ROUTINE:
        if not evidence.known_device:
            required.append("prove_control_of_existing_trusted_device")

    elif action is ActionTier.SENSITIVE:
        if not evidence.hardware_backed_key:
            required.append("hardware_backed_device_proof")
        if not evidence.recent_user_verification:
            required.append("recent_user_verification")

    elif action is ActionTier.HIGH_RISK:
        if not evidence.hardware_backed_key:
            required.append("hardware_backed_device_proof")
        if not evidence.recent_user_verification:
            required.append("recent_user_verification")
        if not evidence.independent_factor:
            required.append("independent_factor")

    elif action is ActionTier.RECOVERY:
        if not evidence.independent_factor:
            required.append("independent_recovery_evidence")
        if not evidence.recent_user_verification:
            required.append("fresh_user_presence_or_manual_review")

    if required:
        return Result(
            Decision.STEP_UP,
            tuple(required),
            "current evidence is valid but insufficient for this action",
        )

    return Result(Decision.ALLOW, reason="minimum sufficient evidence is present")
