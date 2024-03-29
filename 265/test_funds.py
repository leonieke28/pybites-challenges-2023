import pytest

from funds import max_fund


community = [
    3,
    2,
    6,
    4,
    7,
    5,
    -8,
    -9,
    3,
    8,
    4,
    -12,
    3,
    -10,
    -15,
    2,
    6,
    -10,
    6,
    3,
    -1,
    5,
    -5,
    -8,
    11,
    7,
    -9,
    -5,
    -6,
    -2,
    7,
    8,
    11,
    8,
    6,
    -1,
    -6,
    9,
    8,
    6,
    -3,
    4,
    -8,
    3,
    -4,
    1,
    2,
    8,
    -2,
    9,
    -3,
    8,
    -10,
    -8,
    5,
    -4,
    -6,
    5,
    -1,
    4,
    2,
    2,
    7,
    3,
    -2,
    5,
    1,
    4,
    -7,
    5,
    8,
    4,
    2,
    10,
    -24,
    -10,
    -9,
    -2,
    1,
    6,
    1,
    3,
    -44,
    3,
    6,
    -1,
    9,
    -6,
    5,
    4,
    3,
    6,
    -1,
    0,
    11,
    4,
    8,
    16,
    -33,
    8,
    -2,
    4,
    5,
    3,
    2,
    -8,
    -7,
    -5,
    0,
    2,
    5,
    -2,
    4,
    1,
    2,
    4,
    2,
    -5,
    7,
    4,
    5,
    -2,
    7,
    5,
    -8,
]

poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]


@pytest.mark.parametrize(
    "data, expected",
    [
        (community, (100, 31, 74)),
        (poverty, (13, 6, 9)),
        (some, (50, 9, 12)),
        (extreme, (0, 0, 0)),
    ],
)
def test_funds(data, expected):
    assert max_fund(data) == expected
