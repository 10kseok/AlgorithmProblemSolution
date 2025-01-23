def solution(arr):
    nums, signs = list(map(int, arr[::2])), ["+"] + arr[1::2]
    n = len(nums)
    
    def apply(left: int, right: int, sign: str):
        if sign == "+":
            return left + right
        elif sign == "-":
            return left - right
        else:
            raise Exception("부호에 해당하는 문자가 아닙니다 : " + sign)
            
    dp = [[[float('inf'), -float('inf')] for _ in range(n + 1)] for _ in range(n + 1)]

    MIN, MAX = 0, 1
    for i in range(1, n + 1):
        dp[i][i] = [int(nums[i - 1]), int(nums[i - 1])]
    
    for chunk_size in range(1, n):
        for i in range(1, n - chunk_size + 1):
            j = i + chunk_size
            for k in range(i, j):
                buffer = [
                    apply(dp[i][k][l], dp[k + 1][j][m], signs[k])
                    for l in (MIN, MAX)
                    for m in (MIN, MAX)
                ]
                dp[i][j][MIN] = min(dp[i][j][MIN], min(buffer))
                dp[i][j][MAX] = max(dp[i][j][MAX], max(buffer))
                
    return dp[1][n][MAX]
    