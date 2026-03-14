# подключаем модуль
import doctest

# описываем класс
class Counter:
    # выполняем действие
    """
    simple counter with increment and decrement

    >>> counter = Counter()
    >>> counter.get_value()
    0
    >>> counter.increment()
    >>> counter.get_value()
    1
    >>> counter.decrement()
    >>> counter.get_value()
    0
    >>> counter.decrement()
    >>> counter.get_value()
    -1
    """

    # описываем функцию
    def __init__(self):
        # сохраняем значение в переменную
        self.value = 0

    # описываем функцию
    def increment(self):
        # сохраняем значение в переменную
        self.value += 1

    # описываем функцию
    def decrement(self):
        # сохраняем значение в переменную
        self.value -= 1

    # описываем функцию
    def get_value(self):
        # возвращаем результат
        return self.value

# проверяем прямой запуск файла
if __name__ == '__main__':
    # сохраняем значение в переменную
    doctest.testmod(verbose=True)
