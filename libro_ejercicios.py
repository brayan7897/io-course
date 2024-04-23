import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return (24 - 6*x) / 4

def f2(x):
    return (6 - x) / 2

def f3(x):
    return x + 1

# Rangos de valores para x e y
x_values = np.linspace(0, 10, 400)

# Calcular los valores correspondientes de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)
y3_values = f3(x_values)


plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$6x + 4y \leq 24$', linewidth=2, linestyle='-')
plt.plot(x_values, y2_values, label=r'$x + 2y \leq 6$', linewidth=2, linestyle='-')
plt.plot(x_values, y3_values, label=r'$-x + y \leq 1$', linewidth=2, linestyle='-')
plt.axhline(2, color='red', linestyle='-', linewidth=2, label=r'$y \leq 2$')
plt.axvline(0, color='green', linestyle='-', linewidth=2, label=r'$x \geq 0$')

y4_values = np.minimum.reduce([y1_values, y2_values, y3_values, np.ones_like(x_values) * 2])
plt.fill_between(x_values, 0, y4_values, where=(x_values >= 0) & (y4_values <= 2), color='gray', alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de restricciones')


plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(0, 8) # Limitar el eje x hasta 8
plt.ylim(0, 6) # Limitar el eje y hasta 4

plt.show()

