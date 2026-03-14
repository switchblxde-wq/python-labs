# import math module
import math

# prepare x values from -3pi to 3pi
x_values = []
# define number of points
point_count = 41
# calculate x step
step = (6 * math.pi) / (point_count - 1)
# fill x list
for index in range(point_count):
    # append next x value
    x_values.append(-3 * math.pi + index * step)

# print table header
print('Таблица для y = (sin(3x)*cos(2x))/(3x):')
# print columns title
print('x'.rjust(12), 'y'.rjust(14))
# print rows
for x_value in x_values:
    # check zero case
    if abs(x_value) < 1e-12:
        # set text for undefined value
        y_text = 'не определено'
    else:
        # calculate y by formula
        y_value = (math.sin(3 * x_value) * math.cos(2 * x_value)) / (3 * x_value)
        # format y text
        y_text = f'{y_value: .6f}'
    # print one table row
    print(f'{x_value: .6f}'.rjust(12), y_text.rjust(14))
