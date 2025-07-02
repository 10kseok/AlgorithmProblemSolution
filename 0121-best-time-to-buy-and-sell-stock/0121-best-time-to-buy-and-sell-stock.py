class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 특정 날을 고르고 그 뒤 날짜 중 가장 큰 수익을 찾아라

        # 제약 조건
        # 1. 차이의 최소값은 0
        # 2. 요소는 최대 100_000개까지 존재
        # 3. 특정 날의 이전 날짜 선택 불가

        # 문제
        # 1. 배열에서 2개의 원소를 추출하여 그 차이가 가장 큰 값을 찾아야함
        # 2. a2 - a1 > 0인 경우만 차이값으로 인정
        # 3. a2 - a1 > 0인 경우가 없으면 0을 반환

        # 풀이 1 (실패 - 시간 초과 (198/212))
        # 1. 순열로 모든 경우의 수를 구한다.
        # 2. 그 중 가장 큰 값과 0을 비교하여 큰 값을 반환한다.

        # max_profit = [0]
        # def find_max_profit(prices):
        #     if len(prices) < 2:
        #         return
        #     for i in range(1, len(prices)):
        #         max_profit[0] = max(max_profit[0], prices[i] - prices[0])
        #     find_max_profit(prices[1:])

        # find_max_profit(prices)

        # return max_profit[0]

        # case1. 7 1 5 3 6 4
        # case2. 7 6 4 3 1

        # 풀이 2 (DP)
        # 풀이 1에서는 경우의 수가 너무 많았음, 이렇다 보니 길이가 10만에 가까울 때 time limit exceeded
        # 최대 nlog(n)의 시간 복잡도가 되어야함
        # 1. 각 날짜를 부분 문제로 나누기 위해 사고 바로 다음날 판 경우의 수익을 구한다.
        # 2. 합산할 범위를 늘려가며 최대 수익을 구한다.
        # 특정 날짜의 차이는 아래와 같이 표현 가능
        # [a1 a2 a3] => (a2 - a1) + (a3 - a2) = a3 - a1
        # pass

        # 풀이 3 (Two Pointer)
        # 1. 최소값 추적용 포인터, 최대 수익 추적용 포인터 두 개를 사용한다.
        # 2. 전부 탐색해서 매 탐색마다 최소값을 항상 찾는다.
        # 3. 탐색한 최소값과 현재 탐색하고 있는 주식의 가격을 비교해서 수익을 구한다.
        # 4. 구한 수익을 최대 수익과 비교하여 갱신한다.
        min_value = prices[0]
        max_profit = 0
        n = len(prices)
        for i in range(n):
            min_value = min(min_value, prices[i])
            max_profit = max(max_profit, prices[i] - min_value)
        return max_profit

        

        
        



