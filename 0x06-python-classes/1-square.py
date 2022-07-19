#!/usr/bin/python3
class Square:
    """Represents a square.
    private instance attribute: size.
    Instantiation with size (no type/value verifcation).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
