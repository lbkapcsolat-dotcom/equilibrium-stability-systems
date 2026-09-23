# Public-safe claim ceiling

## Allowed

- This repository implements a small offline fail-closed claim-admission kernel.
- It recomputes SHA-256 from supplied evidence bytes.
- It checks a frozen local authority record for declared scope.
- It gives human veto unconditional stopping power.
- It rejects a predeclared claim when `C(q) > V(q)`.
- Its bundled replay exposes five negative controls and produces deterministic receipts.
- The bundled public baseline reports only bounded research evidence claims.

## Not allowed

Do **not** claim that this repository:

- is production-ready;
- is safety-certified;
- controls or protects real critical infrastructure;
- proves arbitrary AI or software systems safe;
- provides cryptographic human identity or external authorization;
- proves `C ≤ V` is a universal mathematical or physical law;
- establishes universal correctness beyond the declared finite research tests;
- replaces domain-specific validation, cybersecurity review, formal verification, or operational safety engineering.

## Publication label

**RESEARCH-STAGE · EXPERIMENTAL · NOT PRODUCTION · NO REAL ACTUATION**
