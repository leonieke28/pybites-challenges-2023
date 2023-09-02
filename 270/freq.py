from collections import Counter


def freq_digit(num: int) -> int:
    return int(sorted(Counter(str(num)).most_common(1))[0][0])
