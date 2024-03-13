# Дан ориентированный граф, в котором могут быть кратные ребра и петли. Каждое ребро имеет вес, выражающийся целым числом
# (возможно, отрицательным). Гарантируется, что циклы отрицательного веса отсутствуют. Требуется посчитать длины кратчайших 
# путей от вершины номер 1 до всех остальных вершин.

# Формат ввода
# Программа получает сначала число N (1 <= N <= 100) – количество вершин графа и число M (0 <= M <= 10000) – 
# количество ребер. В следующих строках идет M троек чисел, описывающих ребра: начало ребра, конец ребра и вес 
# (вес – целое число от -100 до 100).

# Формат вывода
# Программа должна вывести N чисел – расстояния от вершины номер 1 до всех вершин графа. Если пути до соответствующей 
# вершины не существует, вместо длины пути выведите число 30000.

n, m = map(int, input().split())

edges = [] 
for i in range(m):
    u, v, dist = map(int, input().split())
    edges.append([u - 1, v - 1, dist])

visited = [False for _ in range(n)]
distance = [30000 for _ in range(n)]
distance[0] = 0


for i in range(n - 1):
    for u, v, dist in edges:
        if distance[u] != 30000 and distance[v] > distance[u] + dist:
            distance[v] = distance[u] + dist

print(" ".join(map(str, distance)))