
import sys
from src.examen_p1 import ejecutar_examen_p1
from src.examen_p2 import ejecutar_examen_p2

def main(args):
    if args[1] == "examen_p1":
        ejecutar_examen_p1()
    elif args[1] == "examen_p2":
        ejecutar_examen_p2()
    else:
        print("Opción inválida. Usa 'examen_p1' o 'examen_p2'.")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Falta argumento. Ejemplo de uso:")
        print("python main.py examen_p1")
        print("python main.py examen_p2")
