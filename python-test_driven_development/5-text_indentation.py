#!/usr/bin/python3
"""
Define a function of text indentation
"""


def text_indentation(text):
    """
    Prints a 2 new lines after each text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new = text.split('\n')
    print('\n'.join(line.strip(' ') for line in new), end='')
