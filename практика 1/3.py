# пробуем выполнить код
try:
    # сохраняем значение в переменную
    size = int(input('Введите размер списка: '))
except EOFError:
    # сохраняем значение в переменную
    size = 3
except ValueError:
    # сохраняем значение в переменную
    size = 3

# сохраняем значение в переменную
numbers = []
# проходим цикл
for index in range(size):
    # пробуем выполнить код
    try:
        # сохраняем значение в переменную
        value = int(input(f'Введите элемент {index + 1}: '))
    except EOFError:
        # сохраняем значение в переменную
        value = index + 1
    except ValueError:
        # сохраняем значение в переменную
        value = index + 1
    # выполняем действие
    numbers.append(value)

# выводим результат
print('Исходный список:', numbers)
# проверяем условие
if size > 1:
    # сохраняем значение в переменную
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
# выводим результат
print('Обновленный список:', numbers)
