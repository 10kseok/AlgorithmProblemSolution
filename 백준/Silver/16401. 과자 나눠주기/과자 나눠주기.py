from sys import stdin

input = stdin.readline

def solution(m, n):
    snacks = list(map(int, input().split()))

    lower, upper = 1, max(snacks)
    answer = 0
    while lower <= upper:
        length = (lower + upper) >> 1
        if sum([snack // length for snack in snacks]) >= m:
            answer = length
            lower = length + 1
        else:
            upper = length - 1
    print(answer)

if __name__=="__main__":
    M, N = map(int, input().split())
    solution(M, N)
