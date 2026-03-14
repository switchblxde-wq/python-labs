import os

filename = 'z3.1-11.txt'

if not os.path.exists(filename):
    print(f"Файл {filename} не найден. Создаю новый файл с числами 5 и 345.")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('5 345\n')
else:
    print(f"Файл {filename} найден.")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        if not line:
            print("Файл пуст. Записываю числа по умолчанию.")
    
            with open(filename, 'w', encoding='utf-8') as fw:
                fw.write('5 345\n')
            line = '5 345'
   
        parts = line.split()
        if len(parts) < 2:
            print("В строке должно быть два числа, разделённых пробелом. Использую значения по умолчанию.")
            a, b = 5, 345
        else:
            a = int(parts[0])
            b = int(parts[1])
        total = a + b
        print(f"Сумма чисел {a} и {b} равна {total}")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{a} {b}\n")   
        f.write(str(total))     
    print("Результат записан во вторую строку файла")

except FileNotFoundError:
    print(f"Не удалось создать или открыть файл {filename}.")
except ValueError:
    print("Ошибка преобразования чисел. Убедитесь, что в файле записаны целые числа.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
