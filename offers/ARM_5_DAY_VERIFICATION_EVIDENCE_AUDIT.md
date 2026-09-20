# 5-Day Independent Verification-Evidence Audit for Arm-Based Software Systems

**Equilibrium Stability Systems (ESS) - bounded pilot offer**

## Executive proposition

A build can succeed, a test suite can be green, and the evidence can still be too weak to justify the technical claim that matters.

This five-day pilot asks a narrower question:

> **What exactly does the available software verification evidence justify us claiming about this Arm-targeted component, and what condition forces HOLD?**

The pilot is independent. It does not replace Arm design reviews, Arm Approved programs, functional safety processes, silicon verification, product certification, or internal engineering sign-off.

## Why this fits the Arm ecosystem

Arm's public ecosystem explicitly spans software development, design verification, embedded systems, cloud/edge, AI, automotive, IoT, and partner/supplier relationships.

For software teams, evidence often crosses:

- declared target architecture
- build/toolchain assumptions
- requirements and interfaces
- test coverage
- negative and wrong-target cases
- reproducibility
- release claims
- portability boundaries

A technically successful build does not automatically prove the release claim.

## Five-day pilot

### Day 1 - Claim and target map

Freeze one bounded software component and one technical claim.

Deliverables:

- declared claim
- target / architecture assumptions
- evidence inventory
- claim-to-evidence matrix
- claim ceiling

### Day 2 - Interface and assumption challenge

Identify assumptions that can silently break the claim.

Examples:

- wrong architecture / wrong target
- ABI or interface mismatch
- optional feature assumed as mandatory
- unsupported environment
- missing negative case

Deliverables:

- assumption register
- negative-control set
- explicit failure boundaries

### Day 3 - Reproducibility and provenance

Test whether another evaluator can recreate the evidence chain.

Deliverables:

- build and test provenance
- toolchain identity
- repeatability checks
- hashes where appropriate
- missing-vs-negative evidence separation

### Day 4 - Verification adequacy challenge

Ask whether the test evidence is adequate for the declared purpose rather than merely whether tests ran.

Deliverables:

- adequacy criteria
- counterexamples
- unsupported claim detection
- HOLD / escalate criteria

### Day 5 - Independent evidence receipt

Final package:

- one-page executive receipt
- PASS / HOLD classification against predeclared criteria
- evidence-to-claim traceability matrix
- negative-control results
- reproducibility notes
- prioritized remediation list
- explicit claim ceiling

## Public Arm-targeted proof

ESS includes a small public architecture-target evidence demonstration:

https://github.com/lbkapcsolat-dotcom/equilibrium-stability-systems/tree/main/demos/arm_aarch64_target_evidence_v1

It compiles one original C source twice for AArch64, checks byte repeatability, verifies the ELF target identity, and rejects an x86-64 wrong-target negative control.

Observed reference result:

```text
same-environment AArch64 build equality: PASS
AArch64 ELF target identity: PASS
wrong-target negative control rejected: PASS
overall gate: PASS_BOUNDED
```

Claim ceiling:

```text
NO_RUNTIME_CORRECTNESS
NO_HARDWARE_VALIDATION
NO_ARM_ENDORSEMENT
```

## Suggested first pilot

- one software component
- one declared Arm target
- one existing build/test package
- sanitized or open-source artifacts acceptable
- no production-system access required for the initial pilot

## What makes the pilot different

It does not ask only:

> "Did the tests pass?"

It asks:

> "Which exact claim do those tests support, what could falsify it, and where must the claim stop?"

## Success criteria

An independent evaluator should be able to answer:

1. What is the exact technical claim?
2. What Arm-target or environment assumptions are part of it?
3. Which evidence supports it?
4. Which negative controls challenge it?
5. Can the evidence chain be reproduced?
6. What condition forces HOLD?
7. What does the evidence **not** prove?

## Boundary

**INDEPENDENT · RESEARCH_STAGE · NOT ARM CERTIFICATION · NO ARM AFFILIATION OR ENDORSEMENT CLAIM**

No functional-safety, regulatory, certification, production-readiness, or silicon-correctness opinion is implied.

## Public research entry point

https://github.com/lbkapcsolat-dotcom/equilibrium-stability-systems

## Official Arm routes

Arm Developer Program:
https://developer.arm.com/arm-developer-program

Arm Partner Program:
https://www.arm.com/partners

Arm Procurement / Suppliers:
https://www.arm.com/company/suppliers
