#!/usr/bin/python3
"""square docstring"""


class Square:
    """document for Square"""

    def __init__(self, size=0):
        """init method to initialize instance attributes
        Args:
            size (int): size of square parameter
        """
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        
