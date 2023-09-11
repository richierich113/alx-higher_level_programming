#!/usr/bin/python3
"""This module inherits from the list class
"""


class MyList(list):
    def print_sorted(self):
        sorted_list = tuple(self)
        print(sorted_list)
