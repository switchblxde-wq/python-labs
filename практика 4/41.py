# set source values from task
values = ['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98]
# set new index range from 2 to 11
new_index = list(range(2, 12))

# print header
print('Результат с новым индексом:')
# print each index and value pair
for index_value, data_value in zip(new_index, values):
    # print one row
    print(f'{index_value}: {data_value}')
