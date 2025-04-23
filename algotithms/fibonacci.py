from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive_memoization(n: int) -> int:
    """_summary_

    Parameters
    ----------
    n : int
        _description_

    Returns
    -------
    int
        _description_
    """
    if n <= 1:
        return n
    return fibonacci_recursive_memoization(n - 1) + fibonacci_recursive_memoization(n - 2)

def fibonacci_recursive_naive(n: int) -> int:
    """
    Calculates the n-th Fibonacci number recursively.
    
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    Parameters
    ----------
    n : int
        N-th position in the Fibonacci sequence

    Returns
    -------
    int
        N-th Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive_naive(n - 1) + fibonacci_recursive_naive(n - 2)

def fibonacci_iterative(n: int) -> int:
    """_summary_

    Parameters
    ----------
    n : _type_
        _description_

    Returns
    -------
    int
        _description_
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_analytic(n: int) -> int:
    """
    Calculates the n-th Fibonacci number using the analytic formula:
    F_{n} = ((1 + sqrt(5))^(n) - (1 - sqrt(5))^(n)) / (2^(n) * sqrt(5))
    
    Time Complexity: O(1)
    Space Complexity: O(1)

    Parameters
    ----------
    n : int
        N-th position in the Fibonacci sequence

    Returns
    -------
    int
        N-th Fibonacci number
    """
    phi: float = (1 + sqrt(5)) / 2 # Golden Ratio
    psi: float = (1 - sqrt(5)) / 2
    f_n: int = int((phi ** (n) - psi ** (n)) / sqrt(5))
    #if n < 0:
    #    return (-1) ** (n + 1) * f_n
    return f_n

if __name__ == '__main__':
    print("\nFibonacci Recursive Naive")
    for number in range(10):
        print(f"Fibonacci number #{number}: {fibonacci_recursive_naive(n=number)}")
    print("\nFibonacci Recursive Memoization")
    for number in range(10):
        print(f"Fibonacci number #{number}: {fibonacci_recursive_memoization(n=number)}")
    print("\nFibonacci Iterative")
    for number in range(10):
        print(f"Fibonacci number #{number}: {fibonacci_iterative(n=number)}")
    print("\nFibonacci Analytic")
    for number in range(10):
        print(f"Fibonacci number #{number}: {fibonacci_analytic(n=number)}")
#print("\nFibonacci Analytic - Negative")
#for number in range(-9, 10):
#    print(f"Fibonacci number #{number}: {fibonacci_analytic(n=number)}")