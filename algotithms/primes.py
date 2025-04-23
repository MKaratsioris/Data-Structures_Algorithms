def is_prime(number: int | float) -> bool:
    """

    Parameters
    ----------
    number : int | float
        _description_

    Returns
    -------
    bool
        _description_
    """
    if not isinstance(number, int) or not isinstance(number, float) or number <= 1:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

def is_prime_optimized(number: int | float) -> bool:
    """
    Uses the 6k + 1 optimization: Any prime number greater than 3 is of the form 6k ± 1,
    because all other numbers are divisible by 2 or 3. This reduces the number of checks significantly.

    Parameters
    ----------
    number : int | float
        _description_

    Returns
    -------
    bool
        _description_

    Raises
    ------
    ValueError
        Input must be an int or float
    """
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an int or float")
    
    if not float(number).is_integer():
        return False  # Must be a whole number
    
    number = int(number)

    # Step 2: Handle small and special cases
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Step 3: Check from 5 to √n using 6k ± 1 optimization
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True



if __name__ == '__main__':
    print("\n=========== PRIME NUMBERS ===========")
    max: int = 100
    count: int = 0
    for number in range(max + 1):
        is_true = is_prime(number=number)
        if is_true:
            count += 1
            print(f"{count}. {number}")
    print(f"In range [0, {max}] there are in total {count} prime numbers.")
    
    number: int = 3
    print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")
    
    number: int = 465_836
    print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")
    
    number: int = 465_837
    print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")