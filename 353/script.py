import typer  # use typer.run and typer.Argument
from typing_extensions import Annotated


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(
    a: Annotated[
        int, typer.Argument(help="The value of the first summand", default=...)
    ],
    b: Annotated[
        int, typer.Argument(help="The value of the second summand", default=...)
    ],
):
    """
    CLI that allows you to add two numbers
    """
    result = sum_numbers(a, b)
    typer.echo(result)


if __name__ == "__main__":
    typer.run(main)
