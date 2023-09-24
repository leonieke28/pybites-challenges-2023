import time

import typer
from rich.progress import track

app = typer.Typer()


@app.command()
def progress():
    total = 0
    for _ in track(range(100), description="Processing..."):
        time.sleep(0.1)
        total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    app()
