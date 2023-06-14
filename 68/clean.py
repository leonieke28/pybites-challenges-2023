import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return "".join("" if char in string.punctuation else char for char in input_string)
