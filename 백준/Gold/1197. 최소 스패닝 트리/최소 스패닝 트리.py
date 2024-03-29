import heapq
import sys

V, E = map(int, sys.stdin.readline().split())

# Cruskal's Algorithm
# edges = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x:x[-1])
# parent = [i for i in range(0, V + 1)]
# cur_edge = 0

# def find(vertex):
#     if parent[vertex] != vertex:
#         parent[vertex] = find(parent[vertex])
#     return parent[vertex]

# def union(v1, v2):
#     small = find(v1)
#     large = find(v2)
#     # 작은 값을 부모 노드
#     parent[max(small, large)] = min(small, large)

# def cruskal(edge_idx):
#     global cur_edge
#     start_vertex = edges[edge_idx][0]
#     target_vertex = edges[edge_idx][1]
#     if find(start_vertex) != find(target_vertex):
#         union(start_vertex, target_vertex)
#         cur_edge += 1
#         return edges[edge_idx][-1]
#     return 0

# weights = [cruskal(i) for i in range(0, len(edges)) if cur_edge <= V - 1]
# print(sum(weights))

# prim's Algorithm
graph = [[] for _ in range(0, V + 1)]
visited = [False] * (V + 1)

for i in range(E):
    start, target, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, target))
    graph[target].append((weight, start))

visited[1] = True
priorityQ = graph[1]
heapq.heapify(priorityQ)
weights = 0

while priorityQ:
    weight, target = heapq.heappop(priorityQ)
    if not visited[target]:
        visited[target] = True
        weights += weight
        for edge in graph[target]:
            if not visited[edge[1]]:
                heapq.heappush(priorityQ, edge)

print(weights)