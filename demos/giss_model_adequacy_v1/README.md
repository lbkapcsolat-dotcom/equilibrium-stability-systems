# ESS GISS Model Adequacy — 5-Minute Reproducible Demo V1

**Artifact ID**

```text
ESS__GISS_MODEL_ADEQUACY
__5_MINUTE_REPRODUCIBLE_DEMO
__MODELE_STYLE_DECISION_SAFEGUARD
__V1
```

## Boundary first

This is an **independent synthetic methodological demonstration**.

It:

- does **not** use NASA or GISS data;
- does **not** run, reproduce, test, or validate NASA GISS ModelE;
- does **not** imply endorsement, review, collaboration, or affiliation with NASA, GISS, Gavin Schmidt, or the ModelE team.

The name identifies the intended level and domain of methodological scrutiny, not institutional provenance.

## The question

Can the same model be:

```text
NUMERICALLY_STABLE
```

while still being:

```text
INADEQUATE_FOR_THE_DECLARED_DECISION
```

?

This demo constructs a deterministic synthetic example where the answer is yes.

## What happens

A simple linear model is fitted to 101 synthetic observations.

Inside the observed regime:

- five-fold validation RMSE is small;
- fitted intercepts vary very little;
- fitted slopes vary very little.

By the predeclared numerical-stability checks, the model passes.

Then a structural stress case is introduced:

```text
x >= 0.60 -> an omitted process adds +0.16 to the real outcome
```

The observed predictor `x` itself has not moved outside its original range. The failure is therefore not presented as simple predictor-range extrapolation. The mapping from observed state to outcome has changed because a relevant mechanism was omitted.

The candidate model remains exactly the same.

The decision rule is:

```text
outcome >= 1.02 -> positive action
```

The declared safeguard permits at most a 5% false-negative rate among actual positive cases.

Under structural stress, the model predicts no positive cases while 41 cases are actually positive.

Therefore:

```text
NUMERICALLY_STABLE = TRUE
DECISION_ADEQUATE = FALSE
SAFEGUARD_STATE = HOLD__STRUCTURAL_MODEL_INADEQUACY
```

## Run in under five minutes

Requires Python 3.10+ and no third-party packages.

```bash
cd demos/giss_model_adequacy_v1
python demo.py
python -m unittest -v
```

## Expected qualitative result

The exact floating-point values are generated deterministically, but the important output is:

```text
numerically_stable: true
stress_actual_positive_count: 41
stress_predicted_positive_count: 0
stress_false_negative_count: 41
stress_false_negative_rate: 1.0
decision_adequate: false
safeguard_state: HOLD__STRUCTURAL_MODEL_INADEQUACY
```

## Why this matters

A model-quality workflow that checks only in-regime predictive stability can conclude:

```text
MODEL LOOKS GOOD
```

while a purpose-conditioned decision safeguard concludes:

```text
DO NOT ADMIT THIS MODEL FOR THIS DECISION
```

The distinction is:

```text
UNCERTAINTY WITHIN THE MODEL
!=
UNCERTAINTY ABOUT MODEL ADEQUACY
```

and:

```text
GOOD MODEL FIT
!=
ADEQUATE FOR A DECLARED DECISION PURPOSE
```

## Falsification path

This artifact is useful only if it is easy to disprove.

It should be marked **HOLD** if any of these fail:

1. `demo.py` is deterministic across repeated runs in the same Python environment;
2. the numerical-stability checks do not pass;
3. the structural stress does not generate decision failures;
4. the safeguard does not reject the model;
5. the tests fail;
6. the artifact is represented as evidence about actual ModelE behavior.

## Claim ceiling

Supported:

> A deterministic synthetic counterexample can exhibit strong in-regime numerical stability while failing a predeclared decision-purpose safeguard under an omitted structural regime.

Not supported:

- any claim about actual ModelE adequacy;
- any claim about NASA/GISS model quality;
- any climate prediction;
- any system-wide validation of Equilibrium;
- any production-readiness claim.

## Next research step

Replace the synthetic structural perturbation with a **public, independently sourced model intercomparison or controlled-model experiment** while preserving the same admission contract:

```text
MODEL PERFORMANCE
-> STRUCTURAL CHALLENGE
-> DECISION CONSEQUENCE
-> PURPOSE-CONDITIONED ADMISSION
-> EXPLICIT CLAIM CEILING
```
