# grapher.py

import matplotlib.pyplot as plt

def graficar(t_cont, t_disc, n, titulo, cont, disc):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(t_cont, cont, label="Continua")
    plt.title(titulo + " (continua)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.stem(n, disc, linefmt='b', markerfmt='bo', basefmt='k')
    plt.title(titulo + " (discreta)")
    plt.xlabel("n")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def continuous_plotter(t, x, titulo="Señal"):
    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label='x(t)')
    plt.title(titulo)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
def discrete_plotter(n, señal_modificada, señal_referencia):
    plt.figure()
    plt.stem(n, señal_modificada, linefmt='b-', markerfmt='bo', basefmt=' ', label='Señal modificada')
    plt.stem(n, señal_referencia, linefmt='r--', markerfmt='ro', basefmt=' ', label='Señal de referencia')
    plt.title('Señal en Tiempo Discreto')
    plt.xlabel('n (muestras)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.show()
