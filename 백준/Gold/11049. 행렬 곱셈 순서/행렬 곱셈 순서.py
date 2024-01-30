import sys
input = sys.stdin.readline
INF = 2 ** 31

def minimum(M, A, i, j):
    min_value = INF
    for k in range(i, j):
        value = M[i][k] + M[k+1][j] + A[i-1] * A[k] * A[j]
        if value < min_value:
            min_value = value
    return min_value

def solution():
    N = int(input())
    A = []
    r, c = map(int, input().split())
    A.append(r)
    A.append(c)
    for i in range(1, N):
        _, c = map(int, input().split())
        A.append(c)
    N = len(A) - 1
    M = [[0] * (N + 1) for _ in range(N + 1)]

    for diagonal in range(1, N):
        for i in range(1, N - diagonal + 1):
            j = i + diagonal
            M[i][j] = minimum(M, A, i, j)

    print(M[1][N])

solution()