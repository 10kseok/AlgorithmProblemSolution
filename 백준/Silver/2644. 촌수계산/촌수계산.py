import sys
input = sys.stdin.readline
result = [-1]

def dfs(start, count, visited):
    if result[0] != -1: return
    if start == end:
        result[0] = count
        return
    
    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node, count + 1, visited)
    
def solution():
    global end, graph
    n = int(input())
    start, end = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    visited = [False] * (n + 1)
    visited[start] = True
    dfs(start, 0, visited)
    print(result[0])

        
if __name__=="__main__":
    solution() 


