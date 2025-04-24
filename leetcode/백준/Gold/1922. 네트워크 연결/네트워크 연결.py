from sys import stdin

input = stdin.readline

def solution(n, m):
    parents = [i for i in range(n + 1)]
    graph = [list(map(int, input().split())) for _ in range(m)]
    graph.sort(key=lambda x: x[2], reverse=True)
    
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(parent_a, parent_b):
        parents[max(parent_a, parent_b)] = min(parent_a, parent_b)
    
    # Use Kruskal algorithm
    total_cost, edges = 0, 0
    while edges < n - 1:
        u, v, cost = graph.pop()
        if u == v:
            continue
        parent_u, parent_v = find(u), find(v)
        if parent_u != parent_v:
            union(parent_u, parent_v)
            total_cost += cost
            edges += 1
            
    print(total_cost)
            
if __name__=="__main__":
    N = int(input())
    M = int(input())
    solution(N, M)
