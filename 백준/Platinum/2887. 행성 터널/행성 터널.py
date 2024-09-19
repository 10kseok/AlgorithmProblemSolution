from sys import stdin
from heapq import heapify, heappop
input = stdin.readline

def solution(n):
    planets = [list(map(int, input().split())) for _ in range(n)]
    x_list = { idx : x for idx, (x, _, _) in enumerate(planets) }
    y_list = { idx : y for idx, (_, y, _) in enumerate(planets) }
    z_list = { idx : z for idx, (_, _, z) in enumerate(planets) }
    position_list = [x_list, y_list, z_list]
    graph = []

    for pos_list in position_list:
        sorted_pos = sorted(pos_list.items(), key=lambda x:x[1])
        for i in range(1, n):
            prev, cur = sorted_pos[i - 1][0], sorted_pos[i][0]
            graph.append((abs(pos_list[cur] - pos_list[prev]), prev, cur))
    
    parents = [i for i in range(n)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        a, b = find(x), find(y)
        if a == b:
            return False
        parents[max(a, b)] = min(a, b)
        return True
    
    edges, total_cost = 0, 0
    heapify(graph)
    while edges < n - 1:
        cost, u, v = heappop(graph)
        if union(u, v):
            total_cost += cost
            edges += 1        
    
    print(total_cost)

if __name__=="__main__":
    N = int(input())
    solution(N)