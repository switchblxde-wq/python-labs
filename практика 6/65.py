# подключаем модуль
import unittest


# описываем функцию

def f4(numbers):
    # выполняем действие
    even_numbers = [number for number in numbers if number % 2 == 0]
    # сохраняем значение в переменную
    odd_numbers = [number for number in numbers if number % 2 != 0]
    # сохраняем значение в переменную
    even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
    # сохраняем значение в переменную
    odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0
    # проверяем условие
    if even_avg > odd_avg:
        # возвращаем результат
        return f'Среднее чётных ({even_avg:.2f}) больше среднего нечётных ({odd_avg:.2f})'
    elif odd_avg > even_avg:
        # возвращаем результат
        return f'Среднее нечётных ({odd_avg:.2f}) больше среднего чётных ({even_avg:.2f})'
    else:
        # возвращаем результат
        return f'Средние равны ({even_avg:.2f})'


# описываем функцию

def f5(first_value, second_value):
    # проверяем условие
    if first_value > second_value:
        # возвращаем результат
        return first_value
    else:
        # возвращаем результат
        return second_value


# описываем класс
class TestFunctions(unittest.TestCase):
    # описываем функцию
    def test_f4_mixed(self):
        # выполняем действие
        self.assertEqual(f4([1, 2, 3, 4]), 'Среднее чётных (3.00) больше среднего нечётных (2.00)')

    # описываем функцию
    def test_f4_only_even(self):
        # выполняем действие
        self.assertEqual(f4([2, 4, 6]), 'Среднее чётных (4.00) больше среднего нечётных (0.00)')

    # описываем функцию
    def test_f4_only_odd(self):
        # выполняем действие
        self.assertEqual(f4([1, 3, 5]), 'Среднее нечётных (3.00) больше среднего чётных (0.00)')

    # описываем функцию
    def test_f4_empty(self):
        # выполняем действие
        self.assertEqual(f4([]), 'Средние равны (0.00)')

    # описываем функцию
    def test_f4_equal(self):
        # выполняем действие
        self.assertEqual(f4([1, 2, 3]), 'Средние равны (2.00)')

    # описываем функцию
    def test_f5_first_greater(self):
        # выполняем действие
        self.assertEqual(f5(5, 3), 5)

    # описываем функцию
    def test_f5_second_greater(self):
        # выполняем действие
        self.assertEqual(f5(3, 5), 5)

    # описываем функцию
    def test_f5_equal(self):
        # выполняем действие
        self.assertEqual(f5(4, 4), 4)


# проверяем прямой запуск файла
if __name__ == '__main__':
    # выполняем действие
    unittest.main()
