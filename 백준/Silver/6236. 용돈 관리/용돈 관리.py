import sys

input = sys.stdin.readline

def count_withdraw(k, costs_per_day):
    IMPOSSIBLE = 100_001
    withdraw_cnt = 1
    budget = k
    for cost in costs_per_day:
        if cost <= budget:
            budget -= cost
            continue
        if k < cost:
            return IMPOSSIBLE
        budget = k - cost
        withdraw_cnt += 1
    return withdraw_cnt

def solution():
    N, M = map(int, input().split())
    costs_per_day = [int(input()) for _ in range(N)]
    
    lower, upper = 0, N * 10_000 + 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if count_withdraw(mid, costs_per_day) > M:
            lower = mid + 1
            continue
        # count_withdraw(mid, costs_per_day) <= M
        K = mid
        upper = mid - 1
    print(K)
if __name__=="__main__":
    solution() 