from sys import stdin
from heapq import heappush, heappop, heapify

input = stdin.readline
        
def solution(n):
    cards = [int(input()) for _ in range(n)]
    heapify(cards)
    comparasion = 0
    while len(cards) > 1:
        a, b = heappop(cards), heappop(cards)
        comparasion += a + b
        heappush(cards, a + b)
    print(comparasion)
    
if __name__=="__main__":
    n = int(input())
    solution(n)