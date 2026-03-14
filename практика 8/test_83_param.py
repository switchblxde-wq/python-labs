# import pytest for param tests
import pytest

# import local functions
from functions83 import add_numbers, is_even


# test sum function with several inputs
@pytest.mark.parametrize('first_number, second_number, expected', [
    (1, 2, 3),
    (-5, 5, 0),
    (10, -3, 7),
    (0, 0, 0),
])
def test_add_numbers(first_number, second_number, expected):
    # compare real result with expected value
    assert add_numbers(first_number, second_number) == expected


# test even function with several inputs
@pytest.mark.parametrize('number, expected', [
    (2, True),
    (7, False),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(number, expected):
    # compare real result with expected value
    assert is_even(number) == expected
