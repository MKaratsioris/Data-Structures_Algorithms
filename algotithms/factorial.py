from re import sub

def factorial_recursive(number: int) -> int:
    """
    Recursive factorial algorithm

    Parameters
    ----------
    number : int
        _description_

    Returns
    -------
    int
        _description_
    """
    return 1 if number in (0, 1) else number * factorial_recursive(number - 1)

def factorial_iterative(number: int) -> int:
    """
    Iterative factorial algorithm

    Parameters
    ----------
    number : int
        _description_

    Returns
    -------
    int
        _description_
    """
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

def number_formatter(number: int) -> str:
    """
    re.sub() is a function from the re (regular expressions) module. 
    It replaces occurrences of a pattern in the string with a specified replacement.

    The pattern r'(\d{3})' is a regular expression. It matches any sequence of exactly three digits (\d{3}).
    The parentheses around \d{3} create a capture group, which means that the matched digits will be remembered for later use.

    \\1, is the replacement string. The \\1 refers to the first capture group (the three digits), and the , adds a comma after the digits.
    """
    number_str: str = sub(r'(\d{3})', '\\1,', str(number)[::-1])[::-1]
    return number_str[1:] if number_str[0] == ',' else number_str

if __name__ == '__main__':
    print("\n=========== FACTORIAL RECURSIVE ===========")
    maximum: int = 20
    for number in range(maximum):
        fact: int = factorial_recursive(number=number)
        factorial: str = number_formatter(number=fact)
        print(f"{number}! = {factorial}")
    
    print("\n=========== FACTORIAL ITERATIVE ===========")
    maximum: int = 20
    for number in range(maximum):
        fact: int = factorial_iterative(number=number)
        factorial: str = number_formatter(number=fact)
        print(f"{number}! = {factorial}")