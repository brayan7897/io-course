import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return (16 - 12*x) / 6

def f2(x):
    return (12 - 4*x) / 12

# Crear un rango de valores para x
x_values = np.linspace(0, 3, 100)

# Calcular los valores correspondientes de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)

# Graficar las restricciones
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$12x + 6y \geq 16$')
plt.plot(x_values, y2_values, label=r'$4x + 12y \geq 12$')

# Rellenar la región factible
plt.fill_between(x_values, y1_values, y2_values, where=(y1_values >= y2_values), color='gray', alpha=0.4)
plt.fill_between(x_values, y1_values, y2_values, where=(y2_values >= y1_values), color='red', alpha=0.3)
plt.fill_between(x_values, y1_values, 4, color='blue', alpha=0.2)

# Etiquetas de los ejes y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico de restricciones')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
