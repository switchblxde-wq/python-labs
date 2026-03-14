# import doctest for running examples from docstring
import doctest

# create counter class for variant 5
class Counter:
    # describe class and examples for checks
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

    # set start value
    def __init__(self):
        # store current value
        self.value = 0

    # increase value by one
    def increment(self):
        # update value
        self.value += 1

    # decrease value by one
    def decrement(self):
        # update value
        self.value -= 1

    # return current value
    def get_value(self):
        # give saved value
        return self.value

# run doctest from main for odd variant
if __name__ == '__main__':
    # start doctest with verbose output
    doctest.testmod(verbose=True)
