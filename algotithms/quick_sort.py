from typing import Any, Literal
from collections.abc import Iterable

def swap(a: int, b: int, arr: Iterable) -> None:
    """
    Swapping two elements of an iterable.

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

def hoare_partition(iterable: Iterable, start: int, end: int) -> int:
    """
    Hoare partition scheme.

    Parameters
    ----------
    iterable : Iterable
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
    pivot: Any = iterable[pivot_index]
    while start < end:
        while start < len(iterable) and iterable[start] <= pivot:
            start += 1
        while iterable[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, iterable)
    swap(pivot_index, end, iterable)
    return end

def lomuto_partition(iterable: Iterable, start: int, end: int) -> int:
    """
    Lomuto partition scheme.

    Parameters
    ----------
    iterable : Iterable
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
    pivot = iterable[end]
    p_index = start

    for i in range(start, end):
        if iterable[i] <= pivot:
            swap(i, p_index, iterable)
            p_index += 1
    swap(p_index, end, iterable)
    return p_index

def quick_sort(iterable: Iterable, start: int, end: int, partition_scheme: Literal['hoare', 'lomuto'] = 'hoare') -> None:
    """
    Quick Sort Algorithm
    
    Time complexity:    O(logN)
    Space complexity:   O(1)

    Parameters
    ----------
    iterable : Iterable
        _description_
    start : Any
        _description_
    end : Any
        _description_
    partition_scheme : str
        Partition scheme to implement. Acceptable values are 'hoare' and 'lomuto' with the default value set to 'hoare'.
    """
    if len(iterable)== 1:
        return
    if start < end:
        pi: int = lomuto_partition(iterable, start, end) if partition_scheme == 'lomuto' else hoare_partition(iterable, start, end)
        quick_sort(iterable, start, pi-1)
        quick_sort(iterable, pi+1, end)

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

    for index, test in enumerate(tests):
        print(f"{test=}")
        partition_scheme: str = 'lomuto' if index % 2 == 0 else 'hoare'
        quick_sort(test, 0, len(test)-1, partition_scheme='lomuto')
        quick_sort(test, 0, len(test)-1, partition_scheme='hoare')
        print(f'sorted array: {test}')
        print(f"{partition_scheme=}\n")

