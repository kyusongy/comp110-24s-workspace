"""Splitting a dictionary into two lists."""

__author__ = "730720425"


def get_keys(my_dict: dict[str, int]) -> list[str]:
    """Produce a list of all the keys in the input dictionary."""
    l1: list[str] = []
    if len(my_dict) == 0:
        return l1
    else:
        for key in my_dict:
            l1.append(key)
        return l1
    

def get_values(my_dict: dict[str, int]) -> list[int]:
    """Produce a list of all the values in the input dictionary."""
    l2: list[int] = []
    if len(my_dict) == 0:
        return l2
    else:
        for key in my_dict:
            l2.append(my_dict[key])
        return l2