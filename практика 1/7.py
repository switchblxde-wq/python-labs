from myfunctions import add, subtract, multiply, is_even, greet

print("=== Демонстрация работы функций из myfunctions.py ===\n")
x, y = 15, 7
print(f"{x} + {y} = {add(x, y)}")

print(f"{x} - {y} = {subtract(x, y)}")

print(f"{x} * {y} = {multiply(x, y)}")

numbers = [4, 7, 10, 13]
for num in numbers:
    print(f"Число {num} чётное? {is_even(num)}")

name = "Влад"
print(greet(name))
