#!/usr/bin/python3
"""Contains code for working with rectangles"""


class Rectangle:
    """Rectangle representantion

    Attributes:
        None
    Methods:
        None
    """
    def __init__(self, width=0, height=0):
        """ initialise width and height
            Args:
                width (int): defaults to zero
                height (int): default to zero
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
