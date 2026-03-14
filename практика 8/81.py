# комментарий
import doctest

# комментарий
class Counter:
    # комментарий
    """
    simple counter with increment and decrement

    >>> counter = Counter()
    >>> counter.get_value()
    0
    >>> counter.increment()
    >>> counter.get_value()
    1
    >>> counter.decrement()
    >>> counter.get_value()
    0
    >>> counter.decrement()
    >>> counter.get_value()
    -1
    """

    # комментарий
    def __init__(self):
        # комментарий
        self.value = 0

    # комментарий
    def increment(self):
        # комментарий
        self.value += 1

    # комментарий
    def decrement(self):
        # комментарий
        self.value -= 1

    # комментарий
    def get_value(self):
        # комментарий
        return self.value

# комментарий
if __name__ == '__main__':
    # комментарий
    doctest.testmod(verbose=True)
