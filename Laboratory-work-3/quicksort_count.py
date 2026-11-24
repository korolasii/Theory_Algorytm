def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    i = l - 1
    j = r + 1
    assignments += 3

    while True:
        i += 1
        assignments += 1
        comparisons += 1
        while a[i] < pivot:
            i += 1
            assignments += 1
            comparisons += 1

        j -= 1
        assignments += 1
        comparisons += 1
        while a[j] > pivot:
            j -= 1
            assignments += 1
            comparisons += 1

        if i >= j:
            return j, comparisons, assignments

        a[i], a[j] = a[j], a[i]
        assignments += 3


def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        q, c1, a1 = partition(a, l, r)
        assignments += 1
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        comparisons += c1 + c2 + c3
        assignments += a1 + a2 + a3
        recursive_calls += r2 + r3

    return comparisons, assignments, recursive_calls


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
comps, assigns, calls = quicksort(my_list, 0, len(my_list) - 1)
print("Відсортований масив:", my_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
print(f"Загальна кількість викликів: {calls}")
