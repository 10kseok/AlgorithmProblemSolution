from sys import stdin
from heapq import heappush, heappop, heapify

input = stdin.readline

def solution(n):
    lectures = [tuple(map(int, input().split())) for _ in range(n)]
    rooms = []
    
    heapify(lectures)
    while lectures:
        if not rooms:
            rooms.append(heappop(lectures)[1])
            continue
        start, end = heappop(lectures)
        
        if rooms and rooms[0] <= start:
            heappop(rooms)
        heappush(rooms, end)
            
    print(len(rooms))
    
if __name__=="__main__":
    n = int(input())
    solution(n)