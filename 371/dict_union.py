def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      The Values of any shared keys are summed up.
    """
    # Your code goes here.
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError
    if not all(isinstance(value, int) for value in a.values()) or not all(
        isinstance(value, int) for value in a.values()
    ):
        raise TypeError
    else:
        return {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}
