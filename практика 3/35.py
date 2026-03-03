import matplotlib.pyplot as plt

y_values = list(map(float, input("Введите высоты столбцов через пробел: ").split()))
x_values = list(range(len(y_values)))

plt.bar(x_values, y_values, color='blue')
plt.xlabel('Номер столбца')
plt.ylabel('Высота')
plt.title('Столбчатая диаграмма по введённым данным')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
