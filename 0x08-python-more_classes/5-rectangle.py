#!/usr/bin/python3
"""Classe Rectangle qui définit un rectangle"""


class Rectangle:
    """Créez la classe Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initialise les variables

        Args:
            width (int): Largeur du rectangle
            height (int): Hauteur du rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtient la valeur de la largeur"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Définit la valeur de la largeur

        Args:
            value (int): Valeur de la largeur à définir
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtient la valeur de la hauteur"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Définit la valeur de la hauteur

        Args:
            value (int): Valeur de la hauteur à définir
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule et renvoie l'aire du rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calcule et renvoie le périmètre du rectangle"""
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """ Renvoie une représentation en utilisant #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return string
        for i in range(self.__height):
            string += "#" * self.__width + "\n"
        return (string[:-1])

    def __repr__(self):
        """Renvoie une représentation de dimensions """
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (string)

    def __del__(self):
        """Destructeur pour afficher un message"""
        print("Bye rectangle...")
