import sys
from collections import deque

input = sys.stdin.readline
DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
SEA = 0

def melt_with_bfs(cur_x, cur_y, visited):
    visited[cur_x][cur_y] = True
    iceberg_queue = deque([(cur_x, cur_y)])

    while iceberg_queue:
        cur_x, cur_y = iceberg_queue.popleft()

        for dx, dy in DIRECTION:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if not visited[next_x][next_y]:
                if sea_and_iceberg[cur_x][cur_y] != SEA and sea_and_iceberg[next_x][next_y] == SEA:
                    sea_and_iceberg[cur_x][cur_y] -= 1

                if sea_and_iceberg[next_x][next_y] != SEA: # 바로 직전 빙산이 된 바다는 포함하지 않기 위해
                    visited[next_x][next_y] = True # 빙산이므로 방문 체크
                    iceberg_queue.append((next_x, next_y)) # 해당 빙산 주위로 다시 바다를 확인해야되니 큐 삽입

        if sea_and_iceberg[cur_x][cur_y] == 0:
            cur_iceberg.remove((cur_x, cur_y))

def solution():
    global N, M, sea_and_iceberg, cur_iceberg
    N, M = map(int, input().split())
    sea_and_iceberg = [list(map(int, input().split())) for _ in range(N)]
    cur_iceberg = set()
    
    for i in range(N):
        for j in range(M):
            if sea_and_iceberg[i][j] != 0:
                cur_iceberg.add((i, j))

    year = 0
    while True:
        count = 0
        visited = [[False] * M for _ in range(N)]
        iceberg_proxy = cur_iceberg.copy()
        for i, j in iceberg_proxy:
            if sea_and_iceberg[i][j] != 0 and not visited[i][j]:
                melt_with_bfs(i, j, visited)
                count += 1
        
        if count >= 2:
            print(year)
            return
        if count == 0:
            print(0)
            return
        year += 1

if __name__=="__main__":
    solution()