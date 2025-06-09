import sys
import os
sys.path.append(os.path.abspath("src"))
from src.tarea1 import senoidal, exponencial, triangular, cuadrada
from src.tarea2 import graficar_senal_senoidal as ejecutar_tarea2
from src.tarea3 import ejecutar_tarea3  

def main():
    if ejecutar_tarea_desde_argumentos():
        return  

    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        if opcion == "1":
            ejecutar_tarea1()
        elif opcion == "2":
            print("Para ejecutar la tarea 2, usa el siguiente comando en consola:")
            print("Ejemplo: python main.py tarea2 6")
            break  
        elif opcion == "3":
            print("Para ejecutar la tarea 3, usa el siguiente comando en consola:")
            print("Ejemplo: python main.py tarea3 1 2 0.785")
            break
        elif opcion == "0":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción inválida, intente de nuevo.")

def mostrar_menu():
    print("\nSeleccione la tarea a ejecutar:")
    print("1. Tarea 1")
    print("2. Tarea 2")
    print("3. Tarea 3")
    print("0. Salir")

def mostrar_menu_tarea1():
    print("\nTarea 1: Seleccione una señal")
    print("1. Señal senoidal")
    print("2. Señal exponencial")
    print("3. Señal triangular")
    print("4. Señal cuadrada")

def ejecutar_tarea1():
    while True:
        mostrar_menu_tarea1()
        opcion = input("Ingrese la señal que desea ejecutar: ").strip()
        if opcion == "1":
            senoidal()
        elif opcion == "2":
            exponencial()
        elif opcion == "3":
            triangular()
        elif opcion == "4":
            cuadrada()
        else:
            print("Opción inválida, intente de nuevo.")

def ejecutar_tarea_desde_argumentos():
    if len(sys.argv) < 2:
        return False  

    tarea = sys.argv[1].lower()

    if tarea == "tarea2":
        if len(sys.argv) < 3:
            print("Error: faltó la frecuencia")
            sys.exit(1)
        try:
            frecuencia = float(sys.argv[2])
            ejecutar_tarea2(frecuencia)
            return True
        except ValueError:
            print("La frecuencia debe ser un número.")
            sys.exit(1)

    elif tarea == "tarea3":
        if len(sys.argv) < 5:
            print("Uso correcto: python main.py tarea3 <amplitud> <frecuencia> <fase>")
            sys.exit(1)
        try:
            A = float(sys.argv[2])
            f = float(sys.argv[3])
            fase = float(sys.argv[4])
            ejecutar_tarea3(A, f, fase)
            return True
        except ValueError:
            print("Los parámetros deben ser números.")
            sys.exit(1)

    print("Comando no reconocido. Ejemplos válidos:\n")
    print("  python main.py tarea1 senoidal")
    print("  python main.py tarea2 6")
    print("  python main.py tarea3 1 2 0.785")
    sys.exit(1)

if __name__ == "__main__":
    main()



