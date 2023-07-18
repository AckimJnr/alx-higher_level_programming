#!/usr/bin/python3
"""
Contains operations for working with squares
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from base class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Construct right values for our variables
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Get variable number arguments, and key pair sets
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns dictionary rep of the square
        """
        return {
            'id': self.id, 'x': self.x,
            'size': self.size, 'y': self.y
        }
