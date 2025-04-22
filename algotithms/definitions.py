from typing import Union
from string import ascii_uppercase, digits

Iterables = Union[list | tuple | set]
Simple = Union[int | float | complex | str | bytes]
DataTypes = Union[Simple | Iterables | bool]

LETTERS_2_NUMBERS: dict[str, list[int]] = {
    "A": [13, 18, 33, 47, 79, 85, 89, 95],
    "B": [4, 5, 35, 56, 83, 97, 107],
    "C": [6, 17, 20, 24, 27, 29, 48, 55, 58, 96, 98, 112],
    "D": [66, 105, 110],
    "E": [63, 68, 99],
    "F": [9, 26, 87, 100, 114],
    "G": [31, 32, 64],
    "H": [1, 2, 67, 72, 80, 108],
    "I": [49, 53, 77],
    "J": [201],
    "K": [19, 36],
    "L": [3, 57, 71, 103, 116],
    "M": [12, 25, 42, 101, 109],
    "N": [7, 10, 11, 28, 41, 60, 93, 102],
    "O": [8, 76],
    "P": [15, 46, 59, 61, 78, 82, 84, 91, 94],
    "Q": [202],
    "R": [37, 44, 45, 75, 86, 88, 104, 111],
    "S": [14, 16, 21, 34, 38, 50, 51, 62, 106],
    "T": [22, 43, 52, 65, 69, 73, 81, 90],
    "U": [92, 113, 115, 117, 118],
    "V": [23],
    "W": [74],
    "X": [54],
    "Y": [39, 70],
    "Z": [30, 40],
    " ": [203],    
}

NUMBERS_2_LETTERS: dict[int, str] = {number: letter for letter, numbers in LETTERS_2_NUMBERS.items() for number in numbers}

CHARACTERS: list[str] = [*ascii_uppercase] #+ [' ']
