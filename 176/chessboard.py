WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    for row in range(size):
        for column in range(size):
            if (row + column) % 2 == 0:
                print(WHITE, end="")
            else:
                print(BLACK, end="")
        print()
