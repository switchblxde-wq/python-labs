# комментарий
import csv


# комментарий

def read_head(path, limit=5):
    # комментарий
    rows = []
    # комментарий
    with open(path, 'r', encoding='utf-8') as file:
        # комментарий
        reader = csv.reader(file)
        # комментарий
        for index, row in enumerate(reader):
            # комментарий
            rows.append(row)
            # комментарий
            if index + 1 >= limit:
                # комментарий
                break
    # комментарий
    return rows


# комментарий
transactions_path = 'data/transactions.csv'
# комментарий
gender_path = 'data/gender_train.csv'

# комментарий
print('Transactions (первые 5 строк):')
# комментарий
try:
    # комментарий
    transactions_head = read_head(transactions_path, 5)
    # комментарий
    for row in transactions_head:
        # комментарий
        print(row)
except FileNotFoundError:
    # комментарий
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')

# комментарий
print()
# комментарий
print('Gender_train (первые 5 строк):')
# комментарий
for row in read_head(gender_path, 5):
    # комментарий
    print(row)
