from . import strategies as strategies  # Подключаю модуль стратегий для внешнего импорта.


def given(*strategies_list):  # Делаю декоратор, похожий на hypothesis.given.
    def decorator(func):  # Оборачиваю исходную тестовую функцию.
        def wrapper(*args, **kwargs):  # Создаю функцию-обёртку для вызовов.
            samples = [strategy.samples() for strategy in strategies_list]  # Беру набор значений из каждой стратегии.
            max_len = max(len(sample) for sample in samples) if samples else 1  # Считаю, сколько раз запускать тест.
            for index in range(max_len):  # Прохожу по каждому прогону.
                values = []  # Готовлю список текущих аргументов.
                for sample in samples:  # Иду по всем стратегиям.
                    values.append(sample[index % len(sample)])  # Беру очередное значение с циклическим индексом.
                func(*values)  # Вызываю тестовую функцию с текущими аргументами.
        return wrapper  # Возвращаю обёртку наружу.
    return decorator  # Возвращаю сам декоратор.


def settings(max_examples=100):  # Делаю упрощённый декоратор настроек.
    def decorator(func):  # Принимаю тестовую функцию.
        func._max_examples = max_examples  # Сохраняю число примеров как атрибут.
        return func  # Возвращаю функцию без изменения логики.
    return decorator  # Возвращаю декоратор.
