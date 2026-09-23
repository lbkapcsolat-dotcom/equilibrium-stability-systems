# One-page technical specification

## Purpose

The kernel decides whether an offline synthetic claim/state-transition request is **admissible for replay**. Its policy is fail-closed.

## Decision contract

For claim `q`, admission requires all of the following:

`SchemaValid ∧ EvidenceVerified ∧ AuthorityVerified ∧ ¬HumanVeto ∧ C(q) ≤ V(q)`

Any failed or unresolved gate produces `HOLD / WOULD_NOT_EXECUTE`.

`C(q)` is a predeclared normalized effective-complexity score for the claim. `V(q)` is the predeclared normalized verification-capacity score. In this public V1 they are scalar values in `[0,1]`. They are governance inputs, not automatically measured physical quantities.

## Gate order

1. **Schema**: exact required fields, exact types, canonical SHA-256 format.
2. **Veto**: `human_veto=true` stops the request.
3. **Evidence**: SHA-256 is recomputed from actual evidence bytes and compared to the payload.
4. **Authority**: a frozen local authority record is decoded from its verified canonical bytes and checked for action, target, claim, and nonce scope.
5. **Claim profile**: the claim must be predeclared.
6. **C≤V**: `C>V` produces HOLD.

## Receipt

Every decision returns a deterministic receipt whose SHA-256 binds the kernel/schema version, decision and reason, payload SHA-256, actual evidence SHA-256, authority-record SHA-256, `C`, `V`, and gate results.

## Replay contract

`./verify.sh` performs no network calls. It verifies the public baseline summary, runs unit tests, and executes six visible cases: one clean PASS plus five negative controls.

## Public evidence boundary

The bundled `PUBLIC_BASELINE.json` records only bounded, publication-safe evidence claims. Detailed internal research manifests, host/runtime identities, development lineage, and infrastructure-specific receipts are intentionally omitted.
