from sys import stdin
from collections import deque

input = stdin.readline
        
def solution(n):
    sequences = deque(sorted([int(input()) for _ in range(n)]))

    total = 0 
    while sequences:
        if sequences[-1] > 0:
            num = sequences.pop()
            if sequences and sequences[-1] > 0:
                num2 = sequences.pop()
                total += max(num + num2, num * num2)
            else:
                total += num
        else:
            num = sequences.popleft()
            if sequences:
                num2 = sequences.popleft()
                total += max(num + num2, num * num2)
            else:
                total += num
    print(total)
        
    
if __name__=="__main__":
    n = int(input())
    solution(n)