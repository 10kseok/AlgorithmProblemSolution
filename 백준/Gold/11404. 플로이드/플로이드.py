import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
INF = 100_000 * n + 1
graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j: graph[i][j] = INF

for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for g in graph:
    print(*g)