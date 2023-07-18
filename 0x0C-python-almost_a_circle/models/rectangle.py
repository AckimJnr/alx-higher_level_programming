#!/usr/bin/python3
"""
Contains operations for working with rectangles
"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Construct right values for our variables
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Draws the rectangle to stdout
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}"
            )

    def display(self):
        """
        Draw the rectangle to stdout, with respect to x and y positions
        """

        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assign arguments to each attrib
        """
        if args:
            argc = len(args)
            if argc >= 1:
                self.id = args[0]
            if argc >= 2:
                self.width = args[1]
            if argc >= 3:
                self.height = args[2]
            if argc >= 4:
                self.x = args[3]
            if argc >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
