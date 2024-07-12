from sys import stdin

input = stdin.readline

def solution():
    N = int(input())
    buildings = [(0, 0)] + [(i + 1, int(l)) for i, l in enumerate(input().split())]
    building_stack, NUM, HEIGHT = [], 0, 1 # (index, l)
    answer, COUNT, NEAREST_NUM = [[0, 0] for _ in range(N + 1)], 0, 1 # count, nearest_num
    # forward
    for i in range(1, N + 1):
        while building_stack and building_stack[-1][HEIGHT] <= buildings[i][HEIGHT]:
            building_stack.pop()
            
        answer[i][COUNT] = len(building_stack)
        
        if building_stack:
            answer[i][NEAREST_NUM] = building_stack[-1][NUM]
        building_stack.append(buildings[i])
    building_stack = []
    # reverse
    for i in range(N, 0, -1):
        while building_stack and building_stack[-1][HEIGHT] <= buildings[i][HEIGHT]:
            building_stack.pop()
            
        answer[i][COUNT] += len(building_stack)
        
        if building_stack and (answer[i][NEAREST_NUM] == 0 or abs(i - answer[i][NEAREST_NUM]) > abs(i - building_stack[-1][NUM])):
            answer[i][NEAREST_NUM] = building_stack[-1][NUM]
        building_stack.append(buildings[i])

    for ans in answer[1:]:
        if ans[1] == 0:
            print(0)
            continue
        print(*ans)
if __name__=="__main__":
    solution()