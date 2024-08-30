from sys import stdin

input = stdin.readline
        
def solution(string, bomb):
    stack = []
    
    for char in string:
        stack.append(char)
        if len(stack) >= len(bomb) and stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()
    
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')
        
if __name__=="__main__":
    N = input().strip()
    M = input().strip()
    solution(N, M)
