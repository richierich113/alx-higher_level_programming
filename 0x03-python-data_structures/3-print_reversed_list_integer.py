#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_mylist = my_list[::-1]
    for num in reversed_mylist:
        print("{:d}".format(num))
