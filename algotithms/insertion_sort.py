from collections.abc import Iterable

def insertion_sort(iterable: Iterable) -> None:
    for i in range(1, len(iterable)):
        anchor = iterable[i]
        j = i -1
        while j >= 0 and anchor < iterable[j]:
            iterable[j + 1] = iterable[j]
            j -= 1
        iterable[j + 1] = anchor

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
        insertion_sort(test)
        print(f'sorted array: {test}\n')