from sys import stdin

input = stdin.readline
        
def solution(n, budgets, m):
    lower, upper = 1, max(budgets)
    while lower <= upper:
        upper_budget = (lower + upper) >> 1
        
        total_budget = sum(upper_budget if budget >= upper_budget else budget for budget in budgets)

        if total_budget > m:
            upper = upper_budget - 1
        else:
            lower = upper_budget + 1
    print(upper)
            
if __name__=="__main__":
    N = int(input())
    args = list(map(int, input().split()))
    M = int(input())
    solution(N, args, M)

    
