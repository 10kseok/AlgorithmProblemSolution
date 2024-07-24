from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**8)

def solution(n, region):    
    def dfs(i, j, precipitation):
        visited[i][j] = True
        for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
            ni, nj = i + di, j + dj
            if 0 > ni or ni >= n or 0 > nj or nj >= n \
                or visited[ni][nj] or region[ni][nj] <= precipitation:
                continue
            dfs(ni, nj, precipitation)
        
    max_region_cnt = 1
    max_height = max(map(max, region))
    for i in range(1, max_height):
        visited = [[False] * n for _ in range(n)]
        region_cnt = 0
        for j in range(n):
            for k in range(n):
                if region[j][k] <= i or visited[j][k]:
                    continue
                dfs(j, k, i)
                region_cnt += 1
        max_region_cnt = max(region_cnt, max_region_cnt)
                    
    print(max_region_cnt)        
    
if __name__=="__main__":
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    solution(N, region)
