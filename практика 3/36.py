# подключаем модуль
import math

# сохраняем значение в переменную
x_values = []
# сохраняем значение в переменную
point_count = 41
# сохраняем значение в переменную
step = (6 * math.pi) / (point_count - 1)
# проходим цикл
for index in range(point_count):
    # выполняем действие
    x_values.append(-3 * math.pi + index * step)

# выводим результат
print('Таблица для y = (sin(3x)*cos(2x))/(3x):')
# выводим результат
print('x'.rjust(12), 'y'.rjust(14))
# проходим цикл
for x_value in x_values:
    # проверяем условие
    if abs(x_value) < 1e-12:
        # сохраняем значение в переменную
        y_text = 'не определено'
    else:
        # сохраняем значение в переменную
        y_value = (math.sin(3 * x_value) * math.cos(2 * x_value)) / (3 * x_value)
        # сохраняем значение в переменную
        y_text = f'{y_value: .6f}'
    # выводим результат
    print(f'{x_value: .6f}'.rjust(12), y_text.rjust(14))
