import sys, heapq
input = sys.stdin.readline
def solution():
    N = int(input())
    min_heap = []
    for _ in range(N):
        x = int(input())
        if x > 0:
            heapq.heappush(min_heap, x)
        else:
            print(heapq.heappop(min_heap) if len(min_heap) > 0 else 0)        
if __name__=="__main__":
    solution()