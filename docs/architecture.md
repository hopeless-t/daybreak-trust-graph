# Architecture

## Objective

Provide strong, phishing-resistant access to high-risk capabilities while minimizing repeated identity collection, unnecessary hardware purchases, and authentication ceremony.

## Components

### Identity Verifier

Performs the expensive privacy-sensitive event: government-ID verification, liveness checks, or equivalent proofing.

Its output should be a purpose-bound signed attestation containing only claims the relying service actually needs. Raw identity artifacts should follow the verifier's deletion policy and should not be treated as the reusable credential.

### Identity Attestation

A compact credential asserting facts such as verification method, assurance class, verification time, expiration, and revocation handle.

Properties:

- signed by a trusted issuer;
- bound to an opaque subject identifier;
- short enough to inspect and audit;
- revocable;
- purpose-limited;
- renewable without automatically re-collecting raw ID.

### Device Trust Roots

Accounts may bind multiple device-backed non-exportable keys. A device registration record should include only the metadata required for policy evaluation and revocation.

The important property is not "phone" versus "USB key". It is whether the key is:

- hardware protected;
- resistant to export/cloning;
- gated by user presence or local authentication;
- individually revocable.

### Trust Graph

The graph stores relationships among:

- subject;
- identity attestations;
- trusted devices;
- optional roaming authenticators;
- recovery factors;
- sessions;
- revocations and compromise events.

A graph is preferable to a single `verified=true` bit because a policy can reason about *which* evidence is still valid.

### Policy Engine

The engine evaluates the requested action against available evidence and returns one of:

- **ALLOW** — current evidence is sufficient;
- **STEP_UP** — request the cheapest additional proof that closes the assurance gap;
- **DENY_RECOVER** — a hard compromise/revocation condition exists.

## Evidence minimization

The policy engine should request the **minimum sufficient additional evidence**.

Example:

```text
Known device + valid identity attestation + routine action
    => ALLOW

New device + valid identity attestation
    => STEP_UP using an already-bound device

Account recovery + no trusted device
    => STEP_UP using recovery code / roaming key / fresh identity proof

Revoked identity attestation
    => DENY_RECOVER
```

## Platform authenticator nuance

A synced passkey and a device-bound non-exportable key are not identical security objects. A production design should explicitly distinguish:

- synced multi-device credentials;
- device-bound hardware-backed credentials;
- roaming hardware credentials.

Where browser APIs cannot expose the required device-bound semantics, a first-party native application can hold a separate hardware-backed companion key used only for high-assurance attestation.

## Privacy boundary

The relying service does not need a permanent copy of the identity document to remember that identity verification occurred.

The verifier can retain whatever is legally and operationally required under its own policy, while the relying service keeps only the smallest reusable attestation necessary for access control.
