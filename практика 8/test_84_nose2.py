import importlib.util  # Подключаю инструмент для импорта модуля по пути.
import pathlib  # Подключаю работу с путями.
import unittest  # Подключаю стандартный модуль тестирования.

module_path = pathlib.Path(__file__).with_name('84.py')  # Нахожу файл с функциями.
spec = importlib.util.spec_from_file_location('practice8_task84', module_path)  # Готовлю описание модуля.
module = importlib.util.module_from_spec(spec)  # Создаю объект модуля.
spec.loader.exec_module(module)  # Загружаю код из файла.


class TestFunctions(unittest.TestCase):  # Создаю набор параметризованных тестов.
    def test_add_numbers(self):  # Проверяю сложение на нескольких данных.
        cases = [(1, 2, 3), (-1, 1, 0), (10, 5, 15)]  # Готовлю набор входов.
        for a_value, b_value, expected in cases:  # Перебираю каждую тройку.
            with self.subTest(a=a_value, b=b_value):  # Делаю подпроверку как параметризацию.
                self.assertEqual(module.add_numbers(a_value, b_value), expected)  # Сверяю результат.

    def test_multiply_numbers(self):  # Проверяю умножение на нескольких данных.
        cases = [(2, 3, 6), (0, 5, 0), (-2, 4, -8)]  # Готовлю набор входов.
        for a_value, b_value, expected in cases:  # Перебираю каждую тройку.
            with self.subTest(a=a_value, b=b_value):  # Делаю подпроверку как параметризацию.
                self.assertEqual(module.multiply_numbers(a_value, b_value), expected)  # Сверяю результат.

    def test_is_positive(self):  # Проверяю признак положительности.
        cases = [(5, True), (0, False), (-3, False)]  # Готовлю входные примеры.
        for value, expected in cases:  # Иду по каждому примеру.
            with self.subTest(value=value):  # Отдельный подпункт теста.
                self.assertEqual(module.is_positive(value), expected)  # Сверяю результат.

    def test_first_symbol(self):  # Проверяю извлечение первого символа.
        cases = [('кот', 'к'), ('a', 'a'), ('', '')]  # Готовлю разные строки.
        for text, expected in cases:  # Иду по примерам.
            with self.subTest(text=text):  # Разделяю подпроверки.
                self.assertEqual(module.first_symbol(text), expected)  # Проверяю ответ.

    def test_list_sum(self):  # Проверяю сумму списка.
        cases = [([1, 2, 3], 6), ([], 0), ([-1, 1, 5], 5)]  # Готовлю тестовые списки.
        for values, expected in cases:  # Перебираю примеры.
            with self.subTest(values=values):  # Разделяю подпроверки.
                self.assertEqual(module.list_sum(values), expected)  # Сверяю итог.


if __name__ == '__main__':  # Позволяю запускать тесты обычным python.
    unittest.main()  # Стартую тестовый прогон.
