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
        if distance[cur_city] != INF and K <= distance[cur_city]: continue
        for adj in graph[cur_city]:
            if not visited[adj]:
                visited[adj] = True
                distance[adj] = distance[cur_city] + 1
                queue.append(adj)

shortest_K = map(str, filter(lambda x: distance[x] == K, range(N + 1)))
bfs(X)
print("\n".join(shortest_K) or -1)