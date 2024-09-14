import threading
import time
import matplotlib.pyplot as plt
import random

# Función que simula una tarea para un hilo
def tarea_hilo(identificador, delay, errores):
    try:
        for i in range(10):
            if random.random() < 0.2:  # Simular un error con una probabilidad del 20%
                raise Exception(f"Error simulado en el hilo {identificador}")
            print(f'Hilo {identificador}: Realizando tarea {i}')
            time.sleep(delay)
    except Exception as e:
        if identificador in errores:
            errores[identificador] += 1
        else:
            errores[identificador] = 1

# Inicializar diccionario para errores
errores = {}

# Crear e iniciar hilos
hilos = []
for i in range(1, 4):
    hilo = threading.Thread(target=tarea_hilo, args=(i, random.uniform(0.5, 1.5), errores))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print('Programa principal: Todas las tareas han sido completadas.')

# Graficar los resultados
nombres_hilos = list(errores.keys())
errores_hilos = list(errores.values())

plt.bar(nombres_hilos, errores_hilos, color='red')
plt.xlabel('ID del Hilo')
plt.ylabel('Cantidad de Errores')
plt.title('Errores por Hilo')
plt.show()

# Mostrar errores
for hilo_id, error_count in errores.items():
    print(f"Hilo {hilo_id} tuvo {error_count} errores.")
