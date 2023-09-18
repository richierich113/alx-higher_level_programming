#!/usr/bin/python3
"""rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """
        self.__width = width
    
