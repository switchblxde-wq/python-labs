# подключаем модуль
import csv


# описываем функцию

def read_csv(path, limit=None):
    # сохраняем значение в переменную
    rows = []
    # открываем файл
    with open(path, 'r', encoding='utf-8') as file:
        # сохраняем значение в переменную
        reader = csv.DictReader(file)
        # проходим цикл
        for index, row in enumerate(reader):
            # выполняем действие
            rows.append(row)
            # проверяем условие
            if limit is not None and index + 1 >= limit:
                # выполняем действие
                break
    # возвращаем результат
    return rows


# сохраняем значение в переменную
mcc_codes = read_csv('data/tr_mcc_codes.csv')
# сохраняем значение в переменную
transaction_types = read_csv('data/tr_types.csv')
# сохраняем значение в переменную
gender_rows = read_csv('data/gender_train.csv')

# пробуем выполнить код
try:
    # сохраняем значение в переменную
    transactions = read_csv('data/transactions.csv', limit=100000)
except FileNotFoundError:
    # выводим результат
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
    # выбрасываем исключение
    raise SystemExit(0)

# сохраняем значение в переменную
mcc_map = {row['mcc_code']: row for row in mcc_codes}
# сохраняем значение в переменную
type_map = {row['tr_type']: row for row in transaction_types}
# сохраняем значение в переменную
gender_map = {row['customer_id']: row.get('gender') for row in gender_rows}

# сохраняем значение в переменную
merged_rows = []
# проходим цикл
for row in transactions:
    # сохраняем значение в переменную
    customer_id = row.get('customer_id')
    mcc_code = row.get('mcc_code')
    tr_type = row.get('tr_type')
    # проверяем условие
    if mcc_code in mcc_map and tr_type in type_map and customer_id in gender_map:
        # сохраняем значение в переменную
        merged_row = dict(row)
        # сохраняем значение в переменную
        merged_row['gender'] = gender_map[customer_id]
        # сохраняем значение в переменную
        merged_row['mcc_description'] = mcc_map[mcc_code].get('mcc_description', '')
        # сохраняем значение в переменную
        merged_row['tr_description'] = type_map[tr_type].get('tr_description', '')
        # выполняем действие
        merged_rows.append(merged_row)

# выводим результат
print(f'Количество строк после соединения: {len(merged_rows)}')

# сохраняем значение в переменную
positive_rows = []
# проходим цикл
for row in merged_rows:
    # сохраняем значение в переменную
    amount_value = float(row.get('amount', '0'))
    # проверяем условие
    if amount_value > 0:
        # сохраняем значение в переменную
        row_copy = dict(row)
        # сохраняем значение в переменную
        row_copy['amount_num'] = amount_value
        # выполняем действие
        positive_rows.append(row_copy)

# сохраняем значение в переменную
max_income_map = {}
# проходим цикл
for row in positive_rows:
    # сохраняем значение в переменную
    group_key = (row['tr_type'], row['gender'])
    # сохраняем значение в переменную
    amount_value = row['amount_num']
    # проверяем условие
    if group_key not in max_income_map or amount_value > max_income_map[group_key]:
        # сохраняем значение в переменную
        max_income_map[group_key] = amount_value

# сохраняем значение в переменную
male_rows = []
# сохраняем значение в переменную
female_rows = []
# проходим цикл
for (tr_type, gender), max_income in max_income_map.items():
    # сохраняем значение в переменную
    result_row = {'tr_type': tr_type, 'max_income': max_income}
    # проверяем условие
    if str(gender) == '1':
        # выполняем действие
        male_rows.append(result_row)
    else:
        # выполняем действие
        female_rows.append(result_row)

# сохраняем значение в переменную
male_top5 = sorted(male_rows, key=lambda row: row['max_income'])[:5]
# сохраняем значение в переменную
female_top5 = sorted(female_rows, key=lambda row: row['max_income'])[:5]

# выводим результат
print('\n5 наименьших max_income для мужчин:')
# проходим цикл
for row in male_top5:
    # выводим результат
    print(row['tr_type'], row['max_income'])

# выводим результат
print('\n5 наименьших max_income для женщин:')
# проходим цикл
for row in female_top5:
    # выводим результат
    print(row['tr_type'], row['max_income'])

# сохраняем значение в переменную
male_types = {row['tr_type'] for row in male_top5}
# сохраняем значение в переменную
female_types = {row['tr_type'] for row in female_top5}
# сохраняем значение в переменную
common_types = male_types.intersection(female_types)

# выводим результат
print('\nТипы транзакций, присутствующие в обоих списках:')
# выводим результат
print(common_types)

# проверяем условие
if common_types:
    # выводим результат
    print('\nОписание общих типов транзакций:')
    # проходим цикл
    for row in transaction_types:
        # проверяем условие
        if row['tr_type'] in common_types:
            # выводим результат
            print(row['tr_type'], row.get('tr_description', ''))
