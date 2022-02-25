"""
    task is to sort a given string. Each word in the string will contain a single number. 
    This number is the position the word should have in the result.
"""

import re
from typing import List, Dict


def order(sentence: str):
    # split sentence into a list
    list_of_words: List = sentence.split(" ")
    list_of_tuple = []
    # loop through the list of words
    for i in range(len(list_of_words)):
        list_of_tuple.extend(
            (l, list_of_words[i]) for l in list_of_words[i] if l.isdigit()
        )

    # sort the list of tuples
    sorted_words = sorted(list_of_tuple)
    # return and join the the values of the sorted list
    print(" ".join([word[1] for word in sorted_words]))


def order_v2(sentence: str):
    t = sorted(
        [(word[re.search("\d", word).start()], word) for word in sentence.split()]
    )
    print(" ".join([word[1] for word in t]))


order_v2("is2 Thi1s T4est 3a")
# order_v2("4of Fo1r pe6ople g3ood th5e the2")
# order_v2("")
