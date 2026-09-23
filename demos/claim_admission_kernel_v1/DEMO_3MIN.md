# 3-minute demo

## 0:00–0:30 — The rule

Show the README and say:

> This is a tiny offline admission kernel. A request advances only when the schema, actual evidence bytes, scoped authority, human-control gate and claim-specific C≤V rule all pass. PASS means WOULD_EXECUTE in simulation, nothing more.

## 0:30–1:00 — One command

Run:

```bash
./verify.sh
```

Point out that it uses only the Python standard library and verifies a publication-safe bounded baseline before running the tests.

## 1:00–2:20 — Five failures that must stop

The replay visibly demonstrates:

1. **Unexpected field** → schema HOLD.
2. **One evidence byte changed** → SHA-256 mismatch HOLD.
3. **Action outside authority scope** → authority HOLD.
4. **Human veto** → immediate HOLD.
5. **C > V** → claim-capacity HOLD.

Then show the clean synthetic request returning `PASS / WOULD_EXECUTE`.

## 2:20–2:45 — Receipt

Explain that each result has a deterministic receipt binding the payload, actual evidence hash, frozen authority record, C/V scores, gate results and final decision.

## 2:45–3:00 — Claim boundary

End with:

> This is a research-stage executable claim-admission artifact. It has no real actuator, no production integration and no universal safety claim. The point is not to trust a model more. The point is to make unsupported transitions mechanically harder to admit.
