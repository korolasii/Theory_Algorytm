def sub(num):
    return str(num).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))


def show(arr):
    return "[" + ", ".join(f"{v}{sub(p)}" for v, p in arr) + "]"


def sink(arr, i, n):
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n and arr[j + 1][0] > arr[j][0]:
            j += 1
        if arr[k][0] >= arr[j][0]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def heapsort_pairs(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n)
    print("Масив після побудови купи:", show(arr))
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
        print(f"Обмін кореня з a[{i}], масив: {show(arr)}")
    return arr


# Послідовність варіанту 7, у якій 67 замінено на 68, щоб були рівні ключі.
# Кожен елемент - пара (ключ, початковий індекс)
values = [41, 68, 68, 10, 7, 69, 95, 43, 98]
data = [(v, p) for p, v in enumerate(values)]
print("Початковий масив:", show(data))
result = heapsort_pairs(data.copy())
print("Відсортований масив:", show(result))

order = [p for v, p in result if v == 68]
print(f"Порядок елементів 68 після сортування: {order}")
if order == sorted(order):
    print("Порядок рівних елементів збережено")
else:
    print("Порядок рівних елементів змінився: сортування нестійке")
