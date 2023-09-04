from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError("n should be greater than or equal to 1")

    power_numbers = [str(number * (10 ** (n - 1))) for number in numbers]

    n_digits = []
    for power_number in power_numbers:
        if power_number.startswith("-"):
            n_digits.append(int(power_number[: n + 1]))
        else:
            n_digits.append(int(power_number[:n]))

    return n_digits
