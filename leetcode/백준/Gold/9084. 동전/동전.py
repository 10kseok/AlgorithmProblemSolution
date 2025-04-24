import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    result = []
    for _ in range(T):
        N, coins, M = int(input()), list(map(int, input().split())), int(input())

        dp = [0] * (M + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, M + 1):
                dp[i] += dp[i - coin]
        result.append(f'{dp[M]}')
    print("\n".join(result))
solution()