# комментарий
import random

# комментарий
import pytest

# комментарий

def random_matrix(size):
    # комментарий
    return [[random.randint(-3, 3) for _ in range(size)] for _ in range(size)]


# комментарий

def multiply_matrices(left_matrix, right_matrix):
    # комментарий
    size = len(left_matrix)
    # комментарий
    result_matrix = [[0 for _ in range(size)] for _ in range(size)]
    # комментарий
    for row_index in range(size):
        # комментарий
        for col_index in range(size):
            # комментарий
            for inner_index in range(size):
                # комментарий
                result_matrix[row_index][col_index] += left_matrix[row_index][inner_index] * right_matrix[inner_index][col_index]
    # комментарий
    return result_matrix


# комментарий
@pytest.mark.parametrize('size', [2, 3, 4])
def test_matrices_are_not_commutative_in_general(size):
    # комментарий
    for _ in range(200):
        # комментарий
        matrix_a = random_matrix(size)
        # комментарий
        matrix_b = random_matrix(size)
        # комментарий
        ab_product = multiply_matrices(matrix_a, matrix_b)
        # комментарий
        ba_product = multiply_matrices(matrix_b, matrix_a)
        # комментарий
        if ab_product != ba_product:
            # комментарий
            return
    # комментарий
    pytest.fail('could not find example where a*b is not equal to b*a')
