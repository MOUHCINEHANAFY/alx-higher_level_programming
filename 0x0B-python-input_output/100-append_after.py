#!/usr/bin/python3
"""innsertion fct"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text.

    Args:
        filename (str): File name.
        search_string (str): Lookup string.
        new_string (str): The string to add.
        """
        text = ""
        with open(filename) as r:
            for line in r:
                text += line
                if search_string in line:
                    text += new_string
        with open(filename, "w") as w:
        w.write(text)
