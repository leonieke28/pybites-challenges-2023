import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r"[^\w\s,]")


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    # result = [i for i, char in enumerate(text) if char == IS_EMOJI]
    return [i for i, char in enumerate(text) if bool(IS_EMOJI.match(char))]
