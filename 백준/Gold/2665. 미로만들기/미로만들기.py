import sys
from collections import deque

input = sys.stdin.readline
DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution():
    board_size = int(input())
    board = [input() for _ in range(board_size)]
    
    visited = [[False] * board_size for _ in range(board_size)]
    black_rooms = [[float('inf')] * board_size for _ in range(board_size)]
    visited[0][0] = True
    black_rooms[0][0] = 0
    queue = deque([(0, 0)])
    
    while queue:
        row, col = queue.popleft()
        visited[row][col] = True
        for k in range(4):
            next_r, next_c = row + DIRECTION[k][0], col + DIRECTION[k][1]
            if next_r < 0 or next_r >= board_size or next_c < 0 or next_c >= board_size: continue
            # '0' -> 검은 방, '1' -> 흰 방
            if board[next_r][next_c] == '0' and black_rooms[next_r][next_c] > black_rooms[row][col] + 1:
                black_rooms[next_r][next_c] = black_rooms[row][col] + 1
                queue.append((next_r, next_c))
            elif board[next_r][next_c] == '1' and black_rooms[next_r][next_c] > black_rooms[row][col]:
                black_rooms[next_r][next_c] = black_rooms[row][col]
                queue.append((next_r, next_c))  
            elif not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                queue.append((next_r, next_c))
    print(black_rooms[-1][-1])
if __name__=="__main__":
    solution() 