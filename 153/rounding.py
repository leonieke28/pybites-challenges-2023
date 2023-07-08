import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
    If up=True (default) round up, else round down.
    Return a new list of rounded values
    """
    rounded_numbers = []
    for num in transactions:
        if up:
            rounded_numbers.append(math.ceil(num))
        else:
            rounded_numbers.append(math.floor(num))

    return rounded_numbers
