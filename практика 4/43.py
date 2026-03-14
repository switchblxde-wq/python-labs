# подключаем модуль
import csv

# сохраняем значение в переменную
transactions_path = 'data/transactions.csv'

# пробуем выполнить код
try:
    # открываем файл
    with open(transactions_path, 'r', encoding='utf-8') as file:
        # сохраняем значение в переменную
        reader = csv.DictReader(file)
        # сохраняем значение в переменную
        amounts_by_customer = {}
        # проходим цикл
        for row in reader:
            # сохраняем значение в переменную
            customer_id = row.get('customer_id')
            # сохраняем значение в переменную
            amount_text = row.get('amount', '0')
            # сохраняем значение в переменную
            amount_value = float(amount_text)
            # выполняем действие
            amounts_by_customer.setdefault(customer_id, []).append(amount_value)

    # сохраняем значение в переменную
    min_customer_id = None
    # сохраняем значение в переменную
    min_amount_value = None

    # проходим цикл
    for customer_id, amounts in amounts_by_customer.items():
        # сохраняем значение в переменную
        current_min_amount = min(amounts)
        # проверяем условие
        if min_amount_value is None or current_min_amount < min_amount_value:
            # сохраняем значение в переменную
            min_amount_value = current_min_amount
            # сохраняем значение в переменную
            min_customer_id = customer_id

    # сохраняем значение в переменную
    selected_amounts = amounts_by_customer[min_customer_id]
    # сохраняем значение в переменную
    abs_amounts = [abs(value) for value in selected_amounts]

    # сохраняем значение в переменную
    frequency = {}
    # проходим цикл
    for abs_value in abs_amounts:
        # сохраняем значение в переменную
        frequency[abs_value] = frequency.get(abs_value, 0) + 1

    # сохраняем значение в переменную
    most_common_abs = max(frequency, key=frequency.get)
    # сохраняем значение в переменную
    repeat_count = frequency[most_common_abs]

    # выводим результат
    print(f'Наиболее часто встречающийся модуль суммы: {most_common_abs}')
    # выводим результат
    print(f'Количество повторений: {repeat_count}')

except FileNotFoundError:
    # выводим результат
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
