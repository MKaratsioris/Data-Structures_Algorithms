"""
Use Periodic Table Chemical Elements numbers to map the letters of the alphabet.

TODO    Implement filters for digits
TODO    Implement filters for special characters
TODO    Implement functionality for recognizing phrases, based in full-stops.
"""

from random import randint

from definitions import LETTERS_2_NUMBERS, NUMBERS_2_LETTERS, CHARACTERS


def chemo_encrypt(plain_text: str) -> str:
    cipher_text: str = ""
    for character in plain_text.upper():
        if character in CHARACTERS or character == ' ':
            cipher_text += character
    for letter, numbers in LETTERS_2_NUMBERS.items():
        if letter in cipher_text:
            index = randint(0, len(numbers) - 1)
            number = f"{numbers[index]}-" if numbers[index] // 10 >= 1 else f"0{numbers[index]}-"
            cipher_text = cipher_text.replace(letter, number)
    return cipher_text

def chemo_decrypt(cipher_text: str) -> str:
    plain_text: str = ""
    numbers: list[str] = cipher_text.strip().split('-')
    for number in numbers:
        if number.isnumeric():
            plain_text += NUMBERS_2_LETTERS.get(int(number))
    return plain_text.capitalize()


if __name__ == "__main__":
    print("\n=========== CHEMO CIPHER ===========")
    plain_text: str = "~Gooooodmorning Vietnam!!!!!!!!!"
    print(f"{plain_text=}")
    cipher_text: str = chemo_encrypt(plain_text=plain_text)
    print(f"{cipher_text=}")
    plain_text = chemo_decrypt(cipher_text=cipher_text)
    print(f"{plain_text=}\n\n")
    plain_text: str = "Hello world!"
    print(f"{plain_text=}")
    cipher_text: str = chemo_encrypt(plain_text=plain_text)
    print(f"{cipher_text=}")
    plain_text = chemo_decrypt(cipher_text=cipher_text)
    print(f"{plain_text=}\n\n")
    plain_text: str = "Hello! My name is Michalis"
    print(f"{plain_text=}")
    cipher_text: str = chemo_encrypt(plain_text=plain_text)
    print(f"{cipher_text=}")
    plain_text = chemo_decrypt(cipher_text=cipher_text)
    print(f"{plain_text=}\n\n")