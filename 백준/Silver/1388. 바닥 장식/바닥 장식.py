N, M = map(int, input().split())

floor = [input() for _ in range(N)]
counted = [[False] * M for _ in range(N)]
count = 0

def dfs(i, j, shape):
    if i > N - 1 or j > M - 1 \
        or floor[i][j] != shape or counted[i][j]:
        return
    
    counted[i][j] = True

    if shape == "-":
        dfs(i, j + 1, shape)
    else:
        dfs(i + 1, j, shape)


for i in range(N):
    for j in range(M):
        if not counted[i][j]:
            dfs(i, j, floor[i][j])
            count += 1

print(count)