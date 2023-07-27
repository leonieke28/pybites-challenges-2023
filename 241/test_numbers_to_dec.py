import pytest

from numbers_to_dec import list_to_decimal


def test_correct_input():
    assert list_to_decimal([0, 4, 2, 8]) == 428
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([3]) == 3


@pytest.mark.parametrize(
    "wrong_input_type", [[6, 2, True], [3.6, 4, 1], ["4", 5, 3, 1]]
)
def test_type_errors(wrong_input_type):
    with pytest.raises(TypeError):
        list_to_decimal(wrong_input_type)


@pytest.mark.parametrize("wrong_input_values", [[-3, 12], [11, 23]])
def test_value_errors(wrong_input_values):
    with pytest.raises(ValueError):
        list_to_decimal(wrong_input_values)
