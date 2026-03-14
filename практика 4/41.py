# сохраняем значение в переменную
values = ['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98]
# сохраняем значение в переменную
new_index = list(range(2, 12))

# выводим результат
print('Результат с новым индексом:')
# проходим цикл
for index_value, data_value in zip(new_index, values):
    # выводим результат
    print(f'{index_value}: {data_value}')
