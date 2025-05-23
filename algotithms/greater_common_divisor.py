def greater_common_divisor_recursive(a: int, b: int) -> int:
    """
    Recursive implementation of the Euclidean Algorithm to calculate the Greatest Common Divisor.

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        The Greatest Common Divisor.
    """
    if b == 0:
        return a
    return greater_common_divisor_recursive(b, a % b)

def greater_common_divisor_iterative(a: int, b: int) -> int:
    """
    Iterative implementation of the Euclidean Algorithm to calculate the Greatest Common Divisor.

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        The Greatest Common Divisor.
    """
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print("\n=========== GREATEST COMMON DIVISOR RECURSIVE ===========")
    a: int = 0
    b: int = 192
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 192
    
    a: int = 270
    b: int = 0
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t\t{gcd=}")         # Answer: 270
    
    a: int = 270
    b: int = 192
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 6
    
    a: int = 1_000
    b: int = 11
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 1
    
    a: int = 88
    b: int = 16
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 8
    
    a: int = 32
    b: int = 256
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 32
    
    a: int = 347_595_023
    b: int = 34_729
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t{b=}\t\t\t{gcd=}")         # Answer: 1
    
    a: int = 178_296
    b: int = 268_442
    gcd: int = greater_common_divisor_recursive(a=a, b=b)
    print(f"{a=}\t\t{b=}\t\t{gcd=}")         # Answer: 2
    
    
    print("\n=========== GREATEST COMMON DIVISOR ITERATIVE ===========")
    a: int = 0
    b: int = 192
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 192
    
    a: int = 270
    b: int = 0
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t\t{gcd=}")         # Answer: 270
    
    a: int = 270
    b: int = 192
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 6
    
    a: int = 1_000
    b: int = 11
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 1
    
    a: int = 88
    b: int = 16
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 8
    
    a: int = 32
    b: int = 256
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t\t{b=}\t\t\t{gcd=}")         # Answer: 32
    
    a: int = 347_595_023
    b: int = 34_729
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t{b=}\t\t\t{gcd=}")         # Answer: 1
    
    a: int = 178_296
    b: int = 268_442
    gcd: int = greater_common_divisor_iterative(a=a, b=b)
    print(f"{a=}\t\t{b=}\t\t{gcd=}")         # Answer: 2