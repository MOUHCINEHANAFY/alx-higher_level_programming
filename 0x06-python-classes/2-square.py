#!/usr/bin/python3
"""Square class def."""


class Square:
    """square class."""

    def __init__(self, size=0):
        """Init Square.

        Args:
            size (int): The size of square obj.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
