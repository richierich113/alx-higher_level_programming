#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_mylist = reversed(my_list)
    for num in reversed_mylist:
        print("{:d}".format(num))
