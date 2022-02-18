"""
    task is to sort a given string. Each word in the string will contain a single number. 
    This number is the position the word should have in the result.
"""


from typing import List, Dict


def order(sentence: str):
    # split sentence into a list
    list_of_words: List = sentence.split(" ")
    list_of_tuple = []
    # loop through the list of words
    for i in range(len(list_of_words)):
        # loop through the word
        for l in list_of_words[i]:
            # check if the letter is a number
            if l.isdigit():
                # if letter is a number then create a tuple with the number as the key
                # and the word as the value then append it to list_of_tuple
                list_of_tuple.append((l, list_of_words[i]))
    # sort the list of tuples
    sorted_words = sorted(list_of_tuple)
    # return and join the the values of the sorted list
    print(" ".join([word[1] for word in sorted_words]))


order("is2 Thi1s T4est 3a")
order("4of Fo1r pe6ople g3ood th5e the2")
order("")
