FIRST, SECOND = f'0{input()}', f'0{input()}'
N_FIRST, N_SECOND = len(FIRST), len(SECOND)
dp = [0] * N_SECOND

#   0 S E C O N D
# 0 0 0 0 0 0 0 0
# F 0
# I 0
# R 0
# S 0
# T 0

for i in range(1, N_FIRST):
    count = 0
    for j in range(1, N_SECOND):
        if count < dp[j]:
            count = dp[j]
        elif FIRST[i] == SECOND[j]:
            dp[j] = count + 1

print(max(dp))