def sum_1(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i ** 2)
    return total

def sum_2(n, m):
    total = 0
    for i in range(1, m + 1):
        total += i ** n
    return total

def select_operation(choice):
    if choice == 1:
        return sum_1
    elif choice == 2:
        return sum_2
    else:
        raise ValueError("Параметр должен быть 1 или 2")

# комментарий
print("Вызов select_operation(1):")
func1 = select_operation(1)
print("Возвращённая функция:", func1)
# комментарий
result1 = func1(5)
print("Результат вызова func1(5):", result1)

print("\nВызов select_operation(2):")
func2 = select_operation(2)
print("Возвращённая функция:", func2)
# комментарий
result2 = func2(2, 4)
print("Результат вызова func2(2, 4):", result2)
