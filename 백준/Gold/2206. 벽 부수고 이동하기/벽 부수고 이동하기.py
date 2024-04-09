from collections import deque
import sys
input = sys.stdin.readline

MAX_DISTANCE = 1_000_001
DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
NOT_BREAKED, BREAKED = 0, 1

def solution():
    global N, M
    N, M = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    distance_table = [[[MAX_DISTANCE] * 2 for _ in range(M)] for _ in range(N) ]

    shortest_Q = deque([])
    shortest_Q.append((0, 0, 0))
    distance_table[0][0][NOT_BREAKED] = 1
    
    while shortest_Q:
        row, col, has_breaked = shortest_Q.popleft()
        if row == N - 1 and col == M - 1:
            print(distance_table[row][col][has_breaked])
            return
        
        for d in DIRECTIONS:
            nr, nc = row + d[0], col + d[1]
            if nr < 0 or N <= nr or nc < 0 or M <= nc:
                continue
            if matrix[nr][nc] == 1 and not has_breaked:
                distance_table[nr][nc][BREAKED] = distance_table[row][col][NOT_BREAKED] + 1
                shortest_Q.append((nr, nc, BREAKED))
            elif matrix[nr][nc] == 0 and distance_table[nr][nc][has_breaked] == MAX_DISTANCE:
                distance_table[nr][nc][has_breaked] = distance_table[row][col][has_breaked] + 1
                shortest_Q.append((nr, nc, has_breaked))
                
    print(-1)
   
if __name__=="__main__":
    solution() 
