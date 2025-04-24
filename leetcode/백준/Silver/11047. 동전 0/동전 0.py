import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
total_count = 0
i = 1
while i <= N:
    if K >= coins[-i]:
        coin_count = K // coins[-i]
        K -= (coins[-i] * coin_count)
        total_count += coin_count
    i += 1
print(total_count)

