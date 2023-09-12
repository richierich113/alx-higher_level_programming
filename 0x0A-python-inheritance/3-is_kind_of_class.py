#!/usr/bin/python3
"""Module with a function
"""


def is_kind_of_class(obj, a_class):
    """a function that checks if an object is exactly
    an instance of a specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False


if __name__ == "__main__":
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
