"""Independent synthetic model-adequacy demonstration.

Artifact:
ESS__GISS_MODEL_ADEQUACY__5_MINUTE_REPRODUCIBLE_DEMO
__MODELE_STYLE_DECISION_SAFEGUARD__V1

This code does not use NASA/GISS data, does not run or validate ModelE,
and does not imply NASA/GISS endorsement or affiliation.

Purpose:
Show that a model can be numerically stable on in-regime validation data
while being inadequate for a declared decision purpose under a plausible
unmodelled structural regime.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from typing import Iterable


DECISION_THRESHOLD = 1.02
MAX_FALSE_NEGATIVE_RATE = 0.05
MAX_CV_RMSE = 0.01
MAX_INTERCEPT_RANGE = 0.001
MAX_SLOPE_RANGE = 0.001


@dataclass(frozen=True)
class LinearModel:
    intercept: float
    slope: float

    def predict(self, x: float) -> float:
        return self.intercept + self.slope * x


@dataclass(frozen=True)
class DemoResult:
    artifact_id: str
    sample_count: int
    decision_threshold: float
    max_false_negative_rate: float
    full_fit_intercept: float
    full_fit_slope: float
    cv_max_rmse: float
    cv_intercept_range: float
    cv_slope_range: float
    numerically_stable: bool
    stress_structural_shift: float
    stress_trigger_x: float
    stress_actual_positive_count: int
    stress_predicted_positive_count: int
    stress_false_negative_count: int
    stress_false_negative_rate: float
    decision_adequate: bool
    safeguard_state: str
    claim_ceiling: str


def make_baseline_data() -> tuple[list[float], list[float]]:
    xs = [i / 100 for i in range(101)]
    ys = [0.8 + 0.2 * x + 0.004 * math.sin(12 * x) for x in xs]
    return xs, ys


def fit_linear(xs: Iterable[float], ys: Iterable[float]) -> LinearModel:
    x = list(xs)
    y = list(ys)
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y must have equal length >= 2")

    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    denominator = sum((value - x_mean) ** 2 for value in x)
    if denominator == 0:
        raise ValueError("x must vary")

    slope = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in zip(x, y)
    ) / denominator
    intercept = y_mean - slope * x_mean
    return LinearModel(intercept=intercept, slope=slope)


def rmse(model: LinearModel, xs: Iterable[float], ys: Iterable[float]) -> float:
    x = list(xs)
    y = list(ys)
    return math.sqrt(
        sum((actual - model.predict(value)) ** 2 for value, actual in zip(x, y))
        / len(x)
    )


def five_fold_stability(xs: list[float], ys: list[float]) -> dict[str, float]:
    models: list[LinearModel] = []
    fold_rmse: list[float] = []

    for fold in range(5):
        train_idx = [i for i in range(len(xs)) if i % 5 != fold]
        test_idx = [i for i in range(len(xs)) if i % 5 == fold]

        model = fit_linear(
            [xs[i] for i in train_idx],
            [ys[i] for i in train_idx],
        )
        models.append(model)
        fold_rmse.append(
            rmse(
                model,
                [xs[i] for i in test_idx],
                [ys[i] for i in test_idx],
            )
        )

    intercepts = [model.intercept for model in models]
    slopes = [model.slope for model in models]

    return {
        "max_rmse": max(fold_rmse),
        "intercept_range": max(intercepts) - min(intercepts),
        "slope_range": max(slopes) - min(slopes),
    }


def make_structural_stress_truth(
    xs: list[float],
    baseline_ys: list[float],
    *,
    trigger_x: float = 0.60,
    shift: float = 0.16,
) -> list[float]:
    """Add an unmodelled regime effect while keeping observed x unchanged."""
    return [
        baseline + (shift if x >= trigger_x else 0.0)
        for x, baseline in zip(xs, baseline_ys)
    ]


def run_demo() -> DemoResult:
    xs, baseline_ys = make_baseline_data()
    model = fit_linear(xs, baseline_ys)
    stability = five_fold_stability(xs, baseline_ys)

    numerically_stable = (
        stability["max_rmse"] <= MAX_CV_RMSE
        and stability["intercept_range"] <= MAX_INTERCEPT_RANGE
        and stability["slope_range"] <= MAX_SLOPE_RANGE
    )

    trigger_x = 0.60
    shift = 0.16
    stress_truth = make_structural_stress_truth(
        xs, baseline_ys, trigger_x=trigger_x, shift=shift
    )
    predictions = [model.predict(x) for x in xs]

    actual_positive = [
        actual >= DECISION_THRESHOLD for actual in stress_truth
    ]
    predicted_positive = [
        predicted >= DECISION_THRESHOLD for predicted in predictions
    ]

    false_negative_count = sum(
        actual and not predicted
        for actual, predicted in zip(actual_positive, predicted_positive)
    )
    actual_positive_count = sum(actual_positive)
    predicted_positive_count = sum(predicted_positive)

    false_negative_rate = (
        false_negative_count / actual_positive_count
        if actual_positive_count
        else 0.0
    )

    decision_adequate = (
        numerically_stable
        and false_negative_rate <= MAX_FALSE_NEGATIVE_RATE
    )
    safeguard_state = (
        "ADEQUATE_FOR_DECLARED_PURPOSE"
        if decision_adequate
        else "HOLD__STRUCTURAL_MODEL_INADEQUACY"
    )

    return DemoResult(
        artifact_id=(
            "ESS__GISS_MODEL_ADEQUACY__5_MINUTE_REPRODUCIBLE_DEMO"
            "__MODELE_STYLE_DECISION_SAFEGUARD__V1"
        ),
        sample_count=len(xs),
        decision_threshold=DECISION_THRESHOLD,
        max_false_negative_rate=MAX_FALSE_NEGATIVE_RATE,
        full_fit_intercept=model.intercept,
        full_fit_slope=model.slope,
        cv_max_rmse=stability["max_rmse"],
        cv_intercept_range=stability["intercept_range"],
        cv_slope_range=stability["slope_range"],
        numerically_stable=numerically_stable,
        stress_structural_shift=shift,
        stress_trigger_x=trigger_x,
        stress_actual_positive_count=actual_positive_count,
        stress_predicted_positive_count=predicted_positive_count,
        stress_false_negative_count=false_negative_count,
        stress_false_negative_rate=false_negative_rate,
        decision_adequate=decision_adequate,
        safeguard_state=safeguard_state,
        claim_ceiling=(
            "SYNTHETIC_METHOD_DEMO_ONLY__NO_MODELE_VALIDATION__"
            "NO_NASA_GISS_ENDORSEMENT_OR_AFFILIATION"
        ),
    )


def main() -> int:
    result = run_demo()
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
