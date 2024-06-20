import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

def calcular_tiempo_vaciado(A, a, g, h0, h):
    # A es el área de la sección transversal del tanque
    # a es el área de la abertura en el fondo del tanque
    # g es la aceleración debido a la gravedad
    # h0 es la altura inicial del agua en el tanque
    # h es la altura final del agua en el tanque

    # Calculamos el coeficiente k
    k = (2 * A) / (a * math.sqrt(2 * g))

    # Calculamos el tiempo t usando la fórmula derivada
    t = k * (math.sqrt(h0) - math.sqrt(h))

    return t

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

def graficar_nivel_agua():
    try:
        A = float(entrada_A.get())
        a = float(entrada_a.get())
        g = float(entrada_g.get())
        h0 = float(entrada_h0.get())

        tiempos = np.linspace(0, calcular_tiempo_vaciado(A, a, g, h0, 0.01), 500)
        niveles = [calcular_nivel_agua(A, a, g, h0, t) for t in tiempos]

        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, niveles, label='Nivel del agua en el tanque')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Altura del agua (m)')
        plt.title('Reducción del nivel del agua en el tanque con el tiempo')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Error: Debe ingresar valores numéricos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tiempo de vaciado del tanque")

# Crear etiquetas y entradas para las variables
etiqueta_A = tk.Label(ventana, text="Área de la sección transversal del tanque (m^2):")
etiqueta_A.grid(column=0, row=0)
entrada_A = tk.Entry(ventana)
entrada_A.grid(column=1, row=0)

etiqueta_a = tk.Label(ventana, text="Área de la abertura en el fondo del tanque (m^2):")
etiqueta_a.grid(column=0, row=1)
entrada_a = tk.Entry(ventana)
entrada_a.grid(column=1, row=1)

etiqueta_g = tk.Label(ventana, text="Aceleración debido a la gravedad (m/s^2):")
etiqueta_g.grid(column=0, row=2)
entrada_g = tk.Entry(ventana)
entrada_g.grid(column=1, row=2)

etiqueta_h0 = tk.Label(ventana, text="Altura inicial del agua en el tanque (m):")
etiqueta_h0.grid(column=0, row=3)
entrada_h0 = tk.Entry(ventana)
entrada_h0.grid(column=1, row=3)

# Crear botón para graficar
boton_graficar = tk.Button(ventana, text="Graficar", command=graficar_nivel_agua)
boton_graficar.grid(column=1, row=4)

# Iniciar ventana principal
ventana.mainloop()