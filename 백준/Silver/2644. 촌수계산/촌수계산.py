import sys
input = sys.stdin.readline

def solution():
    global result
    n = int(input())
    start, end = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    result = -1
    visited = [False] * (n + 1)
    visited[start] = True
    def dfs(start, count):
        global result
        if result != -1: return
        if start == end:
            result = count
            return
        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                dfs(node, count + 1)
    dfs(start, 0)
    
    print(result)

        
if __name__=="__main__":
    solution() 


