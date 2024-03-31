"""Functions that implement sorting algorithms."""

__author__ = "730720425"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sorted: int = 0
    for unsorted in range(1, len(x)):
        current = x[unsorted]
        while unsorted > 0 and x[unsorted - 1] > current:
            new_max: int = x[unsorted - 1]
            x[unsorted] = new_max
            x[unsorted - 1] = current
            unsorted -= 1
        sorted += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    counter: int = 0
    while counter <= len(x):
        for idx in range(counter, len(x)):
            current: int = x[counter]
            if x[idx] < current:
                new_min: int = x[idx]
                x[counter] = new_min
                x[idx] = current
        counter += 1
    return None
    