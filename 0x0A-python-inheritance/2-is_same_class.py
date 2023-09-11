#!/usr/bin/python3
"""Module with a function
"""


def is_same_class(obj, a_class):
    """a function that checks if an object is exactly
    an instance of a specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
