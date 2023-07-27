import pytest

from numbers_to_dec import list_to_decimal


def test_list_to_decimal():
    assert list_to_decimal([3]) == 3
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([0, 4, 2, 8]) == 428
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 4, 1])
    with pytest.raises(TypeError):
        list_to_decimal(["4", 5, 3, 1])
