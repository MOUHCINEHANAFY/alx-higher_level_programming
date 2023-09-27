#!/usr/bin/python3
"""Définir une classe Carré."""


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
            raise TypeError("size doit être un entier")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourner l'aire actuelle du carré."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Définir la comparaison == pour un Carré."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Définir la comparaison != pour un Carré."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Définir la comparaison < pour un Carré."""
        return self.area() < other.area()

    def __le__(self, other):
        """Définir la comparaison <= pour un Carré."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Définir la comparaison > pour un Carré."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Définir la comparaison >= pour un Carré."""
        return self.area() >= other.area()
