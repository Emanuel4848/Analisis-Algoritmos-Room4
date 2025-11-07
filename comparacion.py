import random
import time
from bubble_sort import bubble_sort

def medir_tiempo(func, datos):
    inicio = time.perf_counter()
    func(datos.copy())
    fin = time.perf_counter()
    return fin - inicio

tamaños = [100, 500, 1000, 5000]

for n in tamaños:
    lista = [random.randint(0, 10000) for _ in range(n)]
    tiempo_bubble = medir_tiempo(bubble_sort, lista)
    tiempo_sorted = medir_tiempo(sorted, lista)
    print(f"n={n} → BubbleSort={tiempo_bubble:.4f}s | sorted()={tiempo_sorted:.4f}s")
