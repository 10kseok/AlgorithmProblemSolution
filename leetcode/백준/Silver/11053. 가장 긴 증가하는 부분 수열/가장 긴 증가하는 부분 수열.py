import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    dp = [1] * (N + 1)
    
    for i in range(1, N + 1):
        max_value = 0
        for j in range(1, i):
            if A[i] > A[j] and max_value < dp[j]:
                max_value = dp[j]
        dp[i] = max_value + 1
    print(max(dp))

solution()