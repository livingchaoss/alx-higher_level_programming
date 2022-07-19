#!/usr/bin/python3
"""Define a class square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """Initialize the new square

        Args:
            size (int): size of new square.
        """
    @property
    def size(self):
        """set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self._size)
