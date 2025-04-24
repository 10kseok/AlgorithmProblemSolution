from sys import stdin

input = stdin.readline
        
def solution(string, bomb):
    stack = []

    # 1. append and pop
    # for char in string:
    #     stack.append(char)
    #     if len(stack) >= len(bomb) and stack[-len(bomb):] == list(bomb):
    #         for _ in range(len(bomb)):
    #             stack.pop()
    
    # 2. append and reallocate => time over
    # for char in string:
    #     stack.append(char)
    #     if len(stack) >= len(bomb) and stack[-len(bomb):] == list(bomb):
    #         stack = stack[:-len(bomb)]
    
    # 3. append and remove once
    # bomb = list(bomb)
    # for char in string:
    #     stack.append(char)
    #     if len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
    #         del stack[-len(bomb):]

    # 4. check last character, use Time & Spatial Locality
    bomb, bomb_size = list(bomb), len(bomb)
    for char in string:
        stack.append(char)
        if stack[-1] == bomb[-1] and stack[-bomb_size:] == bomb:
            del stack[-bomb_size:]
    
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')
        
if __name__=="__main__":
    N = input().strip()
    M = input().strip()
    solution(N, M)
