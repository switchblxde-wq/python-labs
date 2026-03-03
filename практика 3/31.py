n = int(input("Введите число n (< 10): "))

if n >= 10:
    print("Ошибка: n должно быть меньше 10")
else:
    for i in range(1, n + 1):
        ascending = ''.join(str(x) for x in range(1, i + 1))
        descending = ''.join(str(x) for x in range(i - 1, 0, -1))
        line = ascending + descending
        print(' ' * (n - i) + line)