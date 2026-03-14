# комментарий

def main():
    # комментарий
    try:
        # комментарий
        age_border = int(input('Введите возраст B: '))
    except (EOFError, ValueError):
        # комментарий
        age_border = 30

    # комментарий
    try:
        # комментарий
        diagnosis_filter = input('Введите диагноз C: ').strip().lower()
    except EOFError:
        # комментарий
        diagnosis_filter = 'грипп'

    # комментарий
    encodings = ['utf-8']
    # комментарий
    lines = None

    # комментарий
    for encoding in encodings:
        # комментарий
        try:
            # комментарий
            with open('klinika.txt', 'r', encoding=encoding) as file:
                # комментарий
                lines = file.readlines()
            # комментарий
            print(f'Файл успешно прочитан в кодировке {encoding}')
            # комментарий
            break
        except UnicodeDecodeError:
            # комментарий
            continue

    # комментарий
    if lines is None:
        # комментарий
        print('Не удалось прочитать файл ни в одной из распространённых кодировок')
        # комментарий
        return

    # комментарий
    patients = []
    # комментарий
    for line in lines:
        # комментарий
        line = line.strip()
        # комментарий
        if not line:
            # комментарий
            continue

        # комментарий
        parts = line.split()
        # комментарий
        if len(parts) < 5:
            # комментарий
            continue

        # комментарий
        surname, gender, age_text, city, diagnosis = parts
        # комментарий
        try:
            # комментарий
            age = int(age_text)
        except ValueError:
            # комментарий
            continue

        # комментарий
        if age > age_border and diagnosis.lower() == diagnosis_filter:
            # комментарий
            patients.append(f'{surname} {gender} {age} {city} {diagnosis}')

    # комментарий
    if patients:
        # комментарий
        print('Список пациентов старше', age_border, 'лет с диагнозом', diagnosis_filter + ':')
        # комментарий
        for patient in patients:
            # комментарий
            print(patient)
    else:
        # комментарий
        print('Пациентов, удовлетворяющих условию, не найдено')


# комментарий
if __name__ == '__main__':
    # комментарий
    main()
