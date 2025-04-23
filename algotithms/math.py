from collections.abc import Iterable
from typing import Any

def maximum(iterable: Iterable) -> Any:
    """_summary_

    Parameters
    ----------
    iterable : Iterable
        _description_

    Returns
    -------
    Any
        _description_
    """
    max = None
    for element in iterable:
        if max == None or element > max:
            max = element
    return max

def minimum(iterable: Iterable) -> Any:
    """_summary_

    Parameters
    ----------
    iterable : Iterable
        _description_

    Returns
    -------
    Any
        _description_
    """
    min = None
    for element in iterable:
        if min == None or element < min:
            min = element
    return min

def summation(iterable: Iterable[int | float]) -> int | float:
    """_summary_

    Parameters
    ----------
    iterable : Iterable[int  |  float]
        _description_

    Returns
    -------
    int | float
        _description_
    """
    sum: int | float = 0
    for number in iterable:
        if not isinstance(number, (int, float)):
            return None
        sum += number
    return sum

def average(iterable: Iterable[int | float]) -> float:
    """_summary_

    Parameters
    ----------
    iterable : Iterable[int | float]
        _description_

    Returns
    -------
    float
        _description_
    """
    if not isinstance(number, (int, float)):
        return None
    return summation(iterable=iterable) / len(iterable) if len(iterable) > 0 else None

def median(sorted_iterable: Iterable[int | float]) -> int | float | None:
    """_summary_

    Parameters
    ----------
    iterable : Iterable[int  |  float]
        _description_

    Returns
    -------
    int | float
        _description_
    """
    size: int = len(sorted_iterable)
    if not size:
        return None
    if size % 2 == 1:
        return sorted_iterable[size // 2]
    return (sorted_iterable[(size // 2) - 1] + sorted_iterable[size // 2]) / 2

if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        [88, 93, 75, 100, 80, 67, 71, 92, 90, 83],
        ["Michalis", "Alejandra", "Shiushin", "Tina", "Alejandro"],
        ["Michalis", "michalis", "miChalis", "MiChalis"]
    ]

    for test in tests:
        print(f"{test=}")
        print(f'Max: {maximum(test)}')
        print(f'Min: {minimum(test)}')
        print(f'Avg: {average(test)}')
        print(f'Med: {median(test)}\n')
        