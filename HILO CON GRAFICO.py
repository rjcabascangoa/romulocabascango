import threading
import time
import psutil
import matplotlib.pyplot as plt

# Función que simula una tarea para un hilo
def tarea_hilo(identificador, delay):
    for i in range(10):
        print(f'Hilo {identificador}: Realizando tarea {i}')
        time.sleep(delay)

# Crear instancias de hilos
hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1))
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8))
hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2))

# Iniciar los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Función para monitorear el consumo de CPU y memoria del proceso
def monitorear_recursos(intervalo, duracion):
    pid = psutil.Process().pid
    uso_cpu = []
    uso_memoria = []
    tiempo = []

    for _ in range(int(duracion / intervalo)):
        proceso = psutil.Process(pid)
        uso_cpu.append(proceso.cpu_percent(interval=intervalo))
        uso_memoria.append(proceso.memory_info().rss / (1024 * 1024))  # Convertir a MB
        tiempo.append(time.time() - inicio)
        time.sleep(intervalo)

    return tiempo, uso_cpu, uso_memoria

# Configurar monitoreo de recursos
intervalo_monitoreo = 1  # Intervalo en segundos
duracion_monitoreo = 15  # Duración total del monitoreo en segundos

inicio = time.time()
tiempo, uso_cpu, uso_memoria = monitorear_recursos(intervalo_monitoreo, duracion_monitoreo)

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print('Programa principal: Todas las tareas han sido completadas.')

# Graficar los resultados
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(tiempo, uso_cpu, 'g-')
ax2.plot(tiempo, uso_memoria, 'b-')

ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Uso de CPU (%)', color='g')
ax2.set_ylabel('Uso de Memoria (MB)', color='b')

plt.title('Consumo de recursos del proceso')
plt.show()
