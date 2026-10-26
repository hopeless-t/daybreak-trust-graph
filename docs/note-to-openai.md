# Note to OpenAI

The intent of this proposal is not to weaken Daybreak-class access controls.

It is to ask a narrower systems question:

> If a person has already completed strong identity proofing, can later security upgrades preserve that assurance without making the person repeatedly prove the same fact or buy a specific additional object when equivalent hardware trust already exists?

A stronger design may be possible by separating four things that are often bundled together:

1. **Identity proofing** — who is this person?
2. **Device assurance** — is this request backed by a trusted, non-exportable key?
3. **Session/action risk** — how much assurance does this operation require right now?
4. **Recovery** — how can the same person regain control after losing one factor?

The proposal is:

- delete raw identity artifacts as early as policy permits;
- preserve a minimal, signed, revocable identity attestation;
- bind that attestation to hardware trust already available on user devices;
- use risk-adaptive step-up instead of constant ceremony;
- keep roaming FIDO2 keys as a strong option rather than assuming one physical form factor is always the only acceptable trust root;
- design recovery as a threshold of independent evidence, not one irreplaceable token.

The target is **less work with equal or higher assurance**.

If the model is wrong, the most useful feedback would be the invariant it fails to preserve.
