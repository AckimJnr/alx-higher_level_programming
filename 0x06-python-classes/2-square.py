#!/usr/bin/python3

class Square:
"""A Class defining a square and its ops """


	def __init__(self, size=0):
		"""
		Constructor to initilize the square values

		Args:
			size (int, optional): The size of the square

		Raises:
			TypeError: If size is not an interger
			Value Error: if size is less than 0
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an interger")
		elif size < 0:
		 	raise ValueError("size must be >= 0")
		 else:
		 	self.__size = size

