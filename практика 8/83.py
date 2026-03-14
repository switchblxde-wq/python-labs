from hypothesis import given  # Подключаю декоратор генеративного тестирования.
from hypothesis import settings  # Подключаю настройку числа запусков.
from hypothesis import strategies as st  # Подключаю генераторы входных данных.


def abs_number(value):  # Пишу простую функцию для отдельной проверки.
    if value >= 0:  # Если число неотрицательное.
        return value  # Возвращаю как есть.
    return -value  # Иначе меняю знак на плюс.


@settings(max_examples=150)  # Явно задаю количество прогонов теста.
@given(st.integers(min_value=-10_000, max_value=10_000))  # Генерирую много целых чисел.
def test_abs_not_negative(value):  # Тестирую, что модуль не бывает меньше нуля.
    assert abs_number(value) >= 0  # Проверяю главное условие задачи.
