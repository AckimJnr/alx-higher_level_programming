#!/usr/bin/python3
"""Checks if an object is of an instance of the given class"""


def is_same_class(obj, a_class):
    """Checks if an object is of an instance of the given class"""
    return type(obj) is a_class
