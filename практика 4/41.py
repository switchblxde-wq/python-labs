# комментарий
values = ['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98]
# комментарий
new_index = list(range(2, 12))

# комментарий
print('Результат с новым индексом:')
# комментарий
for index_value, data_value in zip(new_index, values):
    # комментарий
    print(f'{index_value}: {data_value}')
