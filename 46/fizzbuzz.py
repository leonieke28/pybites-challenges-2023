from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 5 == 0:
        return "Fizz Buzz" if num % 3 == 0 else "Buzz"
    return "Fizz" if num % 3 == 0 else num
