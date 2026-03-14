# подключаем модуль
import random


# описываем функцию
def print_matrix(matrix):
    # проверяем условие
    if not matrix:
        # выполняем действие
        return
    # сохраняем значение в переменную
    cols = len(matrix[0])
    # сохраняем значение в переменную
    row_format = '{:>3}' * cols
    # проходим цикл
    for row in matrix:
        # выводим результат
        print(row_format.format(*row))


# проверяем прямой запуск файла
if __name__ == '__main__':
    # пробуем выполнить код
    try:
        # сохраняем значение в переменную
        row_count = int(input('Введите количество строк N: '))
    except (EOFError, ValueError):
        # сохраняем значение в переменную
        row_count = 2

    # пробуем выполнить код
    try:
        # сохраняем значение в переменную
        col_count = int(input('Введите количество столбцов M: '))
    except (EOFError, ValueError):
        # сохраняем значение в переменную
        col_count = 3

    # сохраняем значение в переменную
    matrix = [[random.randint(20, 80) for _ in range(col_count)] for _ in range(row_count)]
    # выводим результат
    print('Сгенерированная матрица:')
    # выполняем действие
    print_matrix(matrix)
