from sys import stdin

input = stdin.readline

def solution(n, m):
    '''
    1 <= N <= 2,000,000,000 , 1 ≤ M ≤ 10,000
    '''
    amusements = list(map(int, input().split())) # 놀이기구당 소요시간
    if N <= M:
        print(N)
        return

    lower, upper = 1, max(amusements) * n
    done_time = None
    while lower <= upper:
        collapsed_time = (lower + upper) >> 1
        total_n = m + sum(collapsed_time // amusement for amusement in amusements)
        if total_n >= n:
            done_time = collapsed_time
            upper = collapsed_time - 1
        else:
            lower = collapsed_time + 1
            
    if not done_time:
        raise Exception("UNEXPECTED DATA")
    
    # 완료 1초 전 몇 명이 탔는 지 계산
    total_n = m + sum((done_time - 1) // amusement for amusement in amusements)
    for i in range(m):
        total_n += 1 if done_time % amusements[i] == 0 else 0
        if total_n == n:
            print(i + 1)
            return
        
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)