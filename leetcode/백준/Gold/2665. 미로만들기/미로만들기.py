import sys
from heapq import heappush, heappop

input = sys.stdin.readline
DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution():
    board_size = int(input())
    board = [input() for _ in range(board_size)]
    dark_rooms = [[float('inf')] * board_size for _ in range(board_size)]

    queue = [(0, 0, 0)]
    while queue:
        dark_room, row, col = heappop(queue)
        for k in range(4):
            next_r, next_c = row + DIRECTION[k][0], col + DIRECTION[k][1]
            if next_r < 0 or next_r >= board_size or next_c < 0 or next_c >= board_size: continue
            # '0' -> 검은 방, '1' -> 흰 방
            if board[next_r][next_c] == '0' and dark_rooms[next_r][next_c] > dark_room + 1:
                dark_rooms[next_r][next_c] = dark_room + 1
                heappush(queue, (dark_room + 1, next_r, next_c))
            elif board[next_r][next_c] == '1' and dark_rooms[next_r][next_c] > dark_room:
                dark_rooms[next_r][next_c] = dark_room
                heappush(queue, (dark_room, next_r, next_c))
    print(dark_rooms[-1][-1])
if __name__=="__main__":
    solution()