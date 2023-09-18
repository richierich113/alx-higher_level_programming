#!/usr/bin/python3
"""base module for all other classes in this project
"""


class Base:
    """base class for use with other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of  the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
