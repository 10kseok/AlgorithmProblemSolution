import sys
input = sys.stdin.readline

def solution():
    # X = ROW, Y = COLUMN
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range (N)]
    total_ranges = [list(map(int, input().split())) for _ in range (M)]

    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = table[i - 1][j - 1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i -1][j - 1]
            
    for start_x, start_y, end_x, end_y in total_ranges:
        total = prefix_sum[end_x][end_y]  + prefix_sum[start_x -1][start_y -1] - prefix_sum[end_x][start_y - 1] - prefix_sum[start_x - 1][end_y]
        print(total)

if __name__=="__main__":
    solution() 