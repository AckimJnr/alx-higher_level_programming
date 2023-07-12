#!/usr/bin/python3
"""student module"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs="None"):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            serial_data = {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
        else:
            serial_data = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        return serial_data
