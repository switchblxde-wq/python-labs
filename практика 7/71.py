# Подключаем warnings для предупреждений.
import warnings

# Фильтруем элементы списка по точному типу.
def filter_by_type(items, data_type):
    # Проверяем, что первый аргумент действительно список.
    if not isinstance(items, list):
        # Выбрасываем ошибку, если передали не список.
        raise TypeError('Первый аргумент должен быть списком')
    # Задаём разрешённые типы из задания.
    allowed_types = (int, str, float, bool)
    # Проверяем, что тип для фильтрации разрешён.
    if data_type not in allowed_types:
        # Выбрасываем ошибку при неподходящем типе.
        raise TypeError(f'Тип должен быть одним из {allowed_types}')
    # Собираем элементы с неподдерживаемыми типами.
    other_types = [item for item in items if not isinstance(item, allowed_types)]
    # Если нашли такие элементы, показываем предупреждение.
    if other_types:
        # Выводим понятное предупреждение для пользователя.
        warnings.warn('В списке есть элементы с неподдерживаемыми типами, они пропущены', UserWarning)
    # Возвращаем элементы только точного нужного типа.
    return [item for item in items if type(item) is data_type]
