from collections import deque

def solution(n, edge):
    answer = 0
    distance_table = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        src, dst = e
        graph[src].append(dst)
        graph[dst].append(src)
    
    search_Q = deque([])
    search_Q.append((1, 0))
    distance_table[1] = -1 
    while search_Q:
        node, distance = search_Q.popleft()
        
        for next_n in graph[node]:
            if distance_table[next_n] != 0:
                continue
            distance_table[next_n] = distance + 1
            search_Q.append((next_n, distance + 1))
    
    longest_d = max(distance_table)
    answer = len([d for d in distance_table if d == longest_d])
    return answer