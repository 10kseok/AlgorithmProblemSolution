import sys

input = sys.stdin.readline
    
def solution():
    N = int(input())
    MAGIC_NUMBER = 10_007
    # 각 자릿수가 자신보다 같거나 큰 경우의 수를 구하라!
    # N = 1
    # 0 1 2 3 4 5 6 7 8 9 => 10
    # N = 2
    # 00 ~ 09 (10), 11 ~ 19 (9), 22 ~ 29 (8), 33 ~ 39 (7), ..., 99 (1) => 55
    # 10 - 0 + 10 - 1 + 10 - 2
    # N = 3
    # 000 ~ 009 (10), 011 ~ 019 (9), ..., 099(1) => 55
    # 111 ~ 119 (9), 122 ~ 129 (8), ..., 199(1) => 45
    # 222 ~ 229 (8), ..., 299(1) => 36
    # ...
    # 999 (1) => 1
    dp = [[1 for _ in range(10)] for _ in range(N + 1)]
    total = [0 for _ in range(N + 1)]
    total[1] = sum(dp[1])
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][0] = total[i - 1]
                continue
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
        total[i] = sum(dp[i]) % MAGIC_NUMBER
    print(total[N])
if __name__=="__main__":
    solution() 