import sys
from heapq import heappop, heappush
input = sys.stdin.readline
DIST, DEST = 0, 1

def dijk(start, target):
    distance_table = [float('inf')] * (N + 1)
    distance_table[start] = 0
    route_Q = [(0, start)]
    while route_Q:
        cur_dist, cur_node = heappop(route_Q)
        if cur_dist > distance_table[cur_node]:
            continue
        
        for next_n in graph[cur_node]:
            n_dist, n_dest = next_n[DIST], next_n[DEST]
            if distance_table[n_dest] > n_dist + distance_table[cur_node]:
                distance_table[n_dest] = n_dist + distance_table[cur_node]
                heappush(route_Q, next_n)
                
    return distance_table[target]
        
def solution():
    global graph, N
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, distance = map(int, input().split())
        graph[a].append((distance, b))
        graph[b].append((distance, a))
    stopover1, stopover2 = map(int, input().split())

    distance_table = [float('inf')] * (N + 1)
    distance_table[1] = 0
    case1 = dijk(1, stopover1) + dijk(stopover1, stopover2) + dijk(stopover2, N)
    case2 = dijk(1, stopover2) + dijk(stopover2, stopover1) + dijk(stopover1, N)
    answer = min(case1, case2)
    print(answer if answer != float('inf') else -1)
    
if __name__=="__main__":
    solution() 
