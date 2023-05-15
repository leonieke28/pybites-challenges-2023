from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    deq = deque(string)
    if n > 0:
        deq.rotate(-n)
    else:
        deq.rotate(abs(n))
    return "".join(deq)
