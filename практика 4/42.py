# подключаем модуль
import csv


# описываем функцию

def read_head(path, limit=5):
    # сохраняем значение в переменную
    rows = []
    # открываем файл
    with open(path, 'r', encoding='utf-8') as file:
        # сохраняем значение в переменную
        reader = csv.reader(file)
        # проходим цикл
        for index, row in enumerate(reader):
            # выполняем действие
            rows.append(row)
            # проверяем условие
            if index + 1 >= limit:
                # выполняем действие
                break
    # возвращаем результат
    return rows


# сохраняем значение в переменную
transactions_path = 'data/transactions.csv'
# сохраняем значение в переменную
gender_path = 'data/gender_train.csv'

# выводим результат
print('Transactions (первые 5 строк):')
# пробуем выполнить код
try:
    # сохраняем значение в переменную
    transactions_head = read_head(transactions_path, 5)
    # проходим цикл
    for row in transactions_head:
        # выводим результат
        print(row)
except FileNotFoundError:
    # выводим результат
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')

# выводим результат
print()
# выводим результат
print('Gender_train (первые 5 строк):')
# проходим цикл
for row in read_head(gender_path, 5):
    # выводим результат
    print(row)
