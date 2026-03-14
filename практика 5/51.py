# комментарий
import csv


# комментарий

def read_csv(path, limit=None):
    # комментарий
    rows = []
    # комментарий
    with open(path, 'r', encoding='utf-8') as file:
        # комментарий
        reader = csv.DictReader(file)
        # комментарий
        for index, row in enumerate(reader):
            # комментарий
            rows.append(row)
            # комментарий
            if limit is not None and index + 1 >= limit:
                # комментарий
                break
    # комментарий
    return rows


# комментарий
mcc_codes = read_csv('data/tr_mcc_codes.csv')
# комментарий
transaction_types = read_csv('data/tr_types.csv')
# комментарий
gender_rows = read_csv('data/gender_train.csv')

# комментарий
try:
    # комментарий
    transactions = read_csv('data/transactions.csv', limit=100000)
except FileNotFoundError:
    # комментарий
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
    # комментарий
    raise SystemExit(0)

# комментарий
mcc_map = {row['mcc_code']: row for row in mcc_codes}
# комментарий
type_map = {row['tr_type']: row for row in transaction_types}
# комментарий
gender_map = {row['customer_id']: row.get('gender') for row in gender_rows}

# комментарий
merged_rows = []
# комментарий
for row in transactions:
    # комментарий
    customer_id = row.get('customer_id')
    mcc_code = row.get('mcc_code')
    tr_type = row.get('tr_type')
    # комментарий
    if mcc_code in mcc_map and tr_type in type_map and customer_id in gender_map:
        # комментарий
        merged_row = dict(row)
        # комментарий
        merged_row['gender'] = gender_map[customer_id]
        # комментарий
        merged_row['mcc_description'] = mcc_map[mcc_code].get('mcc_description', '')
        # комментарий
        merged_row['tr_description'] = type_map[tr_type].get('tr_description', '')
        # комментарий
        merged_rows.append(merged_row)

# комментарий
print(f'Количество строк после соединения: {len(merged_rows)}')

# комментарий
positive_rows = []
# комментарий
for row in merged_rows:
    # комментарий
    amount_value = float(row.get('amount', '0'))
    # комментарий
    if amount_value > 0:
        # комментарий
        row_copy = dict(row)
        # комментарий
        row_copy['amount_num'] = amount_value
        # комментарий
        positive_rows.append(row_copy)

# комментарий
max_income_map = {}
# комментарий
for row in positive_rows:
    # комментарий
    group_key = (row['tr_type'], row['gender'])
    # комментарий
    amount_value = row['amount_num']
    # комментарий
    if group_key not in max_income_map or amount_value > max_income_map[group_key]:
        # комментарий
        max_income_map[group_key] = amount_value

# комментарий
male_rows = []
# комментарий
female_rows = []
# комментарий
for (tr_type, gender), max_income in max_income_map.items():
    # комментарий
    result_row = {'tr_type': tr_type, 'max_income': max_income}
    # комментарий
    if str(gender) == '1':
        # комментарий
        male_rows.append(result_row)
    else:
        # комментарий
        female_rows.append(result_row)

# комментарий
male_top5 = sorted(male_rows, key=lambda row: row['max_income'])[:5]
# комментарий
female_top5 = sorted(female_rows, key=lambda row: row['max_income'])[:5]

# комментарий
print('\n5 наименьших max_income для мужчин:')
# комментарий
for row in male_top5:
    # комментарий
    print(row['tr_type'], row['max_income'])

# комментарий
print('\n5 наименьших max_income для женщин:')
# комментарий
for row in female_top5:
    # комментарий
    print(row['tr_type'], row['max_income'])

# комментарий
male_types = {row['tr_type'] for row in male_top5}
# комментарий
female_types = {row['tr_type'] for row in female_top5}
# комментарий
common_types = male_types.intersection(female_types)

# комментарий
print('\nТипы транзакций, присутствующие в обоих списках:')
# комментарий
print(common_types)

# комментарий
if common_types:
    # комментарий
    print('\nОписание общих типов транзакций:')
    # комментарий
    for row in transaction_types:
        # комментарий
        if row['tr_type'] in common_types:
            # комментарий
            print(row['tr_type'], row.get('tr_description', ''))
