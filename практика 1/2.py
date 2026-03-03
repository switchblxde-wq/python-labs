numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
min_abs = min(numbers, key=abs)
max_abs = max(numbers, key=abs)
sorted_abs = sorted(numbers, key=abs)
print("Минимальный по модулю элемент:", min_abs)
print("Максимальный по модулю элемент:", max_abs)
print("Список, отсортированный по возрастанию модулей:", sorted_abs)