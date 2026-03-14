# import warnings module
import warnings


# filter list items by exact type

def filter_by_type(items, data_type):
    # validate first argument as list
    if not isinstance(items, list):
        # raise error for invalid first argument
        raise TypeError('First argument must be a list')

    # define allowed types
    allowed_types = (int, str, float, bool)
    # validate requested type
    if data_type not in allowed_types:
        # raise error for unsupported type
        raise TypeError(f'data_type must be one of {allowed_types}, got {data_type}')

    # collect unsupported item types
    other_types = [item for item in items if not isinstance(item, allowed_types)]
    # emit warning if unsupported items were found
    if other_types:
        # show warning text
        warnings.warn(
            f'List contains elements of types other than int, str, float, bool: {other_types}. '
            'They will be ignored in filtering.',
            UserWarning
        )

    # return only exact type matches
    return [item for item in items if type(item) is data_type]
