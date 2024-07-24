from sys import stdin

input = stdin.readline

def solution(n, d):
    # Use heapq
    # from heapq import heappush, heappop
    # shortcuts_graph = [[(1, i + 1)] if i != d else [] for i in range(d + 1)]
    # for _ in range(n):
    #     s, e, distance = map(int, input().split())
    #     if s < d and e <= d:
    #         shortcuts_graph[s].append((distance, e))
    # distances = [10_001 for _ in range(d + 1)]
    # distances[0] = 0
    # Q = [(0, 0)]
    # while Q:
    #     distance, pos = heappop(Q)
        
    #     if distance > distances[pos]:
    #         continue
    
    #     for n_d, n_pos in shortcuts_graph[pos]:
    #         if distances[n_pos] > distances[pos] + n_d:
    #             distances[n_pos] = distances[pos] + n_d
    #             heappush(Q, (distances[n_pos], n_pos))
    # print(distances[-1])
    
    # Use just table, retrieve all shortcut
    shortcuts = [[] for _ in range(d + 1)]
    dp = [i for i in range(d + 1)]
    dp[0] = 0
    for _ in range(n):
        s, e, distance = map(int, input().split())
        if s < d and e <= d:
            shortcuts[s].append((e, distance))
    
    for i in range(d + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        for e, distance in shortcuts[i]:
            dp[e] = min(dp[e], dp[i] + distance)
            
    print(dp[-1])
if __name__=="__main__":
    N, D = map(int, input().split())
    solution(N, D)
