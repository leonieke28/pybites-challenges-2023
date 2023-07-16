from itertools import combinations


def find_number_pairs(numbers, N=10):
    number_pairs = list(combinations(numbers, 2))
    return [pair for pair in number_pairs if pair[0] + pair[1] == N]
