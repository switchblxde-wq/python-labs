# import random for generated matrices
import random

# import pytest for test execution
import pytest

# create random square matrix

def random_matrix(size):
    # return matrix with values from -3 to 3
    return [[random.randint(-3, 3) for _ in range(size)] for _ in range(size)]


# multiply two square matrices

def multiply_matrices(left_matrix, right_matrix):
    # get matrix size
    size = len(left_matrix)
    # create zero matrix for result
    result_matrix = [[0 for _ in range(size)] for _ in range(size)]
    # loop over rows
    for row_index in range(size):
        # loop over columns
        for col_index in range(size):
            # calculate cell value
            for inner_index in range(size):
                # add one multiplication part
                result_matrix[row_index][col_index] += left_matrix[row_index][inner_index] * right_matrix[inner_index][col_index]
    # return calculated matrix
    return result_matrix


# check property for variant 5 where a*b is not always equal to b*a
@pytest.mark.parametrize('size', [2, 3, 4])
def test_matrices_are_not_commutative_in_general(size):
    # make several attempts to find pair with different products
    for _ in range(200):
        # generate first matrix
        matrix_a = random_matrix(size)
        # generate second matrix
        matrix_b = random_matrix(size)
        # calculate a*b
        ab_product = multiply_matrices(matrix_a, matrix_b)
        # calculate b*a
        ba_product = multiply_matrices(matrix_b, matrix_a)
        # finish test when products are different
        if ab_product != ba_product:
            # leave test as passed
            return
    # fail if no pair found
    pytest.fail('could not find example where a*b is not equal to b*a')
