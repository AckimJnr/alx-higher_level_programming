#!/usr/bin/python3


class Square:
    """A Class defining a square and its ops """

    def __init__(self, size=0):
        """
        Constructor to initialize the square values

        Args:
            size (int, optional): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
