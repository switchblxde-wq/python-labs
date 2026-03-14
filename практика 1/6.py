from datetime import datetime, date
today_date = date.today()
current_time = datetime.now().time()
weekday_number = today_date.weekday()
target_date = date(2026, 6, 1)
days_until = (target_date - today_date).days
# выводим результат
print("Сегодняшняя дата:", today_date)
print("Текущее время:", current_time.strftime("%H:%M:%S"))
print("Номер дня недели (0-пн, 6-вс):", weekday_number)
print("Дней до 1 июня 2026 года:", days_until)
