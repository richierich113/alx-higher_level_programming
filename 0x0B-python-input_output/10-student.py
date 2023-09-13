#!/usr/bin/python3
"""module has a class Student"""


class Student:
    """student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict of Student in json form
        """
        is_all_strs = True
        if isinstance(attrs, list):
            for elem in attrs:
                if not isinstance(elem, str):
                    is_all_strs = False
        else:
            is_all_strs = False

        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys()) and
                (not is_all_strs or key in attrs)}
