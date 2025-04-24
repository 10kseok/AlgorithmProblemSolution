import sys
input = sys.stdin.readline
JUMP_DIR = [(1, 1), (0, 1), (-1, 1)]

def solution():
    N, M = map(int, input().split())
    info_island = [input().rstrip() for _ in range(N)]
    carrot_table = [[-1] * M for _ in range(N)]
    carrot_max = -1
    
    # find rabbit
    rabit = None
    for i in range(N):
        for j in range(M):
            if info_island[i][j] == 'R':
                rabit = (i, j)
                carrot_table[i][j] = 0
    
    for c in range(rabit[1] + 1, M):
        for r in range(N):
            if info_island[r][c] == '#':
                continue
            cur_carrot = -1
            for dr, dc in JUMP_DIR:
                next_r, next_c = r - dr, c - dc
                if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                    continue
                cur_carrot = max(cur_carrot, carrot_table[next_r][next_c])
            if cur_carrot == -1:
                continue
            if info_island[r][c] == 'C':
                cur_carrot += 1
            if info_island[r][c] == 'O':
                carrot_max = max(carrot_max, cur_carrot)
            carrot_table[r][c] = cur_carrot
    print(carrot_max)
    
if __name__=="__main__":
    solution() 

