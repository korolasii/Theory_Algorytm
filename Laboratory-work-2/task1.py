def merge_iterative(a, left, mid, right):
    comparisons = 0
    assignments = 0
    it1 = 0
    it2 = 0
    result = [0] * (right - left)
    assignments += 3

    print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({a[left:mid]}) "
          f"і a[{mid}:{right}] ({a[mid:right]})")

    # Зливаємо елементи, порівнюючи їх
    while left + it1 < mid and mid + it2 < right:
        comparisons += 1
        print(f"  Порівняння: {a[left + it1]} <= {a[mid + it2]}")
        if a[left + it1] <= a[mid + it2]:
            result[it1 + it2] = a[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = a[mid + it2]
            it2 += 1
        assignments += 2

    # Копіюємо елементи, що залишилися в першому підмасиві
    while left + it1 < mid:
        result[it1 + it2] = a[left + it1]
        it1 += 1
        assignments += 2

    # Копіюємо елементи, що залишилися в другому підмасиві
    while mid + it2 < right:
        result[it1 + it2] = a[mid + it2]
        it2 += 1
        assignments += 2

    # Повертаємо злиті елементи в масив a
    for i in range(it1 + it2):
        a[left + i] = result[i]
        assignments += 1

    print(f"Масив після об'єднання: {a}")
    print("-" * 30)
    return comparisons, assignments


def merge_sort_iterative(a):
    comparisons = 0
    assignments = 0
    n = len(a)
    i = 1
    assignments += 2

    while i < n:
        j = 0
        assignments += 1
        while j < n - i:
            c, s = merge_iterative(a, j, j + i, min(j + 2 * i, n))
            comparisons += c
            assignments += s
            j += 2 * i
            assignments += 1
        i *= 2
        assignments += 1

    return a, comparisons, assignments


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
print("-" * 30)
sorted_list, comps, assigns = merge_sort_iterative(my_list.copy())
print("Відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
