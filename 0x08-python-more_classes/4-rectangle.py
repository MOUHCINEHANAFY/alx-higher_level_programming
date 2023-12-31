#!/usr/bin/python3
"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Create Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Initialize variables

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width value

        Args:
            value (int): Width value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width value

        Args:
            value (int): Height value to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to get area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method to get perimeter"""
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """print rectangle using #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return string
        for i in range(self.__height):
            string += "#" * self.__width + "\n"
        return (string[:-1])

    def __repr__(self):
        """print string"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (string)
