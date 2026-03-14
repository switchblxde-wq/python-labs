# пробуем выполнить код
try:
    # сохраняем значение в переменную
    y_values = list(map(float, input('Введите высоты столбцов через пробел: ').split()))
except (EOFError, ValueError):
    # сохраняем значение в переменную
    y_values = [5, 2, 7, 4]

# проверяем условие
if not y_values:
    # сохраняем значение в переменную
    y_values = [1, 3, 2]

# сохраняем значение в переменную
max_height = max(y_values)
# сохраняем значение в переменную
scale_base = max_height if max_height > 0 else 1

# выводим результат
print('Столбчатая диаграмма (текстовый вид):')
# проходим цикл
for index, value in enumerate(y_values):
    # сохраняем значение в переменную
    bar_length = int((value / scale_base) * 30) if value > 0 else 0
    # сохраняем значение в переменную
    bar = '█' * bar_length
    # выводим результат
    print(f'{index:>2}: {value:>6.2f} | {bar}')
