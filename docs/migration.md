# Migration Plan

This document describes a generic migration from an older trusted-access flow to a stronger one without forcing already-verified users through unnecessary repeated work.

## Phase 1 — Preserve existing assurance

For every previously verified account, convert the existing verification result into a versioned identity-attestation record where policy and legal constraints permit.

Do **not** require raw-ID resubmission solely because the access-control architecture changed.

## Phase 2 — Bind existing devices

When a verified user signs in on a known first-party device, offer device binding using hardware-backed key material where available.

This can be a progressive rollout rather than an immediate lockout deadline.

## Phase 3 — Add high-risk step-up

Require stronger proof only at meaningful risk boundaries:

- adding a new trusted device;
- changing recovery methods;
- accessing an unusually sensitive capability;
- anomalous or compromised sessions;
- attestation expiry or revocation.

## Phase 4 — Offer roaming hardware keys

Support FIDO2 roaming keys as a strong option for:

- users who prefer a physically separate trust anchor;
- cross-device workflows;
- break-glass recovery;
- environments where platform hardware cannot meet the required assurance.

The migration should distinguish **required assurance properties** from **a particular retail object**.

## Phase 5 — Explain transitions

When policy changes, show the user:

- what security property is newly required;
- which of their existing authenticators already satisfy it;
- the cheapest valid way to close any remaining gap;
- how recovery works if that factor is lost.

## Success metrics

Security:

- account takeover rate;
- phishing-success rate;
- privileged-action compromise rate;
- recovery fraud rate.

Friction:

- repeat identity-verification rate;
- forced hardware-purchase rate;
- lockout rate;
- median authentication ceremonies per 30 active days;
- support contacts per 1,000 high-assurance users.

The ideal migration improves the first group while reducing the second.
