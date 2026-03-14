# try to get list size from user
try:
    # read list size
    size = int(input('Введите размер списка: '))
except EOFError:
    # use default size when input is closed
    size = 3
except ValueError:
    # use default size when value is invalid
    size = 3

# create empty list
numbers = []
# loop by list size
for index in range(size):
    # try to read next element
    try:
        # read integer value
        value = int(input(f'Введите элемент {index + 1}: '))
    except EOFError:
        # use generated value when input is closed
        value = index + 1
    except ValueError:
        # use generated value when input is invalid
        value = index + 1
    # append value to list
    numbers.append(value)

# print original list
print('Исходный список:', numbers)
# swap first and last items when list has more than one item
if size > 1:
    # do swap
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
# print updated list
print('Обновленный список:', numbers)
