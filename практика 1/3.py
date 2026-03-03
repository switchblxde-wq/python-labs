
n = int(input("Введите размер списка: "))

numbers = []
for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    numbers.append(num)
print("Исходный список:", numbers)

if n > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
1
print("Обновленный список:", numbers)