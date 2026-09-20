from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
SOURCE = ROOT / "source.c"

# ELF e_machine values.
AARCH64_MACHINE = 183
X86_64_MACHINE = 62


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def elf_machine(path: Path) -> int:
    data = path.read_bytes()
    if len(data) < 20 or data[:4] != b"\x7fELF":
        raise ValueError(f"Not an ELF file: {path}")

    ei_data = data[5]
    if ei_data == 1:
        fmt = "<H"
    elif ei_data == 2:
        fmt = ">H"
    else:
        raise ValueError("Unknown ELF data encoding")

    return struct.unpack(fmt, data[18:20])[0]


def run(cmd: list[str]) -> None:
    subprocess.run(
        cmd,
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def compile_object(target: str, out: Path) -> None:
    run([
        "clang",
        f"--target={target}",
        "-c",
        str(SOURCE),
        "-O2",
        "-ffreestanding",
        "-fno-ident",
        "-o",
        str(out),
    ])


def main() -> int:
    if shutil.which("clang") is None:
        print(json.dumps({"status": "HOLD", "reason": "clang_not_found"}, indent=2))
        return 2

    compiler_version = subprocess.run(
        ["clang", "--version"],
        check=True,
        text=True,
        capture_output=True,
    ).stdout.splitlines()[0]

    BUILD.mkdir(exist_ok=True)

    arm_a = BUILD / "arm_a.o"
    arm_b = BUILD / "arm_b.o"
    wrong = BUILD / "wrong_target_x86_64.o"

    compile_object("aarch64-none-elf", arm_a)
    compile_object("aarch64-none-elf", arm_b)
    compile_object("x86_64-none-elf", wrong)

    arm_hash_a = sha256(arm_a)
    arm_hash_b = sha256(arm_b)
    wrong_hash = sha256(wrong)

    arm_machine = elf_machine(arm_a)
    wrong_machine = elf_machine(wrong)

    repeated_build_equal = arm_hash_a == arm_hash_b
    declared_target_matches = arm_machine == AARCH64_MACHINE
    negative_control_rejected = wrong_machine != AARCH64_MACHINE

    admitted = (
        repeated_build_equal
        and declared_target_matches
        and negative_control_rejected
    )

    result = {
        "artifact_id": (
            "ESS__ARM_AARCH64_TARGET_EVIDENCE"
            "__REPRODUCIBLE_OBJECT_GATE__V1"
        ),
        "declared_target": "AArch64 ELF relocatable object",
        "compiler": compiler_version,
        "compiler_target": "aarch64-none-elf",
        "repeated_build_equal": repeated_build_equal,
        "arm_object_sha256_run_1": arm_hash_a,
        "arm_object_sha256_run_2": arm_hash_b,
        "arm_elf_machine": arm_machine,
        "expected_arm_elf_machine": AARCH64_MACHINE,
        "declared_target_matches": declared_target_matches,
        "negative_control_target": "x86_64-none-elf",
        "negative_control_sha256": wrong_hash,
        "negative_control_elf_machine": wrong_machine,
        "expected_x86_64_elf_machine": X86_64_MACHINE,
        "negative_control_rejected": negative_control_rejected,
        "gate": "PASS_BOUNDED" if admitted else "HOLD",
        "claim_ceiling": (
            "BUILD_ARTIFACT_TARGET_AND_REPEATABILITY_ONLY__"
            "NO_RUNTIME_CORRECTNESS__NO_HARDWARE_VALIDATION__"
            "NO_ARM_ENDORSEMENT"
        ),
    }

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
