# подключаем модуль
import warnings


# описываем функцию

def filter_by_type(items, data_type):
    # проверяем условие
    if not isinstance(items, list):
        # выбрасываем исключение
        raise TypeError('First argument must be a list')

    # сохраняем значение в переменную
    allowed_types = (int, str, float, bool)
    # проверяем условие
    if data_type not in allowed_types:
        # выбрасываем исключение
        raise TypeError(f'data_type must be one of {allowed_types}, got {data_type}')

    # сохраняем значение в переменную
    other_types = [item for item in items if not isinstance(item, allowed_types)]
    # проверяем условие
    if other_types:
        # выполняем действие
        warnings.warn(
            f'List contains elements of types other than int, str, float, bool: {other_types}. '
            'They will be ignored in filtering.',
            UserWarning
        )

    # возвращаем результат
    return [item for item in items if type(item) is data_type]
