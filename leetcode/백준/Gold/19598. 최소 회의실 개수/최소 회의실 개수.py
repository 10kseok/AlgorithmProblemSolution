from sys import stdin

input = stdin.readline

def solution(times):
    # Use heapq
    # from heapq import heappush, heappop
    # times.sort()
    # cnt = 1
    # last_meeting = [times[0][1]]
    # for s, e in times[1:]:
    #     if last_meeting[0] <= s:
    #         heappop(last_meeting)
    #     else:
    #         cnt += 1
    #     heappush(last_meeting, e)
    # print(cnt)
    
    # Use sort twice
    starts = sorted(list(map(lambda x:x[0], times)))
    ends = sorted(list(map(lambda x:x[1], times)))
    N = len(times)
    
    cursor = 0
    for s in starts:
        if ends[cursor] <= s:
            N -= 1
            cursor += 1
    print(N)
    
if __name__=="__main__":
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    solution(times)