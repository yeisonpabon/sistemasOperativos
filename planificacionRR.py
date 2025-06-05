"""yeison andres villegas pabon
juan david tezna londoño"""

from collections import deque

# Proceso con tiempo de llegada y su rafaga
class Proceso:
    def __init__(self, pid, rafaga):
        self.pid = pid
        self.rafaga = rafaga
        self.restante = rafaga
        self.tiempo_espera = 0
        self.tiempo_ejecucion = 0

def round_robin(procesos, quantum):
    cola = deque(procesos)
    tiempo = 0

    while cola:
        proceso = cola.popleft()
        ejec = min(proceso.restante, quantum)
        print(f"Ejecutando P{proceso.pid} por {ejec} unidades.")
        tiempo += ejec
        proceso.restante -= ejec

        for p in cola:
            p.tiempo_espera += ejec

        if proceso.restante > 0:
            cola.append(proceso)
        else:
            proceso.tiempo_ejecucion = tiempo
            print(f"Proceso P{proceso.pid} terminado en t={tiempo}")

    print("\n--- Resultados ---")
    for p in procesos:
        print(f"P{p.pid} -> Espera: {p.tiempo_espera}, Ejecución: {p.tiempo_ejecucion}")

# Lista de procesos (PID, ráfaga)
procesos = [Proceso(1, 6), Proceso(2, 4), Proceso(3, 8)]
quantum = 3
round_robin(procesos, quantum)
