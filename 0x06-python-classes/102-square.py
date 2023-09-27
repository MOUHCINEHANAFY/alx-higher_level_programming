#!/usr/bin/python3
"""Définir une classe Carré (Square)."""


class Carré:
    """Représente un carré."""

    def __init__(self, taille=0):
        """Initialiser un nouveau carré.

        Args:
            taille (int): La taille du nouveau carré.
        """
        self.taille = taille

    @property
    def taille(self):
        """Obtenir/définir la taille actuelle du carré."""
        return self.__taille

    @taille.setter
    def taille(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("la taille doit être un entier")
        elif valeur < 0:
            raise ValueError("la taille doit être >= 0")
        self.__taille = valeur

    def aire(self):
        """Retourner l'aire actuelle du carré."""
        return self.__taille * self.__taille

    def __eq__(self, autre):
        """Définir la comparaison == pour un Carré."""
        return self.aire() == autre.aire()

    def __ne__(self, autre):
        """Définir la comparaison != pour un Carré."""
        return self.aire() != autre.aire()

    def __lt__(self, autre):
        """Définir la comparaison < pour un Carré."""
        return self.aire() < autre.aire()

    def __le__(self, autre):
        """Définir la comparaison <= pour un Carré."""
        return self.aire() <= autre.aire()

    def __gt__(self, autre):
        """Définir la comparaison > pour un Carré."""
        return self.aire() > autre.aire()

    def __ge__(self, autre):
        """Définir la comparaison >= pour un Carré."""
        return self.aire() >= autre.aire()
