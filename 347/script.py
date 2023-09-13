from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    left_chars = []
    right_chars = []

    for char in list(word.upper()):
        if char in LEFT_HAND_CHARS:
            left_chars.append(char)
        elif char in RIGHT_HAND_CHARS:
            right_chars.append(char)

    if not left_chars:
        return Hand.RIGHT

    elif not right_chars:
        return Hand.LEFT

    elif len(left_chars) > 0 and len(right_chars) > 0:
        return Hand.BOTH
