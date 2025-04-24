from sys import stdin

input = stdin.readline

def solution(K, coins):    
    coins.sort()
    dp = [0] * (K + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, K + 1):
            dp[i] += dp[i - coin]
    print(dp[K])
if __name__=="__main__":
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    solution(K, coins)

