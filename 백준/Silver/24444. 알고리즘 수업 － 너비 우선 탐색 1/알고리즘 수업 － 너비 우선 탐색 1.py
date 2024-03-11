from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
                
    orders = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    
    queue = deque([R])
    visited[R] = True
    order = 1
    orders[R] = order
    while queue:
        node = queue.popleft()
        graph[node].sort()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                order += 1
                orders[v] = order
    
    print(*orders[1:], sep="\n")

if __name__=="__main__":
    solution() 