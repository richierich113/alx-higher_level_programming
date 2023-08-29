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

    @property
    def size(self):
        """getter property for size instance attribute
        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter property for size instance attribute
        Returns:
            int: value of size
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """function for finding area of square
            Returns:
                int: area of square
        """
        return self.__size * self.__size
