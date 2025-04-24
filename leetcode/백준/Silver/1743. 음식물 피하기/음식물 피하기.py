import sys

input = sys.stdin.readline
BLANK, TRASH = 0, 1

def bfs(i, j, path):
    global row, col
    size = 1
    queue = [(i, j)]
    path[i][j] = BLANK
    while queue:
        r, c = queue.pop()
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr, nc = r + dr, c + dc
            if nr <= 0 or nc <= 0 or nr > row or nc > col or path[nr][nc] == BLANK:
                continue 
            queue.append((nr, nc))
            path[nr][nc] = BLANK
            size += 1
    return size
    
def solution():
    global row, col
    row, col, k = map(int, input().split())
    path = [[BLANK] * (col + 1) for _ in range(row + 1)]
    for _ in range(k):
        r, c = map(int, input().split())
        path[r][c] = TRASH
    
    size = 1
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if path[i][j] == BLANK:
                continue
            size = max(size, bfs(i, j, path))
    print(size)
    
if __name__=="__main__":
    solution() 