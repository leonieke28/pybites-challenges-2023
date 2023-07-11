def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be an integer or a float")
    fmt = fmt.lower()
    if fmt in {"cm", "in"}:
        return round(value * 2.54, 4) if fmt == "cm" else round(value / 2.54, 4)
    else:
        raise ValueError("fmt must be 'cm' or 'in'")
