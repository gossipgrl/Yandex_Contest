# Напишите программу, которая будет находить расстояния в неориентированном взвешенном графе с неотрицательными длинами ребер, 
# от указанной вершины до всех остальных. Программа должна работать быстро для больших разреженных графов.

# Формат ввода
# В первой строке входных данных задано число NUM — количество различных запусков алгоритма Дейкстры (на разных графах). 
# Далее следуют NUM блоков, каждый из которых имеет следующую структуру. Первая строка блока содержит два числа N и M, 
# разделенные пробелом — количество вершин и количество ребер графа. Далее следуют M строк, каждая из которых содержит 
# по три целых числа, разделенные пробелами. Первые два из них в пределах от 0 до N–1 каждое и обозначают концы соответствующего 
# ребра, третье — в пределах от 0 до 20000 и обозначает длину этого ребра. Далее, в последней строке блока, записанное 
# единственное число от 0 до N–1 — вершина, расстояния от которой надо искать. Количество различных графов в одном 
# тесте NUM не превышает 5. Количество вершин не превышает 60000, рёбер — 200000.

# Формат вывода
# Выведите на стандартный выход (экран) NUM строк, в каждой из которых по Ni чисел, разделенных пробелами — расстояния 
# от указанной начальной вершины взвешенного неориентированного графа до его 0-й, 1-й, 2-й и т. д. вершин 
# (допускается лишний пробел после последнего числа). Если некоторая вершина недостижима от указанной начальной, 
# вместо расстояния выводите число 2009000999 (гарантировано, что все реальные расстояния меньше).

import heapq
import sys

def custom_dijkstra(graph, start, n):
    INF = 2009000999
    distance = [INF] * n
    distance[start] = 0
    heap = [(0, start)]

    visited = [False] * n

    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True

        for neighbor, weight in graph[node]:
            if visited[neighbor]:
                continue
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distance

def process_custom_graph_input():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    start = int(sys.stdin.readline())
    return custom_dijkstra(graph, start, n)


sys.stdin = open('input.txt', 'r')
num = int(sys.stdin.readline())
output = []
for _ in range(num):
    distances = process_custom_graph_input()
    output.append(' '.join(map(str, distances)) + '\n')

sys.stdout.write(''.join(output))