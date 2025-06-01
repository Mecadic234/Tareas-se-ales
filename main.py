import sys
import os

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "tarea_1":
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_path = os.path.join(current_dir, "src")
        if src_path not in sys.path:
            sys.path.insert(0, src_path)

        import tarea_1  
    else:
        print("Por favor proporcione el numero de la tarea.")
        print("Ejemplo: python main.py tarea_1")
