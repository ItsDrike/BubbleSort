import typing as t


def bubble_sort(lst: t.List[t.Union[int, float]]) -> list:
    """
    Use bubble sort algorithm to sort any given list of
    numbers or floats, this is being done in O(n^2).
    """
    # Work on a copy of `lst` instead of directly
    # manipulating the original list,
    # this is required to preserve the original list
    lst = lst[:]
    # Bubble sort
    for m in range(1, len(lst)):
        for i in range(len(lst) - m):
            # Pick 2 elements and compare them
            # if el_1 is higher, swap them, else keep them
            element_1 = lst[i]
            element_2 = lst[i + 1]
            if element_1 > element_2:
                lst[i] = element_2
                lst[i + 1] = element_1
    return lst
