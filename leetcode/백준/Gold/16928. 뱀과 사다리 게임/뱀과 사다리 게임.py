import sys
from collections import deque

input = sys.stdin.readline

def solution():
    ladder, snake = map(int, input().split())
    board = [i for i in range(101)]
    for _ in range(ladder + snake):
        dep, dest = map(int, input().split())
        board[dep] = dest
    
    dice_queue = deque([(1, 0)]) # 현재 위치, 주사위 횟수
    visited = [False] * 101 # 방문 배열을 둠으로써, 방문횟수를 100번으로 제한할 수 있음.
    visited[1] = True
    min_dice = float('inf')
    while dice_queue:
        cur_pos, dice = dice_queue.popleft()
        for i in range(1, 7):
            next_pos = cur_pos + i
            if next_pos > 100: break
            if not visited[next_pos]:
                visited[next_pos] = True
                dice_queue.append((board[next_pos], dice + 1))
            if board[next_pos] == 100:
                min_dice = min(min_dice, dice + 1)
    print(min_dice)

if __name__=="__main__":
    solution() 