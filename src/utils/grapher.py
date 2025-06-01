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
