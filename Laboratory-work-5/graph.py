V = 8
# Граф варіанту 7; вагу ребра (2, 5), пропущену в завданні, прийнято рівною 7
EDGES = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1), (1, 7, 1), (2, 4, 3),
    (2, 5, 7), (3, 5, 2), (3, 6, 4), (3, 7, 4), (4, 5, 9),
    (4, 7, 9), (4, 8, 4), (5, 6, 3), (6, 8, 1), (7, 8, 6),
]


def build_matrix(n, edges):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, w in edges:
        matrix[u][v] = w
        matrix[v][u] = w
    return matrix


def build_lists(n, edges):
    lists = {v: [] for v in range(1, n + 1)}
    for u, v, w in edges:
        lists[u].append((v, w))
        lists[v].append((u, w))
    for v in lists:
        lists[v].sort()
    return lists


matrix = build_matrix(V, EDGES)
lists = build_lists(V, EDGES)

print("Матриця суміжності:")
print("   " + " ".join(str(v) for v in range(1, V + 1)))
for u in range(1, V + 1):
    print(f"{u}: " + " ".join(str(matrix[u][v]) for v in range(1, V + 1)))

print("Списки суміжності (вершина, вага):")
for u in range(1, V + 1):
    print(f"{u}: " + " -> ".join(f"({v}, {w})" for v, w in lists[u]))
