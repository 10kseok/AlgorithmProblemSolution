from sys import stdin

input = stdin.readline

def solution(nums):
    answer = []
    
    for num in nums:
        INCLUDE_NUM = num + 1
        dp = [1 for _ in range(INCLUDE_NUM)]
        for i in range(2, 4):
            for j in range(i, INCLUDE_NUM):
                dp[j] = dp[j] + dp[j - i]
        answer.append(f'{dp[num]}')
    
    print("\n".join(answer))
    
if __name__=="__main__":
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    solution(nums)
    
