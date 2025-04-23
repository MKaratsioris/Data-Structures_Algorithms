from collections.abc import Iterable
from random import randint
from typing import Any

def bubble_sort(iterable: Iterable, key: Any = None) -> Iterable:
    """
    Bubble Sorting Algorithm

    Time Complexity:    O(N^2)
    Space Complexity:   O(1)

    Parameters
    ----------
    iterable : Iterable
        _description_
    key : Any
        -description_

    Returns
    -------
    Iterable
        _description_
    """
    size: int = len(iterable)
    swapped: bool = False
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if not key:
                if iterable[j] > iterable[j + 1]:
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
                    swapped = True
            else:
                if iterable[j][key] > iterable[j + 1][key]:
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
                    swapped = True
        if not swapped:
            return iterable
    return iterable


if __name__ == '__main__':
    print("\n------- int -------")
    numbers: list[int] = [randint(a=1, b=1_000) for _ in range(10)]
    print(f"{numbers=}")
    print(f"{bubble_sort(iterable=numbers)=}")
    numbers_sorted: list[int] = [number for number in range(10)]
    print(f"{numbers_sorted=}")
    print(f"{bubble_sort(iterable=numbers_sorted)=}")
    print("\n------- str -------")
    names: list[str] = ['Michalis', 'Tina', 'Alejandra', 'Shiushin', 'Alejandro']
    print(f"{names=}")
    print(f"{bubble_sort(iterable=names)=}")
    print("\n------- dict -------")
    transactions = [
        { 'name': 'Michalis',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'Alejandra', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'Tina',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'Shiushin',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    print(f"{transactions=}")
    print(f"{bubble_sort(iterable=transactions, key='transaction_amount')=}")
    print(f"{bubble_sort(iterable=transactions, key='name')=}")