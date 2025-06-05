import time                
import random            
from queue import Queue 

# Definición de la clase Proceso, que representa cada proceso en el sistema
class Proceso:
    def __init__(self, id, duracion):
        self.id = id                    # Asigna un id único al proceso
        self.duracion = duracion        # Define la duración total 
        self.tiempo_restante = duracion # Establece el tiempo restante, que se actualizará durante la ejecucionución
        self.estado = "Bloqueado"           # Establece el estado inicial del proceso

    def __str__(self):
        return f"Proceso {self.id} | Estado: {self.estado} | Tiempo restante: {self.tiempo_restante}s"

     # Función para cambiar el estado a "Bloqueado"
    def Cambiar_estado(self):
        if self.estado == "En ejecucionución":
            self.estado = "Bloqueado"
            print(f"Proceso {self.id} ha sido suspendido.")

    # Función para Reanudar un proceso suspendido
    def Reanudar_proceso(self):
        if self.estado == "Bloqueado":
            self.estado = "Listo"
            print(f"Proceso {self.id} ha sido reanudado.")

    # Función para marcar el proceso como terminado
    def terminar(self):
        self.estado = "Terminado"
        self.tiempo_restante = 0
        print(f"Proceso {self.id} ha terminado.")

# Función para simular el cambio de contexto
def Cambio_contexto(proceso):
    print(f"\nCambio de contexto: Proceso {proceso.id} pasa a estado {proceso.estado}")

# Crear una cola de procesos para gestionar los procesos listos para ejecucionutarse
cola_procesos = Queue()

# Generar algunos procesos aleatorios y añadirlos a la cola de procesos
for i in range(5):                                  # Cambia este número para agregar más procesos si se desea
    duracion = random.randint(2, 5)                 # Asigna una duración aleatoria entre 2 y 5 segundos
    proceso = Proceso(id=i + 1, duracion=duracion)  # Crea un proceso con un identificador y duración
    # Cambiar aleatoriamente algunos procesos a "Listo"
    if i==0 or random.choice([True, False]):
        proceso.estado = "Listo"
    cola_procesos.put(proceso)                      # Añade el proceso a la cola

# Muestra la cola inicial de procesos antes de la ejecucionución
print("Cola de procesos inicial:")
for proceso in list(cola_procesos.queue):   # Recorre cada proceso en la cola para mostrar su información
    print(proceso)                          # Imprime la información de cada proceso

# Estructura del planificador
def planificador(cola_procesos, quantum=2, expulsivo=False):

    # Mientras la cola de procesos no esté vacía, sigue ejecucionutando
    while not cola_procesos.empty():
        proceso = cola_procesos.get()  # Obtiene el primer proceso en la cola
        
        if proceso.estado != "Listo":
            print(f"Proceso {proceso.id} no está listo para ejecucionutarse. Estado actual: {proceso.estado}")
            if proceso.estado == "Bloqueado":
                if random.choice([True, False]):  # Decide aleatoriamente si Reanudar_proceso
                    proceso.Reanudar_proceso()
                    print(f"Proceso {proceso.id} se ha reanudado.")
                    cola_procesos.put(proceso)
                else:
                    # Solo volver a ponerlo en la cola si no ha terminado
                    if proceso.estado != "Terminado":
                        cola_procesos.put(proceso) 
                continue

        proceso.estado = "En ejecucionución"  # Cambia el estado del proceso a "En ejecucionución"
        print(f"\nejecucionutando {proceso}")  # Imprime el estado actual del proceso

        if expulsivo:                                                  
            tiempo_ejecucion = min(proceso.tiempo_restante, quantum)    
            proceso.tiempo_restante -= tiempo_ejecucion                 # Reduce el tiempo restante del proceso
            time.sleep(tiempo_ejecucion)                                # Simula el tiempo que el proceso pasa en ejecucionución
            if proceso.tiempo_restante > 0:                             
                proceso.estado = "Listo"                                
                cola_procesos.put(proceso)                              
                Cambio_contexto(proceso)
            else:
                proceso.terminar()
        else:
        
            time.sleep(proceso.tiempo_restante)  # Espera el tiempo restante completo del proceso
            proceso.terminar()
        
        #simulacro
        if proceso.estado == "En ejecucionución" and random.choice([True, False]):
            proceso.Cambiar_estado()
            cola_procesos.put(proceso)


print("\nIniciando la simulación del planificador de procesos")
planificador(cola_procesos) 