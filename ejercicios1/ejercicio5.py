import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return x - 1

def f2(x):
    return 2 + 0.5 * x

# Rangos de valores para x e y
x_values = np.linspace(0, 10, 400)

# Calcular los valores correspondientes de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)

# Graficar las restricciones
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$x - y \geq 1$', linewidth=2, linestyle='-')
plt.plot(x_values, y2_values, label=r'$\frac{1}{2}x + y \leq 2$', linewidth=2, linestyle='-')

# Rellenar la región factible
plt.fill_between(x_values, y1_values, where=(x_values >= y2_values), color='gray', alpha=0.5)
plt.fill_between(x_values, y1_values, where=((x_values <= y2_values)), color='gray', alpha=0.5)
plt.fill_between(x_values, y1_values, color='b', alpha=0.5)
plt.fill_between(x_values, y2_values, color='r', alpha=0.5)
# Etiquetas de los ejes y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de restricciones')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(0, 10) # Limitar el eje x hasta 3
plt.ylim(0, 10) # Limitar el eje y hasta 3

plt.show()
