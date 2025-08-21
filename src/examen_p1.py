
import sys
import os
import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.grapher import continuous_plotter, discrete_plotter

def ejecutar_examen_p1():
    """
    Calcula y grafica la DFT de una señal modulada:
    x(t) = [1 + m*cos(2*pi*fm*t)] * sin(2*pi*fc*t)
    """
    
    fm = 0.5      
    fc = 8        
    m = 0.5
    fs = 50       
    T = 2         

    
    t = np.arange(0, T, 1/fs)
    x = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

   
    continuous_plotter(t, x)

    
    N = len(x)
    X = np.fft.fft(x)
    X_mag = np.abs(X) / N
    freqs = np.fft.fftfreq(N, d=1/fs)

    
    idx = freqs >= 0
    freqs_pos = freqs[idx]
    X_mag_pos = X_mag[idx]

   
    discrete_plotter(freqs_pos, X_mag_pos)

   
    df = fs / N
    print(f"Resolución en frecuencia: Δf = {df:.3f} Hz")

   
    peak_indices = np.argsort(X_mag_pos)[-3:][::-1]
    print("Picos espectrales (frecuencia [Hz] : magnitud):")
    for i in peak_indices:
        print(f"{freqs_pos[i]:.3f} Hz : {X_mag_pos[i]:.3f}")


