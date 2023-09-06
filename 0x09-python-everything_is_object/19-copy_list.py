#!/usr/bin/python3
"""
This module contains a function def copy_list(l)
"""


def copy_list(l):
    """Returns a copy of l
    Args:
        l (list): list parameter
    Returns: Copy of l
    """
    l = [1, 2, 3]
    return l


if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(my_list)
    new_list = copy_list(my_list)
    print(my_list)
    print(new_list)
    print(new_list == my_list)
    print(new_list is my_list)
