#!/usr/bin/python3
"""module for Rectangle class
"""


class Rectangle:
    """empty Rectangle method
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor for Rectangle class instantiation
        Args:
            width (int): width instnce attribute
            height (int): height instnce attribute
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            perim_val = 0
        else:
            perim_val = (2 * self.__height) + (2 * self.__width)

        return perim_val

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() <= rect_1.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new rectangle with width==height==size
        """
        return cls(size, size)

    def __str__(self):
        """__str__ method for class object when str()
            or print() is called
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return str()
        for i in range(0, self.height):
            for j in range(0, self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """__repr__ method for class object when repr()
            is called, or eval().
        """
        string = f"Rectangle({self.width}, {self.height})"
        return string

    def __del__(self):
        """ called when a rectangle instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {}".format(my_square.area()))
    print("Perimeter: {}".format(my_square.perimeter()))
    print(my_square)
