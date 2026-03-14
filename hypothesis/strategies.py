class ЦелыеСтратегия:  # Создаю класс стратегии для генерации целых чисел.
    def __init__(self, min_value=None, max_value=None):  # Принимаю границы значений.
        self.min_value = -10 if min_value is None else min_value  # Ставлю нижнюю границу по умолчанию.
        self.max_value = 10 if max_value is None else max_value  # Ставлю верхнюю границу по умолчанию.

    def примеры(self):  # Делаю метод, который возвращает набор примеров.
        середина = (self.min_value + self.max_value) // 2  # Считаю среднее число для покрытия диапазона.
        кандидаты = [self.min_value, середина, self.max_value, 0, 1, -1, 2, -2]  # Готовлю типичные точки.
        результат = []  # Создаю список для итоговых примеров.
        for число in кандидаты:  # Иду по всем кандидатам.
            if self.min_value <= число <= self.max_value:  # Оставляю только подходящие числа.
                if число not in результат:  # Убираю повторы, чтобы не гонять одно и то же.
                    результат.append(число)  # Добавляю число в итоговый набор.
        return результат  # Возвращаю готовый список значений.


def integers(min_value=None, max_value=None):  # Повторяю привычное имя функции из hypothesis.strategies.
    return ЦелыеСтратегия(min_value=min_value, max_value=max_value)  # Возвращаю объект стратегии.
