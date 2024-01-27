import sys

N, MAX_W = map(int, sys.stdin.readline().split())

weight_value = [(0, 0)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weight_value.append((W, V))
weight_value.sort() 

def knapsack(MAX_W, weight_value, n):
    dp = [[0 for _ in range(MAX_W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight =  weight_value[i][0]
        value  =  weight_value[i][1]
        for w in range(1, MAX_W + 1):
            if (w - weight) >= 0:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][MAX_W]

print(knapsack(MAX_W, weight_value, N))
