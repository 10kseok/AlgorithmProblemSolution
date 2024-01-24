from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
DEFAULT_DIRECTION, UP, DOWN = 0, 1, -1

def bfs(start, graph, direction):
    queue = deque([start])
    direction[start] = UP
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if direction[next] == DEFAULT_DIRECTION:
                direction[next] = direction[node] * -1
                queue.append(next)
            elif direction[next] == direction[node]:
                return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    directions = [DEFAULT_DIRECTION] * (V + 1)
    result = "YES"
    for i in range(1, V + 1):
        if directions[i] == DEFAULT_DIRECTION and \
            not bfs(i, graph, directions):
            result = "NO"  
            break
    print(result)