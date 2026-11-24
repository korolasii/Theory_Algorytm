def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Зовнішній цикл: n-1 проходів
    for i in range(n - 1):
        print(f"Ітерація {i}:")
        print(f"  Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print(f"  Шукаємо мінімальний елемент у частині: {arr[i:]}")

        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1

        # Внутрішній цикл: пошук мінімуму в решті списку
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1

        print(f"  Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")

        # Обмін, якщо мінімум не на своєму місці
        comparisons += 1
        if min_index != i:
            print(f"  Обмін arr[{i}] ({arr[i]}) і "
                  f"arr[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        else:
            print("  Обмін не потрібен, елемент на своєму місці")

        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)

    return arr, comparisons, assignments


my_list = [41, 68, 67, 10, 7, 69, 95, 43, 98]
print("Початковий масив:", my_list)
print("-" * 30)
sorted_list, comps, assigns = selection_sort(my_list.copy())
print("Сортування завершено.")
print("Фінальний відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоєнь: {assigns}")
