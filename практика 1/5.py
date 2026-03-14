# комментарий
import random


# комментарий
def print_matrix(matrix):
    # комментарий
    if not matrix:
        # комментарий
        return
    # комментарий
    cols = len(matrix[0])
    # комментарий
    row_format = '{:>3}' * cols
    # комментарий
    for row in matrix:
        # комментарий
        print(row_format.format(*row))


# комментарий
if __name__ == '__main__':
    # комментарий
    try:
        # комментарий
        row_count = int(input('Введите количество строк N: '))
    except (EOFError, ValueError):
        # комментарий
        row_count = 2

    # комментарий
    try:
        # комментарий
        col_count = int(input('Введите количество столбцов M: '))
    except (EOFError, ValueError):
        # комментарий
        col_count = 3

    # комментарий
    matrix = [[random.randint(20, 80) for _ in range(col_count)] for _ in range(row_count)]
    # комментарий
    print('Сгенерированная матрица:')
    # комментарий
    print_matrix(matrix)
