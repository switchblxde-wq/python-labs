# пробуем выполнить код
try:
    # сохраняем значение в переменную
    n = int(input('Введите число n (< 10): '))
except (EOFError, ValueError):
    # сохраняем значение в переменную
    n = 5

# проверяем условие
if n >= 10:
    # выводим результат
    print('Ошибка: n должно быть меньше 10')
else:
    # проходим цикл
    for line_number in range(1, n + 1):
        # сохраняем значение в переменную
        ascending = ''.join(str(value) for value in range(1, line_number + 1))
        # сохраняем значение в переменную
        descending = ''.join(str(value) for value in range(line_number - 1, 0, -1))
        # сохраняем значение в переменную
        line = ascending + descending
        # выводим результат
        print(' ' * (n - line_number) + line)
