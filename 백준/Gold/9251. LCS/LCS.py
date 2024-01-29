FIRST, SECOND = f'0{input()}', f'0{input()}'
N_FIRST, N_SECOND = len(FIRST), len(SECOND)
dp = [[0] * (N_SECOND) for _ in range(N_FIRST)]

#   0 S E C O N D
# 0 0 0 0 0 0 0 0
# F 0
# I 0
# R 0
# S 0
# T 0

for i in range(1, N_FIRST):
    for j in range(1, N_SECOND):
        if FIRST[i] == SECOND[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 

print(dp[-1][-1])