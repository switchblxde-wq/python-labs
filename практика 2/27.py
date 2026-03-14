# main function for task

def main():
    # try to read age border
    try:
        # read age border value
        age_border = int(input('Введите возраст B: '))
    except (EOFError, ValueError):
        # use default age border
        age_border = 30

    # try to read diagnosis
    try:
        # read diagnosis text
        diagnosis_filter = input('Введите диагноз C: ').strip().lower()
    except EOFError:
        # use default diagnosis
        diagnosis_filter = 'грипп'

    # list of encodings to try
    encodings = ['utf-8']
    # storage for file lines
    lines = None

    # try each encoding
    for encoding in encodings:
        # open file and read lines
        try:
            # read all file lines
            with open('klinika.txt', 'r', encoding=encoding) as file:
                # save lines
                lines = file.readlines()
            # print success message
            print(f'Файл успешно прочитан в кодировке {encoding}')
            # break after success
            break
        except UnicodeDecodeError:
            # continue with next encoding
            continue

    # stop when file was not read
    if lines is None:
        # print error message
        print('Не удалось прочитать файл ни в одной из распространённых кодировок')
        # exit function
        return

    # result list for filtered patients
    patients = []
    # process each line
    for line in lines:
        # strip spaces
        line = line.strip()
        # skip empty line
        if not line:
            # continue loop
            continue

        # split line into parts
        parts = line.split()
        # skip broken rows
        if len(parts) < 5:
            # continue loop
            continue

        # unpack parts
        surname, gender, age_text, city, diagnosis = parts
        # parse age to int
        try:
            # convert text to int
            age = int(age_text)
        except ValueError:
            # skip invalid row
            continue

        # check filter condition
        if age > age_border and diagnosis.lower() == diagnosis_filter:
            # append matching patient
            patients.append(f'{surname} {gender} {age} {city} {diagnosis}')

    # print results when found
    if patients:
        # print header line
        print('Список пациентов старше', age_border, 'лет с диагнозом', diagnosis_filter + ':')
        # print each patient
        for patient in patients:
            # print one patient row
            print(patient)
    else:
        # print empty result message
        print('Пациентов, удовлетворяющих условию, не найдено')


# start main on direct run
if __name__ == '__main__':
    # call main function
    main()
