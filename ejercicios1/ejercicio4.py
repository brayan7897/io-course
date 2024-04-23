import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f1(x):
    return (2 + 4*x)

def f2(x):
    return np.ones_like(x) * 2

def f3(x):
    return 3 - x

def objective_function(x , y):
    return x + y 

# Crear rangos de valores para x e y
x_values = np.linspace(0, 5, 400)

# Calcular los valores correspondientes de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)
y3_values = f3(x_values)

# Graficar las restricciones
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$-4X1 + 2X2 \leq 2$', linewidth=2, linestyle='-')
plt.axvline(2, color='red', linestyle='-', linewidth=2, label=r'$X1 \leq 3$')
plt.plot(x_values, y3_values, label=r'$2X1 + 2X2 \leq 6$', linewidth=2, linestyle='-')

plt.fill_between(x_values, 0, y3_values, where=(x_values <= 2) & (y1_values >= y3_values), color='blue', alpha=0.2)
plt.fill_between(x_values, 0, y3_values, where=(x_values <= 2) & (y1_values <= y3_values), color='blue', alpha=0.2)
plt.fill_between(x_values, y1_values, 4, color='red', alpha=0.2)
plt.fill_between(x_values, y3_values,0, color='green', alpha=0.2)

# Etiquetas de los ejes y título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Gráfico de restricciones')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(0, 3) # Limitar el eje x hasta 2
plt.ylim(0, 3) # Limitar el eje y hasta 2

plt.show()




