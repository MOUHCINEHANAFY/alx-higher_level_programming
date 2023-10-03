#!/usr/bin/python3
"""

Function print full name

"""


def say_my_name(first_name, last_name=""):
    """
    def of full name fcnt

    Args:
        first_name (str): The first name.
        last_name (str): The last name
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except Exception as e:
        raise Exception(e)
