letters = ['a', 'b', 'c', 'd', 'e']
numbers = [10, 20, 30, 40, 50]


dictionary = dict(zip(letters, numbers))


print("Словарь:", dictionary)

total = sum(dictionary.values())
print("Сумма всех значений:", total)

with open('ex2-1.txt', 'w') as file:
    file.write(str(total))