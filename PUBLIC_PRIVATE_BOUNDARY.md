# Public / Private Boundary

## Public by design

This repository may expose:

- names and links of public research repositories;
- high-level architecture relationships;
- bounded claim ceilings;
- reproducibility and verification references already public;
- research-stage status and limitations.

## Private by default

This repository must not expose:

- credentials, API keys, tokens, secrets, session material, or connector state;
- private authority, pointer, Master, Boot, seal, or control records;
- private scoring weights, unreleased formulas, or internal thresholds;
- private operational telemetry or user data;
- unpublished source artifacts;
- production runtime admission state.

## Fail-closed publication rule

If it is unclear whether an artifact is public, publication is blocked until its status is independently established.

```text
UNKNOWN_PUBLICATION_STATUS -> DO_NOT_PUBLISH
```

## No authority transfer

The existence of this umbrella repository does not promote it to a production control-plane authority and does not modify authority inside any linked repository.
