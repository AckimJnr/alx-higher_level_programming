#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """returns dictionary, string, interger and boolean"""
    attrs = vars(obj)

    serial_data = {}

    for attr_name, attr_value in attrs.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serial_data[attr_name] = attr_value

    return serial_data
