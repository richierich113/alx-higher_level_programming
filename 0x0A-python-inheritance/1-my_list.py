#!/usr/bin/python3
"""This module inherits a list class
"""


class MyList(list):
     """A class that prints a list"""
    def print_sorted(self):
        sorted_list = tuple(self)
        print(sorted_list)
