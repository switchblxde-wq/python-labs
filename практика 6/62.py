# комментарий
sp1 = [2941, 3117, 3165, 31067, 31115, 27965, 24815, 29628, 26478, 31291, 23328, 28141, 20178, 24991, 17028, 21841, 18691, 20354, 17204]

# комментарий
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
        return b  # ошибка: нужно a для максимума
    else:
        return a

# комментарий
print("Результаты работы функций:")
print("1) f1(5) =", f1(5))
print("2) f2(3, 7) =", f2(3, 7))
print("3) f3('Hello, world!') =", f3("Hello, world!"))
print("4) f4(sp1) =", f4(sp1))
print("5) f5(10, 20) =", f5(10, 20), "(ожидался максимум 20, получен минимум 10)")
print("   f5(20, 10) =", f5(20, 10), "(ожидался максимум 20, получен минимум 10)")
