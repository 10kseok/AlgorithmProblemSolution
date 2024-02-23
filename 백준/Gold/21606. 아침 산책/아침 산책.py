import sys
input = sys.stdin.readline

OUTSIDE, INSIDE, PADDING = '0', '1', '0'

def solution():
    N = int(input())
    place = PADDING + input()
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    global cnt
    cnt = 0
    def dfs(idx, visited, start_flag):
        global cnt
        if visited[idx]: return
        if start_flag == 0 and place[idx] == INSIDE:
            cnt += 1
            return
        
        visited[idx] = True
        for target in graph[idx]:
            if not visited[target]:
                dfs(target, visited, 0)
                
    for i in range(1, N + 1):
        if place[i] == OUTSIDE: continue
        dfs(i, [False] * (N + 1), 1)

    print(cnt)
    
if __name__=="__main__":
    solution()