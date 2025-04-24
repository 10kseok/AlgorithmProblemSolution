import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def count_earthworm(i, j, cabbage_field):
    if 0 > i or i >= N or 0 > j or j >= M or cabbage_field[i][j] == 0: return
    cabbage_field[i][j] = 0
    count_earthworm(i    , j + 1, cabbage_field)
    count_earthworm(i    , j - 1, cabbage_field)
    count_earthworm(i + 1, j    , cabbage_field)
    count_earthworm(i - 1, j    , cabbage_field)

def solution():
    global M, N
    T = int(input())
    result = []
    for _ in range(T):    
        M, N, K = map(int, input().split())
        cabbage_field = [[0] * M for _ in range(N)]
        for _ in range(K):
            j, i = map(int, input().split())
            cabbage_field[i][j] = 1
            
        earthworm_cnt = 0
        for i in range(N):
            for j in range(M):
                if cabbage_field[i][j] == 1:
                    count_earthworm(i, j, cabbage_field)
                    earthworm_cnt += 1
        result.append(earthworm_cnt)
    print(*result, sep="\n")
            
if __name__=="__main__":
    solution()
    