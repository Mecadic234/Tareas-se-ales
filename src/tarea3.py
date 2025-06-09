import sys
import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def ejecutar_tarea3(A, f, fase):
    if len(sys.argv) < 5:
        print("Uso correcto: python main.py tarea3 <amplitud> <frecuencia> <fase>")
        sys.exit(1)

    try:
        A = float(sys.argv[2])  
        f = float(sys.argv[3])  
        phi = float(sys.argv[4])  
    except ValueError:
        print("Error: los parámetros deben ser números válidos.")
        sys.exit(1)

    
    t = np.linspace(0, 1, 1000)
    x_cont = A * np.sin(2 * np.pi * f * t + phi)
    x_ref_cont = 1 * np.sin(2 * np.pi * 1 * t + 0)  

    Ts = 0.01
    n = np.arange(0, 100)
    t_disc = n * Ts
    x_disc = A * np.sin(2 * np.pi * f * t_disc + phi)
    x_ref_disc = 1 * np.sin(2 * np.pi * 1 * t_disc + 0)


    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t, x_cont, label='Señal modificada')
    plt.plot(t, x_ref_cont, '--', label='Señal de referencia')
    plt.title('Señal en Tiempo Continuo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    
    discrete_plotter(n, x_disc, x_ref_disc)

    
