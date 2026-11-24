def merge(left, right, pad):
    comparisons = 0
    assignments = 0
    result = []
    i = 0
    j = 0
    assignments += 3

    print(f"{pad}Зливаємо {left} та {right}")

    # Зливаємо елементи, порівнюючи їх
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            print(f"{pad}  Порівняння: {left[i]} <= {right[j]} -> True. "
                  f"Додаємо {left[i]}")
            result.append(left[i])
            i += 1
        else:
            print(f"{pad}  Порівняння: {left[i]} <= {right[j]} -> False. "
                  f"Додаємо {right[j]}")
            result.append(right[j])
            j += 1
        assignments += 2

    # Додаємо елементи, що залишилися
    while i < len(left):
        print(f"{pad}  Додаємо залишок з лівого масиву: {left[i]}")
        result.append(left[i])
        i += 1
        assignments += 2
    while j < len(right):
        print(f"{pad}  Додаємо залишок з правого масиву: {right[j]}")
        result.append(right[j])
        j += 1
        assignments += 2

    print(f"{pad}Злиття завершено. Результат: {result}")
    return result, comparisons, assignments


def merge_sort_recursive(arr, depth=0):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    pad = "  " * depth
    print(f"{pad}Розділяємо масив: {arr}")

    n = len(arr)
    assignments += 1
    if n <= 1:
        return arr, comparisons, assignments, recursive_calls

    mid = n // 2
    assignments += 1
    # Копіювання половин: одне присвоювання на елемент
    left_half = arr[:mid]
    right_half = arr[mid:]
    assignments += n

    sorted_left, c1, a1, r1 = merge_sort_recursive(left_half, depth + 1)
    sorted_right, c2, a2, r2 = merge_sort_recursive(right_half, depth + 1)
    result, c3, a3 = merge(sorted_left, sorted_right, pad)

    comparisons += c1 + c2 + c3
    assignments += a1 + a2 + a3
    recursive_calls += r1 + r2
    return result, comparisons, assignments, recursive_calls


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
sorted_list, comps, assigns, calls = merge_sort_recursive(my_list.copy())
print("Відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
print(f"Загальна кількість викликів: {calls}")
