def main():
    B = int(input("Введите возраст B: "))
    C = input("Введите диагноз C: ").strip().lower()

    encodings_to_try = ['utf-8']
    lines = None
    for enc in encodings_to_try:
        try:
            with open('klinika.txt', 'r', encoding=enc) as f:
                lines = f.readlines()
            print(f"Файл успешно прочитан в кодировке {enc}")
            break
        except UnicodeDecodeError:
            continue

    if lines is None:
        print("Не удалось прочитать файл ни в одной из распространённых кодировок.")
        return

    patients = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        surname, gender, age_str, city, diagnosis = parts
        try:
            age = int(age_str)
        except ValueError:
            continue
        if age > B and diagnosis.lower() == C:
            patients.append(f"{surname} {gender} {age} {city} {diagnosis}")

    if patients:
        print("Список пациентов старше", B, "лет с диагнозом", C + ":")
        for p in patients:
            print(p)
    else:
        print("Пациентов, удовлетворяющих условию, не найдено.")

if __name__ == "__main__":
    main()