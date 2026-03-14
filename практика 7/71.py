import warnings  # Подключаю предупреждения для лишних типов.


def filter_by_type(items, data_type):  # Делаю функцию фильтрации по точному типу.
    if not isinstance(items, list):  # Проверяю, что пришёл именно список.
        raise TypeError('First argument must be a list')  # Ругаюсь, если не список.
    allowed_types = (int, str, float, bool)  # Задаю типы, которые разрешены по заданию.
    if data_type not in allowed_types:  # Проверяю, что тип для фильтра разрешён.
        raise TypeError(f'data_type must be one of {allowed_types}, got {data_type}')  # Даю понятную ошибку.
    other_types = [item for item in items if not isinstance(item, allowed_types)]  # Собираю неподходящие элементы.
    if other_types:  # Если такие элементы нашлись.
        warnings.warn(  # Показываю предупреждение пользователю.
            f'List contains elements of types other than int, str, float, bool: {other_types}. They will be ignored in filtering.',  # Текст предупреждения.
            UserWarning,  # Тип предупреждения.
        )  # Закрываю вызов предупреждения.
    return [item for item in items if type(item) is data_type]  # Возвращаю элементы только точного типа.
