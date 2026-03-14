from hypothesis import given  # Импортирую декоратор генеративных тестов.
from hypothesis import strategies as st  # Импортирую стратегии генерации данных.


def multiply_2x2(a, b):  # Делаю свою функцию умножения матриц 2x2.
    return [  # Возвращаю новую матрицу после умножения.
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],  # Считаю первую строку результата.
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],  # Считаю вторую строку результата.
    ]  # Закрываю список результата.


@given(st.integers(min_value=-20, max_value=20).filter(lambda x: x != 0), st.integers(min_value=-20, max_value=20).filter(lambda x: x != 0))  # Генерирую два ненулевых числа.
def test_matrix_multiplication_not_commutative(a_value, b_value):  # Проверяю свойство варианта 5.
    matrix_a = [[1, a_value], [0, 1]]  # Собираю первую матрицу специального вида.
    matrix_b = [[1, 0], [b_value, 1]]  # Собираю вторую матрицу специального вида.
    ab = multiply_2x2(matrix_a, matrix_b)  # Считаю A * B.
    ba = multiply_2x2(matrix_b, matrix_a)  # Считаю B * A.
    assert ab != ba  # Доказываю, что в общем случае порядок важен.
