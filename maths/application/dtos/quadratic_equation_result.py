from dataclasses import dataclass


@dataclass(frozen=True)
class QuadraticEquationResult:
    x1: float
    x2: float
