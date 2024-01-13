n = int(input())
T = [int(input()) for _ in range(n)]

partitions = [(4, 10_000) for _ in range(n)]
max_T_idx = max(T) + 1
prime_table = [i for i in range(0, max_T_idx)]
prime_table[0] = 0

# 소수 테이블 작성
for i in range(2, max_T_idx):
    if prime_table[i] == 0:
        continue
    for j in range(i * 2, max_T_idx, i):
        if prime_table[j] == 0:
            continue
        prime_table[j] = 0
# 소수 합 찾기
for idx, t in enumerate(T):
    for num in range(2, t + 1):
        if prime_table[num] == 0:
            continue
        if prime_table[t - num] != 0 \
            and abs((t - num) - num) < abs(partitions[idx][0] - partitions[idx][1]):
            diff = t - num
            partitions[idx] = (min(num, diff), max(num, diff))

for p in partitions:
    print(*p)