from sys import stdin

input = stdin.readline
        
def solution(n):
    # previous greater element
    tops = list(map(int, input().split()))
    received_top, stack = [0] * n, []
    for i in range(n):
        while stack and tops[i] > tops[stack[-1]]:
            stack.pop()
        
        if stack:
            received_top[i] = stack[-1] + 1
        stack.append(i)
    print(*received_top)
    
if __name__=="__main__":
    N = int(input())
    solution(N)
