import sys
input = sys.stdin.readline

def solution():
    step_count = int(input())
    steps = [0]
    for _ in range(step_count):
        steps.append(int(input()))
    
    dp = [0 for _ in range(step_count + 1)]
    dp[0] = 0
    dp[1] = steps[1]
    for i in range(2, step_count + 1):
        dp[i] = max(dp[i - 3] + steps[i - 1], dp[i - 2]) + steps[i]

    print(dp[step_count])

if __name__=="__main__":
    solution()
