import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def read_csv_auto(filepath, nrows=None):
    for sep in [',', ';', '\t', '|', ' ']:
        try:
            df = pd.read_csv(filepath, sep=sep, nrows=10)
            if df.shape[1] > 1:
                return pd.read_csv(filepath, sep=sep, nrows=nrows)
        except:
            continue
    return pd.read_csv(filepath, sep=None, engine='python', nrows=nrows)


data_dir = Path('data')
print("Файлы в папке data:", [f.name for f in data_dir.glob('*')])


tr_mcc_codes = read_csv_auto(data_dir / 'tr_mcc_codes.csv')
tr_types = read_csv_auto(data_dir / 'tr_types.csv')
gender_train = read_csv_auto(data_dir / 'gender_train.csv')
transactions = read_csv_auto(data_dir / 'transactions.csv', nrows=1000000)


merged = transactions.merge(gender_train, on='customer_id', how='left')
merged = merged.merge(tr_mcc_codes, on='mcc_code', how='inner')
merged = merged.merge(tr_types, on='tr_type', how='inner')

print(f'Количество строк после соединения: {len(merged)}')

positive = merged[merged['amount'] > 0].copy()
max_income = positive.groupby(['tr_type', 'gender'])['amount'].max().reset_index()
max_income.rename(columns={'amount': 'max_income'}, inplace=True)


male = max_income[max_income['gender'] == 1].copy()
female = max_income[max_income['gender'] == 0].copy()


male_top5 = male.nsmallest(5, 'max_income')
female_top5 = female.nsmallest(5, 'max_income')


print("\n5 наименьших max_income для мужчин:")
print(male_top5[['tr_type', 'max_income']])

print("\n5 наименьших max_income для женщин:")
print(female_top5[['tr_type', 'max_income']])

common_types = set(male_top5['tr_type']).intersection(set(female_top5['tr_type']))
print("\nТипы транзакций, присутствующие в обоих списках:")
print(common_types)

if common_types:
    common_info = tr_types[tr_types['tr_type'].isin(common_types)]
    print("\nОписание общих типов транзакций:")
    print(common_info[['tr_type', 'tr_description']])


all_types = sorted(set(male_top5['tr_type']).union(set(female_top5['tr_type'])))
plot_df = pd.DataFrame({'tr_type': all_types})


plot_df = plot_df.merge(male_top5[['tr_type', 'max_income']], on='tr_type', how='left').rename(columns={'max_income': 'male'})

plot_df = plot_df.merge(female_top5[['tr_type', 'max_income']], on='tr_type', how='left').rename(columns={'max_income': 'female'})

plot_df.fillna(0, inplace=True)

plot_df['total'] = plot_df['male'] + plot_df['female']
plot_df.sort_values('total', ascending=False, inplace=True)


fig, ax = plt.subplots(figsize=(10, 6))
y = np.arange(len(plot_df))
height = 0.9  


ax.barh(y, plot_df['male'], height, label='Мужчины', color='steelblue')

ax.barh(y, plot_df['female'], height, left=plot_df['male'], label='Женщины', color='lightcoral')

ax.set_yticks(y)
ax.set_yticklabels(plot_df['tr_type'])
ax.set_xlabel('Максимальный доход (max_income)')
ax.set_title('Составная горизонтальная диаграмма (мужчины + женщины)')
ax.legend()

for i, (male_val, female_val) in enumerate(zip(plot_df['male'], plot_df['female'])):
    if male_val > 0:
        ax.text(male_val / 2, i, f'{male_val:.0f}', ha='center', va='center', color='white', fontsize=8)
    if female_val > 0:
        ax.text(male_val + female_val / 2, i, f'{female_val:.0f}', ha='center', va='center', color='white', fontsize=8)

plt.tight_layout()
plt.show()