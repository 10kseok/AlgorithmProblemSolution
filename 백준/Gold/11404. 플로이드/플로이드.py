import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    m = int(input())

    INF = 1000000000
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        distance[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        if distance[a][b] > c:
            distance[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    for i in range(1, n + 1):
        print(*[x if x != INF else 0 for x in distance[i][1:]])


solution()
