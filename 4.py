# Пусть расстояние от вершины u до вершины v — это минимальное количество рёбер в пути между u и v ; так, расстояние между 
# u и u — 0, а расстояние между любыми двумя различными соседними вершинами — 1.Волновым обходом графа из вершины 
# v назовём последовательность вершин u1,u2,…,ur такую, что:
# u1=v,
# Каждая вершина графа, достижимая из v, встречается в ней хотя бы один раз, и
# Каждая следующая вершина последовательности удалена от вершины v не меньше, чем предыдущая.
# Задан связный неориентированный граф и его вершина v. Выведите любой волновой обход этого графа

# Формат ввода
# В первой строке входного файла заданы числа N, M и v через пробел — количество вершин и рёбер в графе и начальная вершина обхода (
# 1≤N≤100, 0≤M≤10000, 1≤v≤N). Следующие M строк содержат по два числа ui и vi через пробел (1≤ui,vi≤N); каждая такая строка означает, 
# что в графе существует ребро между вершинами ui и vi.


# Формат вывода
# В первой строке входного файла выведите число r — количество вершин в найденном волновом обходе (1≤r≤10000; гарантируется, что обход, 
# удовлетворяющий этим ограничениям, существует). Во второй строке выведите сами числа 
# u1,u2,…,ur через пробел.

n, m, v = map(int, input().split())
graf = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graf[a].append(b)
    graf[b].append(a)

visited = set()
queue = [v]
res = []

while queue:
    cur = queue.pop(0)
    if cur not in visited:
        visited.add(cur)
        res.append(cur)
        queue.extend(graf[cur])

print(len(res))
print(*res)