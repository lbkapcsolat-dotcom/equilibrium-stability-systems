# Equilibrium Stability Systems (ESS)

**Evidence-bounded AI · Model adequacy · Reproducible decision support**

Equilibrium Stability Systems (ESS) is a research-stage technical program focused on making high-stakes technical claims easier to inspect, challenge, reproduce, and bound.

The public question is simple:

> **What evidence supports this claim, what could falsify it, and where must the claim stop?**

> **Status:** RESEARCH_STAGE · NOT_PRODUCTION_CLAIM

## Public demonstrations

### Evaluate one mechanism in 5 minutes
**[Evaluate Equilibrium in 5 Minutes](EVALUATE_IN_5_MINUTES.md)**

A small runnable example with bounded tests, adversarial controls, and an explicit claim ceiling.

### C≤V claim-admission kernel
**[C≤V Claim Admission Kernel](demos/claim_admission_kernel_v1/README.md)**

Offline research-stage fail-closed admission gate with one-command replay and five visible negative controls. Claim ceiling: synthetic replay only, no real actuation or production admission.

### Synthetic model-adequacy challenge
**[5-Minute Synthetic Model Adequacy Demo](demos/giss_model_adequacy_v1/README.md)**

Demonstrates:

```text
NUMERICALLY_STABLE
does not imply
ADEQUATE_FOR_THE_DECLARED_DECISION
```

This demo does not use or validate NASA/GISS ModelE and does not imply NASA/GISS endorsement or affiliation.

### AArch64 target-evidence gate
**[Arm AArch64 Target-Evidence Demo](demos/arm_aarch64_target_evidence_v1/README.md)**

Checks same-environment build repeatability, verifies AArch64 ELF target identity, and rejects a wrong-target x86-64 negative control.

Claim ceiling: build-artifact target and repeatability only. No runtime correctness, hardware validation, certification, or Arm endorsement claim.

## Enterprise pilot offers

- [KUKA 5-Day Test-Evidence Audit](offers/KUKA_5_DAY_TEST_EVIDENCE_AUDIT.md)
- [Arm 5-Day Verification-Evidence Audit](offers/ARM_5_DAY_VERIFICATION_EVIDENCE_AUDIT.md)

## Research / technical collaboration

**[Research & Technical Services](SERVICES.md)**

## Public evidence policy

This public repository is deliberately capability-focused.

It publishes selected demonstrations, bounded verification references, service descriptions, and claim limits.

It is **not** intended to expose or document internal system architecture, internal operating structure, private implementation details, or non-public research state.

See:
- [Public evidence surfaces](PUBLIC_EVIDENCE.md)
- [Publication boundary](PUBLIC_PRIVATE_BOUNDARY.md)
- [Claim ceiling](CLAIM_CEILING.md)
- [Verification notes](VERIFICATION_MAP.md)

## Contact

Research and technical collaboration:

https://www.linkedin.com/in/%C3%A1ron-csaba-r%C3%B3zs%C3%A1s-638383425

---

This repository is the public research and collaboration surface for Equilibrium Stability Systems.
