#!/usr/bin/python3
"""Module with class Square inheriting Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class, inheriting Rectangle class
    """
    def __init__(self, size):
        """Initialize a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
