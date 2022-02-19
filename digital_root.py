def digital_root(n):
    # first convert the number into a string
    # loop through the number(str) and append it to a list then convert it back into an int
    # sum the list of number
    sum_num = sum([int(n) for n in str(n)])
    if sum_num < 10:
        # return sum_num if less then 10
        return sum_num
    else:
        # rerun the function till number is less then 10
        return digital_root(n=sum_num)


print(digital_root(16))
print(digital_root(9422))
