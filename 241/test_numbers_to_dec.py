import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([3], 3),
    ],
)
def test_valid_values(test_input, expected):
    actual = list_to_decimal(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input",
    [
        [6, 2, True],
        [3.6, 4, 1],
        ["4", 5, 3, 1],
    ],
)
def test_invalid_input_types(test_input):
    with pytest.raises(TypeError):
        list_to_decimal(test_input)


def test_invalid_range():
    test_input = [-3, 12]

    with pytest.raises(ValueError):
        list_to_decimal(test_input)
