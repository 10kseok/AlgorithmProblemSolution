import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

OUTSIDE, INSIDE, PADDING = '0', '1', '0'
def solution():
    N = int(input())
    place = PADDING + input()
    graph = [[] for _ in range(N + 1)]
    total_cnt = 0
    
    for _ in range(N - 1):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
        if (place[start] == INSIDE and place[end] == INSIDE): total_cnt += 2
    
    def dfs(node, visited, inside_cnt):
        visited[node] = True
        for next_node in graph[node]:
            if visited[next_node]: continue
            if place[next_node] == INSIDE:
                inside_cnt += 1
                continue
            if place[next_node] == OUTSIDE:
                inside_cnt = dfs(next_node, visited, inside_cnt)
        return inside_cnt

    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i] and place[i] == OUTSIDE:
            inside_cnt = dfs(i, visited, 0)
            total_cnt += inside_cnt * (inside_cnt - 1)
    
    print(total_cnt)
    
if __name__=="__main__":
    solution()