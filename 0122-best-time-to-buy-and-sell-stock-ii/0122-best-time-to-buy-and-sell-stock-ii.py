class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 주식을 최대 한주 보유한 상황에서 최대 수익 구하기

        # 제약 조건
        # 1. 주식 가격의 배열의 길이는 최대 30_000개
        # 2. 주식 가격의 최대는 10_000
        # 3. 주식은 최대 한 주만 가질 수 있다
        # 4. 매수 당일 매도 가능

        # 문제
        # 1. 배열 탐색에서 매수 매도 여러번 가능
        # 2. 무작정 가장 작은 값과 큰 값을 구하면 안됨 ([1, 5, 3, 6] 같은 경우)
        # 3. 모든 경우의 수를 구하긴 최대 길이가 너무 김
        # 4. 각 범위별 최대 수익을 구하는 방법 필요

        # 풀이 1 (greedy)
        # 1. 매수/매도가 여러번 가능하므로 수익이 날 수 있을 때마다 판다.
        # 2. 어제보다 오늘이 더 비싸면 어제 주식을 사고 오늘 바로 판다.
        # 3. 수익이 나면 총합에 더한다.

        # Case 1
        # [7,1,5,3,6,4]
        # 1. 1,5 -> 4
        # 2. 3,6 -> 3
        # 3 + 4 = 7

        # Case 2
        # [1,2,3,4,5]
        # 1. 1, 2 -> 1
        # 2. 2, 3 -> 1
        # ...
        # max_profit = 0
        # n = len(prices)
        # if n == 1:
        #     return 0
        # for i in range(1, n):
        #     if prices[i - 1] < prices[i]:
        #         max_profit += prices[i] - prices[i - 1]

        # return max_profit

        # if not prices:
        # return 0

        # 풀이 2 (DP)
        n = len(prices)
        hold = -prices[0]
        sell = 0
        for i in range(1, n):
            prev_hold = hold
            hold = max(hold, sell - prices[i])
            sell = max(sell, prev_hold + prices[i])
        return sell
