import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(i, visited):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            parent[j] = i
            dfs(j, visited)

dfs(1, [False for _ in range(N + 1)])

print(*parent[2:], sep="\n")

