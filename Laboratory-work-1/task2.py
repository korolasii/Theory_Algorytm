def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # i - індекс елемента, який потрібно вставити
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        print(f"Ітерація {i}:")
        print(f"  Елемент для вставки (key): {key}")
        print(f"  Відсортована частина: {arr[:i]}")

        # Зсуваємо вправо елементи, більші за key
        while j >= 0 and arr[j] > key:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key}. True. Зсуваємо {arr[j]} вправо.")
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        # Порівняння, на якому умова while стала хибною
        if j >= 0:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key}. False. Цикл завершено.")
        else:
            print("  Досягнуто початку масиву. Цикл завершено.")

        arr[j + 1] = key
        assignments += 1
        print(f"  Вставка {key} на позицію {j + 1}.")
        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)

    return arr, comparisons, assignments


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
print("-" * 30)
sorted_list, comps, assigns = insertion_sort(my_list.copy())
print("Сортування завершено.")
print("Фінальний відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоєнь: {assigns}")
