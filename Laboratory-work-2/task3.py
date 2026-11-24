def partition(a, l, r, pad):
    comparisons = 0
    assignments = 0

    pivot = a[l]
    i = l - 1
    j = r + 1
    assignments += 3
    print(f"{pad}  Вибираємо опорний елемент (pivot): {pivot}")

    while True:
        # Шукаємо зліва елемент, не менший за опорний
        i += 1
        assignments += 1
        comparisons += 1
        while a[i] < pivot:
            i += 1
            assignments += 1
            comparisons += 1

        # Шукаємо справа елемент, не більший за опорний
        j -= 1
        assignments += 1
        comparisons += 1
        while a[j] > pivot:
            j -= 1
            assignments += 1
            comparisons += 1

        if i >= j:
            print(f"{pad}  i = {i}, j = {j}. Індекси перетнулися. "
                  f"Повертаємо j = {j}")
            return j, comparisons, assignments

        left_value = a[i]
        right_value = a[j]
        a[i], a[j] = a[j], a[i]
        assignments += 3
        print(f"{pad}  i = {i}, j = {j}. Обмінюємо a[{i}] ({left_value}) "
              f"і a[{j}] ({right_value}). Підмасив: {a[l:r + 1]}")


def quicksort(a, l, r, depth=0):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    pad = "  " * depth
    print(f"{pad}Quicksort виклик: l = {l}, r = {r}, "
          f"підмасив = {a[l:r + 1]}")

    if l < r:
        q, c1, a1 = partition(a, l, r, pad)
        assignments += 1
        c2, a2, r2 = quicksort(a, l, q, depth + 1)
        c3, a3, r3 = quicksort(a, q + 1, r, depth + 1)
        comparisons += c1 + c2 + c3
        assignments += a1 + a2 + a3
        recursive_calls += r2 + r3
        print(f"{pad}Після Quicksort для l = {l}, r = {r}: {a[l:r + 1]}")

    return comparisons, assignments, recursive_calls


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
comps, assigns, calls = quicksort(my_list, 0, len(my_list) - 1)
print("Відсортований масив:", my_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
print(f"Загальна кількість викликів: {calls}")
