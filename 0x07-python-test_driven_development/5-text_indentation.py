#!/usr/bin/python3
"""
Special print function
"""


def text_indentation(text):
    """Print text with two new lines after . , ? :

    Args:
        text (string): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newText = ""
    for i in range(len(text)):
        if not i == 0 and text[i] == " " and text[i - 1] in ".?:":
            continue
        newText += text[i]
        if text[i] in ".?:":
            newText += "\n\n"
    print(newText, end="")
