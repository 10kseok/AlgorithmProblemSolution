import sys
from collections import deque

# 위, 아래, 상, 우, 하, 좌
directions=[[1,0,0], [-1,0,0], [0,1,0], [0,0,1], [0,-1,0],[0,0,-1]]

M,N,H = map(int,sys.stdin.readline().rstrip().split())
matrix = []

# matrix 만들기
for floor in range(H):
    rows = []
    for row in range(N):
        r = list(map(int, sys.stdin.readline().rstrip().split()))
        rows.append(r)
    matrix.append(rows)


# [z,y,x]
dq = deque([])

# 이미 익어있는 토마토 구별하기
for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[z][y][x] == 1:
                dq.append([z,y,x])

# 인접해 있는 토마토 익혀버리기!
while dq:
    cz,cy,cx = dq.popleft()
    for direction in directions:
        nz = cz + direction[0]
        ny = cy + direction[1]
        nx = cx + direction[2]

        if 0<=nz<H and 0<=ny<N and 0<=nx<M and matrix[nz][ny][nx] == 0:
            matrix[nz][ny][nx] = matrix[cz][cy][cx] + 1
            dq.append([nz,ny,nx])

# 익은날 = 최대일수 -1
maxDay = -99
for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[z][y][x] == 0:
                print(-1)
                exit()
            if maxDay < matrix[z][y][x]:
                maxDay = matrix[z][y][x]

print(maxDay-1)