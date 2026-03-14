# import unittest for local tests
import unittest


# compare average values of even and odd numbers

def f4(numbers):
    # collect even numbers
    even_numbers = [number for number in numbers if number % 2 == 0]
    # collect odd numbers
    odd_numbers = [number for number in numbers if number % 2 != 0]
    # calculate even average or zero
    even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
    # calculate odd average or zero
    odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0
    # compare averages
    if even_avg > odd_avg:
        # return message for even average
        return f'Среднее чётных ({even_avg:.2f}) больше среднего нечётных ({odd_avg:.2f})'
    elif odd_avg > even_avg:
        # return message for odd average
        return f'Среднее нечётных ({odd_avg:.2f}) больше среднего чётных ({even_avg:.2f})'
    else:
        # return message for equal averages
        return f'Средние равны ({even_avg:.2f})'


# return maximum from two numbers

def f5(first_value, second_value):
    # return first when it is larger
    if first_value > second_value:
        # return max value
        return first_value
    else:
        # return max value
        return second_value


# tests for functions
class TestFunctions(unittest.TestCase):
    # test mixed list case
    def test_f4_mixed(self):
        # check expected text
        self.assertEqual(f4([1, 2, 3, 4]), 'Среднее чётных (3.00) больше среднего нечётных (2.00)')

    # test only even list case
    def test_f4_only_even(self):
        # check expected text
        self.assertEqual(f4([2, 4, 6]), 'Среднее чётных (4.00) больше среднего нечётных (0.00)')

    # test only odd list case
    def test_f4_only_odd(self):
        # check expected text
        self.assertEqual(f4([1, 3, 5]), 'Среднее нечётных (3.00) больше среднего чётных (0.00)')

    # test empty list case
    def test_f4_empty(self):
        # check expected text
        self.assertEqual(f4([]), 'Средние равны (0.00)')

    # test equal average case
    def test_f4_equal(self):
        # check expected text
        self.assertEqual(f4([1, 2, 3]), 'Средние равны (2.00)')

    # test first greater case
    def test_f5_first_greater(self):
        # check max value
        self.assertEqual(f5(5, 3), 5)

    # test second greater case
    def test_f5_second_greater(self):
        # check max value
        self.assertEqual(f5(3, 5), 5)

    # test equal values case
    def test_f5_equal(self):
        # check equal max value
        self.assertEqual(f5(4, 4), 4)


# run tests on direct execution
if __name__ == '__main__':
    # start unittest runner
    unittest.main()
