#!/usr/bin/python3
""" Module that works on objects """

def lookup(obj):
    """
    Returns a list of attributes and methods of an object

    Args:
        obj: The object to inspect
    Returns:
        a list of available attributes and methods of the object
    """
    return dir(obj)
