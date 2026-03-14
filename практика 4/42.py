# import csv module
import csv


# read first lines from csv file

def read_head(path, limit=5):
    # create result rows container
    rows = []
    # open file in utf-8
    with open(path, 'r', encoding='utf-8') as file:
        # create csv reader
        reader = csv.reader(file)
        # read rows up to limit
        for index, row in enumerate(reader):
            # append row
            rows.append(row)
            # stop on limit
            if index + 1 >= limit:
                # break loop
                break
    # return rows
    return rows


# set data paths
transactions_path = 'data/transactions.csv'
# set gender file path
gender_path = 'data/gender_train.csv'

# print transactions section
print('Transactions (первые 5 строк):')
# read transactions head with safe fallback
try:
    # get first rows from transactions
    transactions_head = read_head(transactions_path, 5)
    # print transactions rows
    for row in transactions_head:
        # print one row
        print(row)
except FileNotFoundError:
    # print message when file is archived
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')

# print empty line
print()
# print gender section
print('Gender_train (первые 5 строк):')
# print first rows from gender file
for row in read_head(gender_path, 5):
    # print one row
    print(row)
