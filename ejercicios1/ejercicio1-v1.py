import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return (30 - 6*x) / 3

def f2(x):
    return (24 - 2*x) / 8

def objective_function(x):
    return (30 - 6*x) / 3

A = np.array([[6, 3], [2, 8]])
b = np.array([30, 24])
intersection_point = np.linalg.solve(A, b)

x_values = np.linspace(0, 10, 400)

# Calculamos los valores correspondientes para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)
objective_values = objective_function(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$6x + 3y \geq 30$')
plt.plot(x_values, y2_values, label=r'$2x + 8y \geq 24$')


plt.fill_between(x_values, y1_values, y2_values, where=(y1_values >= y2_values), color='gray', alpha=0.5)
plt.fill_between(x_values, y1_values, y2_values, where=(y2_values >= y1_values), color='red', alpha=0.5)

plt.plot(x_values, objective_values, label=r'$50x + 100y$', color='red')


plt.fill_between(x_values, objective_values, 15, color='blue', alpha=0.3)


plt.plot(intersection_point[0], intersection_point[1], 'ro', label='Solución óptima')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico de restricciones y función objetivo')


plt.legend()

plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
