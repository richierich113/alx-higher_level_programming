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
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)
    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")
