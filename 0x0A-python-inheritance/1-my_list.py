#!/usr/bin/python3
"""Inhereted list class MyList."""


class MyList(list):
    """Print sorted classes."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
