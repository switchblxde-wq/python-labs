# комментарий
import warnings


# комментарий

def filter_by_type(items, data_type):
    # комментарий
    if not isinstance(items, list):
        # комментарий
        raise TypeError('First argument must be a list')

    # комментарий
    allowed_types = (int, str, float, bool)
    # комментарий
    if data_type not in allowed_types:
        # комментарий
        raise TypeError(f'data_type must be one of {allowed_types}, got {data_type}')

    # комментарий
    other_types = [item for item in items if not isinstance(item, allowed_types)]
    # комментарий
    if other_types:
        # комментарий
        warnings.warn(
            f'List contains elements of types other than int, str, float, bool: {other_types}. '
            'They will be ignored in filtering.',
            UserWarning
        )

    # комментарий
    return [item for item in items if type(item) is data_type]
