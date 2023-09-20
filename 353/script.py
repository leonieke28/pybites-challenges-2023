import typer  # use typer.run and typer.Argument


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
):
    """
    CLI that allows you to add two numbers
    """
    result = sum_numbers(a, b)
    typer.echo(result)


if __name__ == "__main__":
    typer.run(main)
