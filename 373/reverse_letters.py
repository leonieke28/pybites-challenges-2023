def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    letters = [char for char in string if char.isalpha()]
    reversed_letters = letters[::-1]
    return "".join(
        reversed_letters.pop(0) if char.isalpha() else char for char in string
    )
