# комментарий
import unittest


# комментарий

def f4(numbers):
    # комментарий
    even_numbers = [number for number in numbers if number % 2 == 0]
    # комментарий
    odd_numbers = [number for number in numbers if number % 2 != 0]
    # комментарий
    even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
    # комментарий
    odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0
    # комментарий
    if even_avg > odd_avg:
        # комментарий
        return f'Среднее чётных ({even_avg:.2f}) больше среднего нечётных ({odd_avg:.2f})'
    elif odd_avg > even_avg:
        # комментарий
        return f'Среднее нечётных ({odd_avg:.2f}) больше среднего чётных ({even_avg:.2f})'
    else:
        # комментарий
        return f'Средние равны ({even_avg:.2f})'


# комментарий

def f5(first_value, second_value):
    # комментарий
    if first_value > second_value:
        # комментарий
        return first_value
    else:
        # комментарий
        return second_value


# комментарий
class TestFunctions(unittest.TestCase):
    # комментарий
    def test_f4_mixed(self):
        # комментарий
        self.assertEqual(f4([1, 2, 3, 4]), 'Среднее чётных (3.00) больше среднего нечётных (2.00)')

    # комментарий
    def test_f4_only_even(self):
        # комментарий
        self.assertEqual(f4([2, 4, 6]), 'Среднее чётных (4.00) больше среднего нечётных (0.00)')

    # комментарий
    def test_f4_only_odd(self):
        # комментарий
        self.assertEqual(f4([1, 3, 5]), 'Среднее нечётных (3.00) больше среднего чётных (0.00)')

    # комментарий
    def test_f4_empty(self):
        # комментарий
        self.assertEqual(f4([]), 'Средние равны (0.00)')

    # комментарий
    def test_f4_equal(self):
        # комментарий
        self.assertEqual(f4([1, 2, 3]), 'Средние равны (2.00)')

    # комментарий
    def test_f5_first_greater(self):
        # комментарий
        self.assertEqual(f5(5, 3), 5)

    # комментарий
    def test_f5_second_greater(self):
        # комментарий
        self.assertEqual(f5(3, 5), 5)

    # комментарий
    def test_f5_equal(self):
        # комментарий
        self.assertEqual(f5(4, 4), 4)


# комментарий
if __name__ == '__main__':
    # комментарий
    unittest.main()
