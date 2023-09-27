#!/usr/bin/python3
"""Définir une classe Square (Carré)."""


class Square:
    """Représente un carré (square)."""

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du nouveau carré.
        """
        if not isinstance(size, int):
            raise TypeError("size doit être un entier (integer)")
        elif size < 0:
            raise ValueError("size doit être >= 0")
        self.__size = size

    def area(self):
        """Retourne la superficie actuelle du carré."""
        return (self.__size * self.__size)
