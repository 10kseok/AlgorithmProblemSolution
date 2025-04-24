from collections import deque
import sys
input = sys.stdin.readline
DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
H_DIRECTION = [(-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1), (-2, -1)]

def solution():
    K = int(input())
    W, H = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(H) ]
    jump_table = [ [[0] * (K + 1) for _ in range(W)] for _ in range(H) ]
            
    queue = deque([])
    queue.append((0, 0, 0))
    
    while queue:
        x, y, jump = queue.popleft()
        if x == H - 1 and y == W - 1:
            print(jump_table[x][y][jump])
            return
        
        if jump < K:
            for i in range(8):
                nx, ny = x + H_DIRECTION[i][0], y + H_DIRECTION[i][1]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if not jump_table[nx][ny][jump + 1] and board[nx][ny] == 0:
                    jump_table[nx][ny][jump + 1] = jump_table[x][y][jump] + 1
                    queue.append((nx, ny, jump + 1))
        
        for i in range(4):
            nx, ny = x + DIRECTION[i][0], y + DIRECTION[i][1]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if not jump_table[nx][ny][jump] and board[nx][ny] == 0:
                jump_table[nx][ny][jump] = jump_table[x][y][jump] + 1
                queue.append((nx, ny, jump))  
    print(-1) 
if __name__=="__main__":
    solution() 

