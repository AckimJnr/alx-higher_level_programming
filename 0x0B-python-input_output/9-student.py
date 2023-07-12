#!/usr/bin/python3
"""student module"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        serial_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return serial_data
