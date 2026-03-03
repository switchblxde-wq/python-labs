import sys
import os
import pytest
from lab71 import filter_by_type

def test_filter_int():
    items = [1, 2.5, "hello", True, 3]
    result = filter_by_type(items, int)
    assert result == [1, 3]
    print("test_filter_int passed")

def test_filter_float():
    items = [1, 2.5, "hello", True, 3.14]
    result = filter_by_type(items, float)
    assert result == [2.5, 3.14]
    print("test_filter_float passed")

def test_filter_str():
    items = [1, "world", "hello", True]
    result = filter_by_type(items, str)
    assert result == ["world", "hello"]
    print("test_filter_str passed")

def test_filter_bool():
    items = [1, True, 0, False, "hello"]
    result = filter_by_type(items, bool)
    assert result == [True, False]
    print("test_filter_bool passed")

def test_empty_list():
    items = []
    result = filter_by_type(items, int)
    assert result == []
    print("test_empty_list passed")

def test_mixed_list_no_match():
    items = [1, 2.5, "hello"]
    result = filter_by_type(items, bool)
    assert result == []
    print("test_mixed_list_no_match passed")

def test_exception_non_list():
    with pytest.raises(TypeError, match="First argument must be a list"):
        filter_by_type("not a list", int)
    print("test_exception_non_list passed")

def test_exception_invalid_type():
    with pytest.raises(TypeError, match="data_type must be one of.*list"):
        filter_by_type([1, 2], list)  # list не входит в разрешённые типы
    print("test_exception_invalid_type passed")