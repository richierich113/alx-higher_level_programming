#!/usr/bin/python3
"""module of square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that  inherits Rectangle and use the logic of the
    __init__ of the Rectangle class.
    The width and height must be assigned
    to the value of size
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides __str__ method and return 
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{ self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates attributes of an instance
        """
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        """
        new_d = super().to_dictionary()
        del new_d['height']
        del new_d['width']
        new_d['size'] = self.size
        return new_d

    def to_csv(self):
        """returns a list containing of  csv file type of rectangle
        """
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
