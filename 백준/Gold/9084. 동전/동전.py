import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    result = []
    for _ in range(T):
        N, coins, M = int(input()), list(map(int, input().split())), int(input())
        
        dp = [0] * (M + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(M + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
        result.append(f'{dp[M]}')
    print("\n".join(result))
solution()