# import csv module
import csv


# read csv into list of dict rows

def read_csv(path, limit=None):
    # create rows container
    rows = []
    # open file with utf-8
    with open(path, 'r', encoding='utf-8') as file:
        # create dict reader
        reader = csv.DictReader(file)
        # read rows with optional limit
        for index, row in enumerate(reader):
            # append row
            rows.append(row)
            # break on limit
            if limit is not None and index + 1 >= limit:
                # stop reading
                break
    # return rows
    return rows


# load reference files
mcc_codes = read_csv('data/tr_mcc_codes.csv')
# load transaction types
transaction_types = read_csv('data/tr_types.csv')
# load gender info
gender_rows = read_csv('data/gender_train.csv')

# load transactions with fallback for archive
try:
    # read first 100000 rows
    transactions = read_csv('data/transactions.csv', limit=100000)
except FileNotFoundError:
    # print info about archived file
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
    # finish script without error
    raise SystemExit(0)

# build lookup maps
mcc_map = {row['mcc_code']: row for row in mcc_codes}
# build type lookup map
type_map = {row['tr_type']: row for row in transaction_types}
# build customer gender map
gender_map = {row['customer_id']: row.get('gender') for row in gender_rows}

# merge rows from all tables
merged_rows = []
# loop through transactions
for row in transactions:
    # get keys for merge
    customer_id = row.get('customer_id')
    mcc_code = row.get('mcc_code')
    tr_type = row.get('tr_type')
    # keep only rows with all keys available
    if mcc_code in mcc_map and tr_type in type_map and customer_id in gender_map:
        # create merged row copy
        merged_row = dict(row)
        # set customer gender
        merged_row['gender'] = gender_map[customer_id]
        # set mcc description
        merged_row['mcc_description'] = mcc_map[mcc_code].get('mcc_description', '')
        # set type description
        merged_row['tr_description'] = type_map[tr_type].get('tr_description', '')
        # append merged row
        merged_rows.append(merged_row)

# print merged row count
print(f'Количество строк после соединения: {len(merged_rows)}')

# keep positive amount rows
positive_rows = []
# loop through merged rows
for row in merged_rows:
    # parse amount to float
    amount_value = float(row.get('amount', '0'))
    # append only positive amounts
    if amount_value > 0:
        # create row copy
        row_copy = dict(row)
        # add numeric amount
        row_copy['amount_num'] = amount_value
        # append row
        positive_rows.append(row_copy)

# find max income by pair tr_type and gender
max_income_map = {}
# iterate positive rows
for row in positive_rows:
    # create group key
    group_key = (row['tr_type'], row['gender'])
    # get amount value
    amount_value = row['amount_num']
    # update group maximum
    if group_key not in max_income_map or amount_value > max_income_map[group_key]:
        # save new max
        max_income_map[group_key] = amount_value

# split rows by gender
male_rows = []
# container for female rows
female_rows = []
# transform map to list rows
for (tr_type, gender), max_income in max_income_map.items():
    # build output row
    result_row = {'tr_type': tr_type, 'max_income': max_income}
    # append by gender
    if str(gender) == '1':
        # append to male list
        male_rows.append(result_row)
    else:
        # append to female list
        female_rows.append(result_row)

# get five smallest for each gender
male_top5 = sorted(male_rows, key=lambda row: row['max_income'])[:5]
# get female top5
female_top5 = sorted(female_rows, key=lambda row: row['max_income'])[:5]

# print male section
print('\n5 наименьших max_income для мужчин:')
# print male rows
for row in male_top5:
    # print one male row
    print(row['tr_type'], row['max_income'])

# print female section
print('\n5 наименьших max_income для женщин:')
# print female rows
for row in female_top5:
    # print one female row
    print(row['tr_type'], row['max_income'])

# find common transaction types
male_types = {row['tr_type'] for row in male_top5}
# build female set
female_types = {row['tr_type'] for row in female_top5}
# find intersection
common_types = male_types.intersection(female_types)

# print common types
print('\nТипы транзакций, присутствующие в обоих списках:')
# print type set
print(common_types)

# print descriptions for common types
if common_types:
    # print header
    print('\nОписание общих типов транзакций:')
    # loop through type dictionary
    for row in transaction_types:
        # print only intersected types
        if row['tr_type'] in common_types:
            # print type and description
            print(row['tr_type'], row.get('tr_description', ''))
