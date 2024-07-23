from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def solution(v, e, k):    
    MAX_W = 300_000 * 10 + 1
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    dp = [MAX_W] * (v + 1)
    dp[k] = 0
    
    Q = [(0, k)]
    while Q:
        w, cur = heappop(Q)
        # next weight, next vertex
        for n_w, n_v in graph[cur]:
            if dp[n_v] > w + n_w:
                dp[n_v] = w + n_w
                heappush(Q, (dp[n_v], n_v))         
    print("\n".join(map(lambda x: str(x) if x < MAX_W else 'INF', dp[1:])))
if __name__=="__main__":
    V, E = map(int, input().split())
    K = int(input())
    solution(V, E, K)

