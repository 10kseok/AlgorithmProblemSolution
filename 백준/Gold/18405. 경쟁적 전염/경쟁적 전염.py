from collections import deque
import heapq
import sys 
# (X-1, Y-1)부터 시작해서, DFS로 늘려나가서 제일 먼저 만나는 바이러스를 탐색하는 방식을 구상했으나 실패.
# 작은 번호부터 바이러스를 BFS를 통해서 S초 동안 늘려놓고, X-1, Y-1 위치에 위치한 바이러스를 찾는 방식으로 변경

input = sys.stdin.readline

N, K = map(int, input().split()) 

test_case = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split()) 

# 상하좌우
dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]

queue = []
for i in range(N):
    for j in range(N):
        if test_case[i][j] != 0:
            queue.append((test_case[i][j], i, j, 0))
queue.sort()
queue = deque(queue)

def bfs(X, Y, queue, S):
    while queue:
        location = queue.popleft()
        virus_num = location[0]
        count = location[3]
        if count >= S:
            break

        for i in range(4):
            cur_x, cur_y = location[1], location[2]
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N \
                and test_case[next_x][next_y] == 0:
                test_case[next_x][next_y] = virus_num
                queue.append((virus_num, next_x, next_y, count + 1))
        
    return test_case[X][Y]
print(bfs(X - 1, Y - 1, queue, S))
