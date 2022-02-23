def digital_root(n):
    # first convert the number into a string
    # loop through the number(str) and append it to a list then convert it back into an int
    # sum the list of number
    sum_num = sum(int(n) for n in str(n))
    return sum_num if sum_num < 10 else digital_root(n=sum_num)


def digital_root_one_liner(n):
    # same as above but a one liner
    return n if n < 10 else digital_root_one_liner(sum(int(n) for n in str(n)))


print(digital_root_one_liner(16))
print(digital_root_one_liner(9422))
