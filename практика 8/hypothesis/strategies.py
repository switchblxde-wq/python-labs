class IntegerStrategy:  # Делаю стратегию генерации целых чисел.
    def __init__(self, min_value=-100, max_value=100):  # Задаю границы диапазона.
        self.min_value = min_value  # Сохраняю нижнюю границу.
        self.max_value = max_value  # Сохраняю верхнюю границу.
        self._predicate = None  # Пока дополнительного фильтра нет.

    def filter(self, predicate):  # Добавляю фильтр значений.
        self._predicate = predicate  # Сохраняю функцию-проверку.
        return self  # Возвращаю ту же стратегию для цепочки вызовов.

    def samples(self):  # Возвращаю небольшой набор пробных значений.
        points = [self.min_value, 0, self.max_value, (self.min_value + self.max_value) // 2, 1, -1]  # Собираю опорные точки.
        result = []  # Готовлю список итоговых значений.
        for value in points:  # Прохожу по каждой опорной точке.
            if value < self.min_value or value > self.max_value:  # Пропускаю числа вне диапазона.
                continue  # Переход к следующему числу.
            if self._predicate is not None and not self._predicate(value):  # Пропускаю числа, не прошедшие фильтр.
                continue  # Переход к следующему числу.
            if value not in result:  # Не добавляю дубликаты.
                result.append(value)  # Кладу значение в итоговый список.
        if not result:  # Если список оказался пустым.
            result.append(self.min_value)  # Добавляю нижнюю границу как запасной вариант.
        return result  # Возвращаю готовый набор.


def integers(min_value=-100, max_value=100):  # Функция создаёт стратегию целых чисел.
    return IntegerStrategy(min_value=min_value, max_value=max_value)  # Возвращаю объект стратегии.
