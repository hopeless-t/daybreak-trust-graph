# Threat Model

## Assets

- access to high-risk capabilities;
- account identity and recovery control;
- identity-attestation integrity;
- device-binding integrity;
- privacy of raw identity documents;
- revocation state.

## Adversaries

### Stolen password/session attacker

Mitigation: hardware-backed key challenge, session binding, step-up on sensitive transitions, rapid session revocation.

### Phishing attacker

Mitigation: phishing-resistant WebAuthn/FIDO2 or equivalent origin-bound authentication; never treat OTP alone as sufficient for the highest-assurance actions.

### Stolen unlocked device

Mitigation: require local user verification for sensitive operations; allow remote device revocation; use short-lived privileged grants.

### Malware on a trusted endpoint

Mitigation: non-exportable keys limit credential theft but do not make a compromised endpoint trustworthy. High-risk operations may require an independent device or roaming authenticator.

### Recovery-channel attacker

Mitigation: no single weak recovery channel; progressive delay/manual review at the highest risk; user-visible alerts and revocation.

### Malicious or compromised verifier

Mitigation: issuer allow-list, signed attestations, narrow claims, expiry, revocation, verifier diversity for exceptional cases, audit logs.

### Database breach

Mitigation: do not store raw ID artifacts in the relying service; store opaque subject identifiers and minimal attestations; encrypt sensitive metadata; keep signing keys outside the application database.

## Failure modes to avoid

### "One lost key = lost identity"

A roaming key is evidence, not the human being. Recovery must be possible with a threshold of independent evidence.

### "Verified forever"

Attestations expire and can be revoked. Reuse means reuse of proof, not infinite trust.

### "Risk score says yes"

A scalar risk score must never override hard policy conditions such as explicit revocation or known compromise.

### "More factors always means safer"

Adding factors can create support burden, lockout risk, and new social-engineering surfaces. The objective is *independent, appropriate assurance*, not factor count.

## Security invariants

1. Raw identity documents are not the long-term authentication credential.
2. No single recoverable secret grants the highest-risk access after a compromise event.
3. Revocation is checked before privileged access.
4. A new device cannot silently inherit all privileges from a password-only session.
5. Step-up grants are short-lived and scoped to the requested capability.
