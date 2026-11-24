INF = float("inf")
V = 8
# Граф варіанту 7; вагу ребра (2, 5), пропущену в завданні, прийнято рівною 7
EDGES = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1), (1, 7, 1), (2, 4, 3),
    (2, 5, 7), (3, 5, 2), (3, 6, 4), (3, 7, 4), (4, 5, 9),
    (4, 7, 9), (4, 8, 4), (5, 6, 3), (6, 8, 1), (7, 8, 6),
]


def build_lists(n, edges):
    lists = {v: [] for v in range(1, n + 1)}
    for u, v, w in edges:
        lists[u].append((v, w))
        lists[v].append((u, w))
    for v in lists:
        lists[v].sort()
    return lists


def show(x):
    return "∞" if x == INF else str(x)


def extract_min(pq):
    # Вершина з найменшою відстанню (за рівних - з меншим номером)
    u = min(pq, key=lambda v: (pq[v], v))
    del pq[u]
    return u


def dijkstra(n, lists, s):
    pred = {}
    dist = {}
    pq = {}  # черга з пріоритетом: вершина -> поточна відстань
    checks = 0
    updates = 0

    for v in range(1, n + 1):
        pred[v] = -1
        dist[v] = 0 if v == s else INF
        pq[v] = dist[v]

    step = 0
    while pq:
        u = extract_min(pq)
        step += 1
        print(f"{step}. u = {u}, dist[{u}] = {dist[u]}")
        for v, w in lists[u]:
            if v not in pq:
                continue  # вершину вже оброблено
            checks += 1
            new = dist[u] + w
            if dist[v] > new:
                print(f"   v = {v}: {show(dist[v])} > {dist[u]} + {w} = {new} "
                      "-> оновлюємо")
                dist[v] = new
                pred[v] = u
                pq[v] = new
                updates += 1
            else:
                print(f"   v = {v}: {show(dist[v])} > {dist[u]} + {w} = {new} "
                      "-> ні")
        print("   dist =", [show(dist[v]) for v in range(1, n + 1)])
        print("   pred =", [pred[v] for v in range(1, n + 1)])

    return pred, dist, checks, updates


def path_to(pred, v):
    path = [v]
    while pred[v] != -1:
        v = pred[v]
        path.append(v)
    return path[::-1]


pred, dist, checks, updates = dijkstra(V, build_lists(V, EDGES), 1)
print("Найкоротші шляхи з вершини 1:")
for v in range(2, V + 1):
    path = " -> ".join(str(x) for x in path_to(pred, v))
    print(f"{v}: {path}, довжина {dist[v]}")
print("Перевірок умови релаксації:", checks)
print("Оновлень dist:", updates)
