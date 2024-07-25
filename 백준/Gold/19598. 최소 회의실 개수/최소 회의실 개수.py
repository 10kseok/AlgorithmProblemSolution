from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

def solution(times):
    times.sort()

    cnt = 1
    last_meeting = [times[0][1]]
    for s, e in times[1:]:
        if last_meeting[0] <= s:
            heappop(last_meeting)
        else:
            cnt += 1
        heappush(last_meeting, e)
        
    print(cnt)
    
if __name__=="__main__":
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    solution(times)