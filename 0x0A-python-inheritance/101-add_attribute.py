#!/usr/bin/python3
""" Addition on an attribute to an object """


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if its possible

    Args:
        obj: The object to add the attribute to
        attr: name of the attribute
        value: the value to be added

    Raises:
        TypeError: If the object cannot have a new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
