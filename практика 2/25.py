
m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]


result = list(map(lambda x, i: round(x, i), m, range(1, len(m) + 1)))

print("Новый список с округлением:", result)
