from sys import stdin

input = stdin.readline
        
def solution(n, m):
    # 블루레이 크기의 최소값
    bluelays = list(map(int, input().split()))
    max_size = max(bluelays)
    lower, upper = max_size, max_size * n
    # 큰 쪽이 항상 조건을 만족하는 쪽
    while lower <= upper:
        mid = (lower + upper) >> 1
        
        cur_size, cnt = 0, 0
        for bl in bluelays:
            cur_size += bl
            if mid <= cur_size:
                cur_size = 0 if mid == cur_size else bl
                cnt += 1
        if cur_size > 0:
            cnt += 1
                
        if cnt > m:
            lower = mid + 1
        else:
            upper = mid - 1
    print(lower)
            
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)