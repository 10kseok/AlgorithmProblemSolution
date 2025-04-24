N = int(input()) 

map = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []
def dfs(i, j, home):
    if i < 0 or i > N - 1 \
        or j < 0 or j > N - 1 \
        or map[i][j] == '0' \
        or visited[i][j]:
        return
    
    visited[i][j] = True
    home.append((i, j))
    dfs(i + 1, j, home)
    dfs(i - 1, j, home)
    dfs(i, j + 1, home)
    dfs(i, j - 1, home)

    return home


for i in range(N):
    for j in range(N):
        if map[i][j] != '0' and not visited[i][j]:
            home = []
            dfs(i, j, home)
            result.append(len(home))

print(len(result))
print(*sorted(result), sep="\n")