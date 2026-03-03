import warnings

def filter_by_type(items, data_type):
 
    if not isinstance(items, list):
        raise TypeError("First argument must be a list")
    allowed_types = (int, str, float, bool)
    if data_type not in allowed_types:
        raise TypeError(f"data_type must be one of {allowed_types}, got {data_type}")

    # Проверка на элементы неразрешённых типов (для предупреждения)
    other_types = [item for item in items if not isinstance(item, allowed_types)]
    if other_types:
        warnings.warn(
            f"List contains elements of types other than int, str, float, bool: {other_types}. "
            "They will be ignored in filtering.",
            UserWarning
        )

    # Строгая фильтрация по точному типу (чтобы отделить bool от int)
    return [item for item in items if type(item) is data_type]