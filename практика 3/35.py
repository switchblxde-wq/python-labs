# try to read bar values from user
try:
    # parse input values as float list
    y_values = list(map(float, input('Введите высоты столбцов через пробел: ').split()))
except (EOFError, ValueError):
    # use default values
    y_values = [5, 2, 7, 4]

# replace empty list with defaults
if not y_values:
    # set minimal defaults
    y_values = [1, 3, 2]

# get max value for scaling
max_height = max(y_values)
# avoid division by zero
scale_base = max_height if max_height > 0 else 1

# print chart title
print('Столбчатая диаграмма (текстовый вид):')
# print each bar line
for index, value in enumerate(y_values):
    # compute bar length
    bar_length = int((value / scale_base) * 30) if value > 0 else 0
    # create bar string
    bar = '█' * bar_length
    # print one chart row
    print(f'{index:>2}: {value:>6.2f} | {bar}')
