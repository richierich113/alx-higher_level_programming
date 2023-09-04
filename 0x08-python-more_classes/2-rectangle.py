#!/usr/bin/python3
"""module for Rectangle class
"""


class Rectangle:
    """empty Rectangle method
    """
    def __init__(self, width=0, height=0):
        """constructor for Rectangle class instantiation
        Args:
            width (int): width instnce attribute
            height (int): height instnce attribute
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter property for width instance attribute
        Returns:
            int: width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for width instance attribute
        Raises:
            ValueError: if value is < 0
            TypeError: if value is not an integer
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter property for height instance attribute
        Returns:
            int: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for height instance attribute
        Raises:
            ValueError: if value is < 0
            TypeError: if value is not an integer
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns area of Rectangle
        Returns:
            int: area of Rectangle
        """
        area_val = (self.__height) * (self.__width)
        return area_val

    def perimeter(self):
        """returns perimeter of Rectangle
        Returns:
            int: perimeter of Rectangle
        """
        if Rectangle.height == 0 or Rectangle.width == 0:
            perim_val = 0
        else:
            perim_val = (2 * self.__height) + (2 * self.__width)

        return perim_val


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
