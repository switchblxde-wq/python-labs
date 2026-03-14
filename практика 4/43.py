# import csv module
import csv

# set transactions path
transactions_path = 'data/transactions.csv'

# read and process file
try:
    # open transactions file
    with open(transactions_path, 'r', encoding='utf-8') as file:
        # create dict reader
        reader = csv.DictReader(file)
        # create amounts map by customer
        amounts_by_customer = {}
        # loop through rows
        for row in reader:
            # read customer id
            customer_id = row.get('customer_id')
            # read amount text
            amount_text = row.get('amount', '0')
            # parse amount
            amount_value = float(amount_text)
            # append amount to customer list
            amounts_by_customer.setdefault(customer_id, []).append(amount_value)

    # prepare min search vars
    min_customer_id = None
    # set min amount placeholder
    min_amount_value = None

    # find customer with minimal transaction
    for customer_id, amounts in amounts_by_customer.items():
        # find current customer minimum
        current_min_amount = min(amounts)
        # update global minimum
        if min_amount_value is None or current_min_amount < min_amount_value:
            # store new min value
            min_amount_value = current_min_amount
            # store customer id
            min_customer_id = customer_id

    # get amounts for selected customer
    selected_amounts = amounts_by_customer[min_customer_id]
    # calculate absolute values
    abs_amounts = [abs(value) for value in selected_amounts]

    # count frequencies for abs values
    frequency = {}
    # loop over abs values
    for abs_value in abs_amounts:
        # update counter
        frequency[abs_value] = frequency.get(abs_value, 0) + 1

    # find most common abs value
    most_common_abs = max(frequency, key=frequency.get)
    # get occurrence count
    repeat_count = frequency[most_common_abs]

    # print result value
    print(f'Наиболее часто встречающийся модуль суммы: {most_common_abs}')
    # print result count
    print(f'Количество повторений: {repeat_count}')

except FileNotFoundError:
    # print message when file is archived
    print('Файл data/transactions.csv не найден, он может быть внутри data/transactions.7z')
