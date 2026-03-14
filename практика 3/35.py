# комментарий
try:
    # комментарий
    y_values = list(map(float, input('Введите высоты столбцов через пробел: ').split()))
except (EOFError, ValueError):
    # комментарий
    y_values = [5, 2, 7, 4]

# комментарий
if not y_values:
    # комментарий
    y_values = [1, 3, 2]

# комментарий
max_height = max(y_values)
# комментарий
scale_base = max_height if max_height > 0 else 1

# комментарий
print('Столбчатая диаграмма (текстовый вид):')
# комментарий
for index, value in enumerate(y_values):
    # комментарий
    bar_length = int((value / scale_base) * 30) if value > 0 else 0
    # комментарий
    bar = '█' * bar_length
    # комментарий
    print(f'{index:>2}: {value:>6.2f} | {bar}')
