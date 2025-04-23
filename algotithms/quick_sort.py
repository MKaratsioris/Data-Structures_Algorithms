from typing import Any
from collections.abc import Iterable

def swap(a: int, b: int, arr: Iterable) -> None:
    """_summary_

    Parameters
    ----------
    a : int
        _description_
    b : int
        _description_
    arr : Iterable
        _description_
    """
    if a!=b:
        tmp: Any = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(test: Iterable, start: int, end: int) -> int:
    """_summary_

    Parameters
    ----------
    test : Iterable
        _description_
    start : int
        _description_
    end : int
        _description_

    Returns
    -------
    int
        _description_
    """
    pivot_index: int = start
    pivot: Any = test[pivot_index]
    while start < end:
        while start < len(test) and test[start] <= pivot:
            start += 1
        while test[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, test)
    swap(pivot_index, end, test)
    return end

def quick_sort(test: Iterable, start: int, end: int) -> None:
    """
    Quick Sort Algorithm implementing Hoare partition scheme.
    
    Time complexity:    O(logN)
    Space complexity:   O(1)

    Parameters
    ----------
    test : Iterable
        _description_
    start : Any
        _description_
    end : Any
        _description_
    """
    if start < end:
        pi: int = partition(test, start, end)
        quick_sort(test, start, pi-1)
        quick_sort(test, pi+1, end)

if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["Michalis", "Alejandra", "Shiushin", "Tina", "Alejandro"],
        ["Michalis", "michalis", "miChalis", "MiChalis"]
    ]

    for test in tests:
        print(f"{test=}")
        quick_sort(test, 0, len(test)-1)
        print(f'sorted array: {test}\n')

