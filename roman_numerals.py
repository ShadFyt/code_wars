from typing import Dict, List


def solution(n):

    roman_dict: Dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    to_roman: List = []

    while n > 0:
        num = list(roman_dict.items())[0]

        if n >= num[1]:
            n -= num[1]
            to_roman.append(num[0])
        else:
            roman_dict.pop(num[0])
    print("".join(to_roman))


solution(1989)
solution(1889)
solution(3)
