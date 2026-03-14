# комментарий
try:
    # комментарий
    size = int(input('Введите размер списка: '))
except EOFError:
    # комментарий
    size = 3
except ValueError:
    # комментарий
    size = 3

# комментарий
numbers = []
# комментарий
for index in range(size):
    # комментарий
    try:
        # комментарий
        value = int(input(f'Введите элемент {index + 1}: '))
    except EOFError:
        # комментарий
        value = index + 1
    except ValueError:
        # комментарий
        value = index + 1
    # комментарий
    numbers.append(value)

# комментарий
print('Исходный список:', numbers)
# комментарий
if size > 1:
    # комментарий
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
# комментарий
print('Обновленный список:', numbers)
