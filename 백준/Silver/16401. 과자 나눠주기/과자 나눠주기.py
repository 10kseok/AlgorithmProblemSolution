from sys import stdin

input = stdin.readline

def solution(m, n):
    snacks = list(map(int, input().split()))
    def can_divide(snack_length):
        if not snack_length:
            return False
        cnt = 0
        for snack in snacks:
            cnt += snack // snack_length
        return cnt >= m
    
    lower, upper = 1, max(snacks)
    answer = 0
    while lower <= upper:
        mid = (lower + upper) >> 1
        if can_divide(mid):
            answer = mid
            lower = mid + 1
        else:
            upper = mid - 1
    print(answer)

if __name__=="__main__":
    M, N = map(int, input().split())
    solution(M, N)
