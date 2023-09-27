#!/usr/bin/python3
"""Définir une classe Square (Carré)."""


class Square:
    """Représenter un carré."""

    def __init__(self, size):
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

    def my_print(self):
        """Afficher le carré avec le caractère #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
