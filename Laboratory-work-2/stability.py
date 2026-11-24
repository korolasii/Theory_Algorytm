def sub(num):
    return str(num).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))


def show(arr):
    return "[" + ", ".join(f"{v}{sub(p)}" for v, p in arr) + "]"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    print(f"  Злиття: {show(result)}")
    return result


def partition(a, l, r):
    pivot = a[l][0]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while a[i][0] < pivot:
            i += 1
        j -= 1
        while a[j][0] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
        print(f"  Обмін a[{i}] і a[{j}]: {show(a)}")


def quicksort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quicksort(a, l, q)
        quicksort(a, q + 1, r)
    return a


def check(result, value):
    order = [p for v, p in result if v == value]
    print(f"Результат: {show(result)}")
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
print("Сортування злиттям:")
check(merge_sort(data.copy()), 68)
print("Швидке сортування:")
check(quicksort(data.copy(), 0, len(data) - 1), 68)
