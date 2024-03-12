from collections import deque

# N은 세로 , M은 가로
N,M = map(int,input().split())
graph = []
for col in range(N):
    graph.append(list(map(str,input())))

sq = deque() # 고슴도치
wq = deque() # 물

dx,dy = [1,0,-1,0],[0,1,0,-1]
wvisited = [[-1]*M for _ in range(N)]

def bfs():
    while wq:
        y,x = wq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] != 'X' and graph[ny][nx] != 'D':
                    if wvisited[ny][nx] == -1:
                        wvisited[ny][nx] = wvisited[y][x]+1
                        wq.append((ny,nx))

    while sq:
        y,x = sq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == '.':
                    if wvisited[ny][nx] > graph[y][x]+1 or wvisited[ny][nx] == -1:
                        # 물이 도치보다 늦게 도착하거나, 물이 아예 오직 않은 곳이면
                        graph[ny][nx] = graph[y][x]+1
                        sq.append((ny,nx))

                if graph[ny][nx] == 'D': # 탈출구
                    return graph[y][x]+1

    return 'KAKTUS'

for col in range(N):
    for row in range(M):
        if graph[col][row] == '*': # 물부터 움직여!
            wq.append((col,row))
            wvisited[col][row] = 0

        elif graph[col][row] == 'S': # 도치
            sq.append((col,row))
            graph[col][row] = 0

print(bfs())