#!/usr/bin/python3
"""Module with class BaseGeometry
"""


class BaseGeometry():
    """class with Public instance method:
    def area(self)
    """

    def area(self):
        """raises an Exception with a message
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
