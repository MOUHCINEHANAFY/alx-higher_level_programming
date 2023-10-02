#!/usr/bin/python3
"""Classe Rectangle qui définit un rectangl"""


class Rectangle:
    """Créez la classe Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise les variables

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__height

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
        """Méthode pour obtenir l'aire"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Méthode pour obtenir le périmètre"""
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Affiche le rectangle en utilisant le symbole d'impression"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"
        return (string[:-1])

    def __repr__(self):
        """Affiche la largeur et la hauteur du rectangle"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (string)

    def __del__(self):
        """Supprime le rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare deux rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
