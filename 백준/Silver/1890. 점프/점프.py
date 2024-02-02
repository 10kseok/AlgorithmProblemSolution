import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    BOARD = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            jump = BOARD[i][j]
            if jump == 0: continue

            under, right = i + jump, j + jump
            if right < N:
                dp[i][right] += dp[i][j] 
            if under < N:
                dp[under][j] += dp[i][j] 

    print(dp[N - 1][N - 1])

if __name__=="__main__":
    solution()
