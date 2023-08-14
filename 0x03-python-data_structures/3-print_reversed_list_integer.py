#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for idx in range(len(my_list)):
        idx = -(idx + 1)
        print('{:d}'.format(my_list[idx]))
