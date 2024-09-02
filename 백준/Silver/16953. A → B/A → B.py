from sys import stdin
from collections import deque

input = stdin.readline
        
def solution(a, b):
    queue = deque([b])
    cnt = 0
    while queue:
        num = queue.popleft()
        if num == a:
            print(cnt + 1)
            return
        elif num < a:
            continue
        
        if num % 2 == 0:
            converted = num // 2
        elif num % 10 == 1:
            converted = (num - 1) // 10
        else:
            continue
        queue.append(converted)
        cnt += 1
    print(-1)
        
if __name__=="__main__":
    A, B = map(int, input().split())
    solution(A, B)
