import sys
from heapq import heappop, heappush
input = sys.stdin.readline
DIST, DEST, MAX = 0, 1, 200000000

def dijk(start):
    distance_table = [MAX] * (N + 1)
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
                
    return distance_table
        
def solution():
    global graph, N
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, distance = map(int, input().split())
        graph[a].append((distance, b))
        graph[b].append((distance, a))
    stopover_v1, stopover_v2 = map(int, input().split())

    start = dijk(1) # 1로 시작한 최단 경로
    route1 = dijk(stopover_v1) # 경유지 v1으로 시작한 최단 경로
    route2 = dijk(stopover_v2) # 경유지 v2로 시작한 최단 경로
    
    v1_first_route = start[stopover_v1] + route1[stopover_v2] + route2[N]
    v2_first_route = start[stopover_v2] + route2[stopover_v1] + route1[N]
    
    answer = min(v1_first_route, v2_first_route)
    print(answer if answer < MAX else -1)
    
if __name__=="__main__":
    solution() 

