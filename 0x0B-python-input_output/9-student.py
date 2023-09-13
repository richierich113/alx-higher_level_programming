#!/usr/bin/python3
"""module has a class called Student"""


class Student:
    """student class or blueprint"""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ gets dictionary representation of Student"""
        return self.__dict__
