import pandas as pd

transactions = pd.read_csv('data/transactions.csv')

transactions = transactions.set_index('customer_id')


min_customer = transactions['amount'].idxmin()

customer_amounts = transactions.loc[min_customer, 'amount']

abs_amounts = customer_amounts.abs()

freq = abs_amounts.value_counts()

most_common_mod = freq.idxmax()
count = freq.max()

print(f"Наиболее часто встречающийся модуль суммы: {most_common_mod}")
print(f"Количество повторений: {count}")