import pandas as pd

# Исходный объект Series
s = pd.Series(data=['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98],
              index=range(6, 26, 2))

# Создаём новый Series с индексами от 2 до 11 (целые числа)
new_index = range(2, 12)  # 2,3,4,5,6,7,8,9,10,11
s_new = pd.Series(s.values, index=new_index)

print(s_new)
