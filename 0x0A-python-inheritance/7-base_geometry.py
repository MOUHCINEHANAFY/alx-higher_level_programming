#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:
    """definition of the class"""

    def area(self):
        """empty method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """int param def

        Args:
            name (str): Name of param
            value (int): Value of param
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    
