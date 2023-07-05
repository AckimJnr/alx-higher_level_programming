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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

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

    def area(self):
        """Calculates the area of the rectangle

            Returns:
                int: The calculated area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The calculated perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def _generate_rectangle(self):
        """Generate the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """REturn a string representantion of a rectangle"""
        class_module = self.__class__.__module__
        module_parts = class_module.split('.')
        fname = module_parts[-1] if module_parts else class_module
        return f"<{fname}.{self.__class__.__name__} object at {hex(id(self))}>"

    def __str__(self):
        """Return a string representation of the rectangle"""
        return self._generate_rectangle()
