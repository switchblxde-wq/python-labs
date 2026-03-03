import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 1000, endpoint=True)
y = np.where(x == 0, np.nan, (np.sin(3*x) * np.cos(2*x)) / (3*x))

plt.plot(x, y, color='green', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = (sin(3x)*cos(2x))/(3x)')
plt.grid(True, linestyle='--', alpha=0.7)

ticks = np.arange(-3, 4) * np.pi 
labels = [f'{int(t/np.pi)}π' if t != 0 else '0' for t in ticks]
plt.xticks(ticks, labels)

plt.show()