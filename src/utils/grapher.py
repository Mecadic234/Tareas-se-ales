
import matplotlib.pyplot as plt

def continuous_plotter(t, x, titulo="Señal continua"):
    """
    Grafica una señal continua.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label='x(t)')
    plt.title(titulo)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def discrete_plotter(n, x, titulo="Señal discreta"):
    """
    Grafica una señal discreta o su espectro DFT.
    n : eje x (por ejemplo frecuencias)
    x : magnitud de la señal
    titulo : título del gráfico
    """
    plt.figure(figsize=(10, 4))
    plt.stem(n, x, linefmt='b', markerfmt='bo', basefmt='k')
    plt.title(titulo)
    plt.xlabel('Frecuencia [Hz]' if max(n) > 1 else 'n')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
