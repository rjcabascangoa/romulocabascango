import psutil

def listar_procesos():
    # Listar todos los procesos activos
    print(f"{'PID':<10} {'Nombre':<25}")
    print("="*35)
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"{proc.info['pid']:<10} {proc.info['name']:<25}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def eliminar_proceso(pid):
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()
        proceso.wait(timeout=3)
        print(f"Proceso {pid} eliminado exitosamente.")
    except psutil.NoSuchProcess:
        print(f"No existe un proceso con PID {pid}.")
    except psutil.AccessDenied:
        print(f"Permiso denegado para eliminar el proceso con PID {pid}.")
    except psutil.TimeoutExpired:
        print(f"El proceso con PID {pid} no pudo ser terminado en el tiempo esperado.")

if __name__ == "__main__":
    while True:
        print("\nLista de procesos:")
        listar_procesos()
        pid = int(input("\nIntroduce el PID del proceso que deseas eliminar (o -1 para salir): "))
        if pid == -1:
            break
        eliminar_proceso(pid)
