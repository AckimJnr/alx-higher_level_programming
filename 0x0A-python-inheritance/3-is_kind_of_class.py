#!/usr/bin/python3
"""module similiarities between object instance and class"""


def is_kind_of_class(obj, a_class):
    """Returns True if an object is the instance of"""
    if isinstance(obj, a_class):
        return True
    else:
        if isinstance(obj, type):
            return is_kind_of_class(obj, a_class.__bases__)
        else:
            return False
