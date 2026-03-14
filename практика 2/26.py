m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]

result = list(map(lambda x, i: round(x, i), m, range(1, len(m) + 1)))
print("Список после округления:", result)


filtered = list(filter(lambda x: x > 5.0, result))
print("Числа, большие 5.0:", filtered)

filtered2 = list(filter(lambda x: x < 4.0 or x.is_integer(), result))
print("Числа < 4.0 или целые:", filtered2)
