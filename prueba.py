import math
import matplotlib as plt
import numpy as np

def calcular_nivel_agua(A, a, g, h0, t):
    # A es el área de la sección transversal del tanque
    # a es el área de la abertura en el fondo del tanque
    # g es la aceleración debido a la gravedad
    # h0 es la altura inicial del agua en el tanque
    # t es el tiempo transcurrido
    
    # Calculamos el coeficiente k
    k = (2 * A) / (a * math.sqrt(2 * g))
    
    # Calculamos la altura del agua en el tanque en el tiempo t
    h = (math.sqrt(h0) - t / k) ** 2
    return h if h >= 0 else 0  # La altura no puede ser negativa

# Parámetros
A = 1.0  # Área de la sección transversal del tanque en m^2
a = 0.01  # Área de la abertura en el fondo del tanque en m^2
g = 9.81  # Aceleración debido a la gravedad en m/s^2
h0 = 4.0  # Altura inicial del agua en el tanque en metros

# Generar valores de tiempo
tiempos = np.linspace(0, calcular_tiempo_vaciado(A, a, g, h0, 0.01), 500)
niveles = [calcular_nivel_agua(A, a, g, h0, t) for t in tiempos]

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tiempos, niveles, label='Nivel del agua en el tanque')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura del agua (m)')
plt.title('Reducción del nivel del agua en el tanque con el tiempo')
plt.legend()
plt.grid(True)
plt.show()