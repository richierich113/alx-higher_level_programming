#!/usr/bin/python3
"""square docstring"""


class Square:
    """document for Square"""

    def __init__(self, size=0, position=(0, 0)):
        """init method to initialize instance attributes
        Args:
            size (int): size of square parameter
            position (tuple): position of # in square
        """
        self.__size = size
        self.__position = position

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
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """getter property for size instance attribute, position
        Returns:
            int: tuple of # position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter property for size instance attribute
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """function for finding area of square
            Returns:
                int: area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """function for finding area of square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print("")
