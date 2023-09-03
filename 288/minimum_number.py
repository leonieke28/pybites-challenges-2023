from typing import List


def minimum_number(digits: List[int]) -> int:
    if not digits:
        return 0

    digits_set = set(digits)
    return int("".join(map(str, sorted(digits_set))))
