from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    major = Counter(numbers).most_common(1)[0][0]
    minor = Counter(numbers).most_common()[: -1 - 1 : -1][0][0]

    return major, minor
