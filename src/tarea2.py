import numpy as np
from src.utils.grapher import continuous_plotter

def graficar_senal_senoidal(frecuencia):
    A = 1  # amplitud
    t = np.linspace(0, 2, 1000)  # tiempo de 0 a 2 segundos
    x = A * np.sin(2 * np.pi * frecuencia * t)

    titulo = f"Señal Senoidal - Frecuencia = {frecuencia} Hz"
    continuous_plotter(t, x, titulo)

