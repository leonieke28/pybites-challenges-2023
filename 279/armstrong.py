def is_armstrong(n: int) -> bool:
    numbers = [int(x) for x in str(n)]

    if len(numbers) == 1:
        return True

    result = [(number ** len(numbers)) for number in numbers]
    return sum(result) == n
