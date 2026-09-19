# Equilibrium Stability Systems (ESS)

**Canonical public research entry point**

Equilibrium Stability Systems (ESS) is a research-stage architecture for evidence-bounded decision support, explicit admission logic, reproducible receipts, and fail-closed handling of uncertainty.

This repository is the public map of the research program. It does **not** contain the private system root, credentials, authority records, unreleased formulas, or production control state.

> **Claim ceiling:** RESEARCH_STAGE · NOT_PRODUCTION_CLAIM

## Evaluate in 5 minutes

Start here if you want to inspect one concrete Equilibrium mechanism instead of reading the whole architecture:

**[Evaluate Equilibrium in 5 Minutes](EVALUATE_IN_5_MINUTES.md)**

The path runs a public component, executes its bounded test suite, checks adversarial controls, and ends with an explicit claim ceiling.

## Public research map

```text
Equilibrium Stability Systems (ESS)
├── Evidence Gate
│   └── EQ64 / Equilibrium Bridge
├── ALPHA Control Plane
├── ProofPath
└── Benchmarks
    └── Tensor — Frozen 40-State Exact HTM Benchmark
```

## Components

| Component | Surface | Status | Role |
|---|---|---|---|
| **Evidence Gate** | https://github.com/lbkapcsolat-dotcom/evidence-gate | PUBLIC · VERIFIED_BOUNDED · RESEARCH_STAGE · NOT_PRODUCTION_CLAIM | Deterministic, fail-closed evidence classification and ESS evidence-runtime research. |
| **EQ64 / Equilibrium Bridge** | Evidence Gate research line | PUBLIC · EXPERIMENTAL · RESEARCH_STAGE · NOT_PRODUCTION_CLAIM | Finite-state admission logic, exhaustive state testing, and formal bridge work. |
| **ALPHA Control Plane** | private repository | EXPERIMENTAL · RESEARCH_STAGE · NOT_PRODUCTION_CLAIM | Private control-plane and observer research. Not exposed here as a public implementation surface. |
| **ProofPath** | https://github.com/lbkapcsolat-dotcom/proofpath-public | PUBLIC · VERIFIED_BOUNDED · RESEARCH_STAGE · NOT_PRODUCTION_CLAIM | Offline educational evidence-reasoning prototype with an explicit claim ceiling. |
| **Tensor benchmark** | https://github.com/lbkapcsolat-dotcom/tensor-cube-frozen40-benchmark | PUBLIC · VERIFIED_BOUNDED · RESEARCH_STAGE · NOT_PRODUCTION_CLAIM | Bounded 40-state exact-distance benchmark with reproducibility artifacts and scope limits. |

## Core research principle

```text
evidence
→ deterministic classification
→ explicit state / admission logic
→ reproducible receipt or proof
→ bounded claim
```

A locally verified component does not silently promote the whole system:

```text
COMPONENT_A_VERIFIED_BOUNDED
!= COMPONENT_B_VERIFIED
!= ESS_PRODUCTION_READY
```

## Status vocabulary

- **PUBLIC** — publicly visible repository or artifact.
- **VERIFIED_BOUNDED** — reproducibility evidence exists for the specific bounded claim stated by that component.
- **EXPERIMENTAL** — active research or engineering work that may change.
- **RESEARCH_STAGE** — not represented as production infrastructure.
- **NOT_PRODUCTION_CLAIM** — no claim of production readiness, universal validity, or general-world reliability.

## Repository boundary

This repository intentionally contains only the public research map, boundaries, and verification references.

It does not publish:

- credentials, tokens, secrets, or connector state;
- private authority or pointer records;
- private scoring weights or unreleased formulas;
- private operational data;
- production admission state;
- unsupported claims of system-wide validation.

See:

- [Component registry](COMPONENT_REGISTRY.md)
- [Public/private boundary](PUBLIC_PRIVATE_BOUNDARY.md)
- [Claim ceiling](CLAIM_CEILING.md)
- [Verification map](VERIFICATION_MAP.md)

## Current status

This repository is the canonical **public entry point** for Equilibrium Stability Systems research.

It is not a production authority pointer and does not override the local claim ceilings, histories, or evidence requirements of the linked repositories.
