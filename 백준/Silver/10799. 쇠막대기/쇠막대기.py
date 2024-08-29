from sys import stdin

input = stdin.readline
        
def solution(steel_sticks):
    # Use stack
    # stack, cnt = [], 0
    # for i in range(len(steel_sticks)):
    #     stick = steel_sticks[i]
    #     if stick == '(':
    #         stack.append(stick)
    #         continue
    #     stack.pop()
    #     cnt += len(stack) if steel_sticks[i - 1] == '(' else 1
    # print(cnt)
    
    # Just Use count
    fragment, total = 0, 0
    for i in range(len(steel_sticks)):
        stick = steel_sticks[i]
        if stick == '(':
            fragment += 1
            continue
        fragment -= 1
        total += fragment if steel_sticks[i - 1] == '(' else 1
    print(total)
    
if __name__=="__main__":
    N = input().strip()
    solution(N)
