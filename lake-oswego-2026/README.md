# EcoEvidence — Lake Oswego Hacks 2026

**Track:** Hackathon  
**Theme:** Technology for the Planet (Sustainability)  
**Status:** event-window prototype

EcoEvidence is a small, zero-cost browser tool for learning how to inspect sustainability claims without pretending to verify environmental truth.

A student enters:
- a sustainability claim;
- one observation or source excerpt;
- the source type;
- an uncertainty note.

The tool checks four bounded evidence-quality dimensions:
1. traceability;
2. measurement detail;
3. claim/observation vocabulary overlap;
4. uncertainty disclosure.

It returns one of three learning states:
- `READY_TO_COMPARE`
- `NEEDS_CONTEXT`
- `NOT_EVALUABLE`

## Claim ceiling

EcoEvidence does **not** certify that an environmental claim is true, scientifically valid, or policy-worthy. It only checks whether the supplied material is sufficiently structured for a next evidence-comparison step.

## Event-window provenance

This `lake-oswego-2026/` implementation was created during the Lake Oswego Hacks 2026 event window. The surrounding repository predates the event and is not represented as event-created work. Only files inside this directory and the dedicated CI workflow are intended as the event submission artifact.

## Run

Open `index.html` in a browser.

## Test

```bash
node lake-oswego-2026/test.mjs
```

The test suite is dependency-free and deterministic.
