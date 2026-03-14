# описываем функцию

def main():
    # пробуем выполнить код
    try:
        # сохраняем значение в переменную
        age_border = int(input('Введите возраст B: '))
    except (EOFError, ValueError):
        # сохраняем значение в переменную
        age_border = 30

    # пробуем выполнить код
    try:
        # сохраняем значение в переменную
        diagnosis_filter = input('Введите диагноз C: ').strip().lower()
    except EOFError:
        # сохраняем значение в переменную
        diagnosis_filter = 'грипп'

    # сохраняем значение в переменную
    encodings = ['utf-8']
    # сохраняем значение в переменную
    lines = None

    # проходим цикл
    for encoding in encodings:
        # пробуем выполнить код
        try:
            # открываем файл
            with open('klinika.txt', 'r', encoding=encoding) as file:
                # сохраняем значение в переменную
                lines = file.readlines()
            # выводим результат
            print(f'Файл успешно прочитан в кодировке {encoding}')
            # выполняем действие
            break
        except UnicodeDecodeError:
            # выполняем действие
            continue

    # проверяем условие
    if lines is None:
        # выводим результат
        print('Не удалось прочитать файл ни в одной из распространённых кодировок')
        # выполняем действие
        return

    # сохраняем значение в переменную
    patients = []
    # проходим цикл
    for line in lines:
        # сохраняем значение в переменную
        line = line.strip()
        # проверяем условие
        if not line:
            # выполняем действие
            continue

        # сохраняем значение в переменную
        parts = line.split()
        # проверяем условие
        if len(parts) < 5:
            # выполняем действие
            continue

        # сохраняем значение в переменную
        surname, gender, age_text, city, diagnosis = parts
        # пробуем выполнить код
        try:
            # сохраняем значение в переменную
            age = int(age_text)
        except ValueError:
            # выполняем действие
            continue

        # проверяем условие
        if age > age_border and diagnosis.lower() == diagnosis_filter:
            # выполняем действие
            patients.append(f'{surname} {gender} {age} {city} {diagnosis}')

    # проверяем условие
    if patients:
        # выводим результат
        print('Список пациентов старше', age_border, 'лет с диагнозом', diagnosis_filter + ':')
        # проходим цикл
        for patient in patients:
            # выводим результат
            print(patient)
    else:
        # выводим результат
        print('Пациентов, удовлетворяющих условию, не найдено')


# проверяем прямой запуск файла
if __name__ == '__main__':
    # выполняем действие
    main()
