# подключаем модуль
import pytest

# подключаем модуль
from functions83 import add_numbers, is_even


# задаём декоратор
@pytest.mark.parametrize('first_number, second_number, expected', [
    (1, 2, 3),
    (-5, 5, 0),
    (10, -3, 7),
    (0, 0, 0),
])
def test_add_numbers(first_number, second_number, expected):
    # проверяем условие теста
    assert add_numbers(first_number, second_number) == expected


# задаём декоратор
@pytest.mark.parametrize('number, expected', [
    (2, True),
    (7, False),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(number, expected):
    # проверяем условие теста
    assert is_even(number) == expected
