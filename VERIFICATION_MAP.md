# Verification Notes

This file summarizes only public, externally inspectable evidence.

It is not an architecture map.

## Five-minute evaluator

Artifact:

https://github.com/lbkapcsolat-dotcom/equilibrium-stability-systems/blob/main/EVALUATE_IN_5_MINUTES.md

Public evidence includes bounded tests, adversarial controls, and an explicit claim ceiling.

## Synthetic model-adequacy demo

Artifact:

https://github.com/lbkapcsolat-dotcom/equilibrium-stability-systems/tree/main/demos/giss_model_adequacy_v1

Bounded proposition:

```text
strong in-regime numerical stability
does not imply
adequacy for a declared decision purpose
under an omitted structural regime
```

Boundary: no actual ModelE validation, no NASA/GISS endorsement or affiliation claim.

## AArch64 target-evidence demo

Artifact:

https://github.com/lbkapcsolat-dotcom/equilibrium-stability-systems/tree/main/demos/arm_aarch64_target_evidence_v1

Public evidence includes:

- repeated same-environment AArch64 object builds;
- byte-level equality in the reference environment;
- ELF target-identity inspection;
- x86-64 wrong-target negative control;
- automated checks;
- explicit claim ceiling.

Reference result:

```text
repeated_build_equal: true
arm_elf_machine: 183
declared_target_matches: true
negative_control_elf_machine: 62
negative_control_rejected: true
gate: PASS_BOUNDED
```

Boundary: build-artifact target identity and same-environment repeatability only. No runtime correctness, hardware validation, performance, safety, certification, or Arm endorsement claim.

## Verification rule

A public artifact may be described as boundedly verified only when:

1. the exact public claim is stated;
2. the evidence is externally inspectable;
3. reproducibility or direct checks are available where relevant;
4. negative or fail-closed behavior is represented where relevant;
5. the claim ceiling is explicit.

No public artifact implies system-wide validation.
