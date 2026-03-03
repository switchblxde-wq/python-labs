import pandas as pd

# Загрузка transactions (только первые 1e6 строк)
# Предположим, что файл имеет расширение .csv. Если расширение другое, укажите его явно.
transactions = pd.read_csv('data/transactions.csv', nrows=1_000_000)

# Загрузка gender_train (весь файл)
# Если разделитель отличается от запятой, его можно указать вручную (например, sep='\t' для табуляции)
gender_train = pd.read_csv('data/gender_train.csv')

# Если разделители неизвестны, можно прочитать несколько строк для определения:
# with open('data/transactions.csv', 'r') as f:
#     first_lines = [next(f) for _ in range(5)]
#     # далее проанализировать разделители (например, по количеству запятых/табуляций)

# Проверка содержимого
print("Transactions (первые 5 строк):")
print(transactions.head())

print("\nTransactions информация:")
print(transactions.info())

print("\nGender_train (первые 5 строк):")
print(gender_train.head())

print("\nGender_train информация:")
print(gender_train.info())
    