INF = float("inf")
V = 8
# Граф варіанту 7; вагу ребра (2, 5), пропущену в завданні, прийнято рівною 7
EDGES = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1), (1, 7, 1), (2, 4, 3),
    (2, 5, 7), (3, 5, 2), (3, 6, 4), (3, 7, 4), (4, 5, 9),
    (4, 7, 9), (4, 8, 4), (5, 6, 3), (6, 8, 1), (7, 8, 6),
]


def build_weights(n, edges):
    w = [[INF] * n for _ in range(n)]
    for i in range(n):
        w[i][i] = 0
    for u, v, weight in edges:
        w[u - 1][v - 1] = weight
        w[v - 1][u - 1] = weight
    return w


def print_matrix(title, d):
    print(title)
    for row in d:
        print(" ".join(f"{'∞' if x == INF else x:>3}" for x in row))


def floyd(w):
    n = len(w)
    d = [row[:] for row in w]
    comparisons = 0
    updates = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                comparisons += 1
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    updates += 1
        print_matrix(f"D({k + 1}):", d)
    return d, comparisons, updates


weights = build_weights(V, EDGES)
print_matrix("D(0) = W:", weights)
dist, comps, upds = floyd(weights)
print("Загальна кількість порівнянь:", comps)
print("Загальна кількість оновлень:", upds)
