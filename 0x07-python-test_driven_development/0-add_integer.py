#!/usr/bin/python3
"""
module containing a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    a and be must be integers otherwise raise a TypeError
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(a, int):
        raise TypeError("b must be an integer")
    return int(a+b)
