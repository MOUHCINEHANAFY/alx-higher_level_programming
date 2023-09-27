#!/usr/bin/python3
"""Définir une classe Square (Carré)."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialiser un nouveau carré.

        Args:
            size (int): La taille du nouveau carré.
        """
        self.size = size

    @property
    def size(self):
        """Obtenir/définir la taille actuelle du carré."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourner la superficie actuelle du carré."""
        return (self.__size * self.__size)
