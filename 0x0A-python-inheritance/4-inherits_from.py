#!/usr/bin/python3
"""Check inheritance patterns"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
