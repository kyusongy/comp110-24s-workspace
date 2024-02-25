"""Mutating functions."""

__author__ = "730720425"


def manual_append(list: list[int], nbr: int) -> None:
    """Manual append a list."""
    list.append(nbr)


def double(list: list[int]) -> None:
    """Double the input list."""
    i = 0
    while i < len(list):
        list[i] *= 2
        i += 1