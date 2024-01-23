from collections import deque
import sys
    
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = 1_000_001
distance = [INF for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)

def bfs(start):
    queue = deque([start])
    distance[start] = 0
    visited[start] = True

    while queue:
        cur_city = queue.popleft()
        if distance[cur_city] != float('inf') and K < distance[cur_city]: continue
        for adj in graph[cur_city]:
            if not visited[adj]:
                visited[adj] = True
                distance[adj] = min(distance[cur_city] + 1, distance[adj])
                queue.append(adj)

bfs(X)
print("\n".join(map(str, sorted([idx for idx, d in enumerate(distance) if d == K]))) or -1)