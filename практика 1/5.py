# import random module
import random


# print matrix with aligned columns
def print_matrix(matrix):
    # return when matrix is empty
    if not matrix:
        # finish early
        return
    # get column count
    cols = len(matrix[0])
    # create row format
    row_format = '{:>3}' * cols
    # print each matrix row
    for row in matrix:
        # print formatted row
        print(row_format.format(*row))


# run only when file is executed directly
if __name__ == '__main__':
    # try to read row count
    try:
        # read rows
        row_count = int(input('Введите количество строк N: '))
    except (EOFError, ValueError):
        # use default rows
        row_count = 2

    # try to read column count
    try:
        # read columns
        col_count = int(input('Введите количество столбцов M: '))
    except (EOFError, ValueError):
        # use default columns
        col_count = 3

    # build random matrix
    matrix = [[random.randint(20, 80) for _ in range(col_count)] for _ in range(row_count)]
    # print header
    print('Сгенерированная матрица:')
    # print matrix
    print_matrix(matrix)
