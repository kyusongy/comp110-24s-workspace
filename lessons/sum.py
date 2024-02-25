"""Summing the elements of a list using different loops."""

__author__ = "730720425"


def w_sum(vals: list[float]) -> float:
    """While loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """For loop."""
    sum: float = 0.0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    """For i in range loop."""
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum