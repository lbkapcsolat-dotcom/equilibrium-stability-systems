# Arm AArch64 Target-Evidence Demo V1

**Artifact ID**

```text
ESS__ARM_AARCH64_TARGET_EVIDENCE
__REPRODUCIBLE_OBJECT_GATE
__V1
```

## Boundary first

This is an independent public demonstration of a narrow software-evidence pattern.

It:

- uses only a tiny original C source file and Clang;
- produces ELF relocatable objects for a declared AArch64 target;
- checks build repeatability and the object target identity;
- includes a deliberately wrong x86-64 target as a negative control;
- does **not** run software on Arm hardware;
- does **not** establish runtime correctness, performance, safety, silicon correctness, or Arm endorsement.

## The question

Can a software evidence package prove that the produced build artifact is both:

1. repeatable under the same declared build inputs, and
2. actually targeted at the declared architecture,

while rejecting a plausible wrong-target artifact?

This demo answers that bounded question.

## Run

Requirements:

- Python 3.10+
- Clang with AArch64 and x86-64 object-generation support

```bash
cd demos/arm_aarch64_target_evidence_v1
python demo.py
python -m unittest -v
```

## Gate

The demo compiles the same source twice with:

```text
clang --target=aarch64-none-elf
```

and once with the negative-control target:

```text
clang --target=x86_64-none-elf
```

Admission requires:

```text
AARCH64_BUILD_1_SHA256 == AARCH64_BUILD_2_SHA256
AND
AARCH64_ELF_MACHINE == 183
AND
NEGATIVE_CONTROL_ELF_MACHINE != 183
```

Otherwise the gate is HOLD.

## Reference execution

Reference environment:

```text
clang version 17.0.0
```

Observed bounded result:

```text
repeated_build_equal: true
arm_elf_machine: 183
declared_target_matches: true
negative_control_elf_machine: 62
negative_control_rejected: true
gate: PASS_BOUNDED
```

The exact SHA-256 values are compiler/version/environment dependent. The invariant is equality between the two same-environment AArch64 builds, not a universal fixed hash.

## Why this matters

A software artifact can exist and tests can run while the evidence chain still fails to establish that the delivered binary targets the intended architecture.

This demo makes one small part of that chain explicit:

```text
SOURCE
-> DECLARED BUILD TARGET
-> BUILD ARTIFACT
-> TARGET IDENTITY
-> REPEATABILITY
-> NEGATIVE CONTROL
-> BOUNDED RECEIPT
```

The same pattern can be extended to richer embedded/software assurance tasks such as ABI assumptions, feature requirements, interface contracts, reproducible toolchains, and release evidence.

## Claim ceiling

Supported:

> In the reference run, two same-environment AArch64 object builds were byte-identical, the ELF machine field matched AArch64, and an x86-64 wrong-target negative control was rejected.

Not supported:

- runtime correctness on Arm hardware;
- hardware validation;
- performance or energy-efficiency claims;
- functional safety claims;
- compliance or certification claims;
- Arm review, approval, endorsement, or affiliation.

## Official ecosystem context

Arm's public Developer Program provides tools, labs, learning, and expert/community access for developers building on Arm:

https://developer.arm.com/arm-developer-program

Arm's Partner Program:

https://www.arm.com/partners

Arm supplier information:

https://www.arm.com/company/suppliers
