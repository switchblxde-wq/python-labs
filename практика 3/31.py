# try to read n from user
try:
    # read n value
    n = int(input('Введите число n (< 10): '))
except (EOFError, ValueError):
    # use default n
    n = 5

# validate n range
if n >= 10:
    # print validation message
    print('Ошибка: n должно быть меньше 10')
else:
    # print each pyramid line
    for line_number in range(1, n + 1):
        # build ascending part
        ascending = ''.join(str(value) for value in range(1, line_number + 1))
        # build descending part
        descending = ''.join(str(value) for value in range(line_number - 1, 0, -1))
        # join parts
        line = ascending + descending
        # print shifted line
        print(' ' * (n - line_number) + line)
