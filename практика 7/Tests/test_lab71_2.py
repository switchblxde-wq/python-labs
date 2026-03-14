import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
import random 
from lab71 import filter_by_type
# Фикстура, возвращающая случайное число от 1 до 100
@pytest.fixture
def random_number():
    return random.randint(1, 100)

# Тест, проверяющий, что число попадает в диапазон
def test_random_number_in_range(random_number):
    assert 1 <= random_number <= 100
    print(f"Случайное число: {random_number}")

# Ещё один тест для демонстрации, что каждый раз число новое
def test_random_number_again(random_number):
    assert 1 <= random_number <= 100
    print(f"Другое случайное число: {random_number}")

# Ещё один тест для демонстрации, что каждый раз число новое
def test_random_number_again(random_number):
    assert 1 <= random_number <= 100
    print(f"Другое случайное число: {random_number}")
# Основные тесты фильтрации
@pytest.mark.parametrize("items, type_to_filter, expected", [
    ([1, 2.5, "hello", True, 3], int, [1, 3]),
    ([1, 2.5, "hello", True, 3.14], float, [2.5, 3.14]),
    ([1, "world", "hello", True], str, ["world", "hello"]),
    ([1, True, 0, False, "hello"], bool, [True, False]),
    ([], int, []),
    ([1, 2.5, "hello"], bool, []),
])
def test_filter_by_type(items, type_to_filter, expected):
    result = filter_by_type(items, type_to_filter)
    assert result == expected
    print(f"OK: {type_to_filter.__name__}")

# Тесты на исключения
@pytest.mark.parametrize("items, type_to_filter, expected_exception, match", [
    ("not a list", int, TypeError, "First argument must be a list"),
    ([1, 2], list, TypeError, "data_type must be one of.*list"),
])
def test_filter_by_type_exceptions(items, type_to_filter, expected_exception, match):
    with pytest.raises(expected_exception, match=match):
        filter_by_type(items, type_to_filter)
    print(f"OK: exception for {type_to_filter}")
    # Тест на предупреждение (элементы неразрешённых типов)
@pytest.mark.parametrize("items, type_to_filter, expected_result, warning_msg", [
    ([1, "two", 3.0, None, [5], True], int, [1], 
     r"List contains elements of types other than int, str, float, bool: .*None.*\[5\]"),
    ([1, 2, "three", {"a":1}], float, [], 
     r"List contains elements of types other than int, str, float, bool: .*\{'a': 1\}"),
])
def test_filter_by_type_warning(items, type_to_filter, expected_result, warning_msg):
    with pytest.warns(UserWarning, match=warning_msg):
        result = filter_by_type(items, type_to_filter)
    assert result == expected_result
    print(f"OK: warning test for {type_to_filter.__name__}")