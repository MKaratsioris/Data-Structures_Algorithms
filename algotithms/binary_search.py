from decorators import timeit
from definitions import Iterables, Simple

@timeit
def binary_search_loop(sorted_iterable: Iterables, target: Simple) -> tuple[Simple, int] | None:
    """
    Binary Search Looping Algorithm
    -------------------------------
    The input is an iterable of sorted elements. If the element you are looking for is in that sorted iterable, 
    the algorithm  will return its index. Otherwise, the algorithm will return None.

    Time Complexity:    O(logN)
    Space Complexity:   O(1)

    Parameters
    ----------
    sorted_iterable : list | tuple | set
        Sorted collection of data
    target : int | float | complex | str | bytes
        Data to be found in the iterable

    Returns
    -------
    tuple[int | float | complex | str | bytes, int] | None
        A tuple with the position of the item in the sorted_iterable - or None if not found, as well as the 
        number of steps it took to conclude the search
    """
    beg_index = 0
    last_index = len(sorted_iterable) - 1
    steps: int = 0
    while beg_index <= last_index:
        steps += 1
        median = (beg_index + last_index) // 2
        guess: Simple = sorted_iterable[median]
        if guess == target:
            return median, steps
        elif guess < target:
            beg_index = median + 1
        else:
            last_index = median - 1
    return None, steps

def binary_search_recursion(sorted_iterable: Iterables, item: Simple) -> Simple | None:
    """
    Binary Search Recursive Algorithm
    ---------------------------------
    The input is an iterable of sorted elements. If the element you are looking for is in that sorted iterable, 
    the algorithm  will return its index. Otherwise, the algorithm will return None.

    Time Complexity:    O(logN)
    Space Complexity:   O(1)

    Parameters
    ----------
    sorted_iterable : list | tuple | set
        Sorted collection of data
    target : int | float | complex | str | bytes
        Data to be found in the iterable

    Returns
    -------
    int | float | complex | str | bytes | None
        The position of the item in the sorted_iterable. If not found it returns None
    """
    if len(sorted_iterable) == 1:
        if sorted_iterable[0] == item:
            return sorted_iterable[0]
        return None
    low: int = 0
    high: int = len(sorted_iterable) - 1
    middle: int = (high + low) // 2
    guess = sorted_iterable[middle]
    if guess == item:
        return middle
    elif guess < item:
        return binary_search_recursion(sorted_iterable=sorted_iterable[middle + 1:], item=item)
    elif guess > item:
        return binary_search_recursion(sorted_iterable=sorted_iterable[:middle - 1], item=item)


if __name__ == '__main__':
    print("\n======== LOOP ========")
    # 10^(1) => 0 sec
    test_list: list[int] = [x for x in range(11)]
    test_target: int = 10
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) * 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(2) => 0 sec
    test_list: list[int] = [x for x in range(101)]
    test_target: int = 100
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    
    # 10^(3) => 0 sec
    test_list: list[int] = [x for x in range(1_001)]
    test_target: int = 1_000
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(4) => 0 sec
    test_list: list[int] = [x for x in range(10_001)]
    test_target: int = 10_000
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    """
    # 10^(5) => 0 sec
    test_list: list[int] = [x for x in range(100_001)]
    test_target: int = 100_003
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(6) => 0 sec
    test_list: list[int] = [x for x in range(1_000_001)]
    test_target: int = 1_000_000
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search_loop(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    """
    print("\n======== RESURSION ========")
    maximum = 1_025
    guess = maximum - 1
    numbers: list[int] = [number for number in range(maximum)]
    index = binary_search_recursion(numbers, guess)
    print(f"\n{maximum=}\t{index=}\n")