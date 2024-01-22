from collections import deque
import sys

N, M, V = map(int, input().split())
# 가능하면 1, 불가능 0
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

def dfs(i, path, visited):
    visited[i] = True
    for idx, j in enumerate(graph[i]):
        if j == 0: continue
        if not visited[idx]:
            path.append(idx)
            dfs(idx, path, visited)

    return path

def print_bfs(i, visited):
    buffer_queue = deque([idx for idx, j in enumerate(graph[i]) if j == 1])
    visited[i] = True
    path = [i]
    while buffer_queue:
        next_vertex = buffer_queue.popleft()
        if not visited[next_vertex]:
            visited[next_vertex] = True
            path.append(next_vertex)
            for idx, v in enumerate(graph[next_vertex]):
                if v == 0: continue
                if not visited[idx]:
                    buffer_queue.append(idx)
    print(*path)

print(*dfs(V, [V], [False] * (N + 1)))
print_bfs(V, [False] * (N + 1) )