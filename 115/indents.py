def count_indents(text: str) -> int:
    """
    Count and return the number of leading white-space characters (' ').
    """
    count = 0
    for char in text:
        if char == " ":
            count += 1
        else:
            break
    return count
