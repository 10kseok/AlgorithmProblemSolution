from sys import stdin

input = stdin.readline

def solution(nums):    
    MAX_NUM = 10_000 + 1
    dp = [1 for _ in range(MAX_NUM)]
    for i in range(2, 4):
        for j in range(i, MAX_NUM):
            dp[j] += dp[j - i]

    for num in nums:
        print(dp[num])
    
if __name__=="__main__":
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    solution(nums)
    