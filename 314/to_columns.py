from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i, name in enumerate(names):
        if i % cols == 0:
            print("", end="")
        print(f"| {name:<10}", end="")
        if i % cols == cols - 1 or i == len(names) - 1:
            print()
