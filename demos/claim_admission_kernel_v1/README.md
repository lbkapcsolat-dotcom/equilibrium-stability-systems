# C≤V Claim Admission Kernel

**Status: RESEARCH-STAGE · EXPERIMENTAL · NOT PRODUCTION · NO REAL ACTUATION**

A small, independently replayable admission gate for one narrow idea:

> Do not admit a claim or synthetic state transition beyond the verification capacity available for that claim.

The public decision surface is intentionally small:

1. exact schema,
2. actual evidence-byte SHA-256 match,
3. scoped local authority record,
4. human veto,
5. claim-specific `C ≤ V` admission.

A PASS means **`WOULD_EXECUTE` in an offline synthetic replay only**. This repository has no network integration, external-system connector, or actuator path.

## Run it

```bash
./verify.sh
```

No third-party Python packages are required.

The command verifies a deliberately minimal public research-baseline summary, runs unit tests, then shows one positive case and five visible negative controls:

- unexpected schema field,
- evidence-byte mutation,
- authority-scope mismatch,
- human veto,
- `C > V`.

## What it is

A minimal research artifact for testing fail-closed claim admission and reproducible receipts.

## What it is not

It is **not** a safety certification, authorization service, cryptographic identity system, formal proof of arbitrary software correctness, production control layer, or evidence that the `C ≤ V` abstraction is a universal physical law.

Detailed internal research lineage, runtime topology, environment identifiers, and development receipts are intentionally excluded from this public package.

See [TECHNICAL_SPEC.md](TECHNICAL_SPEC.md), [CLAIM_CEILING.md](CLAIM_CEILING.md), and [DEMO_3MIN.md](DEMO_3MIN.md).

## License

MIT. See [`LICENSE`](LICENSE).
