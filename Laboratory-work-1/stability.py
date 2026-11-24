def sub(num):
    return str(num).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))


def show(arr):
    return "[" + ", ".join(f"{v}{sub(p)}" for v, p in arr) + "]"


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"  i={i}: {show(arr)}")
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"  i={i}: {show(arr)}")
    return arr


def check(name, result, value):
    order = [p for v, p in result if v == value]
    print(f"{name}: {show(result)}")
    print(f"Порядок елементів {value}: {order}")
    if order == sorted(order):
        print("Порядок рівних елементів збережено")
    else:
        print("Порядок рівних елементів змінився: сортування нестійке")


# Послідовність варіанту 7, у якій 67 замінено на 68, щоб були рівні ключі.
# Кожен елемент - пара (ключ, початковий індекс)
values = [41, 68, 68, 10, 7, 69, 95, 43, 98]
data = [(v, p) for p, v in enumerate(values)]

print("Початковий масив:", show(data))
print("Сортування вибором:")
check("Результат", selection_sort(data.copy()), 68)
print("Сортування вставками:")
check("Результат", insertion_sort(data.copy()), 68)
