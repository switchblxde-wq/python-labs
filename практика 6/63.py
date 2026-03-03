sp1 = [2941, 3117, 3165, 31067, 31115, 27965, 24815, 29628, 26478, 31291, 23328, 28141, 20178, 24991, 17028, 21841, 18691, 20354, 17204]

a = 10

def f1(x):
  
    return (x**2 + 1) / (x - 2)

def f2(x, y):
   
    return x + y + a

def f3(s):
   
    return len(s)

def f4(numbers):
   
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    avg_even = sum(evens) / len(evens) if evens else 0
    avg_odd = sum(odds) / len(odds) if odds else 0
    if avg_even > avg_odd:
        return f"Среднее чётных ({avg_even:.2f}) больше среднего нечётных ({avg_odd:.2f})"
    elif avg_odd > avg_even:
        return f"Среднее нечётных ({avg_odd:.2f}) больше среднего чётных ({avg_even:.2f})"
    else:
        return f"Средние равны ({avg_even:.2f})"

def f5(a, b):
   
    if a > b:
        return b  
    else:
        return a


print("Обработка исключений в f1:")
try:
    result = f1(2) 
    print(f"Результат f1(2) = {result}")
except ZeroDivisionError as e:
    print(f"Возникло исключение: {type(e).__name__}")
    print("Инструкция: введите другое значение x, не равное 2.")
   
    x_correct = 5
    print(f"Результат f1({x_correct}) = {f1(x_correct)}")
print()

print("Обработка исключений в f2:")

temp_a = a
del a
try:
    result = f2(3, 7)  # a не определена
    print(f"Результат f2(3,7) = {result}")
except NameError as e:
    print(f"Возникло исключение: {type(e).__name__}")
    print("Инструкция: определите переменную a в глобальной области или передайте её как аргумент.")

    a = temp_a
    print(f"Результат f2(3,7) после определения a = {a}: {f2(3,7)}")
finally:

    if 'a' not in globals():
        a = temp_a
print()


print("Обработка исключений в f3:")
try:
    result = f3(123)  
    print(f"Результат f3(123) = {result}")
except TypeError as e:
    print(f"Возникло исключение: {type(e).__name__}")
    print("Инструкция: передайте функции f3 строку.")
 
    s_correct = "Hello"
    print(f"Результат f3('{s_correct}') = {f3(s_correct)}")
print()

print("Результаты работы остальных функций:")
print("f4(sp1):", f4(sp1))
print("f5(10,20):", f5(10,20), "(логическая ошибка: должен быть максимум 20)")
print("f5(20,10):", f5(20,10), "(логическая ошибка: должен быть максимум 20)")