import numpy as np
import matplotlib.pyplot as plt

VFS = 5  # Voltaje de escala completa

def ejecutar_tarea4(bits):
    niveles = 2 ** bits
    paso = VFS / (niveles - 1)
    resolucion = (paso / VFS) * 100

    print(f"\nDAC de {bits} bits:")
    print(f"- Niveles totales: {niveles}")
    print(f"- Tamaño del paso: {paso:.6f} V")
    print(f"- Resolución porcentual: {resolucion:.6f} %")

    entradas = np.arange(niveles)
    salidas = entradas * paso

    plt.figure(figsize=(10, 5))
    plt.stem(entradas, salidas, use_line_collection=True)
    plt.title(f'Salida del DAC para {bits} bits')
    plt.xlabel('Entrada digital')
    plt.ylabel('Salida analógica (V)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
