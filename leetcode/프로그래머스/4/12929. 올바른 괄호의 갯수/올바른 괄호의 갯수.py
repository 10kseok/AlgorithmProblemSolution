def solution(n):
    MAX = 14
    answer = 0
    # ["", ""]
    # 각 인덱스에 몇번 집어넣을지 고려
    # DP? ok, DFS? ok
    # 첫번째 괄호에 몇개의 괄호를 사용하는지에 따라 구해보자 -> DP
    # 괄호는 열고 닫는 것밖에 없고, n이 14기에 크기가 크기않다. 올바른 괄호를 모두 구해보자 -> DFS
    
    # DP
    dp = [0] * (MAX + 1)
    dp[0] = 1; dp[1] = 1; dp[2] = 2; dp[3] = 5;
    for i in range(4, n + 1):
        dp[i] = sum([dp[j] * dp[(i-1) - j] for j in range(0, i)])
    answer = dp[n]
    
    # DFS
    def makeParentheses(_open, _close):
        if _open == n:
            return 1
        if _open - _close < 0:
            return 0
        num = 0
        num += makeParentheses(_open + 1, _close)
        num += makeParentheses(_open, _close + 1)
        return num
    
    answer = makeParentheses(0, 0)
        
    return answer