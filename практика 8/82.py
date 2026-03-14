# подключаем модуль
import random

# подключаем модуль
import pytest

# описываем функцию

def random_matrix(size):
    # возвращаем результат
    return [[random.randint(-3, 3) for _ in range(size)] for _ in range(size)]


# описываем функцию

def multiply_matrices(left_matrix, right_matrix):
    # сохраняем значение в переменную
    size = len(left_matrix)
    # сохраняем значение в переменную
    result_matrix = [[0 for _ in range(size)] for _ in range(size)]
    # проходим цикл
    for row_index in range(size):
        # проходим цикл
        for col_index in range(size):
            # проходим цикл
            for inner_index in range(size):
                # сохраняем значение в переменную
                result_matrix[row_index][col_index] += left_matrix[row_index][inner_index] * right_matrix[inner_index][col_index]
    # возвращаем результат
    return result_matrix


# задаём декоратор
@pytest.mark.parametrize('size', [2, 3, 4])
def test_matrices_are_not_commutative_in_general(size):
    # проходим цикл
    for _ in range(200):
        # сохраняем значение в переменную
        matrix_a = random_matrix(size)
        # сохраняем значение в переменную
        matrix_b = random_matrix(size)
        # сохраняем значение в переменную
        ab_product = multiply_matrices(matrix_a, matrix_b)
        # сохраняем значение в переменную
        ba_product = multiply_matrices(matrix_b, matrix_a)
        # проверяем условие
        if ab_product != ba_product:
            # выполняем действие
            return
    # выполняем действие
    pytest.fail('could not find example where a*b is not equal to b*a')
