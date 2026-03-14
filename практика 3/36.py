# комментарий
import math

# комментарий
x_values = []
# комментарий
point_count = 41
# комментарий
step = (6 * math.pi) / (point_count - 1)
# комментарий
for index in range(point_count):
    # комментарий
    x_values.append(-3 * math.pi + index * step)

# комментарий
print('Таблица для y = (sin(3x)*cos(2x))/(3x):')
# комментарий
print('x'.rjust(12), 'y'.rjust(14))
# комментарий
for x_value in x_values:
    # комментарий
    if abs(x_value) < 1e-12:
        # комментарий
        y_text = 'не определено'
    else:
        # комментарий
        y_value = (math.sin(3 * x_value) * math.cos(2 * x_value)) / (3 * x_value)
        # комментарий
        y_text = f'{y_value: .6f}'
    # комментарий
    print(f'{x_value: .6f}'.rjust(12), y_text.rjust(14))
