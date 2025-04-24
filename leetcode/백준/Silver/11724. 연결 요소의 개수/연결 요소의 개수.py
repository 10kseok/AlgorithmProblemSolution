import sys

sys.setrecursionlimit(10 ** 6)
    
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start, subset):
    visited[start] = True
    subset.add(start)
    for next in graph[start]:
        if not visited[next]:
            dfs(next, subset)
    return subset

for i in range(1, N + 1):
    if not visited[i] and len(dfs(i, set())) > 0:
        count += 1

print(count)