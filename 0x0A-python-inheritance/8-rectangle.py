#!/usr/bin/python3
import importlib.util as ut
spec = ut.spec_from_file_location("base_geometry", "7-base_geometry.py")
base_geometry = ut.module_from_spec(spec)
spec.loader.exec_module(base_geometry)
"""Rectangle module inheriting from BaseGeometry"""


class Rectangle(base_geometry.BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
