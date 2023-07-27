import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "test_input, expected", [([0, 4, 2, 8], 428), ([1, 2], 12), ([3], 3)]
)
def test_list_to_decimal(test_input, expected):
    assert list_to_decimal(test_input) == expected


@pytest.mark.parametrize("test_input", [[6, 2, True], [3.6, 4, 1], ["4", 5, 3, 1]])
def test_type_error(test_input):
    with pytest.raises(TypeError):
        output = list_to_decimal(test_input)


@pytest.mark.parametrize("test_input", [[-3, 5], [23, 11, 1]])
def test_value_error(test_input):
    with pytest.raises(ValueError):
        output = list_to_decimal(test_input)
