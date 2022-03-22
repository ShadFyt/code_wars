"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number."""

from typing import List


def create_phone_number(n: List):
    num_list = [str(num) for num in n]
    part_one = "".join(num_list[:3])
    part_two = "".join(num_list[3:6])
    part_three = "".join(num_list[6:])
    print(part_one)
    return f"({part_one}) {part_two}-{part_three}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
