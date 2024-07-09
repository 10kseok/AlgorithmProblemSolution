import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    line = [int(input()) for _ in range(N)]
    dp = [1] * N
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if line[i] > line[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    
    print(N - max(dp))
        
if __name__=="__main__":
    solution()