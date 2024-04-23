import numpy as np                # crear vectores de números
import matplotlib.pyplot as plt   # crear gráficos de líneas 



def graficar_area_bajo_curva(funcion, intervalo):
    """
    INPUT: Entra una función lambda defiinida por el usuario
    Un intervalo cerrado $[a,b]$ definido a través de una lista de python
    OUTPUT: Gráfico del área bajo la curva
    """
    # Definir la función lambda
    f = funcion  # Cambia esto por tu función
    # Definir los límites del intervalo cerrado
    a = intervalo[0]   # Límite inferior 
    b = intervalo[1]   # Límite superior

    # Generar puntos para graficar la función y las líneas verticales
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)
    x_a = np.array([a, a])  
    y_a = np.array([0, f(a)])
    x_b = np.array([b, b])
    y_b = np.array([0, f(b)])

    # Graficar la función y las líneas verticales
    plt.plot(x_vals, y_vals, label='y = f(x)')
    plt.plot(x_a, y_a, 'r--', label=f'x = {a}')
    plt.plot(x_b, y_b, 'g--', label=f'x = {b}')
    plt.fill_between(x_vals, y_vals, alpha=0.2)

    # Etiquetas y leyenda
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Región de Integración')
    plt.legend()

# Mostrar el gráfico
    plt.grid()

    plt.show()

graficar_area_bajo_curva(funcion = lambda x: np.sin(x), intervalo = [0,np.pi])