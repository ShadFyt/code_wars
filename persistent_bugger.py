"""
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.
"""


def persistence(n):
    tries = 0
    while len(str(n)) >= 2:
        result = 1
        for num in list(str(n)):
            result *= int(num)
        n = result
        tries += 1
        n = str(result)
    print(tries)


persistence(999)
