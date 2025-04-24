from collections import deque
import sys

N, M = map(int, input().split())
maze_input = [sys.stdin.readline() for _ in range(N)]
maze = [[0] * M for _ in range(N)]

MAX_VALUE = 10_001
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1 ,1]

for line in range(N):
    for word in range(M):
        maze[line][word] = MAX_VALUE if int(maze_input[line][word]) == 1 else 0

def bfs(start):
    maze[start[0]][start[1]] = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for i in range(4):
            cur_row = node[0]
            cur_col = node[1]

            next_row = cur_row + dx[i]
            next_col = cur_col + dy[i]

            if next_row < 0 or next_row > N - 1 \
                or next_col < 0 or next_col > M - 1 \
                or maze[next_row][next_col] == 0 \
                or maze[next_row][next_col] != MAX_VALUE: continue
            
            queue.append((next_row, next_col))
            maze[next_row][next_col] = min(maze[next_row][next_col], maze[cur_row][cur_col] + 1)
            if next_row == N - 1 and next_col == M - 1: return

bfs((0, 0))
print(maze[N - 1][M - 1])