from math import sqrt

def fibonacci_recursive(n: int) -> int:
    """
    Calculates the n-th Fibonacci number recursively.
    
    Time Complexity: O(logN)
    Space Complexity: O(logN)

    Parameters
    ----------
    n : int
        N-th position in the Fibonacci sequence

    Returns
    -------
    int
        N-th Fibonacci number
    """
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

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
    print("Fibonacci Recursive")
    for number in range(21):
        print(f"Fibonacci number #{number}: {fibonacci_recursive(n=number)}")
print("\nFibonacci Analytic")
for number in range(10):
    print(f"Fibonacci number #{number}: {fibonacci_analytic(n=number)}")
#print("\nFibonacci Analytic - Negative")
#for number in range(-9, 10):
#    print(f"Fibonacci number #{number}: {fibonacci_analytic(n=number)}")