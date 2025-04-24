from sys import stdin

input = stdin.readline

def solution(n, m, l):
    # 0 <= n <= 50
    rests = [0] + sorted(list(map(int, input().split()))) + [l] if n else [0] + [l]
    n = len(rests)
    
    lower, upper = 1, l - 1
    while lower <= upper:
        gap = (lower + upper) >> 1
        cnt = 0
        for i in range(1, n):
            cnt += (rests[i] - rests[i - 1] - 1) // gap # 이미 있는 위치에 설치하지 않게 하려고 -1
        if cnt <= m:
            upper = gap - 1
        else:
            lower = gap + 1
    print(lower)

if __name__=="__main__":
    N, M, L = map(int, input().split())
    solution(N, M, L)