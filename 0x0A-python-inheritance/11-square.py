#!/usr/bin/python3
"""module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class, inherits Rectangle class
    """
    def __init__(self, size):
        """constructor for class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """magic str method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
