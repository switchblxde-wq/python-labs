class Counter:  # Создаю класс счётчика для варианта 5.
    """Простой счётчик с тремя методами.

    >>> c = Counter()
    >>> c.get_value()
    0
    >>> c.increment()
    >>> c.get_value()
    1
    >>> c.decrement()
    >>> c.get_value()
    0
    >>> c.decrement(); c.get_value()
    -1
    """

    def __init__(self):  # Здесь задаю стартовое значение.
        self.value = 0  # Счётчик начинается с нуля.

    def increment(self):  # Метод увеличивает значение на единицу.
        self.value += 1  # Прибавляю один к текущему числу.

    def decrement(self):  # Метод уменьшает значение на единицу.
        self.value -= 1  # Отнимаю один от текущего числа.

    def get_value(self):  # Метод просто возвращает текущее число.
        return self.value  # Отдаю значение наружу.


if __name__ == '__main__':  # Для нечётного варианта запускаю тесты из main.
    import doctest  # Подключаю модуль для проверки примеров из docstring.
    doctest.testmod(verbose=True)  # Запускаю doctest с подробным выводом.
