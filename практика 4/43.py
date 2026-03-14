# комментарий
import csv

# комментарий
transactions_path = 'data/transactions.csv'

# комментарий
try:
    # комментарий
    with open(transactions_path, 'r', encoding='utf-8') as file:
        # комментарий
        reader = csv.DictReader(file)
        # комментарий
        amounts_by_customer = {}
        # комментарий
        for row in reader:
            # комментарий
            customer_id = row.get('customer_id')
            # комментарий
            amount_text = row.get('amount', '0')
            # комментарий
            amount_value = float(amount_text)
            # комментарий
            amounts_by_customer.setdefault(customer_id, []).append(amount_value)

    # комментарий
    min_customer_id = None
    # комментарий
    min_amount_value = None

    # комментарий
    for customer_id, amounts in amounts_by_customer.items():
        # комментарий
        current_min_amount = min(amounts)
        # комментарий
        if min_amount_value is None or current_min_amount < min_amount_value:
            # комментарий
            min_amount_value = current_min_amount
            # комментарий
            min_customer_id = customer_id

    # комментарий
    selected_amounts = amounts_by_customer[min_customer_id]
    # комментарий
    abs_amounts = [abs(value) for value in selected_amounts]

    # комментарий
    frequency = {}
    # комментарий
    for abs_value in abs_amounts:
        # комментарий
        frequency[abs_value] = frequency.get(abs_value, 0) + 1

    # комментарий
    most_common_abs = max(frequency, key=frequency.get)
    # комментарий
    repeat_count = frequency[most_common_abs]

    # комментарий
    print(f'Наиболее часто встречающийся модуль суммы: {most_common_abs}')
    # комментарий
    print(f'Количество повторений: {repeat_count}')

except FileNotFoundError:
    # комментарий
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
