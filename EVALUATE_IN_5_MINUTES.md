# Evaluate Equilibrium in 5 Minutes

This is the shortest public path for a technically competent reviewer to evaluate one concrete Equilibrium research property without reading the whole architecture.

## What this evaluates

A bounded claim:

> A small public ESS evidence component deterministically maps explicit evidence assessments to one of three states and fails closed on contradiction, missing support, and unknown assessment values.

This is **not** a system-wide validation of Equilibrium.

## 0:00–1:00 — Understand the rule

The public Evidence Gate implements three outcomes:

```text
any contradiction      -> CONFLICTING
otherwise any support  -> SUPPORTED
otherwise              -> INSUFFICIENT
unknown assessment     -> ERROR / fail closed
```

Repository:

https://github.com/lbkapcsolat-dotcom/evidence-gate

The decision rule is deliberately independent of an LLM.

## 1:00–2:00 — Clone and run

Requires Python 3.10+ and no third-party packages.

```bash
git clone https://github.com/lbkapcsolat-dotcom/evidence-gate.git
cd evidence-gate
python evidence_gate.py examples/example.json
```

Expected classification:

```text
SUPPORTED
```

The example contains one supporting item and one insufficient item, with no contradiction.

## 2:00–3:00 — Run the bounded test suite

```bash
python -m unittest -v
```

The public suite checks:

- support without contradiction -> `SUPPORTED`
- any contradiction -> `CONFLICTING`
- no support or contradiction -> `INSUFFICIENT`
- empty evidence -> `INSUFFICIENT`
- unknown assessment -> rejected

A failure in any of these checks means the bounded evaluation is **HOLD**.

## 3:00–4:00 — Run two adversarial controls

### Contradiction must dominate support

```bash
python -c "from evidence_gate import classify_claim; print(classify_claim('demo',[{'assessment':'supports'},{'assessment':'contradicts'}]).status.value)"
```

Expected:

```text
CONFLICTING
```

### Unknown evidence state must not silently pass

```bash
python -c "from evidence_gate import classify_claim; classify_claim('demo',[{'assessment':'maybe'}])"
```

Expected:

```text
ValueError
```

The second command should terminate with an error. That is the intended fail-closed behavior.

## 4:00–5:00 — Check the claim ceiling

What the run supports:

```text
PUBLIC_COMPONENT_EVIDENCE: PRESENT
DETERMINISTIC_RULE: INSPECTABLE
NEGATIVE_CONTROL: PRESENT
FAIL_CLOSED_UNKNOWN_INPUT: PRESENT
```

What it does **not** support:

```text
ESS_PRODUCTION_READY
ESS_SYSTEM_WIDE_VALIDATED
GENERAL_TRUTH_DETECTION
MEDICAL_OR_LEGAL_AUTHORITY
GLOBAL_RUNTIME_ADMISSION
```

## Five-minute decision

Mark the public demonstration:

```text
PASS_BOUNDED
```

only if all of the following are directly observed:

1. the repository is publicly accessible;
2. the example returns the expected state;
3. the public tests pass;
4. contradiction overrides support;
5. an unknown assessment is rejected;
6. the reviewer accepts that the observed evidence supports only the bounded component claim.

Otherwise:

```text
HOLD
```

## Why this path exists

Equilibrium contains deeper work on evidence, finite-state admission logic, formal verification, control-plane boundaries, and reproducibility. A reviewer should not need to understand all of that before seeing one falsifiable mechanism work.

The design principle is:

```text
TECHNICAL_DEPTH
-> MINIMAL_RUNNABLE_CLAIM
-> NEGATIVE_CONTROL
-> OBSERVABLE_RESULT
-> EXPLICIT_CLAIM_CEILING
```

That pattern is intended to be repeated for stronger Equilibrium components as their public evidence surfaces mature.
