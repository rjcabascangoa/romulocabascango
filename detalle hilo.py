import threading
import time
import psutil
import matplotlib.pyplot as plt

# Función que simula una tarea para un hilo
def tarea_hilo(identificador, delay, errores, memoria, stop_event):
    try:
        while not stop_event.is_set():
            memoria[identificador].append(psutil.Process().memory_info().rss / (1024 * 1024))  # Convertir a MB
            print(f'Hilo {identificador}: Realizando tarea')
            time.sleep(delay)
    except Exception as e:
        errores[identificador] = str(e)

# Inicializar diccionarios para errores y uso de memoria
errores = {}
memoria = {1: [], 2: [], 3: []}
stop
