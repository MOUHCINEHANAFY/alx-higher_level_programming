#!/usr/bin/python3
"Create a class Student."""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
     """Initialize nv Student.

     Args:
         first_name (str): First name.
         last_name (str): Last name.
         age (int): Age
         """
         self.first_name = first_name
         self.last_name = last_name
         self.age = age

    def to_json(self):
         """Get a dictionary representation of the Student."""
         return self.__dict__
