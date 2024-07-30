from sys import stdin
from collections import deque

input = stdin.readline

def solution(n, m):
    graph = [([], []) for _ in range(n + 1)] # smaller, larger list
    for _ in range(m):
        s, l = map(int, input().split())
        graph[s][1].append(l)
        graph[l][0].append(s)
    
    cnt = 0
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        visited[i] = True
        queue = deque([i])
        
        standard_cnt = 0
        # smaller
        while queue:
            student = queue.popleft()
            for next_s in graph[student][0]:
                if not visited[next_s]:
                    visited[next_s] = True
                    queue.append(next_s)
                    standard_cnt += 1
        
        # larger
        visited = [False] * (n + 1)
        visited[i] = True
        queue = deque([i])
        while queue:
            student = queue.popleft()
            for next_s in graph[student][1]:
                if not visited[next_s]:
                    visited[next_s] = True
                    queue.append(next_s)
                    standard_cnt += 1
                    
        if standard_cnt == n - 1: # smaller + larger == n - 1
            cnt += 1
                
    print(cnt)
        
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)