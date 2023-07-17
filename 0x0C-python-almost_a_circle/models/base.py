#!/usr/bin/python3
"""
Model to check the object instantiation
"""


class Base:
    """
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Creating our object instance and checking instance number
        """
        if id is None:    
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
