import heapq
import sys

input = sys.stdin.readline
    
def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, cow = map(int, input().split())
        graph[start].append((cow, end))
        graph[end].append((cow, start))
    
    Q = [(0, 1)]
    dp = [1e9] * (N + 1)
    dp[1] = 0
    while Q:
        cow, node = heapq.heappop(Q)
        for nc, nn in graph[node]:
            if dp[nn] > cow + nc:
                dp[nn] = cow + nc
                heapq.heappush(Q, (dp[nn], nn))
    print(dp[N])
if __name__=="__main__":
    solution() 