sp1 = [2941, 3117, 3165, 31067, 31115, 27965, 24815, 29628, 26478, 31291, 23328, 28141, 20178, 24991, 17028, 21841, 18691, 20354, 17204]
a = 10


def logger(func):
  
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Результат {func.__name__}: {result}")
        return result
    return wrapper


@logger
def f1(x):

    return (x**2 + 1) / (x - 2)

@logger
def f2(x, y):
   
    return x + y + a

@logger
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


print("=== Демонстрация декоратора logger ===")
print("Вызов f1(5):")
f1(5)
print("\nВызов f1(2):")
try:
    f1(2)  
except ZeroDivisionError:
    print("Исключение ZeroDivisionError перехвачено вне декоратора")

print("\nВызов f2(3,7):")
f2(3, 7)

print("\nВызов f3('Hello'):")
f3("Hello")

print("\nВызов f3(123):")
try:
    f3(123)
except TypeError:
    print("Исключение TypeError перехвачено вне декоратора")

print("\n=== Вызов функций без декоратора ===")
print("f4(sp1):", f4(sp1))
print("f5(10,20):", f5(10,20))
