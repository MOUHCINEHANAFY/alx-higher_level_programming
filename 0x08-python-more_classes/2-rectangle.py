#!/usr/bin/python3
"""Rectangle class creation"""


class Rectangle:
    """Rectangle class creation"""
    def __init__(self, width=0, height=0):
        """Var init
        Args:
        width (int): Rectangle width
        height (int): Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width value return"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value set"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height value return"""
        return self.__height

    @height.setter
    def height(self, value):
        """Width value set"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to calculate area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method to calculate perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
