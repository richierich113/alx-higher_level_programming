#!/usr/bin/python3


class Rectangle(BaseGeometry):
    """class that defines rectangle BaseGeometry
    base class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))
    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
