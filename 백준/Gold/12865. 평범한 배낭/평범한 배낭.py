import sys

N, MAX_W = map(int, sys.stdin.readline().split())

weight_value = [(0, 0)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weight_value.append((W, V))
weight_value.sort() 

# v1
# 2차원 배열로 모든 최적 조합을 기록하는 방식
def knapsack(MAX_W, weight_value, n):
    dp = [[0 for _ in range(MAX_W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight =  weight_value[i][0]
        value  =  weight_value[i][1]
        for w in range(1, MAX_W + 1):
            if w >= weight:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][MAX_W]

# v2
# 1차원 배열로 모든 최적 조합을 기록하는 방식
# 이전 값이 기록되어있기에, 이전 값을 기준으로 덮어씌우면서 최적값을 수정해나간다.
def knapsack_v2(MAX_W, weight_value, n):
    dp = [0 for _ in range(MAX_W + 1)]

    for i in range(1, n + 1):
        weight =  weight_value[i][0]
        value  =  weight_value[i][1]
        for w in range(MAX_W, 0, -1):
            if weight <= w:
                dp[w] = max(dp[w], dp[w - weight] + value)
    
    return dp[MAX_W]


# v3
# 무게 제한이 W이면, 1 ~ W까지 각 무게별 최적값을 기록해왔다
# -> 무게 조합이 나올 수 없는 경우도 탐색하기에 비효율적이였다.
# --> 가능한 무게 조합만으로 최대 비용을 탐색하는 방법
def knapsack_v3(MAX_W, weight_value):
    # value : weight
    max_value_bag = {0 : 0}
    max_first_wv = sorted(weight_value, reverse=True)

    for w, v in max_first_wv:
        temp_bag = {}
        for _v, _w in max_value_bag.items():
            w_if_added = _w + w
            v_if_added = _v + v
            if w_if_added < max_value_bag.get(v_if_added, MAX_W + 1):
                temp_bag[v_if_added] = w_if_added

        max_value_bag.update(temp_bag)
    return max(max_value_bag.keys())


# print(knapsack(MAX_W, weight_value, N))
# print(knapsack_v2(MAX_W, weight_value, N))
print(knapsack_v3(MAX_W, weight_value))
