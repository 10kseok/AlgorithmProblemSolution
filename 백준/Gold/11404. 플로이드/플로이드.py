import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
INF = 100_000 * n + 1
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    i, j, c = map(int, input().split())
    if graph[i - 1][j - 1] > c:
        graph[i - 1][j - 1] = c
    # graph[i - 1][j - 1] = min(graph[i - 1][j - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for g in graph:
    print(*[x if x != INF else 0 for x in g])

