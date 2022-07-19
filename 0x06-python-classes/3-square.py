#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)
