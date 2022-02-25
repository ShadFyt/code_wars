from ast import List, Tuple


from typing import List

"""
To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
"""


def open_or_senior(data: List[Tuple]):
    # loop through the list of sets
    # first check if member is 55 or older & is handicap greater then 7, if true return "senior"
    # else return "open"
    # members = ["senior" if i[0] >= 55 and i[1] > 7 else "open" for i in data]
    members = [
        # uses tuple unpacking
        "senior" if age >= 55 and handicap > 7 else "open"
        for (age, handicap) in data
    ]

    print(members)


open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)])
open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)])
