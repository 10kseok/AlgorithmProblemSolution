import sys
input = sys.stdin.readline
from collections import deque

def dijkstra(N,M,E):
    costList = [[10**6 for _ in range(N+1)] for _ in range(M+1)]
    pq=deque()
    pq.append((0,0,1))
    while pq:
        distance, cost, node=pq.popleft()
        if costList[cost][node] >= distance:
            for v,c,d in E[node]:
                if cost+c <= M and costList[cost+c][v] > distance+d:
                    pq.append((distance+d,cost+c,v))
                    for j in range(cost+c, M+1):
                        if costList[j][v] > distance+d:
                            costList[j][v]=distance+d
                        else:
                            break
    return 'Poor KCM' if costList[M][N]==10**6 else costList[M][N]

def main():
    input()
    N, M, K = map(int, input().split())
    E = [[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int, input().split())
        E[u].append((v,c,d))
    for i in range(1,N+1):
        E[i].sort(key=lambda x:x[2])
    print(dijkstra(N,M,E))

main()