#!/usr/bin/python3
"""Module that defines a class Rectangle
that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines rectangle BaseGeometry
    base class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """custom str method for str and print
        """
        str_ret = "[" + str(self.__class__.__name__) + "] "
        str_ret += str(self.__width) + '/' + str(self.__height)
        return str_ret

    def area(self):
        """overrides base's method for area for use w/ rectangle
        """
        return (self.__width * self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())
