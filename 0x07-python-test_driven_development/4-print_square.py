#!/usr/bin/python3

"""
This module contains a function that prints a square
using # character
"""


def print_square(size):
    """a function that prints a square using # character
    Args:
        size (int): the length of the square
    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and less than zero
        ValueError: if size is less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for colm in range(0, size):
        for row in range(0, size):
            print("#", end='')
        print("", end='\n')


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
