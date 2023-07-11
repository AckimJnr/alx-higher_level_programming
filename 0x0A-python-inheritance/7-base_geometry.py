#!/usr/bin/python3
"""Geometry module extension"""


class BaseGeometry:
    """Contains operations to work on geometry"""

    def area(self):
        """Area Calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
