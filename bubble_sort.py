def bubble_sort(arr):
    """
    Ordena una lista usando el algoritmo Bubble Sort.
    Complejidad:
      - Peor caso: O(n^2)
      - Mejor caso: O(n) si la lista ya está ordenada
      - Espacio: O(1)
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Si no hubo intercambio, la lista ya está ordenada
    return arr


# Prueba del algoritmo
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", example_list)
    print("Sorted:", bubble_sort(example_list))
