#!/usr/bin/python3


class BaseGeometry():
    """class for geometry calculations
    """

    def area(self):
        """instance method to calculate area of shape
        Raises:
            Exception: as area is not implemeted
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer input
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
