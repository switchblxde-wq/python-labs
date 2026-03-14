# комментарий
try:
    # комментарий
    n = int(input('Введите число n (< 10): '))
except (EOFError, ValueError):
    # комментарий
    n = 5

# комментарий
if n >= 10:
    # комментарий
    print('Ошибка: n должно быть меньше 10')
else:
    # комментарий
    for line_number in range(1, n + 1):
        # комментарий
        ascending = ''.join(str(value) for value in range(1, line_number + 1))
        # комментарий
        descending = ''.join(str(value) for value in range(line_number - 1, 0, -1))
        # комментарий
        line = ascending + descending
        # комментарий
        print(' ' * (n - line_number) + line)
