import pytest
from threesum import three_sum

test_cases = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    (
        [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
        [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
    ),
]


@pytest.mark.parametrize("input_values, expected", test_cases)
def test_three_sum(input_values, expected):
    assert three_sum(input_values) == expected
