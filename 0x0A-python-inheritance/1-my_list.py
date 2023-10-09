#!/usr/bin/python3
"""
class that inherits from list
"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """ Sorted list print"""
        print(sorted(self))
