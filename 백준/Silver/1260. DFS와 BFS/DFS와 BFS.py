from collections import deque
import sys

# 각 자료구조별 특징
# 인접 행렬 -> 연결된 노드들을 찾아서 계산해줘야함 -> 행렬로 인한 공간 복잡도 상승
# 인접 리스트 -> 연결된 노드들을 번호순으로 계속 정렬해줘야함 -> 코드가 훨씬 적어짐.

N, M, V = map(int, input().split())
CONNECTED, NOT_CONNECTED = 1, 0
graph = [[NOT_CONNECTED] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = CONNECTED
    graph[v2][v1] = CONNECTED

def dfs(start, path, visited):
    visited[start] = True
    for target in range(1, N + 1):
        if graph[start][target] == CONNECTED and not visited[target]:
            path.append(target)
            dfs(target, path, visited)

    return path

def print_bfs(base, visited):
    traveral_queue = deque([vertex for vertex in range(1, N + 1) if graph[base][vertex] == CONNECTED])
    path = [base]
    visited[base] = True
    while traveral_queue:
        next_vertex = traveral_queue.popleft()
        if visited[next_vertex]: continue
        # 현재 경로 추가
        visited[next_vertex] = True
        path.append(next_vertex)
        # 인접 경로들 탐색 예정큐에 추가
        for target in range(1, N + 1):
            if graph[next_vertex][target] == CONNECTED and not visited[target]:
                traveral_queue.append(target)
    print(*path)

print(*dfs(V, [V], [False] * (N + 1)))
print_bfs(V, [False] * (N + 1))