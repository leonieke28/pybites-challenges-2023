from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
def test_fibonacci_sequence():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34


def test_fibonacci_negative_input():
    # Test for negative input
    try:
        fib(-1)
    except ValueError:
        pass
    else:
        assert False


def test_fibonacci_with_string_input():
    try:
        fib("not an integer")
    except TypeError:
        pass
    else:
        assert False
