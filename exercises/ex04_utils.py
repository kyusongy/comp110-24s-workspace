"""Useful functions."""

__author__: str = "730720425"


def all(x: list[int], nbr: int) -> bool:
    """Return a bool indicating whether or not all the ints in the list are the same as the given int."""
    count: int = 0
    for i in x:
        if i == nbr:
            count += 1
    if count == len(x):
        return True
    else:
        return False


def max(x: list[int]) -> int:
    """Return the largest in the List."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    temp_max: int = 0
    for i in x:
        if i >= temp_max:
            temp_max = i
    return temp_max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if len(x) != len(y):
        return False
    else:
        count:int = 0
        idx_x: int = 0
        while idx_x < len(x):
            for idx_y in range(0, len(y)):
                idx_x = idx_y
                if x[idx_x] == y[idx_y]:
                    count += 1
            idx_x += 1
        if count == len(x):
            return True
        else:
            return False


def extend(x: list[int], y: list[int]) -> None:
    """Mutate the first list of int values by appending the second lists values to the end of it. """
    for i in y:
        x.append(i)