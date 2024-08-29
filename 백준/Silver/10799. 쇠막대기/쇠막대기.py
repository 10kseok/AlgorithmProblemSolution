from sys import stdin

input = stdin.readline
        
def solution(steel_sticks):
    stack, cnt = [], 0
    for i in range(len(steel_sticks)):
        stick = steel_sticks[i]
        if stick == '(':
            stack.append(stick)
            continue
        stack.pop()
        cnt += len(stack) if steel_sticks[i - 1] == '(' else 1
    print(cnt)
    
if __name__=="__main__":
    N = input().strip()
    solution(N)
