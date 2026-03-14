import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
import random
from lab71 import filter_by_type

# fixture returns random number from 1 to 100
@pytest.fixture
def random_number():
    # return random integer in range
    return random.randint(1, 100)

# check that number is inside range
def test_random_number_in_range(random_number):
    # check lower and upper bounds
    assert 1 <= random_number <= 100
    # print debug value
    print(f'Случайное число: {random_number}')

# second check for fixture behavior
def test_random_number_again(random_number):
    # check lower and upper bounds
    assert 1 <= random_number <= 100
    # print debug value
    print(f'Другое случайное число: {random_number}')

# main filter tests
@pytest.mark.parametrize('items, type_to_filter, expected', [
    ([1, 2.5, 'hello', True, 3], int, [1, 3]),
    ([1, 2.5, 'hello', True, 3.14], float, [2.5, 3.14]),
    ([1, 'world', 'hello', True], str, ['world', 'hello']),
    ([1, True, 0, False, 'hello'], bool, [True, False]),
    ([], int, []),
    ([1, 2.5, 'hello'], bool, []),
])
def test_filter_by_type(items, type_to_filter, expected):
    # run target function
    result = filter_by_type(items, type_to_filter)
    # compare with expected list
    assert result == expected
    # print status
    print(f'OK: {type_to_filter.__name__}')

# exception tests
@pytest.mark.parametrize('items, type_to_filter, expected_exception, match', [
    ('not a list', int, TypeError, 'First argument must be a list'),
    ([1, 2], list, TypeError, 'data_type must be one of.*list'),
])
def test_filter_by_type_exceptions(items, type_to_filter, expected_exception, match):
    # assert exception with text
    with pytest.raises(expected_exception, match=match):
        # run target function
        filter_by_type(items, type_to_filter)
    # print status
    print(f'OK: exception for {type_to_filter}')

# warning tests for unsupported item types
@pytest.mark.parametrize('items, type_to_filter, expected_result, warning_msg', [
    ([1, 'two', 3.0, None, [5], True], int, [1],
     r'List contains elements of types other than int, str, float, bool: .*None.*\[5\]'),
    ([1, 2, 'three', {'a': 1}], float, [],
     r"List contains elements of types other than int, str, float, bool: .*\{'a': 1\}"),
])
def test_filter_by_type_warning(items, type_to_filter, expected_result, warning_msg):
    # assert warning and get result
    with pytest.warns(UserWarning, match=warning_msg):
        # run function under warning context
        result = filter_by_type(items, type_to_filter)
    # compare result
    assert result == expected_result
    # print status
    print(f'OK: warning test for {type_to_filter.__name__}')
