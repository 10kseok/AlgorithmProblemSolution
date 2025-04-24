import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def separate(base_color, i, j, picture, visited):
    if i < 0 or  N <= i or j < 0 or N <= j or picture[i][j] != base_color or visited[i][j]: return
    visited[i][j] = True
    separate(base_color, i    , j + 1, picture, visited)
    separate(base_color, i    , j - 1, picture, visited)
    separate(base_color, i + 1, j    , picture, visited)
    separate(base_color, i - 1, j    , picture, visited)

def solution():
    global N
    N = int(input())
    result = [0, 0]
    RGB = [input().rstrip() for _ in range(N)]
    visited_RGB = [[False] * N for _ in range(N)]
    visited_RG_B = [[False] * N for _ in range(N)]
    RG_B = [''] * N
    for i in range(N):
        for j in range(N):
            RG_B[i] += 'R' if RGB[i][j] == 'G' else RGB[i][j]
            
    for i in range(N):
        for j in range(N):
            if not visited_RGB[i][j]: 
                separate(RGB[i][j], i, j, RGB, visited_RGB)
                result[0] += 1
            if not visited_RG_B[i][j]: 
                separate(RG_B[i][j], i, j, RG_B, visited_RG_B)
                result[1] += 1

    print(*result)
                
if __name__=="__main__":
    solution()