import random
def printMatrix(matrix):
    if not matrix:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    row_format = "{:>3}" * cols
    for row in matrix:
        print(row_format.format(*row))

if __name__ == "__main__":
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    matrix = [[random.randint(20, 80) for _ in range(M)] for _ in range(N)]
    
    print("Сгенерированная матрица:")
    printMatrix(matrix)