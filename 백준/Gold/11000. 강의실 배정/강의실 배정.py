from sys import stdin
# from heapq import heappush, heappop, heapify

input = stdin.readline

def solution(n):
    # Use Two Priority Queue
    # lectures = [tuple(map(int, input().split())) for _ in range(n)]
    # rooms = []
    
    # heapify(lectures)
    # while lectures:
    #     if not rooms:
    #         rooms.append(heappop(lectures)[1])
    #         continue
    #     start, end = heappop(lectures)
        
    #     if rooms and rooms[0] <= start:
    #         heappop(rooms)
    #     heappush(rooms, end)
            
    # print(len(rooms))
    
    # Use One Priority Queue
    # lectures = [tuple(map(int, input().split())) for _ in range(n)]
    # rooms = []
    
    # lectures.sort()
    # for start, end in lectures:
    #     if not rooms:
    #         rooms.append(end)
    #         continue
    #     if rooms and rooms[0] <= start:
    #         heappop(rooms)
    #     heappush(rooms, end)
        
    # print(len(rooms))
    
    # Use Cursor
    starts, ends = [], []
    for _ in range(n):
        s, e = map(int, input().split())
        starts.append(s)
        ends.append(e)
        
    starts.sort()
    ends.sort()
    
    cursor, rooms = 0, n
    for s in starts:
        if ends[cursor] <= s:
            rooms -= 1
            cursor += 1
            
    print(rooms)
if __name__=="__main__":
    n = int(input())
    solution(n)    