from sys import stdin
from heapq import heapify, heappop
input = stdin.readline

def solution(n):
    planets = [list(map(int, input().split())) + [i] for i in range(n)]
    graph = []
    for dim in range(3): # x : 0, y : 1, z : 2, idx : 3
        sorted_pos_by_dimension = sorted(planets, key=lambda x:x[dim])
        for i in range(1, n):
            prev, cur = sorted_pos_by_dimension[i - 1][3], sorted_pos_by_dimension[i][3]
            graph.append((abs(sorted_pos_by_dimension[i][dim] - sorted_pos_by_dimension[i - 1][dim]), prev, cur))
    
    parents = list(range(n))
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
    # use Heap
    # heapify(graph)
    # while edges < n - 1:
    #     cost, u, v = heappop(graph)
    #     if union(u, v):
    #         total_cost += cost
    #         edges += 1  
    
    # use Sort
    graph.sort()
    for i in range(len(graph)):
        cost, u, v = graph[i]
        if union(u, v):
            total_cost += cost
            edges += 1        
            if edges == n - 1:
                break
    print(total_cost)

if __name__=="__main__":
    N = int(input())
    solution(N)