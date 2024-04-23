import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return 4 - x

def f2(x):
    return (8 - 6*x) / 2

def f3(x):
    return (4 - x) / 5

# Crear rangos de valores para x e y
x_values = np.linspace(0, 5, 400)

# Calcular los valores correspondientes de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)
y3_values = f3(x_values)

# Graficar las restricciones
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$X1 + X2 \leq 4$')
plt.plot(x_values, y2_values, label=r'$6X1 + 2X2 = 8$')
plt.plot(x_values, y3_values, label=r'$X1 + 5X2 \geq 4$')

# Restricciones adicionales
plt.axvline(3, color='red', linestyle='-', label=r'$X1 \leq 3$')
plt.axhline(3, color='green', linestyle='-', label=r'$X2 \leq 3$')

plt.plot(8/7, 4/7, 'ro', label='(8/7, 4/7)')

# Etiquetas de los ejes y título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Grafico de restricciones')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(0, 5)
plt.ylim(0, 5) 
plt.show()