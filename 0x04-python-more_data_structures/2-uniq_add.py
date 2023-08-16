#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    # cast my_list to a set
    set_of_list = set(my_list)
    for i in set_of_list:
        sum += i
    return sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result:", result)
