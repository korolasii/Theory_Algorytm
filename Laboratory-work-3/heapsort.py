def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sink(arr, i, n):
    comparisons = 0
    assignments = 0
    k = i
    assignments += 1
    print(f"Починаємо 'занурювати' елемент: {arr[k]} з індексу {k}")

    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента
        assignments += 1

        if j >= n:
            print(f"Елемент {arr[k]} на індексі {k} досяг кінця купи. Завершуємо.")
            break

        # Знаходимо найбільший дочірній елемент
        if j + 1 < n:
            comparisons += 1
            print(f"  Порівнюємо {arr[j]} (лівий) та {arr[j + 1]} (правий).", end=" ")
            if arr[j + 1] > arr[j]:
                j += 1
                assignments += 1
            print(f"Обираємо {arr[j]}")
        else:
            print(f"  Обираємо лівий дочірній елемент: {arr[j]} на індексі {j}")

        # Порівнюємо поточний елемент з найбільшим дочірнім
        comparisons += 1
        if arr[k] >= arr[j]:
            print(f"  {arr[k]} (батько) >= {arr[j]} (найбільший дочірній). "
                  "Елемент на своєму місці.")
            break

        print(f"  Міняємо місцями {arr[k]} (батько) та {arr[j]} (дочірній)")
        swap(arr, k, j)
        assignments += 3
        k = j
        assignments += 1
        print(f"  Масив після обміну: {arr}")

    return comparisons, assignments


def heapsort(arr):
    comparisons = 0
    assignments = 0
    sink_calls = 0
    n = len(arr)
    assignments += 1
    print(f"Початковий масив: {arr}")

    # Фаза 1: побудова максимальної купи
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a
        sink_calls += 1
        print("-" * 30)
    print(f"Масив після побудови купи: {arr}")

    # Фаза 2: сортування
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        assignments += 3
        print(f"Розмір купи зменшився до {i}. Відновлюємо властивості купи.")
        c, a = sink(arr, 0, i)
        comparisons += c
        assignments += a
        sink_calls += 1
        print(f"Масив на поточному кроці: {arr}")

    return arr, comparisons, assignments, sink_calls


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
sorted_list, comps, assigns, calls = heapsort(my_list.copy())
print("Відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
print(f"Загальна кількість викликів Sink: {calls}")
