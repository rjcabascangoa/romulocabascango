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
stop_events = {1: threading.Event(), 2: threading.Event(), 3: threading.Event()}

# Crear instancias de hilos
hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1, errores, memoria, stop_events[1]))
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8, errores, memoria, stop_events[2]))
hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2, errores, memoria, stop_events[3]))

# Iniciar los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Función para monitorear el consumo de recursos del proceso
def monitorear_recursos(intervalo, duracion):
    pid = psutil.Process().pid
    uso_memoria = []
    tiempo = []

    for _ in range(int(duracion / intervalo)):
        proceso = psutil.Process(pid)
        uso_memoria.append(proceso.memory_info().rss / (1024 * 1024))  # Convertir a MB
        tiempo.append(time.time() - inicio)
        time.sleep(intervalo)

    return tiempo, uso_memoria

# Configurar monitoreo de recursos
intervalo_monitoreo = 1  # Intervalo en segundos
duracion_monitoreo = 15  # Duración total del monitoreo en segundos

inicio = time.time()
tiempo, uso_memoria = monitorear_recursos(intervalo_monitoreo, duracion_monitoreo)

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print('Programa principal: Todas las tareas han sido completadas.')

# Graficar los resultados
fig, ax = plt.subplots()

for hilo_id, mem in memoria.items():
    ax.plot(mem, label=f'Hilo {hilo_id}')

ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Uso de Memoria (MB)')
plt.title('Consumo de Memoria por Hilo')
plt.legend()

plt.show()

# Mostrar errores si los hubo
for hilo_id, error in errores.items():
    print(f"Hilo {hilo_id} tuvo un error: {error}")

# Función para detener un hilo
def detener_hilo(hilo_id):
    if hilo_id in stop_events:
        stop_events[hilo_id].set()
        print(f'Hilo {hilo_id} ha sido detenido.')

# Solicitar al usuario que elija un hilo para detener
hilo_a_detener = int(input("Introduce el ID del hilo que deseas detener (1, 2, 3): "))
detener_hilo(hilo_a_detener)