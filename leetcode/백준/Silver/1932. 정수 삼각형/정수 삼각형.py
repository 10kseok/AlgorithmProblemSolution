import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    triangle = [list(map(int, input().split())) for _ in range(N)]
    dp = [row[:] for row in triangle]
    
    for i in range(N - 1):
        for j in range(len(triangle[i])):
            for k in range(2):
                dp[i + 1][j + k] = max(dp[i][j] + triangle[i + 1][j + k], dp[i + 1][j + k])
                
    print(max(dp[-1]))
    
if __name__=="__main__":
    solution() 