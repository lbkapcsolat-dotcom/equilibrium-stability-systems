# Verification Map

This file distinguishes public evidence surfaces from architecture references.

## Evidence Gate

Repository: https://github.com/lbkapcsolat-dotcom/evidence-gate

Publicly inspectable evidence includes deterministic evidence-classification logic and repository history containing bounded ESS evidence-runtime work, exhaustive EQ64 admission testing, and Equilibrium Bridge / Lean CI work.

**Interpretation:** verification is bounded to the artifacts and tests present in that repository. It is not a system-wide ESS verification claim.

## ProofPath

Repository: https://github.com/lbkapcsolat-dotcom/proofpath-public

Publicly inspectable evidence includes the offline educational prototype, its fixed bounded benchmark, tests, and explicit educational claim ceiling.

**Interpretation:** evidence applies only to the stated educational prototype and benchmark.

## Tensor benchmark

Repository: https://github.com/lbkapcsolat-dotcom/tensor-cube-frozen40-benchmark

Publicly inspectable evidence includes the frozen 40-state ledger, exact-distance witnesses, reproduction tooling, regression tests, and explicit scope boundary.

**Interpretation:** evidence applies only to the published benchmark claims.

## ALPHA Control Plane

Surface: private repository

No public implementation verification is claimed from this umbrella repository.

## System-level verification status

```text
PUBLIC_COMPONENT_EVIDENCE: PRESENT
SYSTEM_WIDE_PRODUCTION_VERIFICATION: NOT_CLAIMED
GLOBAL_RUNTIME_ADMISSION: NOT_CLAIMED
```

## Verification rule

A new component may be marked `VERIFIED_BOUNDED` here only when:

1. its public artifact is identifiable;
2. its exact bounded claim is stated;
3. reproducibility evidence or tests are publicly inspectable;
4. the evidence does not rely on undisclosed private state for the advertised public claim.
